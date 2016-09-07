FROM ckan/ckan

COPY ckanext-claircity_theme /usr/lib/ckan/default/src/ckanext-claircity_theme

WORKDIR /usr/lib/ckan/default/src/ckanext-claircity_theme

RUN . /usr/lib/ckan/default/bin/activate && \
  python setup.py develop && \
  cat /etc/ckan/default/development.ini | \
    sed '/^ckan\.plugins/ s/$/ claircity_theme/' > \
      /etc/ckan/default/development.ini

#CMD ["/sbin/my_init"]
