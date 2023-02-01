class Parent1:
    def assign_string_one(self,str):
        self.str = str
    def show_string_one(self):
        return self.str
    def say_hi(self):
        print("I am parent 1")

class Parent2:
    def assign_string_two(self,str):
        self.str = str
    def show_string_two(self):
        return self.str
    def say_hi(self):
        print("I am parent 2")

class Child(Parent1, Parent2):
    def assign_string_three(self,str):
        self.str = str
    def show_string_three(self):
        return self.str
    def say_hi(self):
        super().say_hi()
        #Parent1.say_hi(self)
        print("I am child")

mychild = Child()
mychild.assign_string_three("mango")
mychild.show_string_three()
mychild.say_hi()

print(isinstance(mychild, Child))
print(isinstance(mychild, Parent2))
print(isinstance(mychild, Parent1))

print(Child.__mro__)
# print(Child.mro())

#https://www.programiz.com/python-programming/operator-overloading