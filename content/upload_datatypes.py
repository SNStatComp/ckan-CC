from ckanapi import RemoteCKAN
import os, sys, csv, psycopg2, glob, random
import requests




datadir=os.path.abspath ('./testdata/') 

def get_apikey(username):
	conn = psycopg2.connect("dbname='ckan_default' user='postgres' host='172.17.0.1'")
	handle=conn.cursor()
	handle.execute("select apikey from ckan_default.public.user where name='%s';" % username)
	rows=handle.fetchall();
	apikey=rows[0][0];
	handle.close()
	conn.close()
	return apikey


def get_meta():
        orglist=claircity.action.organization_list()
        packagelist=claircity.action.package_list()
        grouplist=claircity.action.group_list()
        voclist=claircity.action.vocabulary_list()

        citylist=[]
        for v in voclist:
                if v['name']=='cities' :
                        citylist=v['tags']

        f=open('notes.txt')
        notes=f.readlines()
        f.close()

        return orglist, packagelist, grouplist, voclist, citylist, notes

        
username='default'
if len(sys.argv)>1:
	username=sys.argv[1]
apikey=get_apikey(username)

claircity = RemoteCKAN('http://127.0.0.1', apikey=apikey, user_agent='importjob')


orglist, package_list, grouplist, voclist, citylist, notes=get_meta()
notelen=len(notes)
orglen=len(orglist)
grouplen=len(grouplist)
citylen=len(citylist)




filelist = glob.glob(datadir+"/test_private*.csv")

print 'files:', filelist
for fullpath in filelist:       
        names=fullpath.split('/')
        filename=names[-1][:-4]
        filename_safe=filename.lower().replace("'","")
        print filename, filename_safe
        if filename_safe in package_list:
                print 'package already exists, purging'
                #claircity.action.package_delete(id=filename)
                claircity.action.dataset_purge(id=filename_safe)                

        note=notes[random.randrange(0,notelen)]
        orgnr=random.randrange(0,orglen-1)
        groupnr=random.randrange(0,grouplen-1)
        citynr=random.randrange(0,citylen-1)        
        
        
        try:
                claircity.action.package_create (name=filename_safe,
                                         title=filename,
                                         notes=note,
                                         owner_org=orglist[orgnr],
                                         groups=[{'name':grouplist[groupnr]}],
                                         city=citylist[citynr]['name'])
        except:
                # package bestaat wel maar is private?
                print 'package_create: package %s already exists :' % filename_safe
                continue

        e=requests.post('http://127.0.0.1/api/action/resource_create',
              data={"package_id":filename,'name':filename_safe,'url':'http://claircitydev.cbs.nl/test', 'format':'CSV'},
              headers={"X-CKAN-API-Key": apikey},
              files=[('upload', file(fullpath))])
        if (e.status_code)!=200:
                print e.status_code
                print e.text
