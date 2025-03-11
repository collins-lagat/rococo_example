-- PostgreSQL 15
-- Create tables
-- Organization
CREATE TABLE public.organization (
    entity_id CHARACTER VARYING(32) PRIMARY KEY,
    version CHARACTER VARYING(32) NOT NULL,
    previous_version CHARACTER VARYING(32),
    active BOOLEAN NOT NULL,
    changed_by_id CHARACTER VARYING(32) NOT NULL,
    changed_on TIMESTAMP NOT NULL,
    name CHARACTER VARYING(255),
    code CHARACTER VARYING(255),
    description CHARACTER VARYING(255)
);

CREATE TABLE public.organization_audit (
    entity_id CHARACTER VARYING(32) PRIMARY KEY,
    version CHARACTER VARYING(32) NOT NULL,
    previous_version CHARACTER VARYING(32),
    active BOOLEAN NOT NULL,
    changed_by_id CHARACTER VARYING(32) NOT NULL,
    changed_on TIMESTAMP NOT NULL,
    name CHARACTER VARYING(255),
    code CHARACTER VARYING(255),
    description CHARACTER VARYING(255)
);

-- Person
CREATE TABLE public.person (
    entity_id CHARACTER VARYING(32) PRIMARY KEY,
    version CHARACTER VARYING(32) NOT NULL,
    previous_version CHARACTER VARYING(32),
    active BOOLEAN NOT NULL,
    changed_by_id CHARACTER VARYING(32) NOT NULL,
    changed_on TIMESTAMP NOT NULL,
    first_name CHARACTER VARYING(255),
    last_name CHARACTER VARYING(255)
);

CREATE TABLE public.person_audit (
    entity_id CHARACTER VARYING(32) PRIMARY KEY,
    version CHARACTER VARYING(32) NOT NULL,
    previous_version CHARACTER VARYING(32),
    active BOOLEAN NOT NULL,
    changed_by_id CHARACTER VARYING(32) NOT NULL,
    changed_on TIMESTAMP NOT NULL,
    first_name CHARACTER VARYING(255),
    last_name CHARACTER VARYING(255)
);

-- Email
CREATE TABLE public.email (
    entity_id CHARACTER VARYING(32) PRIMARY KEY,
    version CHARACTER VARYING(32) NOT NULL,
    previous_version CHARACTER VARYING(32),
    active BOOLEAN NOT NULL,
    changed_by_id CHARACTER VARYING(32) NOT NULL,
    changed_on TIMESTAMP NOT NULL,
    person CHARACTER VARYING(32) NOT NULL,
    email CHARACTER VARYING(255),
    is_verified BOOLEAN,
    is_default BOOLEAN
);

CREATE TABLE public.email_audit (
    entity_id CHARACTER VARYING(32) PRIMARY KEY,
    version CHARACTER VARYING(32) NOT NULL,
    previous_version CHARACTER VARYING(32),
    active BOOLEAN NOT NULL,
    changed_by_id CHARACTER VARYING(32) NOT NULL,
    changed_on TIMESTAMP NOT NULL,
    person CHARACTER VARYING(32) NOT NULL,
    email CHARACTER VARYING(255),
    is_verified BOOLEAN,
    is_default BOOLEAN
);

-- Person Organization Role
CREATE TABLE public.person_organization_role (
    entity_id CHARACTER VARYING(32) PRIMARY KEY,
    version CHARACTER VARYING(32) NOT NULL,
    previous_version CHARACTER VARYING(32),
    active BOOLEAN NOT NULL,
    changed_by_id CHARACTER VARYING(32) NOT NULL,
    changed_on TIMESTAMP NOT NULL,
    person CHARACTER VARYING(32) NOT NULL,
    organization CHARACTER VARYING(32) NOT NULL,
    role CHARACTER VARYING(255)
);

