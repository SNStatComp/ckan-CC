#!/bin/bash
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<-EOSQL
   CREATE USER "datastore_user" WITH PASSWORD 'pass';
   CREATE DATABASE "datastore_default" OWNER "ckan_user";
    \connect datastore_default

    -- revoke permissions for the read-only user
    REVOKE CREATE ON SCHEMA public FROM PUBLIC;
    REVOKE USAGE ON SCHEMA public FROM PUBLIC;

    GRANT CREATE ON SCHEMA public TO "ckan_user";
    GRANT USAGE ON SCHEMA public TO "ckan_user";

    GRANT CREATE ON SCHEMA public TO "ckan_user";
    GRANT USAGE ON SCHEMA public TO "ckan_user";

    -- take connect permissions from main db
    REVOKE CONNECT ON DATABASE "ckan_default" FROM "datastore_user";

    -- grant select permissions for read-only user
    GRANT CONNECT ON DATABASE "datastore_default" TO "datastore_user";
    GRANT USAGE ON SCHEMA public TO "datastore_user";

    -- grant access to current tables and views to read-only user
    GRANT SELECT ON ALL TABLES IN SCHEMA public TO "datastore_user";

    -- grant access to new tables and views by default
    ALTER DEFAULT PRIVILEGES FOR USER "ckan_user" IN SCHEMA public
    GRANT SELECT ON TABLES TO "datastore_user";
EOSQL