'''a=[1,'a',2,'b',3,'c',4,'d']
b=a[1::2],a[::2]
print(b)

print("insertion")
#insertion 
a.insert(-2,5)
print(a)

a.pop(-3)
print(a)

a.extend([7,8,9])
print(a)

a.append(9)
print(a)

#updation
print("updation")
a[-1]=[10]
print(a)

a[-1]=10
print(a)

#multiple updation
a[7:10]=[20,30,40,50]
print(a)

#deletion
a.pop()
print(a)
a.remove(2)
print(a)
a.clear()
print(a)
'''
'''
#list input
a=input().split
print(a)
 
a=list(map(int.input().split()))
print(a)
'''
a=[1,2,3,45,6]
print("updation")
a[-1]=10
print(a)
a.reverse()
print(a)

#formating strings 
a,b=20,30
print("print of 2 numbers %s is %s"%(a,b))
print("The two numbers are {} and {}".format(a,b))
print(f"The two numbers are {a} and {b}")

