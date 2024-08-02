n=int(input())
b = list(map(int, input().split()))[:n]        #the slice [:n] includes elements from index 0 to n-1.
print(b)
for i in b:
    if i == 0:
        b.remove(i)
        b.append(i)
print(b)
