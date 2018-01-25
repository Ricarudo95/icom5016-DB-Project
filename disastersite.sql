--
-- PostgreSQL database dump
--

-- Dumped from database version 10.1
-- Dumped by pg_dump version 10.1

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: administrator; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE administrator (
    a_id integer NOT NULL,
    r_id integer,
    afirstname character varying(10),
    alastname character varying(20),
    pass character varying(20)
);


ALTER TABLE administrator OWNER TO postgres;

--
-- Name: administrator_a_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE administrator_a_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE administrator_a_id_seq OWNER TO postgres;

--
-- Name: administrator_a_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE administrator_a_id_seq OWNED BY administrator.a_id;


--
-- Name: creditcard; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE creditcard (
    c_id integer NOT NULL,
    u_id integer,
    first_name character varying(10),
    last_name character varying(20),
    card_number integer,
    expiration_date date,
    cvc_code integer
);


ALTER TABLE creditcard OWNER TO postgres;

--
-- Name: creditcard_c_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE creditcard_c_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE creditcard_c_id_seq OWNER TO postgres;

--
-- Name: creditcard_c_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE creditcard_c_id_seq OWNED BY creditcard.c_id;


--
-- Name: reciept; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE reciept (
    rs_id integer NOT NULL,
    u_id integer,
    total_price double precision
);


ALTER TABLE reciept OWNER TO postgres;

--
-- Name: reciept_rs_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE reciept_rs_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE reciept_rs_id_seq OWNER TO postgres;

--
-- Name: reciept_rs_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE reciept_rs_id_seq OWNED BY reciept.rs_id;


--
-- Name: request; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE request (
    rq_id integer NOT NULL,
    u_id integer,
    r_id integer,
    qty_request integer
);


ALTER TABLE request OWNER TO postgres;

--
-- Name: request_rq_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE request_rq_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE request_rq_id_seq OWNER TO postgres;

--
-- Name: request_rq_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE request_rq_id_seq OWNED BY request.rq_id;


--
-- Name: resource; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE resource (
    r_id integer NOT NULL,
    s_id integer,
    rname character varying(20),
    category character varying(20),
    quantity integer,
    price double precision
);


ALTER TABLE resource OWNER TO postgres;

--
-- Name: resource_r_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE resource_r_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE resource_r_id_seq OWNER TO postgres;

--
-- Name: resource_r_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE resource_r_id_seq OWNED BY resource.r_id;


--
-- Name: siteuser; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE siteuser (
    u_id integer NOT NULL,
    ufirstname character varying(10),
    ulastname character varying(20),
    pass character varying(20),
    loc character varying(20),
    ua_id integer
);


ALTER TABLE siteuser OWNER TO postgres;

--
-- Name: siteuser_u_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE siteuser_u_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE siteuser_u_id_seq OWNER TO postgres;

--
-- Name: siteuser_u_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE siteuser_u_id_seq OWNED BY siteuser.u_id;


--
-- Name: stransaction; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE stransaction (
    t_id integer NOT NULL,
    c_id integer,
    item_name character varying(20),
    quantity integer,
    price double precision,
    r_id integer,
    u_id integer,
    a_id integer
);


ALTER TABLE stransaction OWNER TO postgres;

--
-- Name: stransaction_t_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE stransaction_t_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE stransaction_t_id_seq OWNER TO postgres;

--
-- Name: stransaction_t_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE stransaction_t_id_seq OWNED BY stransaction.t_id;


--
-- Name: supplier; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE supplier (
    s_id integer NOT NULL,
    sname character varying(20),
    pass character varying(20),
    loc character varying(20),
    sa_id integer
);


ALTER TABLE supplier OWNER TO postgres;

--
-- Name: supplier_s_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE supplier_s_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE supplier_s_id_seq OWNER TO postgres;

--
-- Name: supplier_s_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE supplier_s_id_seq OWNED BY supplier.s_id;


--
-- Name: supplieraddress; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE supplieraddress (
    sa_id integer NOT NULL,
    location_name character varying(20),
    region character varying(20),
    city character varying(20),
    zip_code integer
);


ALTER TABLE supplieraddress OWNER TO postgres;

--
-- Name: supplieraddress_sa_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE supplieraddress_sa_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE supplieraddress_sa_id_seq OWNER TO postgres;

--
-- Name: supplieraddress_sa_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE supplieraddress_sa_id_seq OWNED BY supplieraddress.sa_id;


