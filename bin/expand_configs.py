from jinja2 import Template
import os,sys,csv

reload(sys)  
sys.setdefaultencoding('utf8')

directory='.'

ckan_site=os.environ.get('CKAN_SITE','.')
git_topdir=os.environ.get('CC_HOME','.')

if ckan_site=='.':
        print "set CKAN_SITE/ CC_HOME by running \'. config\' in ckan-CC directory" 
        sys.exit()

configfile=git_topdir+'/'+ckan_site+'.cfg'

if (len(sys.argv)>1):
	configfile=sys.argv[1]
if (len(sys.argv)>2):
	directory=sys.argv[2]


#passwords inlezen en in dict opslaan
f=open (configfile)
passdict={}
for line in csv.reader(f,delimiter=':'):
	key,value=line[0],line[1]
	passdict[key]=value

if ckan_site=='productie':
        passdict['proxy']=True

topdirectory='.'
extensie='.sjabloon'
extensielengte=len(extensie)

filelist=os.walk (topdirectory)
for dirinfo in filelist:
	filenames=dirinfo[2]
	directory=dirinfo[0]
	for filename in filenames:
		if filename[-extensielengte:]==extensie:
			fullname=directory+'/'+filename
			newname=fullname[:-extensielengte]
			print 'templating %s' % (fullname)
			
			f=open(fullname, 'rb')
			filetxt=f.read()
			f.close()
			perms=os.stat(fullname).st_mode & 0777

			template = Template(filetxt)
			txt=template.render(passdict)
			g=open(newname,'w')
			g.write(txt)
			g.close()
			os.chmod(newname,perms)

