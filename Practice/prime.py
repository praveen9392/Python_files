A = int(input())
for i in range(2, A):
    if A % i == 0:
        print("not prime")
        break
else:
    print("prime")