--
-- Name: test; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE test (
    id integer
);


ALTER TABLE test OWNER TO postgres;

--
-- Name: useraddress; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE useraddress (
    ua_id integer NOT NULL,
    location_name character varying(20),
    region character varying(20),
    city character varying(20),
    zip_code integer
);


ALTER TABLE useraddress OWNER TO postgres;

--
-- Name: useraddress_ua_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE useraddress_ua_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE useraddress_ua_id_seq OWNER TO postgres;

--
-- Name: useraddress_ua_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE useraddress_ua_id_seq OWNED BY useraddress.ua_id;


--
-- Name: administrator a_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY administrator ALTER COLUMN a_id SET DEFAULT nextval('administrator_a_id_seq'::regclass);


--
-- Name: creditcard c_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY creditcard ALTER COLUMN c_id SET DEFAULT nextval('creditcard_c_id_seq'::regclass);


--
-- Name: reciept rs_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY reciept ALTER COLUMN rs_id SET DEFAULT nextval('reciept_rs_id_seq'::regclass);


--
-- Name: request rq_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY request ALTER COLUMN rq_id SET DEFAULT nextval('request_rq_id_seq'::regclass);


--
-- Name: resource r_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY resource ALTER COLUMN r_id SET DEFAULT nextval('resource_r_id_seq'::regclass);


--
-- Name: siteuser u_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY siteuser ALTER COLUMN u_id SET DEFAULT nextval('siteuser_u_id_seq'::regclass);


--
-- Name: stransaction t_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY stransaction ALTER COLUMN t_id SET DEFAULT nextval('stransaction_t_id_seq'::regclass);


--
-- Name: supplier s_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY supplier ALTER COLUMN s_id SET DEFAULT nextval('supplier_s_id_seq'::regclass);


--
-- Name: supplieraddress sa_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY supplieraddress ALTER COLUMN sa_id SET DEFAULT nextval('supplieraddress_sa_id_seq'::regclass);


--
-- Name: useraddress ua_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY useraddress ALTER COLUMN ua_id SET DEFAULT nextval('useraddress_ua_id_seq'::regclass);


--
-- Data for Name: administrator; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY administrator (a_id, r_id, afirstname, alastname, pass) FROM stdin;
\.


--
-- Data for Name: creditcard; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY creditcard (c_id, u_id, first_name, last_name, card_number, expiration_date, cvc_code) FROM stdin;
\.


--
-- Data for Name: reciept; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY reciept (rs_id, u_id, total_price) FROM stdin;
\.


--
-- Data for Name: request; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY request (rq_id, u_id, r_id, qty_request) FROM stdin;
\.


--
-- Data for Name: resource; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY resource (r_id, s_id, rname, category, quantity, price) FROM stdin;
2	1	dasani	agua	10	1
3	1	cocacola	bebida	0	1.5
4	1	medalla	bebida	99	1.25
5	2	medalla	bebida	45	1.2
6	3	medalla	bebida	200	1
7	3	agua	bebida	10000	0.5
\.


--
-- Data for Name: siteuser; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY siteuser (u_id, ufirstname, ulastname, pass, loc, ua_id) FROM stdin;
1	Ricardo	Rodriguez	123	SJ	\N
2	Nelson	Martinez	321	Arecibo	\N
3	Angelica	Santiago	345	Maya	\N
\.


--
-- Data for Name: stransaction; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY stransaction (t_id, c_id, item_name, quantity, price, r_id, u_id, a_id) FROM stdin;
1	\N	medalla	25	25	6	1	\N
\.


--
-- Data for Name: supplier; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY supplier (s_id, sname, pass, loc, sa_id) FROM stdin;
1	Costco	pass	SJ	\N
2	Telco	pass2	Maya	\N
3	Sams	pass2	Maya	\N
\.


--
-- Data for Name: supplieraddress; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY supplieraddress (sa_id, location_name, region, city, zip_code) FROM stdin;
\.


--
-- Data for Name: test; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY test (id) FROM stdin;
1
3
\.


--
-- Data for Name: useraddress; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY useraddress (ua_id, location_name, region, city, zip_code) FROM stdin;
\.


--
-- Name: administrator_a_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('administrator_a_id_seq', 1, false);


--
-- Name: creditcard_c_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('creditcard_c_id_seq', 1, false);


--
-- Name: reciept_rs_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('reciept_rs_id_seq', 1, false);


