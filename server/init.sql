--
-- PostgreSQL database dump
--

DROP SCHEMA public CASCADE;
CREATE SCHEMA public;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO public;

-- Dumped from database version 13.4
-- Dumped by pg_dump version 13.4

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: __EFMigrationsHistory; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."__EFMigrationsHistory" (
    "MigrationId" character varying(150) NOT NULL,
    "ProductVersion" character varying(32) NOT NULL
);


ALTER TABLE public."__EFMigrationsHistory" OWNER TO postgres;

--
-- Name: alphanumerical_tags; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.alphanumerical_tags (
    id integer NOT NULL,
    name text,
    tagset_id integer NOT NULL
);


ALTER TABLE public.alphanumerical_tags OWNER TO postgres;

--
-- Name: alphanumerical_tags_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.alphanumerical_tags ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.alphanumerical_tags_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: cubeobjects; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.cubeobjects (
    id integer NOT NULL,
    file_uri text,
    file_type integer NOT NULL,
    thumbnail_uri text
);


ALTER TABLE public.cubeobjects OWNER TO postgres;

--
-- Name: cubeobjects_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.cubeobjects ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.cubeobjects_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: date_tags; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.date_tags (
    id integer NOT NULL,
    name date NOT NULL,
    tagset_id integer NOT NULL
);


ALTER TABLE public.date_tags OWNER TO postgres;

--
-- Name: date_tags_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.date_tags ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.date_tags_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: hierarchies; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.hierarchies (
    id integer NOT NULL,
    name text,
    tagset_id integer NOT NULL,
    rootnode_id integer NOT NULL
);


ALTER TABLE public.hierarchies OWNER TO postgres;

--
-- Name: hierarchies_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.hierarchies ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.hierarchies_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: nodes; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.nodes (
    id integer NOT NULL,
    tag_id integer NOT NULL,
    hierarchy_id integer NOT NULL,
    parentnode_id integer
);


ALTER TABLE public.nodes OWNER TO postgres;

--
-- Name: nodes_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.nodes ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.nodes_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: numerical_tags; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.numerical_tags (
    id integer NOT NULL,
    name integer NOT NULL,
    tagset_id integer NOT NULL
);


ALTER TABLE public.numerical_tags OWNER TO postgres;

--
-- Name: numerical_tags_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.numerical_tags ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.numerical_tags_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: objecttagrelations; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.objecttagrelations (
    object_id integer NOT NULL,
    tag_id integer NOT NULL
);


ALTER TABLE public.objecttagrelations OWNER TO postgres;

--
-- Name: tag_types; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tag_types (
    id integer NOT NULL,
    description text
);


ALTER TABLE public.tag_types OWNER TO postgres;

--
-- Name: tag_types_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.tag_types ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.tag_types_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: tags; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tags (
    id integer NOT NULL,
    tagtype_id integer NOT NULL,
    tagset_id integer NOT NULL
);


ALTER TABLE public.tags OWNER TO postgres;

--
-- Name: tags_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.tags ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.tags_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: tagsets; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tagsets (
    id integer NOT NULL,
    name text,
    tagtype_id integer NOT NULL
);


ALTER TABLE public.tagsets OWNER TO postgres;

--
-- Name: tagsets_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.tagsets ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.tagsets_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: time_tags; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.time_tags (
    id integer NOT NULL,
    name time without time zone NOT NULL,
    tagset_id integer NOT NULL
);


ALTER TABLE public.time_tags OWNER TO postgres;

--
-- Name: time_tags_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.time_tags ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.time_tags_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: timestamp_tags; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.timestamp_tags (
    id integer NOT NULL,
    name timestamp without time zone NOT NULL,
    tagset_id integer NOT NULL
);


ALTER TABLE public.timestamp_tags OWNER TO postgres;

--
-- Name: timestamp_tags_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.timestamp_tags ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.timestamp_tags_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);

--
-- Name: alphanumerical_tags_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.alphanumerical_tags_id_seq', 1, false);


--
-- Name: cubeobjects_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.cubeobjects_id_seq', 1, false);


--
-- Name: date_tags_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.date_tags_id_seq', 1, false);


--
-- Name: hierarchies_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.hierarchies_id_seq', 1, false);


--
-- Name: nodes_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.nodes_id_seq', 1, false);


--
-- Name: numerical_tags_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.numerical_tags_id_seq', 1, false);


--
-- Name: tag_types_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tag_types_id_seq', 1, false);


--
-- Name: tags_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tags_id_seq', 1, false);


--
-- Name: tagsets_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tagsets_id_seq', 1, false);


--
-- Name: time_tags_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.time_tags_id_seq', 1, false);


--
-- Name: timestamp_tags_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.timestamp_tags_id_seq', 1, false);


