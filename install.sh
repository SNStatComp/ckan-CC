sudo apt-get install python-jinja2
sudo apt-get install postgresql-client python-psycopg2
sudo pip install ckanapi

sudo mkdir /data
sudo chown www-data.www-data /data 
sudo chmod 755 /data

sudo mkdir /src
sudo chown www-data.www-data /src
sudo chmod 755 /src

(cd /src ; \
sudo wget https://github.com/ckan/ckan/archive/ckan-2.5.2.tar.gz  ; \
sudo tar zfxv ckan-2.5.2.tar.gz ; \
sudo rm -f ckan-2.5.2.tar.gz )


