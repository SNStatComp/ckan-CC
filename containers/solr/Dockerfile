FROM solr:6.0
MAINTAINER Open Knowledge

# Enviroment
ENV SOLR_CORE ckan

# User
USER root

# Create Directories
RUN mkdir -p /opt/solr/server/solr/$SOLR_CORE/conf
RUN mkdir -p /opt/solr/server/solr/$SOLR_CORE/data

# Adding Files
ADD ./config/solrconfig.xml \
    ./config/ckan-2.5.2/ckan/config/solr/schema.xml \
    ./config/solr/6.0.0/solr/server/solr/configsets/basic_configs/conf/currency.xml \
    ./config/solr/6.0.0/solr/server/solr/configsets/basic_configs/conf/synonyms.txt \
    ./config/solr/6.0.0/solr/server/solr/configsets/basic_configs/conf/stopwords.txt \
    ./config/solr/6.0.0/solr/server/solr/configsets/basic_configs/conf/protwords.txt \
    ./config/solr/6.0.0/solr/server/solr/configsets/data_driven_schema_configs/conf/elevate.xml \
/opt/solr/server/solr/$SOLR_CORE/conf/

# Create Core.properties
RUN echo name=$SOLR_CORE > /opt/solr/server/solr/$SOLR_CORE/core.properties

# Giving ownership to Solr
RUN chown -R $SOLR_USER:$SOLR_USER /opt/solr/server/solr/$SOLR_CORE

