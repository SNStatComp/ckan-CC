FROM ckan/data_dictionaries
RUN apt-get update && \
    apt-get install -y redis-server

WORKDIR /usr/lib/ckan/default/
RUN . /usr/lib/ckan/default/bin/activate
RUN pip install configparser && \
    pip install -e git+https://github.com/ckan/ckanext-harvest.git#egg=ckanext-harvest && \
    cd /usr/lib/ckan/default/src/ckanext-harvest/ && \
    pip install -r pip-requirements.txt

RUN cat /etc/ckan/default/development.ini | \
    sed '/^ckan\.plugins/ s/$/ harvest ckan_harvester/' > tmp && \
    cp tmp /etc/ckan/default/development.ini && \
    rm tmp

ADD ./edit_development.ini.py ./edit_development.ini.py
ADD ./config.csv ./config.csv
RUN python edit_development.ini.py /etc/ckan/default/development.ini && \
    rm edit_development.ini.py && \
    rm config.csv

#RUN paster --plugin=ckanext-harvest harvester initdb --config=/etc/ckan/default/development.ini
