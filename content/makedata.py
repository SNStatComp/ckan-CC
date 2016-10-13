import glob,os,sys,random, time, datetime


datadir='testdata'
if not os.path.exists(datadir):
    os.makedirs (datadir)
f=open ('words.txt')
words=[w.strip() for w in f.readlines()]
f.close()


datatype=['positive int', 'float', 'int', 'date','datetime','string']
datasizes=[1e5,10e6,25e6,50e6,100e6,200e6]
datasizetxt=['10kb','10mb','25mb','50mb','100mb','200mb']


num_datasets=1000
maxcols=10
maxrows=10000
num_types=len(datatype)


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

    if (coltype<0) or (coltype>5):
        val=''
    return val

    

def make_bigfile (size,sizetxt):

    f=open (datadir+'/test_size_'+sizetxt+'.csv','w')
    totalsize=0
    while totalsize<size:
        num_cols=20
        row=[makevalue(2) for i in range(num_cols)]
        line=','.join(row)+'\n'
        totalsize+=len(line)
        f.write(line)    
    f.close()    
    



filelist = glob.glob(datadir+"/*.csv")
for f in filelist:
    os.remove(f)

for i in range(num_datasets):
    filename=words[random.randrange(0,len(words))]    
    f=open (datadir+'/'+filename+'.csv','w')
    num_cols=random.randrange(0,maxcols)
    print 'writing %s, %d columns' % (filename, num_cols)
    coltypes=[random.randrange(num_types) for col in range(num_cols)]
    rownames=[words[random.randrange(0,len(words))] for i in range(num_cols)]
    f.write(','.join (rownames)+'\n')
    for linenr in range(random.randrange(0,maxrows)):
        #print num_cols
        row=[makevalue(coltypes[i]) for i in range(num_cols)]
       # print row
        f.write(','.join(row)+'\n')
    f.close()



# datatypes testen

for typenr in range(num_types):
    filename='test_type_'+datatype[typenr]
    print 'writing %s' % filename
    f=open (datadir+'/'+filename+'.csv','w')
    for linenr in range(1,1000):
        row=makevalue(typenr)+'\n'
        f.write(row)
    f.close()


# bigfile-test

for i in range (len(datasizes)):
    print 'writing test_size_%s' % datasizetxt[i]
    make_bigfile (datasizes[i],datasizetxt[i])

    
