

f=open('t8.shakespeare.txt','r+')
for i in f:
    print(i)

'Unique count'
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




