import glob,os,sys,random


datadir='testdata'
if not os.path.exists(datadir):
    os.makedirs (datadir)
f=open ('words.txt')
words=[w.strip() for w in f.readlines()]
f.close()


num_datasets=1000
maxcols=10
maxrows=10000

filelist = glob.glob(datadir+"/*.csv")
for f in filelist:
    os.remove(f)

for i in range(num_datasets):
    filename=words[random.randrange(0,len(words))]    
    f=open (datadir+'/'+filename+'.csv','w')
    num_cols=random.randrange(0,maxcols)
    print filename, num_cols
    rownames=[words[random.randrange(0,len(words))] for i in range(num_cols)]
    f.write(','.join (rownames)+'\n')
    for linenr in range(random.randrange(0,maxrows)):
        #print num_cols
        row=[str(random.randrange(0,1000000)) for i in range(num_cols)]
       # print row
        f.write(','.join(row)+'\n')
    f.close()