CREATE TABLE public.person_organization_role_audit (
    entity_id CHARACTER VARYING(32) PRIMARY KEY,
    version CHARACTER VARYING(32) NOT NULL,
    previous_version CHARACTER VARYING(32),
    active BOOLEAN NOT NULL,
    changed_by_id CHARACTER VARYING(32) NOT NULL,
    changed_on TIMESTAMP NOT NULL,
    person CHARACTER VARYING(32) NOT NULL,
    secret CHARACTER VARYING(255),
    name CHARACTER VARYING(255),
    enabled BOOLEAN
);

-- OTP Method
CREATE TABLE public.otp_method (
    entity_id CHARACTER VARYING(32) PRIMARY KEY,
    version CHARACTER VARYING(32) NOT NULL,
    previous_version CHARACTER VARYING(32),
    active BOOLEAN NOT NULL,
    changed_by_id CHARACTER VARYING(32) NOT NULL,
    changed_on TIMESTAMP NOT NULL,
    person CHARACTER VARYING(32) NOT NULL,
    secret CHARACTER VARYING(255),
    name CHARACTER VARYING(255),
    enabled BOOLEAN
);

CREATE TABLE public.otp_method_audit (
    entity_id CHARACTER VARYING(32) PRIMARY KEY,
    version CHARACTER VARYING(32) NOT NULL,
    previous_version CHARACTER VARYING(32),
    active BOOLEAN NOT NULL,
    changed_by_id CHARACTER VARYING(32) NOT NULL,
    changed_on TIMESTAMP NOT NULL,
    person CHARACTER VARYING(32) NOT NULL,
    secret CHARACTER VARYING(255),
    name CHARACTER VARYING(255),
    enabled BOOLEAN
);

-- Recovery Code
CREATE TABLE public.recovery_code (
    entity_id CHARACTER VARYING(32) PRIMARY KEY,
    version CHARACTER VARYING(32) NOT NULL,
    previous_version CHARACTER VARYING(32),
    active BOOLEAN NOT NULL,
    changed_by_id CHARACTER VARYING(32) NOT NULL,
    changed_on TIMESTAMP NOT NULL,
    otp_method CHARACTER VARYING(32) NOT NULL,
    secret CHARACTER VARYING(255),
    name CHARACTER VARYING(255),
    enabled BOOLEAN
);

CREATE TABLE public.recovery_code_audit (
    entity_id CHARACTER VARYING(32) PRIMARY KEY,
    version CHARACTER VARYING(32) NOT NULL,
    previous_version CHARACTER VARYING(32),
    active BOOLEAN NOT NULL,
    changed_by_id CHARACTER VARYING(32) NOT NULL,
    changed_on TIMESTAMP NOT NULL,
    otp_method CHARACTER VARYING(32) NOT NULL,
    secret CHARACTER VARYING(255),
    name CHARACTER VARYING(255),
    enabled BOOLEAN
);

-- Login Method
CREATE TABLE public.login_method (
    entity_id CHARACTER VARYING(32) PRIMARY KEY,
    version CHARACTER VARYING(32) NOT NULL,
    previous_version CHARACTER VARYING(32),
    active BOOLEAN NOT NULL,
    changed_by_id CHARACTER VARYING(32) NOT NULL,
    changed_on TIMESTAMP NOT NULL,
    person CHARACTER VARYING(32) NOT NULL,
    method_type CHARACTER VARYING(255),
    method_data TEXT,
    email CHARACTER VARYING(32) NOT NULL,
    PASSWORD CHARACTER VARYING(255) NOT NULL
);

CREATE TABLE public.login_method_audit (
    entity_id CHARACTER VARYING(32) PRIMARY KEY,
    version CHARACTER VARYING(32) NOT NULL,
    previous_version CHARACTER VARYING(32),
    active BOOLEAN NOT NULL,
    changed_by_id CHARACTER VARYING(32) NOT NULL,
    changed_on TIMESTAMP NOT NULL,
    person CHARACTER VARYING(32) NOT NULL,
    method_type CHARACTER VARYING(255),
    method_data TEXT,
    email CHARACTER VARYING(32) NOT NULL,
    PASSWORD CHARACTER VARYING(255) NOT NULL
);