--
-- Name: request_rq_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('request_rq_id_seq', 1, false);


--
-- Name: resource_r_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('resource_r_id_seq', 7, true);


--
-- Name: siteuser_u_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('siteuser_u_id_seq', 3, true);


--
-- Name: stransaction_t_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('stransaction_t_id_seq', 1, true);


--
-- Name: supplier_s_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('supplier_s_id_seq', 3, true);


--
-- Name: supplieraddress_sa_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('supplieraddress_sa_id_seq', 1, false);


--
-- Name: useraddress_ua_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('useraddress_ua_id_seq', 1, false);


--
-- Name: administrator administrator_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY administrator
    ADD CONSTRAINT administrator_pkey PRIMARY KEY (a_id);


--
-- Name: creditcard creditcard_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY creditcard
    ADD CONSTRAINT creditcard_pkey PRIMARY KEY (c_id);


--
-- Name: reciept reciept_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY reciept
    ADD CONSTRAINT reciept_pkey PRIMARY KEY (rs_id);


--
-- Name: request request_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY request
    ADD CONSTRAINT request_pkey PRIMARY KEY (rq_id);


--
-- Name: resource resource_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY resource
    ADD CONSTRAINT resource_pkey PRIMARY KEY (r_id);


--
-- Name: siteuser siteuser_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY siteuser
    ADD CONSTRAINT siteuser_pkey PRIMARY KEY (u_id);


--
-- Name: stransaction stransaction_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY stransaction
    ADD CONSTRAINT stransaction_pkey PRIMARY KEY (t_id);


--
-- Name: supplier supplier_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY supplier
    ADD CONSTRAINT supplier_pkey PRIMARY KEY (s_id);


--
-- Name: supplieraddress supplieraddress_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY supplieraddress
    ADD CONSTRAINT supplieraddress_pkey PRIMARY KEY (sa_id);


--
-- Name: useraddress useraddress_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY useraddress
    ADD CONSTRAINT useraddress_pkey PRIMARY KEY (ua_id);


--
-- Name: administrator administrator_r_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY administrator
    ADD CONSTRAINT administrator_r_id_fkey FOREIGN KEY (r_id) REFERENCES resource(r_id);


--
-- Name: creditcard creditcard_u_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY creditcard
    ADD CONSTRAINT creditcard_u_id_fkey FOREIGN KEY (u_id) REFERENCES siteuser(u_id);


--
-- Name: reciept reciept_u_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY reciept
    ADD CONSTRAINT reciept_u_id_fkey FOREIGN KEY (u_id) REFERENCES siteuser(u_id);


--
-- Name: request request_r_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY request
    ADD CONSTRAINT request_r_id_fkey FOREIGN KEY (r_id) REFERENCES resource(r_id);


--
-- Name: request request_u_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY request
    ADD CONSTRAINT request_u_id_fkey FOREIGN KEY (u_id) REFERENCES siteuser(u_id);


--
-- Name: resource resource_s_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY resource
    ADD CONSTRAINT resource_s_id_fkey FOREIGN KEY (s_id) REFERENCES supplier(s_id);


--
-- Name: siteuser siteuser_ua_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY siteuser
    ADD CONSTRAINT siteuser_ua_id_fkey FOREIGN KEY (ua_id) REFERENCES useraddress(ua_id);


--
-- Name: stransaction stransaction_a_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY stransaction
    ADD CONSTRAINT stransaction_a_id_fkey FOREIGN KEY (a_id) REFERENCES administrator(a_id);


--
-- Name: stransaction stransaction_c_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY stransaction
    ADD CONSTRAINT stransaction_c_id_fkey FOREIGN KEY (c_id) REFERENCES creditcard(c_id);


--
-- Name: stransaction stransaction_r_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY stransaction
    ADD CONSTRAINT stransaction_r_id_fkey FOREIGN KEY (r_id) REFERENCES resource(r_id);


--
-- Name: stransaction stransaction_u_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY stransaction
    ADD CONSTRAINT stransaction_u_id_fkey FOREIGN KEY (u_id) REFERENCES siteuser(u_id);


--
-- Name: supplier supplier_sa_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY supplier
    ADD CONSTRAINT supplier_sa_id_fkey FOREIGN KEY (sa_id) REFERENCES supplieraddress(sa_id);


--
-- PostgreSQL database dump complete
--

