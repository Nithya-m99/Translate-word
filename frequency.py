from collections import Counter
def wc(fn):
    with open(fn) as f:
        return Counter(f.read().split())
coun=wc('E:/t8.shakespeare.txt')
for i in coun:
    print(i,':',coun[i])
