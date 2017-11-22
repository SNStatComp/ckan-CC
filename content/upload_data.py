from ckanapi import RemoteCKAN
import sys, csv, psycopg2
import requests


def get_apikey(username):
	conn = psycopg2.connect("dbname='ckan_default' user='postgres' host='172.17.0.1'")
	handle=conn.cursor()
	handle.execute("select apikey from ckan_default.public.user where name='%s';" % username)
	rows=handle.fetchall();
	apikey=rows[0][0];
	handle.close()
	conn.close()
	return apikey


username='default'
if len(sys.argv)>1:
	username=sys.argv[1]
apikey=get_apikey(username)


claircity = RemoteCKAN('http://127.0.0.1', apikey=apikey, user_agent='importjob')

orglist=claircity.action.organization_list()
packagelist=claircity.action.package_list()
#print orglist
try:
        claircity.action.dataset_purge(id='test')
except:
        pass
claircity.action.package_create (name='test',title='testdata',notes='notes for testdata',owner_org=orglist[0], city='Aveiro')

e=requests.post('http://127.0.0.1/api/action/resource_create',
              data={"package_id":"test",'name':'testfile','url':'', 'format':'CSV','city':' Aveiro' },
              headers={"X-CKAN-API-Key": apikey},
              files=[('upload', file('data/Kerncijfers_Amsterdam_2015.csv'))])
e=requests.post('http://127.0.0.1/api/action/resource_create',
              data={"package_id":"test",'name':'testfilekomma','url':'', 'format':'CSV'},
              headers={"X-CKAN-API-Key": apikey},
              files=[('upload', file('data/k.csv'))])
print e.text
print e.status_code
