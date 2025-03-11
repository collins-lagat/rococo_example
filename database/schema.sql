-- PostgreSQL 15
-- Create tables
-- Organization
CREATE TABLE public.organization (
    enity_id CHARACTER VARYING(32) PRIMARY KEY,
    version CHARACTER VARYING(32) NOT NULL,
    pervious_version CHARACTER VARYING(32),
    active BOOLEAN NOT NULL,
    changed_by_id CHARACTER VARYING(32) NOT NULL,
    changed_on TIMESTAMP NOT NULL,
    name CHARACTER VARYING(255) NOT NULL,
    code CHARACTER VARYING(255) NOT NULL,
    description CHARACTER VARYING(255) NOT NULL
);

-- Person
CREATE TABLE public.person (
    enity_id CHARACTER VARYING(32) PRIMARY KEY,
    version CHARACTER VARYING(32) NOT NULL,
    pervious_version CHARACTER VARYING(32),
    active BOOLEAN NOT NULL,
    changed_by_id CHARACTER VARYING(32) NOT NULL,
    changed_on TIMESTAMP NOT NULL,
    first_name CHARACTER VARYING(255) NOT NULL,
    last_name CHARACTER VARYING(255) NOT NULL
);

-- Email
CREATE TABLE public.email (
    enity_id CHARACTER VARYING(32) PRIMARY KEY,
    version CHARACTER VARYING(32) NOT NULL,
    pervious_version CHARACTER VARYING(32),
    active BOOLEAN NOT NULL,
    changed_by_id CHARACTER VARYING(32) NOT NULL,
    changed_on TIMESTAMP NOT NULL,
    person CHARACTER VARYING(32) NOT NULL,
    email CHARACTER VARYING(255) NOT NULL,
    is_verified BOOLEAN NOT NULL,
    is_default BOOLEAN NOT NULL
);

-- Person Organization Role
CREATE TABLE public.person_organization_role (
    enity_id CHARACTER VARYING(32) PRIMARY KEY,
    version CHARACTER VARYING(32) NOT NULL,
    pervious_version CHARACTER VARYING(32),
    active BOOLEAN NOT NULL,
    changed_by_id CHARACTER VARYING(32) NOT NULL,
    changed_on TIMESTAMP NOT NULL,
    person CHARACTER VARYING(32) NOT NULL,
    organization CHARACTER VARYING(32) NOT NULL,
    role CHARACTER VARYING(255) NOT NULL
);

-- OTP Method
CREATE TABLE public.otp_method (
    enity_id CHARACTER VARYING(32) PRIMARY KEY,
    version CHARACTER VARYING(32) NOT NULL,
    pervious_version CHARACTER VARYING(32),
    active BOOLEAN NOT NULL,
    changed_by_id CHARACTER VARYING(32) NOT NULL,
    changed_on TIMESTAMP NOT NULL,
    person CHARACTER VARYING(32) NOT NULL,
    secret CHARACTER VARYING(255) NOT NULL,
    name CHARACTER VARYING(255) NOT NULL,
    enabled BOOLEAN NOT NULL
);

-- Recovery Code
CREATE TABLE public.recovery_code (
    enity_id CHARACTER VARYING(32) PRIMARY KEY,
    version CHARACTER VARYING(32) NOT NULL,
    pervious_version CHARACTER VARYING(32),
    active BOOLEAN NOT NULL,
    changed_by_id CHARACTER VARYING(32) NOT NULL,
    changed_on TIMESTAMP NOT NULL,
    otp_method CHARACTER VARYING(32) NOT NULL,
    secret CHARACTER VARYING(255) NOT NULL,
    name CHARACTER VARYING(255) NOT NULL,
    enabled BOOLEAN NOT NULL
);

-- Login Method
CREATE TABLE public.login_method (
    enity_id CHARACTER VARYING(32) PRIMARY KEY,
    version CHARACTER VARYING(32) NOT NULL,
    pervious_version CHARACTER VARYING(32),
    active BOOLEAN NOT NULL,
    changed_by_id CHARACTER VARYING(32) NOT NULL,
    changed_on TIMESTAMP NOT NULL,
    person CHARACTER VARYING(32) NOT NULL,
    method_type CHARACTER VARYING(255),
    method_data TEXT,
    email CHARACTER VARYING(32) NOT NULL,
    PASSWORD CHARACTER VARYING(255) NOT NULL
);
