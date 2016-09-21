from ckanapi import RemoteCKAN
import sys, csv, psycopg2, glob, random
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
grouplist=claircity.action.group_list()
#print orglist


datadir="/home/alex/ckan-CC/content/testdata"
f=open('notes.txt')
notes=f.readlines()
f.close()
notelen=len(notes)
orglen=len(orglist)
grouplen=len(grouplist)


filelist = glob.glob(datadir+"/*.csv")
for fullpath in filelist:        
        names=fullpath.split('/')
        filename=names[-1][:-4]
        

        note=notes[random.randrange(0,notelen)]
        orgnr=random.randrange(0,orglen-1)
        groupnr=random.randrange(0,grouplen-1)        
        filename_safe=filename.lower().replace("'","")
        print filename, filename_safe
        #claircity.action.dataset_purge(id=filename)        
        claircity.action.package_create (name=filename_safe,
                                         title=filename,
                                         notes=note,
                                         owner_org=orglist[orgnr],
                                         groups=[{'id':grouplist[groupnr]}])

        e=requests.post('http://127.0.0.1/api/action/resource_create',
              data={"package_id":filename,'name':filename_safe,'url':'', 'format':'CSV'},
              headers={"X-CKAN-API-Key": apikey},
              files=[('upload', file(fullpath))])
        #print e.text
        print e.status_code

