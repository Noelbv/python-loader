from filemgmt.filehandler import FileHandler
import grpc_client
import json
import threading
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm
import time

class FastJSONHandler(FileHandler):
    
    def importFile(self, path):
        try:
            with open(path, 'r') as file:
                data = json.load(file)
                tagset_id_map = {}
                tag_id_map = {}
                tagset_id_map_lock = threading.Lock()
                tag_id_map_lock = threading.Lock()
                printlock = threading.Lock()
                
                tagsets = data.get('tagsets', [])
                tagset_executor = ThreadPoolExecutor(max_workers=10)
                tagsets_pbar = tqdm(total=len(tagsets), desc="Adding tagsets")
                def processTagset(tagset_item):
                    thread_client = grpc_client.LoaderClient()
                    tagset_id = tagset_item.get('id')
                    tagset_name = tagset_item.get('name')
                    tagset_type = tagset_item.get('type')
                    tagset_response = thread_client.add_tagset(tagset_name, tagset_type)
                    if type(tagset_response) is str:
                        printlock.acquire()
                        print(f"Error adding tagset {tagset_name}: {tagset_response}")
                        printlock.release()
                        tagsets_pbar.update(1)
                        return

                    tagset_id_map_lock.acquire()
                    tagset_id_map[tagset_id] = (tagset_response.id, tagset_response.tagTypeId)
                    tagset_id_map_lock.release()
                    
                    tags = tagset_item.get('tags')
                    for tag_item in tags:
                        value = tag_item.get('value') 
                        tag_response = thread_client.add_tag(tagset_response.id, tagset_type, value)
                        if type(tag_response) is str:
                            printlock.acquire()
                            print(f"Invalid item in tagset {tagset_name} : {tag_response}")
                            printlock.release()
                            continue
                        tag_id_map_lock.acquire()
                        tag_id_map[tag_item.get('id')] = tag_response.id    #type: ignore
                        tag_id_map_lock.release()
                    tagsets_pbar.update(1)

                for tagset_item in tagsets:
                    tagset_executor.submit(processTagset, tagset_item)

                tagset_executor.shutdown()
                
                
                medias_executor = ThreadPoolExecutor(max_workers=10)
                medias = data.get('medias', [])
                medias_pbar = tqdm(total=len(medias), desc="Adding medias")

                def processMedia(media_item):
                    thread_client = grpc_client.LoaderClient()
                    media_path = media_item.get('path')
                    media_response = thread_client.add_file(media_path)
                    if type(media_response) is str:
                        printlock.acquire()
                        print(f"Couldn't add media {media_item}: {media_response}")
                        printlock.release()
                        medias_pbar.update(1)
                        return
                    tags = media_item.get('tags', [])
                    response_iterator = thread_client.add_taggings(media_id=media_response.id, tag_ids=tags)
                    for _ in response_iterator:
                        continue
                    # for response in thread_client.add_taggings(media_id=media_response.id, tag_ids=tags):
                    #     if type(response) is str:
                    #         printlock.acquire()
                    #         print(f"Couldn't add tagging : {response}")
                    #         printlock.release()
                    medias_pbar.update(1)

               
                for media_item in medias:
                    medias_executor.submit(processMedia, media_item)
                
                medias_executor.shutdown()

                hierarchies_executor = ThreadPoolExecutor(max_workers=10)
                hierarchies = data.get('hierarchies', [])
                hierarchies_pbar = tqdm(total=len(hierarchies), desc="Adding hierarchies")
                

                def processHierarchy(hierarchy_item):
                    thread_client = grpc_client.LoaderClient()
                    name = hierarchy_item.get('name')
                    tagset_id = tagset_id_map[hierarchy_item.get('tagset_id')][0]
                    hierarchy_response = thread_client.add_hierarchy(name, tagset_id)
                    if type(hierarchy_response) is str:
                        printlock.acquire()
                        print(f"Couldn't add hierarchy {name}: {hierarchy_response}")
                        printlock.release()
                        hierarchies_pbar.update(1)
                        return
                    hierarchy_id = hierarchy_response.id

                    def addNode(node, parentnode_id):
                        tag_id = tag_id_map[node.get('tag_id')]
                        if tag_id:
                            new_node = thread_client.add_node(tag_id, hierarchy_id, parentnode_id)    # type: ignore
                            child_nodes = node.get('child_nodes')
                            for child_node_item in child_nodes:
                                addNode(child_node_item, new_node.id)

                    
                    rootnode_item = hierarchy_item.get('rootnode')
                    rootnode_tag_id = tag_id_map[rootnode_item.get('tag_id')]
                    if rootnode_tag_id:
                        rootnode_id = thread_client.add_rootnode(rootnode_tag_id, hierarchy_response.id).id   # type: ignore
                        child_nodes = rootnode_item.get('child_nodes')
                        for child_node_item in child_nodes:                    
                            addNode(child_node_item, rootnode_id)
                    hierarchies_pbar.update(1)
                    


                for hierarchy in hierarchies:
                    hierarchies_executor.submit(processHierarchy, hierarchy)

                hierarchies_executor.shutdown()

            
            # print(f"Successfully imported data from JSON file {path}")

        except FileNotFoundError:
            print(f"File not found: {path}")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
    

    def exportFile(self, path):
        start_time = time.time()
        tagsets = []
        tagsets_lock = threading.Lock()
        medias = []
        medias_lock = threading.Lock()
        hierarchies = []
        hierarchies_lock = threading.Lock()

        # response_tagsets = self.client.get_tagsets(-1)
        # tagsets_pbar = tqdm(total=0, desc="Exporting tagsets")
        # def processTagset(tagset_response):
        #     thread_client = grpc_client.LoaderClient()
        #     tags = []
        #     response_tags = thread_client.get_tags(-1, tagset_response.id)
        #     for tag_response in response_tags:
        #         if type(tag_response) is not str:                
        #             tag_id = tag_response.id                               
        #             possible_values = [tag_response.alphanumerical.value,
        #                             tag_response.timestamp.value,
        #                             tag_response.time.value,
        #                             tag_response.date.value,
        #                             tag_response.numerical.value]
        #             value = next(value for value in possible_values if value != "")
        #             tags.append({"id":tag_id, "value":value})
        #     tagsets_lock.acquire()
        #     tagsets.append(
        #         {
        #             "id"  : tagset_response.id,
        #             "name": tagset_response.name,
        #             "type": tagset_response.tagTypeId,
        #             "tags": tags
        #         })
        #     tagsets_lock.release()
        #     tagsets_pbar.update(1)

        
        # tagset_executor = ThreadPoolExecutor(max_workers=10)
        # for tagset_response in response_tagsets:
        #     if type(tagset_response) is not str:
        #         tagsets_pbar.total += 1
        #         tagsets_pbar.refresh()
        #         tagset_executor.submit(processTagset, tagset_response)

        # tagset_executor.shutdown()
        
        medias_pbar = tqdm(total=0, desc="Exporting medias")
        def processMedia(media_response):
            thread_client = grpc_client.LoaderClient()
            tag_ids = []
            tag_ids_response = thread_client.get_media_tags(media_response.id)
            if type(tag_ids_response) is not str:
                tag_ids = list(tag_ids_response)
            medias_lock.acquire()
            medias.append(
                {
                    "path":media_response.file_uri,
                    "tags":tag_ids
                }
            )
            medias_lock.release()
            medias_pbar.update(1)

        response_medias = self.client.get_medias(-1)

        medias_executor = ThreadPoolExecutor(max_workers=10)
        for media_response in response_medias:
            if type(media_response) is not str:
                medias_pbar.total += 1
                medias_pbar.refresh()
                medias_executor.submit(processMedia, media_response)
        
        medias_executor.shutdown()
                
        
        # response_hierarchies = self.client.get_hierarchies(-1)
        # hierarchies_pbar = tqdm(total=0, desc="Exporting hierarchies")
        # def processHierarchy(hierarchy_response):
        #     thread_client = grpc_client.LoaderClient()
        #     hierarchy_name = hierarchy_response.name
        #     hierarchy_tagset_id = hierarchy_response.tagSetId
        #     rootnode = thread_client.get_node(hierarchy_response.rootNodeId)
        #     def fillTree(node):
        #         child_nodes_response = thread_client.get_nodes(parentnode_id=node.id)
        #         child_nodes = []
        #         for child_node in child_nodes_response:
        #             if type(child_node) is not str:
        #                 child_nodes.append(fillTree(child_node))
        #         return {"tag_id": node.tagId, "child_nodes":child_nodes}
            
        #     filled_tree = fillTree(rootnode)
        #     hierarchies_lock.acquire()
        #     hierarchies.append({
        #         "name":hierarchy_name,
        #         "tagset_id":hierarchy_tagset_id,
        #         "rootnode": filled_tree
        #     })
        #     hierarchies_lock.release()
        #     hierarchies_pbar.update(1)

        # hierarchies_executor = ThreadPoolExecutor(max_workers=10)
        # for hierarchy_response in response_hierarchies:
        #     if type(hierarchy_response) is not str:
        #         hierarchies_pbar.total += 1
        #         hierarchies_pbar.refresh()
        #         hierarchies_executor.submit(processHierarchy, hierarchy_response)

        # hierarchies_executor.shutdown()


        data = {"tagsets": tagsets, "medias": medias, "hierarchies": hierarchies}
        print("All data loaded, dumping json file")
        with open(path, "w") as json_file:
            json.dump(data, json_file, indent=4)
        
        end_time = time.time()
        print("Elapsed time: %f seconds" % (end_time-start_time))