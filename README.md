### Warning
This ckan installation has been used for data portal functionality that has been *ended*. The software has not been updated for security patches since, so dont use it for a new installation. For archiving purposes it remains accessible as read-only.

Installation
------------


### Prerequisites


Create a working docker installation, see https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-16-04

Run the install script in this directory (install.sh), which contains these steps:

- Install python, jinja2, graphviz
```
sudo apt-get install python-jinja2 graphviz
```
```
sudo apt-get install postgresql-client python-psycopg2
```

```
sudo pip install ckanapi
sudo mkdir /data /src
sudo chown www-data.www-data /data /src
```

### CKAN installation

0. Put passfile in repository's top directory.
1. Set environment by running 'source config' or '. config'.
2. Build docker-images by running `./build_containers` in the directory containers
3. Start postgres and solr containers with `./run` in psql/solr directories.
4. Create databasestructures by executing `./cleandb`  script in ckan directory.
5. Start ckan container with `./run` script in ckan directory.
5. CKAN-site should be up on [http://127.0.0.1](http://127.0.0.1)
