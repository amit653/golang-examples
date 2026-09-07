'''
group and sum using defaultdict and plain dict
count.txt=
a 1 100
b 1 100
a 5 500
'''
from collections import defaultdict
total=defaultdict(int)
dct={}
print(total,dict)
def group_sum(filename)->dict:
  try:  
    with open (filename,'r')as f:
      for i in f:
        key,col1,col2=i.strip().split()
        print(key,col2,type(key),type(col2))
        total[key]+=int(col2)
        if key in dct:
            dct[key]+=int(col2)
        else:
            dct[key]=int(col2)

  except FileNotFoundError:
    print(filename,"file not found")  

  #print(total,dct)
  return total #dct
 
if __name__ == "__main__":
 result=group_sum('count.txt')
 print(result)
