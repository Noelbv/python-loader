import json
import csv
import datetime
import os
import time
import grpc_client
import threading


class FileHandler:
    def __init__(self) -> None:
        self.client  = grpc_client.LoaderClient()

class FastJSONHandler(FileHandler):
    def addNode(self, node, tagset_id, tagtype_id, hierarchy_id, parentnode_id):
        tag_value = node.get('tag_value')
        if tag_value:
            tag = self.client.add_tag(tagset_id, tagtype_id, tag_value)
            new_node = self.client.add_node(tag.id, hierarchy_id, parentnode_id)    # type: ignore
            child_nodes = node.get('child_nodes')
            for child_node_item in child_nodes:
                self.addNode(child_node_item, tagset_id, tagtype_id, hierarchy_id, new_node.id)

    def importFile(self, path):
        try:
            with open(path, 'r') as file:
                data = json.load(file)
                tagsets = data.get('tagsets', [])
                tagset_id_map = {}
                tag_id_map = {}                

                def processTagset(tagset_item, iterator):
                    tagset_name = tagset_item.get('name')
                    tagset_type = tagset_item.get('type')
                    tagset_response = self.client.add_tagset(tagset_name, tagset_type)
                    if type(tagset_response) is str:
                        print(f"Invalid item in tagsets: {tagset_item}")
                        return
                    
                    tagset_id_map[iterator] = (tagset_response.id, tagset_response.tagTypeId)

                    for tag_item in tagset_item.get('tags'):
                        value = tag_item.get('value') 
                        tag_response = self.client.add_tag(tagset_response.id, tagset_type, value)
                        if type(tag_response) is str:
                            print(f"Invalid item in tagset {tagset_name} : {tag_response}")
                            continue

                        tag_id_map[tag_item.get('id')] = tag_response.id    #type: ignore

                iterator = 0
                for tagset_item in tagsets:
                    iterator += 1
                    processTagset(tagset_item, iterator)
                
                    

                medias = data.get('medias', [])
                for media_item in medias:
                    media_path = media_item.get('path')
                    media_response = self.client.add_file(media_path)
                    if type(media_response) is str:
                        print(f"Invalid item in medias: {media_item}")
                        continue
                    tags = media_item.get('tags', [])
                    for tag_id in tags:
                        self.client.add_tagging(media_id=media_response.id, tag_id=tag_id) 


                # hierarchies = data.get('hierarchies', [])
                # for hierarchy in hierarchies:
                #     name = hierarchy.get('name')
                #     tagset_id = tagset_id_map[hierarchy.get('tagset_id')][0]
                #     tagtype_id = tagset_id_map[hierarchy.get('tagset_id')][1]
                #     if name and tagset_id:
                #         hierarchy_response = self.client.add_hierarchy(name, tagset_id)
                #         rootnode_item = hierarchy.get('rootnode')
                #         rootnode_tag_value = rootnode_item.get('tag_value')
                #         if rootnode_tag_value:
                #             rootnode_tag = self.client.add_tag(tagset_id, tagtype_id, rootnode_tag_value)
                #             rootnode_id = self.client.add_rootnode(rootnode_tag.id, hierarchy_response.id).id   # type: ignore
                #             child_nodes = rootnode_item.get('child_nodes')
                #             for child_node_item in child_nodes:                    
                #                 self.addNode(child_node_item, tagset_id, tagtype_id, hierarchy_response.id, rootnode_id)

                #     else:
                #         print(f"Invalid item in medias: {hierarchy}")
            
            print(f"Successfully imported data from JSON file {path}")

        except FileNotFoundError:
            print(f"File not found: {path}")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")

    def multithreadedImportFile(self, path):
        try:
            with open(path, 'r') as file:
                data = json.load(file)
                tagsets = data.get('tagsets', [])
                tagset_id_map = {}
                tag_id_map = {}
                tagset_threads = []
                tagset_id_map_lock = threading.Lock()
                tag_id_map_lock = threading.Lock()
                

                def processTagset(tagset_item, iterator):
                    tagset_name = tagset_item.get('name')
                    tagset_type = tagset_item.get('type')
                    tagset_response = self.client.add_tagset(tagset_name, tagset_type)
                    if type(tagset_response) is str:
                        print(f"Invalid item in tagsets: {tagset_item}")
                        return

                    tagset_id_map_lock.acquire()
                    tagset_id_map[iterator] = (tagset_response.id, tagset_response.tagTypeId)
                    tagset_id_map_lock.release()

                    for tag_item in tagset_item.get('tags'):
                        value = tag_item.get('value') 
                        tag_response = self.client.add_tag(tagset_response.id, tagset_type, value)
                        if type(tag_response) is str:
                            print(f"Invalid item in tagset {tagset_name} : {tag_response}")
                            continue

                        tag_id_map_lock.acquire()
                        tag_id_map[tag_item.get('id')] = tag_response.id    #type: ignore
                        tag_id_map_lock.release()

                iterator = 0
                for tagset_item in tagsets:
                    iterator += 1
                    thread = threading.Thread(target=processTagset, args=(tagset_item, iterator))
                    thread.start()
                    tagset_threads.append(thread)
                
                for thread in tagset_threads:
                    thread.join()
                    

                medias = data.get('medias', [])
                for media_item in medias:
                    media_path = media_item.get('path')
                    media_response = self.client.add_file(media_path)
                    if type(media_response) is str:
                        print(f"Invalid item in medias: {media_item}")
                        continue
                    tags = media_item.get('tags', [])
                    for tag_id in tags:
                        self.client.add_tagging(media_id=media_response.id, tag_id=tag_id) 


                # hierarchies = data.get('hierarchies', [])
                # for hierarchy in hierarchies:
                #     name = hierarchy.get('name')
                #     tagset_id = tagset_id_map[hierarchy.get('tagset_id')][0]
                #     tagtype_id = tagset_id_map[hierarchy.get('tagset_id')][1]
                #     if name and tagset_id:
                #         hierarchy_response = self.client.add_hierarchy(name, tagset_id)
                #         rootnode_item = hierarchy.get('rootnode')
                #         rootnode_tag_value = rootnode_item.get('tag_value')
                #         if rootnode_tag_value:
                #             rootnode_tag = self.client.add_tag(tagset_id, tagtype_id, rootnode_tag_value)
                #             rootnode_id = self.client.add_rootnode(rootnode_tag.id, hierarchy_response.id).id   # type: ignore
                #             child_nodes = rootnode_item.get('child_nodes')
                #             for child_node_item in child_nodes:                    
                #                 self.addNode(child_node_item, tagset_id, tagtype_id, hierarchy_response.id, rootnode_id)

                #     else:
                #         print(f"Invalid item in medias: {hierarchy}")
            
            print(f"Successfully imported data from JSON file {path}")

        except FileNotFoundError:
            print(f"File not found: {path}")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
    
    def fillTree(self, node):
        child_nodes_response = self.client.get_nodes(parentnode_id=node.id)
        child_nodes = []
        for child_node in child_nodes_response:
            if type(child_node) is not str:
                child_nodes.append(self.fillTree(child_node))
        return {"tag_id": node.tagId, "child_nodes":child_nodes}

    def exportFile(self, path):
        start_time = time.time()
        tagsets = []
        medias = []
        hierarchies = []
        response_tagsets = self.client.get_tagsets(-1)
        for tagset_response in response_tagsets:
            if type(tagset_response) is not str:
                tags = []
                response_tags = self.client.get_tags(-1, tagset_response.id)
                for tag_response in response_tags:
                    if type(tag_response) is not str:                
                        tag_id = tag_response.id                               
                        possible_values = [tag_response.alphanumerical.value,
                                        tag_response.timestamp.value,
                                        tag_response.time.value,
                                        tag_response.date.value,
                                        tag_response.numerical.value]
                        value = next(value for value in possible_values if value != "")
                        tags.append({"id":tag_id, "value":value})
                tagsets.append(
                    {
                        "name": tagset_response.name,
                        "type": tagset_response.tagTypeId,
                        "tags": tags
                    })
        
        response_medias = self.client.get_medias(-1)
        for media_response in response_medias:
            if type(media_response) is not str:
                tag_ids = []
                tag_ids_response = self.client.get_media_tags(media_response.id)
                if type(tag_ids_response) is not str:
                    tag_ids = list(tag_ids_response)
                medias.append(
                    {
                        "path":media_response.file_uri,
                        "tags":tag_ids
                    }
                )
        
        # response_hierarchies = self.client.get_hierarchies(-1)
        # for hierarchy_response in response_hierarchies:
        #     if type(hierarchy_response) is not str:
        #         hierarchy_name = hierarchy_response.name
        #         hierarchy_tagset_id = hierarchy_response.tagSetId
        #         rootnode = self.client.get_node(hierarchy_response.rootNodeId)
        #         filled_tree = self.fillTree(rootnode)
        #         hierarchies.append({
        #             "name":hierarchy_name,
        #             "tagset_id":hierarchy_tagset_id,
        #             "rootnode": filled_tree
        #         })

        data = {"tagsets": tagsets, "medias": medias, "hierarchies": hierarchies}
        print("All data loaded, dumping json file")
        with open(path, "w") as json_file:
            json.dump(data, json_file, indent=4)
        
        end_time = time.time()
        print("Elapsed time: %f seconds" % (end_time-start_time))