--
-- Name: __EFMigrationsHistory PK___EFMigrationsHistory; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."__EFMigrationsHistory"
    ADD CONSTRAINT "PK___EFMigrationsHistory" PRIMARY KEY ("MigrationId");


--
-- Name: alphanumerical_tags PK_alphanumerical_tags; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.alphanumerical_tags
    ADD CONSTRAINT "PK_alphanumerical_tags" PRIMARY KEY (id);


--
-- Name: cubeobjects PK_cubeobjects; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cubeobjects
    ADD CONSTRAINT "PK_cubeobjects" PRIMARY KEY (id);


--
-- Name: date_tags PK_date_tags; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.date_tags
    ADD CONSTRAINT "PK_date_tags" PRIMARY KEY (id);


--
-- Name: hierarchies PK_hierarchies; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.hierarchies
    ADD CONSTRAINT "PK_hierarchies" PRIMARY KEY (id);


--
-- Name: nodes PK_nodes; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.nodes
    ADD CONSTRAINT "PK_nodes" PRIMARY KEY (id);


--
-- Name: numerical_tags PK_numerical_tags; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.numerical_tags
    ADD CONSTRAINT "PK_numerical_tags" PRIMARY KEY (id);


--
-- Name: objecttagrelations PK_objecttagrelations; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.objecttagrelations
    ADD CONSTRAINT "PK_objecttagrelations" PRIMARY KEY (object_id, tag_id);


--
-- Name: tag_types PK_tag_types; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tag_types
    ADD CONSTRAINT "PK_tag_types" PRIMARY KEY (id);


--
-- Name: tags PK_tags; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tags
    ADD CONSTRAINT "PK_tags" PRIMARY KEY (id);


--
-- Name: tagsets PK_tagsets; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tagsets
    ADD CONSTRAINT "PK_tagsets" PRIMARY KEY (id);


--
-- Name: time_tags PK_time_tags; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.time_tags
    ADD CONSTRAINT "PK_time_tags" PRIMARY KEY (id);


--
-- Name: timestamp_tags PK_timestamp_tags; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.timestamp_tags
    ADD CONSTRAINT "PK_timestamp_tags" PRIMARY KEY (id);


--
-- Name: IX_alphanumerical_tags_tagset_id_name; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX "IX_alphanumerical_tags_tagset_id_name" ON public.alphanumerical_tags USING btree (tagset_id, name);


--
-- Name: IX_date_tags_tagset_id_name; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX "IX_date_tags_tagset_id_name" ON public.date_tags USING btree (tagset_id, name);


--
-- Name: IX_hierarchies_tagset_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX "IX_hierarchies_tagset_id" ON public.hierarchies USING btree (tagset_id);


--
-- Name: IX_nodes_hierarchy_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX "IX_nodes_hierarchy_id" ON public.nodes USING btree (hierarchy_id);


--
-- Name: IX_nodes_parentnode_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX "IX_nodes_parentnode_id" ON public.nodes USING btree (parentnode_id);


--
-- Name: IX_nodes_tag_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX "IX_nodes_tag_id" ON public.nodes USING btree (tag_id);


--
-- Name: IX_numerical_tags_tagset_id_name; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX "IX_numerical_tags_tagset_id_name" ON public.numerical_tags USING btree (tagset_id, name);


--
-- Name: IX_objecttagrelations_tag_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX "IX_objecttagrelations_tag_id" ON public.objecttagrelations USING btree (tag_id);


--
-- Name: IX_tags_tagset_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX "IX_tags_tagset_id" ON public.tags USING btree (tagset_id);


--
-- Name: IX_tags_tagtype_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX "IX_tags_tagtype_id" ON public.tags USING btree (tagtype_id);


--
-- Name: IX_tagsets_name; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX "IX_tagsets_name" ON public.tagsets USING btree (name);


--
-- Name: IX_time_tags_tagset_id_name; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX "IX_time_tags_tagset_id_name" ON public.time_tags USING btree (tagset_id, name);


--
-- Name: IX_timestamp_tags_tagset_id_name; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX "IX_timestamp_tags_tagset_id_name" ON public.timestamp_tags USING btree (tagset_id, name);


--
-- Name: alphanumerical_tags FK_alphanumerical_tags_tags_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.alphanumerical_tags
    ADD CONSTRAINT "FK_alphanumerical_tags_tags_id" FOREIGN KEY (id) REFERENCES public.tags(id) ON DELETE CASCADE;


--
-- Name: alphanumerical_tags FK_alphanumerical_tags_tagsets_tagset_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.alphanumerical_tags
    ADD CONSTRAINT "FK_alphanumerical_tags_tagsets_tagset_id" FOREIGN KEY (tagset_id) REFERENCES public.tagsets(id) ON DELETE CASCADE;


