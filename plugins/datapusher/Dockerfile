FROM ckan260

# Solution for 500 internal server error running default CKAN container:
#   upgrade setuptools
RUN DEBIAN_FRONTEND=noninteractive apt-get update
RUN echo "#!/bin/sh\nexit 0" > /usr/sbin/policy-rc.d
RUN . /usr/lib/ckan/default/bin/activate
RUN $CKAN_HOME/bin/pip install --upgrade -r $CKAN_HOME/src/ckan/requirements.txt

# Install Datapusher plugin
RUN mkdir -p /home/install
RUN DEBIAN_FRONTEND=noninteractive apt-get -q -y install \
    python-dev \
    python-virtualenv \
    build-essential \
    libxslt1-dev \
    libxml2-dev \
    git

ADD ./install_datapusher.sh /home/install/install_datapusher.sh
RUN chmod +x /home/install/install_datapusher.sh
RUN /home/install/install_datapusher.sh

#replace ckan.ini with our ckan.ini
ADD ./ckan.ini $CKAN_CONFIG/ckan.ini
