n=int(input())
b=[]
for i in range(1,n):
    if i%2==0:
        b.append(i)
if sum(b)>n:
    print("abandent number")
else:
    print("Not abandent number")