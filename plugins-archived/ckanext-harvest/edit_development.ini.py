import configparser, csv, sys

config = configparser.ConfigParser(allow_no_values = True)

dev_ini = '/etc/ckan/default/development.ini'
if len(sys.argv)>1:
	dev_ini = sys.argv[1]

config.read(dev_ini)

configfile = open(dev_ini, 'w')

with open('config.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        config[row['section']][row['option']] = row['value']

config.write(configfile)
