--
-- PostgreSQL database dump
--

-- Dumped from database version 16.8 (Debian 16.8-1.pgdg120+1)
-- Dumped by pg_dump version 16.8 (Debian 16.8-1.pgdg120+1)

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
-- Name: item; Type: TABLE; Schema: public; Owner: user
--

CREATE TABLE public.item (
    id       serial     PRIMARY KEY,
    name     text       NOT NULL,
    quantity integer    NOT NULL
);



ALTER TABLE public.item OWNER TO "user";

INSERT INTO public.item (name, quantity) VALUES ('Laptop', 15);
INSERT INTO public.item (name, quantity) VALUES ('Keyboard', 45);
INSERT INTO public.item (name, quantity) VALUES ('Mouse', 60);
INSERT INTO public.item (name, quantity) VALUES ('Monitor', 20);
INSERT INTO public.item (name, quantity) VALUES ('Desk Chair', 10);
INSERT INTO public.item (name, quantity) VALUES ('Notebook', 100);
INSERT INTO public.item (name, quantity) VALUES ('Pen', 200);
INSERT INTO public.item (name, quantity) VALUES ('Pencil', 150);
INSERT INTO public.item (name, quantity) VALUES ('USB Drive', 80);
INSERT INTO public.item (name, quantity) VALUES ('External Hard Drive', 25);
INSERT INTO public.item (name, quantity) VALUES ('Smartphone', 30);
INSERT INTO public.item (name, quantity) VALUES ('Tablet', 22);
INSERT INTO public.item (name, quantity) VALUES ('Webcam', 35);
INSERT INTO public.item (name, quantity) VALUES ('Headphones', 40);
INSERT INTO public.item (name, quantity) VALUES ('Charger', 70);
INSERT INTO public.item (name, quantity) VALUES ('Projector', 5);
INSERT INTO public.item (name, quantity) VALUES ('Whiteboard', 12);
INSERT INTO public.item (name, quantity) VALUES ('Stapler', 90);
INSERT INTO public.item (name, quantity) VALUES ('Paper Clips', 300);
INSERT INTO public.item (name, quantity) VALUES ('Calculator', 18);


INSERT INTO public.item (name, quantity) VALUES ('Laptop', 15);
INSERT INTO public.item (name, quantity) VALUES ('Keyboard', 45);
INSERT INTO public.item (name, quantity) VALUES ('Mouse', 60);
INSERT INTO public.item (name, quantity) VALUES ('Monitor', 20);
INSERT INTO public.item (name, quantity) VALUES ('Desk Chair', 10);
INSERT INTO public.item (name, quantity) VALUES ('Notebook', 100);
INSERT INTO public.item (name, quantity) VALUES ('Pen', 200);
INSERT INTO public.item (name, quantity) VALUES ('USB Drive', 80);
INSERT INTO public.item (name, quantity) VALUES ('Webcam', 35);
INSERT INTO public.item (name, quantity) VALUES ('Headphones', 40);


--
-- Data for Name: item; Type: TABLE DATA; Schema: public; Owner: user
--

COPY public.item (name, quantity) FROM stdin;
\.


--
-- PostgreSQL database dump complete
--

