FROM phusion/baseimage

ADD ./config/bash.bashrc /etc/bash.bashrc
ADD ./config/apt.conf  /etc/apt/apt.conf
ADD ./config/environment /etc/environment

ADD ./config/cbsp_root.crt /usr/local/share/ca-certificates/cbsp_root.crt
RUN update-ca-certificates

RUN apt-get update && apt-get install -y \
	apt-utils python-dev libpq-dev python-pip git-core sudo \
	python-polib \
	python-pastescript \
	apache2 libapache2-mod-wsgi libapache2-mod-rpaf nginx \
&& rm -rf /var/lib/apt/lists/*

RUN mkdir /usr/lib/ckan
RUN mkdir /etc/ckan

RUN mkdir -p /usr/lib/ckan/default
RUN chown root /usr/lib/ckan/default
RUN pip --proxy http://10.2.97.12:8080/ install --upgrade pip
RUN pip --proxy http://10.2.97.12:8080/ --trusted-host pypi.python.org install virtualenv

WORKDIR /usr/lib/ckan/default/
RUN virtualenv -v --no-site-packages /usr/lib/ckan/default

ADD ./config/git_2.7.4-0ubuntu1_amd64.deb /tmp/git_2.7.4-0ubuntu1_amd64.deb
ADD ./config/libcurl4-openssl-dev_7.47.0-1ubuntu2.2_amd64.deb /tmp/libcurl4-openssl-dev_7.47.0-1ubuntu2.2_amd64.deb
ADD ./config/libcurl3_7.47.0-1ubuntu2.2_amd64.deb /tmp/libcurl3_7.47.0-1ubuntu2.2_amd64.deb
RUN apt-get install /tmp/libcurl3_7.47.0-1ubuntu2.2_amd64.deb
RUN apt-get install /tmp/libcurl4-openssl-dev_7.47.0-1ubuntu2.2_amd64.deb 
RUN apt-get install /tmp/git_2.7.4-0ubuntu1_amd64.deb -y --allow-downgrades

RUN . /usr/lib/ckan/default/bin/activate
RUN pip --proxy http://10.2.97.12:8080/ install -e 'git+https://github.com/ckan/ckan.git@ckan-2.5.2#egg=ckan'

RUN pip --proxy http://10.2.97.12:8080/ --trusted-host pypi.python.org install -r /usr/lib/ckan/default/src/ckan/requirements.txt
RUN mkdir -p /etc/ckan/default && chown -R `whoami` /etc/ckan/
RUN pip uninstall -y paste
RUN pip uninstall -y pastedeploy
RUN pip --proxy http://10.2.97.12:8080/ --trusted-host pypi.python.org install --upgrade paste
RUN pip --proxy http://10.2.97.12:8080/ --trusted-host pypi.python.org install pastedeploy

#RUN pip install setuptools==20.4
RUN pip --proxy http://10.2.97.12:8080/ --trusted-host pypi.python.org  install pylons==0.9.7
RUN pip --proxy http://10.2.97.12:8080/ --trusted-host pypi.python.org install webob==1.0.8
RUN pip --proxy http://10.2.97.12:8080/ --trusted-host pypi.python.org install html5lib==0.999
RUN pip --proxy http://10.2.97.12:8080/ --trusted-host pypi.python.org install ckanapi

# move to data volume
#RUN mkdir /var/lib/ckan
#RUN chmod 755 /var/lib/ckan
#RUN chown www-data:www-data /var/lib/ckan

ADD ./config/dev.ini /etc/ckan/default/development.ini
ADD ./config/who.ini /etc/ckan/default/who.ini

WORKDIR /usr/lib/ckan/default/src/ckan

#RUN paster db init -c /etc/ckan/default/development.ini


ADD ./config/apache.wsgi /etc/ckan/default/apache.wsgi
ADD ./config/ckan.conf /etc/apache2/sites-available/ckan.conf
ADD ./config/apache2.conf /etc/apache2/apache2.conf
ADD ./config/ports.conf  /etc/apache2/ports.conf

#ADD ./nginx.conf  /etc/nginx/sites-available/ckan
ADD ./config/nginx.conf  /etc/nginx/nginx.conf
RUN mkdir /var/cache/nginx

RUN a2ensite ckan
RUN a2dissite 000-default
#RUN rm -f /etc/nginx/sites-enabled/default
#RUN ln -s /etc/nginx/sites-available/ckan /etc/nginx/sites-enabled/ckan


RUN chown www-data:www-data /etc/ckan/default/apache.wsgi

EXPOSE 80 5000

ADD ./config/contrib/docker/svc /etc/service
#CMD ["paster","serve","/etc/ckan/default/development.ini"]

ADD layout/favicon.ico /usr/lib/ckan/default/src/ckan/ckan/public/base/images/favicon.ico
ADD layout/logo_color.svg /usr/lib/ckan/default/src/ckan/ckan/public/base/images/clair-city-logo.svg

# patch the recline view to replace deprecated mapquest map tiles               
# possible alternatives are: OSM, OSM_HOT, STAMEN, WMFLABS                      
ADD ./patches/OSM map_tile_patch                                                
RUN patch /usr/lib/ckan/default/src/ckan/ckanext/reclineview/theme/public/vendor/recline/recline.js map_tile_patch && rm map_tile_patch

WORKDIR /var/log/nginx
CMD ["/sbin/my_init"]
