#!/bin/bash
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<-EOSQL
--   CREATE USER "ckan_user" WITH PASSWORD 'pass';
--   CREATE DATABASE "ckan_default" OWNER "ckan_user";
    \connect ckan_default

EOSQL