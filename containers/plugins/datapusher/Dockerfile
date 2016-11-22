FROM ckan/ckan


RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    build-essential \
    libxslt1-dev \
    libxml2-dev 
WORKDIR /usr/lib/ckan/default/
RUN . /usr/lib/ckan/default/bin/activate

# Install Datapusher plugin
RUN mkdir -p /home/install

RUN virtualenv --never-download /usr/lib/ckan/datapusher 
RUN mkdir /usr/lib/ckan/datapusher/src
WORKDIR /usr/lib/ckan/datapusher/src


RUN git clone -b stable https://github.com/ckan/datapusher.git
WORKDIR /usr/lib/ckan/datapusher/src/datapusher
RUN /usr/lib/ckan/datapusher/bin/pip install  --proxy http://10.2.97.12:8080/ --trusted-host pypi.python.org --upgrade setuptools
RUN /usr/lib/ckan/datapusher/bin/pip install  --proxy http://10.2.97.12:8080/ --trusted-host pypi.python.org -r requirements.txt
RUN /usr/lib/ckan/datapusher/bin/python setup.py develop

#copy the standard Apache config file
# (use deployment/datapusher.apache2-4.conf if you are running under Apache 2.4)
RUN cp deployment/datapusher.apache2-4.conf /etc/apache2/sites-available/datapusher.conf

#copy the standard DataPusher wsgi file
#(see note below if you are not using the default CKAN install location)
RUN cp deployment/datapusher.wsgi /etc/ckan/

#copy the standard DataPusher settings.
RUN cp deployment/datapusher_settings.py /etc/ckan/

#open up port 8800 on Apache where the DataPusher accepts connections.
#make sure you only run these 2 functions once otherwise you will need
#to manually edit /etc/apache2/ports.conf.
RUN sh -c 'echo "NameVirtualHost *:8800" >> /etc/apache2/ports.conf'
RUN sh -c 'echo "Listen 8800" >> /etc/apache2/ports.conf'

#enable DataPusher Apache site
RUN a2ensite datapusher
#replace ckan.ini with our ckan.ini

ADD ./dev.ini /etc/ckan/default/development.ini
