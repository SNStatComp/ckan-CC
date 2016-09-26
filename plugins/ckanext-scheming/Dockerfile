FROM ckan/claircity_theme

COPY ckanext-scheming /usr/lib/ckan/default/src/ckanext-scheming

WORKDIR /usr/lib/ckan/default/src/ckanext-scheming

RUN . /usr/lib/ckan/default/bin/activate && \
    pip install --upgrade pip && \
    python setup.py develop && \
    pip install -r requirements.txt

RUN cat /etc/ckan/default/development.ini | \
    sed '/^ckan\.plugins/ s/$/ scheming_datasets/' > tmp && \
    cp tmp /etc/ckan/default/development.ini && \
    rm tmp

ADD ./edit_development.ini.py ./edit_development.ini.py
ADD ./config.csv ./config.csv
RUN pip install configparser && \
    python edit_development.ini.py /etc/ckan/default/development.ini && \
    rm edit_development.ini.py && \
    rm config.csv
