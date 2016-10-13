drop database if exists ckan_default ;
drop role if exists ckan_user;
CREATE USER "ckan_user" with password 'pass';
CREATE DATABASE "ckan_default" OWNER "ckan_user";