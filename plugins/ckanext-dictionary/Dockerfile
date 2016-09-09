FROM ckan/organization-hierarchy

WORKDIR /usr/lib/ckan/default/
RUN . /usr/lib/ckan/default/bin/activate

# install plugin
RUN git clone https://github.com/cmuphillycapstone/ckanext-dictionary.git && \
    cd ckanext-dictionary && \
    python setup.py develop && \
    pip install -r dev-requirements.txt

RUN cat /etc/ckan/default/development.ini | \
    sed '/^ckan\.plugins/ s/$/ dictionary/' > tmp && \
    cp tmp /etc/ckan/default/development.ini && \
    rm tmp
