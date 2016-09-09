FROM ckan/datapusher

# Copy the plugin to the container
COPY ckanext-claircity_theme /usr/lib/ckan/default/src/ckanext-claircity_theme

WORKDIR /usr/lib/ckan/default/src/ckanext-claircity_theme

# Install the plugin
RUN . /usr/lib/ckan/default/bin/activate && \
    python setup.py develop && \
    pip install -r dev-requirements.txt 

# Add the plugin to the ini file
RUN cat /etc/ckan/default/development.ini | \
    sed '/^ckan\.plugins/ s/$/ claircity_theme/' > tmp && \
    cp tmp /etc/ckan/default/development.ini && \
    rm tmp
