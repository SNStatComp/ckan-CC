import os, grp, pwd
from jinja2 import Environment

def render(tpl_path, context):
    path, filename = os.path.split(tpl_path)
    return jinja2.Environment(
        loader=jinja2.FileSystemLoader(path or './')
    ).get_template(filename).render(context)



path='/data/dotmaps/'
dotmap_cities=[d for d in os.listdir(path) if os.path.isdir(path+d) and d!='index_files']

print dotmap_cities


dotmaps=[]
for d in dotmap_cities:
    dotmaps.append({'link':d,'name':d})
context={'num':len(dotmap_cities),'dotmaps':dotmaps}


template=open('./dotmap_index_template.html').read()
template = template.decode('utf-8')
txt=Environment().from_string(template).render(context)


f=open('/data/dotmaps/index.html','w')
f.write(txt.encode('utf-8'))
f.close()

uid = pwd.getpwnam("www-data").pw_uid
gid = grp.getgrnam("www-data").gr_gid
os.chown('/data/dotmaps/index.html',uid, gid )

