from jinja2 import Template
import os,sys,csv

reload(sys)  
sys.setdefaultencoding('utf8')

directory='.'
passfile='../passfile'

if (len(sys.argv)>1):
	passfile=sys.argv[1]
if (len(sys.argv)>2):
	directory=sys.argv[2]


#passwords inlezen en in dict opslaan
f=open (passfile)
passdict={}
for line in csv.reader(f,delimiter=':'):
	key,value=line[0],line[1]
	passdict[key]=value


topdirectory='.'
extensie='.sjabloon'
extensielengte=len(extensie)

filelist=os.walk (topdirectory)
for dirinfo in filelist:
	filenames=dirinfo[2]
	directory=dirinfo[0]
	for filename in filenames:
		if filename[-extensielengte:]==extensie:
			print 'templating %s' % (directory+'/'+filename)
			
			f=open(directory+'/'+filename, 'rb')
			filetxt=f.read()
			f.close()
			template = Template(filetxt)
			txt=template.render(passdict)
			g=open(directory+'/'+filename[:-extensielengte],'w')
			g.write(txt)
			g.close()
