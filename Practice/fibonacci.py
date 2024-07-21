n=int(input())
a=[0,1]
while a[-1]+a[-2]<=n:
    a.append(a[-1]+a[-2])   
print(a)