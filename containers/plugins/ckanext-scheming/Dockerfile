FROM ckan/claircity_theme

COPY ckanext-scheming /usr/lib/ckan/default/src/ckanext-scheming

WORKDIR /usr/lib/ckan/default/src/ckanext-scheming

RUN . /usr/lib/ckan/default/bin/activate && \
    pip --proxy http://10.2.97.12:8080/ --trusted-host pypi.python.org  install --upgrade pip && \
    python setup.py develop && \
    pip --proxy http://10.2.97.12:8080/ --trusted-host pypi.python.org  install -r requirements.txt

RUN cat /etc/ckan/default/development.ini | \
    sed '/^ckan\.plugins/ s/$/ scheming_datasets scheming_facets/' > tmp && \
    cp tmp /etc/ckan/default/development.ini && \
    rm tmp

ADD ./edit_development.ini.py ./edit_development.ini.py
ADD ./config.csv ./config.csv
RUN pip --proxy http://10.2.97.12:8080/ --trusted-host pypi.python.org  install configparser && \
    python edit_development.ini.py /etc/ckan/default/development.ini && \
    rm edit_development.ini.py && \
    rm config.csv
