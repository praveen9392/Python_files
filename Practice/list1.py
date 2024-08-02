a=[2,8,5,9,3]
a.sort()
print(a)
a.remove(9)
print(a)
a.pop()
print(a)
a.pop(2)
print(a)

a.append(1)
print("append",a)
a.insert(1,6)
print("insert",a)
a.extend([1,2,3])
print("extend",a)
print("index method",a.index(1))
print("count method",a.count(1))
#print(a.sort())          it directely doesnot return sorted value it returns NONE  because ,list is modified
a.sort(reverse="true")
print(a)
a.clear()
print(a)
a=[1,2,3,4,5,6]
b=a.copy()
print(b)


#list compression   
#Syntax   [expression for variable in iterable]
c=[i**2 for i in a]
print(c)

d=[i for i in a if i%2==0]                #return even numbers using list compression
print(d)

strings = ['hello', 'world', 'python']
uppercase_strings = [s.upper() for s in strings]
print(uppercase_strings)  # ['HELLO', 'WORLD', 'PYTHON']

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
cartesian_product = [(x, y) for x in list1 for y in list2]
print(cartesian_product)  # [(1, 'a'), (1, 'b'), (1, 'c'), (2, 'a'), ...]


f=[1,2,3,4,1,4,5]
g=[]
for i in f:
    if i not in g[:i]:
        g.append(i)  
print("original list",f)     
print("duplicate removed list",g)

#another way to remove the duplicates from the list by simply convert list into set then back to list
'''f=[1,1,2,3,3,4,5,4]
g=list(set(f))
print(g)'''

j=[1,2,3,2,5,5,7,6]
for i in j:
    if i not in j[:i]:
        j.remove(i)
print(j)




