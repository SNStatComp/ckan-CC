Installation
------------


### Prerequisites

- Python, jinja2 
```
sudo apt-get install python-jinja2
```

- working docker installation, see https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-16-04
- postgresql client (psql). 
```
sudo apt-get install postgresql-client
```


### Installation
	
1. Build docker-images by running `./build` in ckan, psql and solr directories.
2. Start postgres and solr containers with `./run` in psql/solr directories.
3. Create databasestructures by executing `./cleandb`  script in ckan directory.
4. Start ckan container with `./run` script in ckan directory.
5. CKAN-site should be up on [http://127.0.0.1](http://127.0.0.1)
