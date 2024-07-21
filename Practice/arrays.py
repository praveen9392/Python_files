import array as a
b = a.array('i', [1, 2, 3, 4])
"""for i in b:
    print(i)
"""
# get output as list in reverse order
"""
c=[]
for i in b:
    c.append(i)
print(c[::-1])

"""
# get this output as array in reverse order: array('i', [4, 3, 2, 1])
d=a.array('i',b[::-1])
print(d)

for i in d:
    print(i)

#array to list conversion
h=b.tolist()
print(h)


# array reverse
b.reverse()
print(b)