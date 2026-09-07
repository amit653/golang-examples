'''
merge 2 files one after the other, and group their sum based on keys
file1.txt=
a 1 100
b 3 300
a 2 200
c 4 230
file2.txt=
a 1 100
b 1 100
a 5 500
'''
from collections import defaultdict
groups = defaultdict(list)
total = defaultdict(int)
with  open("out.txt","w") as out:
    for fname in ["file1.txt","file2.txt"]:
        with open(fname) as f:
          for line in f:
           key,col1,col2=line.strip().split()
           out.write(f"{key} {col1} {col2}\n")
           groups[key].append(int(col2))
           total[key]+=int(col2)
    print(groups)
    print(total)
