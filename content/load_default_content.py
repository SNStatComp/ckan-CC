from ckanapi import RemoteCKAN
import sys, csv, psycopg2


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



#package_list=claircity.action.package_list()
#print 'Removing %d packages' % len(package_list)
#for package in package_list:
#    print package
#    claircity.action.dataset_purge(id=package)
#sys.exit()



print 'Removing organizations'
orglist=claircity.action.organization_list()
for org in orglist:
        print org
        datasets=claircity.action.organization_show(id=org,
                        include_datasets=True, include_tags=False, include_followers=False,
                        include_extras=False, include_users=False,include_groups=False)
        for package in datasets['packages']:
            #print package['name'], package['id']
            claircity.action.dataset_purge(id=package['name'])
        datasets=claircity.action.organization_show(id=org,
                        include_datasets=True, include_tags=False, include_followers=False,
                        include_extras=False, include_users=False,include_groups=False)
	claircity.action.organization_purge(id=org)
        pass
orglist=claircity.action.organization_list()
print ' new orgs:' , orglist
print 'Removing groups'
grouplist=claircity.action.group_list()
print grouplist
for group in grouplist:
	claircity.action.group_purge(id=group)

print 'Removing vocabulary cities'
try:
	vocab = claircity.action.vocabulary_show(id='cities')
	for tag in vocab['tags']:
		claircity.action.tag_delete(id=tag['id'], vocabulary_id=tag['vocabulary_id'])
	claircity.action.vocabulary_delete(id=vocab['id'])
except:
	print 'vocabulary "cities" not found'

print 'adding organizations'
with open('orglist_inline_img.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print row['name'],row['title']
        try:
                claircity.action.organization_create(name=row['name'], title=row['title'], image_url=row['image_url'])
        except:
                print 'error creating org' 
        
        pass
print 'adding groups'
with open('grouplist.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print row['name'],row['title']
        claircity.action.group_create(name=row['name'].lower(), title=row['title'])

print 'adding vocabulary "cities"'
vocab = claircity.action.vocabulary_create(name='cities')
with open('cities_vocab.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		print row['tag']
		claircity.action.tag_create(name=row['tag'], vocabulary_id=vocab['id'])