class JSONHandler(FileHandler):

    def addNode(self, node, tagset_id, tagtype_id, hierarchy_id, parentnode_id):
        tag_value = node.get('tag_value')
        if tag_value:
            tag = self.client.add_tag(tagset_id, tagtype_id, tag_value)
            new_node = self.client.add_node(tag.id, hierarchy_id, parentnode_id)    # type: ignore
            child_nodes = node.get('child_nodes')
            for child_node_item in child_nodes:
                self.addNode(child_node_item, tagset_id, tagtype_id, hierarchy_id, new_node.id)


    def importFile(self, path):
        try:
            with open(path, 'r') as file:
                data = json.load(file)
                tagsets = data.get('tagsets', [])
                id_map = {}
                iterator = 0
                for tagset_item in tagsets:
                    iterator += 1
                    tagset_name = tagset_item.get('name')
                    tagset_type = tagset_item.get('type')
                    if tagset_name and tagset_type:
                        response = self.client.add_tagset(tagset_name, tagset_type)
                        id_map[iterator] = (response.id, response.tagTypeId)                        
                    else:
                        print(f"Invalid item in tagsets: {tagset_item}")

                medias = data.get('medias', [])
                for media_item in medias:
                    media_path = media_item.get('path')
                    if media_path:
                        media_response = self.client.add_file(media_path)
                        tags = media_item.get('tags', [])
                        for tag_item in tags:
                            tagset_id = id_map[tag_item.get('tagset_id')][0]
                            tagtype_id = id_map[tag_item.get('tagset_id')][1]
                            value = tag_item.get('value')
                            tag_response = self.client.add_tag(tagset_id, tagtype_id, value)
                            if type(tag_response) is not str:
                                self.client.add_tagging(media_id=media_response.id, tag_id=tag_response.id) # type: ignore
                    else:
                        print(f"Invalid item in medias: {media_item}")

                hierarchies = data.get('hierarchies', [])
                for hierarchy in hierarchies:
                    name = hierarchy.get('name')
                    tagset_id = id_map[hierarchy.get('tagset_id')][0]
                    tagtype_id = id_map[hierarchy.get('tagset_id')][1]
                    if name and tagset_id:
                        hierarchy_response = self.client.add_hierarchy(name, tagset_id)
                        rootnode_item = hierarchy.get('rootnode')
                        rootnode_tag_value = rootnode_item.get('tag_value')
                        if rootnode_tag_value:
                            rootnode_tag = self.client.add_tag(tagset_id, tagtype_id, rootnode_tag_value)
                            rootnode_id = self.client.add_rootnode(rootnode_tag.id, hierarchy_response.id).id   # type: ignore
                            child_nodes = rootnode_item.get('child_nodes')
                            for child_node_item in child_nodes:                    
                                self.addNode(child_node_item, tagset_id, tagtype_id, hierarchy_response.id, rootnode_id)

                    else:
                        print(f"Invalid item in medias: {hierarchy}")
            
            print(f"Successfully imported data from JSON file {path}")

        except FileNotFoundError:
            print(f"File not found: {path}")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")



    def fillTree(self, node):
        tag_response = self.client.get_tag(node.tagId)
        possible_values = [tag_response.alphanumerical.value,           # type: ignore
                                    tag_response.timestamp.value,                # type: ignore
                                    tag_response.time.value,                     # type: ignore
                                    tag_response.date.value,                     # type: ignore
                                    tag_response.numerical.value]                # type: ignore
        value = next(value for value in possible_values if value != "")
        child_nodes_response = self.client.get_nodes(parentnode_id=node.id)
        child_nodes = []
        for child_node in child_nodes_response:
            if type(child_node) is not str:                         # cheap way to check that we did not get an error
                child_nodes.append(self.fillTree(child_node))
        return {"tag_value": value, "child_nodes":child_nodes}


    def exportFile(self, path):
        tagsets = []
        medias = []
        hierarchies = []

        response_tagsets = self.client.get_tagsets(-1)
        for tagset_response in response_tagsets:
            if type(tagset_response) is not str:
                tagsets.append(
                    {"name": tagset_response.name,      # type: ignore
                    "type": tagset_response.tagTypeId   # type: ignore
                    })
        
        response_medias = self.client.get_medias(-1)
        for media_response in response_medias:
            if type(media_response) is not str:
                media_path = media_response.file_uri
                tags = []
                tag_ids = self.client.get_media_tags(media_response.id)          # type: ignore
                if type(tag_ids) is not str:   
                    for id_tag in tag_ids:
                        tag_response = self.client.get_tag(id_tag)                     
                        tagset_id = tag_response.tagSetId                               # type: ignore
                        possible_values = [tag_response.alphanumerical.value,           # type: ignore
                                        tag_response.timestamp.value,                # type: ignore
                                        tag_response.time.value,                     # type: ignore
                                        tag_response.date.value,                     # type: ignore
                                        tag_response.numerical.value]                # type: ignore
                        value = next(value for value in possible_values if value != "")     # Due to grpc standrads, the numerical value won't be Null if not initialised, 
                                                                                            # but zero. Thus we take advantage of the fact that it is the last possible value and
                                                                                            # that only one value can be set for a specified tag

                        tags.append({"tagset_id":tagset_id, "value":value})

                medias.append({"path": media_path, "tags": tags})

        response_hierarchies = self.client.get_hierarchies(-1)
        for hierarchy_response in response_hierarchies:
            if type(hierarchy_response) is not str:
                hierarchy_name = hierarchy_response.name
                hierarchy_tagset_id = hierarchy_response.tagSetId
                rootnode = self.client.get_node(hierarchy_response.rootNodeId)
                filled_tree = self.fillTree(rootnode)
                hierarchies.append({
                    "name":hierarchy_name,
                    "tagset_id":hierarchy_tagset_id,
                    "rootnode": filled_tree
                })

        data = {"tagsets": tagsets, "medias": medias, "hierarchies": hierarchies}
        print("All data loaded, dumping json file")
        with open(path, "w") as json_file:
            json.dump(data, json_file, indent=4)

    



