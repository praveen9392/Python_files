a=str(input())
sum=0
for i in a:
    sum+=int(i)**3
if sum==int(a):
    print("Armstrong")
else:
    print("not Armstrong")