--
-- Name: date_tags FK_date_tags_tags_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.date_tags
    ADD CONSTRAINT "FK_date_tags_tags_id" FOREIGN KEY (id) REFERENCES public.tags(id) ON DELETE CASCADE;


--
-- Name: date_tags FK_date_tags_tagsets_tagset_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.date_tags
    ADD CONSTRAINT "FK_date_tags_tagsets_tagset_id" FOREIGN KEY (tagset_id) REFERENCES public.tagsets(id) ON DELETE CASCADE;


--
-- Name: hierarchies FK_hierarchies_tagsets_tagset_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.hierarchies
    ADD CONSTRAINT "FK_hierarchies_tagsets_tagset_id" FOREIGN KEY (tagset_id) REFERENCES public.tagsets(id) ON DELETE CASCADE;


--
-- Name: nodes FK_nodes_hierarchies_hierarchy_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.nodes
    ADD CONSTRAINT "FK_nodes_hierarchies_hierarchy_id" FOREIGN KEY (hierarchy_id) REFERENCES public.hierarchies(id) ON DELETE CASCADE;


--
-- Name: nodes FK_nodes_nodes_parentnode_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.nodes
    ADD CONSTRAINT "FK_nodes_nodes_parentnode_id" FOREIGN KEY (parentnode_id) REFERENCES public.nodes(id) ON DELETE RESTRICT;


--
-- Name: nodes FK_nodes_tags_tag_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.nodes
    ADD CONSTRAINT "FK_nodes_tags_tag_id" FOREIGN KEY (tag_id) REFERENCES public.tags(id) ON DELETE RESTRICT;


--
-- Name: numerical_tags FK_numerical_tags_tags_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.numerical_tags
    ADD CONSTRAINT "FK_numerical_tags_tags_id" FOREIGN KEY (id) REFERENCES public.tags(id) ON DELETE CASCADE;


--
-- Name: numerical_tags FK_numerical_tags_tagsets_tagset_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.numerical_tags
    ADD CONSTRAINT "FK_numerical_tags_tagsets_tagset_id" FOREIGN KEY (tagset_id) REFERENCES public.tagsets(id) ON DELETE CASCADE;


--
-- Name: objecttagrelations FK_objecttagrelations_cubeobjects_object_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.objecttagrelations
    ADD CONSTRAINT "FK_objecttagrelations_cubeobjects_object_id" FOREIGN KEY (object_id) REFERENCES public.cubeobjects(id) ON DELETE CASCADE;


--
-- Name: objecttagrelations FK_objecttagrelations_tags_tag_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.objecttagrelations
    ADD CONSTRAINT "FK_objecttagrelations_tags_tag_id" FOREIGN KEY (tag_id) REFERENCES public.tags(id) ON DELETE CASCADE;


--
-- Name: tags FK_tags_tag_types_tagtype_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tags
    ADD CONSTRAINT "FK_tags_tag_types_tagtype_id" FOREIGN KEY (tagtype_id) REFERENCES public.tag_types(id) ON DELETE CASCADE;


--
-- Name: tags FK_tags_tagsets_tagset_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tags
    ADD CONSTRAINT "FK_tags_tagsets_tagset_id" FOREIGN KEY (tagset_id) REFERENCES public.tagsets(id) ON DELETE CASCADE;


--
-- Name: tags FK_tags_tagsets_tagset_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tagsets
    ADD CONSTRAINT "FK_tagsests_tag_types_tagtype_id" FOREIGN KEY (tagtype_id) REFERENCES public.tag_types(id) ON DELETE CASCADE;


--
-- Name: time_tags FK_time_tags_tags_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.time_tags
    ADD CONSTRAINT "FK_time_tags_tags_id" FOREIGN KEY (id) REFERENCES public.tags(id) ON DELETE CASCADE;


--
-- Name: time_tags FK_time_tags_tagsets_tagset_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.time_tags
    ADD CONSTRAINT "FK_time_tags_tagsets_tagset_id" FOREIGN KEY (tagset_id) REFERENCES public.tagsets(id) ON DELETE CASCADE;


--
-- Name: timestamp_tags FK_timestamp_tags_tags_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.timestamp_tags
    ADD CONSTRAINT "FK_timestamp_tags_tags_id" FOREIGN KEY (id) REFERENCES public.tags(id) ON DELETE CASCADE;


--
-- Name: timestamp_tags FK_timestamp_tags_tagsets_tagset_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.timestamp_tags
    ADD CONSTRAINT "FK_timestamp_tags_tagsets_tagset_id" FOREIGN KEY (tagset_id) REFERENCES public.tagsets(id) ON DELETE CASCADE;


--
-- PostgreSQL database dump complete
--

INSERT INTO public.tag_types (id, description) 
VALUES 
(1, 'alphanumerical'),
(2, 'timestamp'),
(3, 'time'),
(4, 'date'),
(5, 'numerical');
COMMIT;
