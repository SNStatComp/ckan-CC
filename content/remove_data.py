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



package_list=claircity.action.package_list()
print 'Removing %d packages' % len(package_list)
for package in package_list:
    print package
    claircity.action.dataset_purge(id=package)
