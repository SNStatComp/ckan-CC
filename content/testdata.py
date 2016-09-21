import os,random

f=open('dictionary_english.dic')
words=f.readlines()
f.close()


new_words=set()
f=open ('words.txt','w')
for i in range (10000):
    v=random.randrange(0,len(words)-1)
    new_words.add(v)

for w in new_words:    
    f.write(words[w])
f.close()
    
