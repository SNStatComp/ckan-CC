import os,csv,sys,requests, shutil

try:
    os.mkdir('./img')
except:
    pass
f=open('orglist.csv')
h=open('orglist_inline_img.csv','w' )
line=f.readline()
h.write(line)
csv=csv.reader(f)
for line in csv:
    org=line[0]
    filename=line[1]
    url=line[2]
    r=requests.get(url, verify=False)
    #filename=url.split('/')[-1]
    
    print url
    g=open('img/'+filename,'wb')
    g.write(r.content)
    g.close()
    h.write('"%s","%s","%s"\n' % (org,filename,'http://claircitydev.cbs.nl/img/'+filename+".png"))
