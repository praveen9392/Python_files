def a(a,b):
    return a+b
print(a(1,3))     #positional arguments ,order does not chnage


def b(a,b,c):
    return a+b+c
print(b(b=1,a=2,c=3))   #keyword based  arguments ,changing order also not a problem

def c(a=5,b=3):
    print(b-a)
c()                    # default arguments ,we are passing the values at the time of creating the functions

def d(*args):
    print(args)
d(1,2,3,4)            # orbitary parameters if we dont know the length or number of arguments simply five * args it takes any numbers of inputs

def e(**args):
    print(args)
e(a=1,b=2,c=3)           

"""
4
6
-2
(1, 2, 3, 4)
{'a': 1, 'b': 2, 'c': 3}       **args output ,stored in dictonary format.
"""