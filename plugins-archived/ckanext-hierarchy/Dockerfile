FROM ckan/ckan

RUN . /usr/lib/ckan/default/bin/activate
WORKDIR /usr/lib/ckan/default/src/

#install plugin
RUN pip install -e "git+https://github.com/datagovuk/ckanext-hierarchy.git#egg=ckanext-hierarchy"

# Add the plugin to the ini file
RUN cat /etc/ckan/default/development.ini | \
    sed '/^ckan\.plugins/ s/$/ hierarchy_display hierarchy_form/' > tmp && \
    cp tmp /etc/ckan/default/development.ini && \
    rm tmp
