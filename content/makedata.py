import glob,os,sys,random, time, datetime


datadir='testdata'
if not os.path.exists(datadir):
    os.makedirs (datadir)
f=open ('words.txt')
words=[w.strip() for w in f.readlines()]
f.close()


num_datasets=1000
maxcols=10
maxrows=10000
num_types=5


#/ 0: positive int (2^32)
#// 1: float
#// 2: int (-2^31--2^31)
#// 3: date
#// 4: datetime
#// 5: string






def makevalue (coltype):
    if coltype==0:
        val=str(random.randrange(0,4294967295))
    if coltype==1:
        val=str(random.uniform(-100000,100000))
    if coltype==2:
        val=str(random.randrange(-2147483645,2147483645 ))
    if coltype==3:
        d=datetime.date(1900,1,1)+datetime.timedelta(random.randrange(120*365))
        
        val='%d-%d-%d' % (d.year, d.month, d.day )
    if coltype==4:
        d=datetime.date(1900,1,1)+datetime.timedelta(random.randrange(120*365)) 
        val=d.isoformat()
    if coltype==5:
        val=words[random.randrange(0,len(words))]
    return val

    
        



filelist = glob.glob(datadir+"/*.csv")
for f in filelist:
    os.remove(f)

for i in range(num_datasets):
    filename=words[random.randrange(0,len(words))]    
    f=open (datadir+'/'+filename+'.csv','w')
    num_cols=random.randrange(0,maxcols)
    print filename, num_cols
    coltypes=[random.randrange(num_types) for col in range(num_cols)]
    rownames=[words[random.randrange(0,len(words))] for i in range(num_cols)]
    f.write(','.join (rownames)+'\n')
    for linenr in range(random.randrange(0,maxrows)):
        #print num_cols
        row=[makevalue(coltypes[i]) for i in range(num_cols)]
       # print row
        f.write(','.join(row)+'\n')
    f.close()

