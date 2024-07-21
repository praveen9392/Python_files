#single line comments using #
# multiple line  comments using triple """ quotes


#indexing 
"""   
a="hello"
b=a[2]
print(b)
"""

#Slicing
"""
# slicing : it is the operation accesing sub part of a string
a='Hello'
b=a[::-1]
print(b)

c=a[1::2]  # start=1 ,stop=default=n-1, step=2
print(c)

"""

#string methods,count(element,start,stop)
'''a="Hello sai"
b=a.title(),a.index('a'),a.find('a'),a.capitalize(),a.upper(),a.lower(),a.isupper(),a.islower(),a.count('a') #in count method pass any word as argument that we want to count
print(b)
'''

#join() & split() methods
'''
a="BathalaPraveenkumar"
b=a.split('a',2),a.split('a',3),a.split('a')
print(b)

#join method join the string with itarations
c='hii'
d=c.join('ABC')
print(d)

'''
#replace(old,new,count)
a='Praveenkumar'
b=a.replace('a','1'),a.replace('a','1',1),a.replace('a','1',2),a.replace('a','1',3)
print(b)








