
'Total words'
f=open('t8.shakespeare.txt','r+')
for i in f:
    print(i)

'Uniqueword count'
f=open('t8.shakespeare.txt','r+')
lines=f.readlines()
n=[]
u=[]
for i in lines:
    n.append(i)
for j in n:
    
    if j not in u:
        u.append(j)
c=0
for k in u:
    c=c+1
print(c) 

'Process time'
etime=time.time()-stime
print("\n")
print("",etime,"Sec")
print("\n")
print(process.memory_info()[0],"Bytes")
print(process.memory_info()[0]/float(2**20),"MB")



