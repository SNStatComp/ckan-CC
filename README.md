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
2. Build docker-images by running `./build` in the directories found in containers-enabled (ckan, psql and solr).
3. Start postgres and solr containers with `./run` in psql/solr directories.
4. Create databasestructures by executing `./cleandb`  script in ckan directory.
5. Start ckan container with `./run` script in ckan directory.
5. CKAN-site should be up on [http://127.0.0.1](http://127.0.0.1)
