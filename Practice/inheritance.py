# single inheritance
"""class Parent:
    def method1(self):
        print("parent")
class child(Parent):
    def method2(self):
        print("child")
obj=child()
obj.method1()
obj.method2()

"""
#multiple inheritance
class Father:
    def method1(self):
        print("father")
class mother:
    def method2(self):
        print("mother")
class child(Father,mother):
    def method(self):
        print(child)
obj=child()
obj.method1()
obj.method2()
obj.method()
