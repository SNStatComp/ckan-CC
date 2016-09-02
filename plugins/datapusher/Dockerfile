FROM ckan/ckan

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    apt-utils

WORKDIR /usr/lib/ckan/default/
RUN . /usr/lib/ckan/default/bin/activate

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
ADD ./development.ini /etc/ckan/default/development.ini
