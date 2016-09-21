from ckanapi import RemoteCKAN
import sys, csv, psycopg2, glob
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


datadir="/home/alex/test/testdata"



filelist = glob.glob(datadir+"/*.csv")
for fullpath in filelist:        
        names=fullpath.split('/')
        filename=names[-1][:-4]
        print filename

        #claircity.action.dataset_purge(id=filename)
        claircity.action.package_create (name=filename,title='testdata',notes='notes for testdata',owner_org=orglist[0])
#claircity.action.resource_create (package_id='test',name='testfile', url=' ', upload='data/Kerncijfers_Amsterdam_2015.csv')
        e=requests.post('http://127.0.0.1/api/action/resource_create',
              data={"package_id":filename,'name':'testfilekomma','url':'', 'format':'CSV'},
              headers={"X-CKAN-API-Key": apikey},
              files=[('upload', file(fullpath))])
        #print e.text
        print e.status_code