class CSVHandler(FileHandler):

    def importFile(self, path):
        try:
            with open(path, 'r') as file:
                reader = csv.reader(file, delimiter=';')
                first_line = next(reader)
                id_map = {}
                iterator = 0

                # Process the first line, i.e the tagsets
                # The syntax is [tagset_name_1];[tagset_type_1];[tagset_name_2];[tagset_type_2]...
                current_name = None
                for item in first_line:
                    if item and current_name is None:
                        iterator += 1
                        current_name = item
                    elif item.isdigit() and current_name is not None:
                        response = self.client.add_tagset(current_name, int(item))
                        if type(response) is dict: # If the tagset already exists
                            response = self.client.get_tagset_by_name(current_name)
                        id_map[iterator] = (response.id, response.tagTypeId)                            # type: ignore
                        current_name = None
                    else:
                        print(f"Invalid item in tagsets: {tagset_item}")                  # type: ignore

                # We the process the following lines, containing medias and their tags: 
                # Syntax: [path];[id_tag1];[value1];[id_tag2];[value2]...[id_tagN];[valueN]
                iterator = 1
                for row in reader:
                    try:
                        iterator += 1
                        if not row:
                            continue        # Skip empty rows
                        path = row[0]
                        media_response = self.client.add_file(path)
                        if not media_response.id:                       # type: ignore
                            raise Exception(f"Invalid media, could not add to DB")
                        for i in range(1, len(row), 2):
                            tagset_id = id_map[int(row[i])][0]          # we have to use the correct tagset_id in db
                            tagtype_id = id_map[int(row[i])][1]
                            if (not tagset_id) or (not tagtype_id):
                                raise Exception(f"Invalid tag definition: {tagset_id}:{tagtype_id}")
                            value = row[i+1]
                            tag_response = self.client.add_tag(tagset_id, tagtype_id, value)
                            if not tag_response.id:                     # type: ignore
                                raise Exception("Could not add tag")
                            tagging_response = self.client.add_tagging(media_id=media_response.id, tag_id=tag_response.id) # type: ignore
                            if not tagging_response.mediaId:            # type: ignore
                                raise Exception("Could not add tag")
                    except Exception as e:
                        print(f"Error at line {iterator}: {e}")

        except FileNotFoundError:
            print(f"File not found: {path}")


    def exportFile(self, path):
        self.client = grpc_client.LoaderClient()
        tagsets = []
        medias = []

        # Prepare the header line with tagset names and types
        header = []
        response_tagsets = self.client.get_tagsets(-1)
        for tagset_response in response_tagsets:
            header.extend([f"\"{tagset_response.name}\"", f"{tagset_response.tagTypeId}"]) # type: ignore
            
        # Write the data to the CSV file
        with open(path, "w", newline="", encoding="UTF-8") as file:
            csv_writer = csv.writer(file, delimiter=";", quoting=csv.QUOTE_NONE, escapechar='', quotechar='')
            csv_writer.writerow(header)


            response_medias = self.client.get_medias(-1)
            for media_response in response_medias:
                path = media_response.file_uri                              # type: ignore
                row = [f'\"{path}\"']
                tag_ids = self.client.get_media_tags(media_response.id)          # type: ignore
                for id_tag in tag_ids:
                    tag_response = self.client.get_tag(int(id_tag))                      # type: ignore
                    tagset_id = tag_response.tagSetId                               # type: ignore
                    possible_values = [tag_response.alphanumerical.value,           # type: ignore
                                    tag_response.timestamp.value,                # type: ignore
                                    tag_response.time.value,                     # type: ignore
                                    tag_response.date.value,                     # type: ignore
                                    tag_response.numerical.value]                # type: ignore
                    value = next(value for value in possible_values if value != "")
                    row.extend([f'{tagset_id}', f'\"{value}\"'])
                    
                csv_writer.writerow(row)
