arr=[1,2,3,4,5,6,7,8] 
b=[]
for i in arr: 
    if (i%2==0):
         b.append(i) 
    else :
         b.insert(0,i) 
print(b)