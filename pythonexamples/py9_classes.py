class Foo:
    """
    Class doc string.

    Be careful what kind of content you default here.
    Mutable data in the base class can be changed between instances.
    """

    bar = "bar"

    def __init__(self, baz):
        self.baz = baz

    @classmethod
    def change_bar(cls, bar):
        """Change the class bar, not the instance of bar."""
        cls.bar = bar

    @staticmethod
    def hello():
        """Print hello."""
        print('hello')

    def get_baz(self):
        """Get baz from instance."""
        return self.baz

    def get_bar(self):
        """Get bar from instance."""
        return self.bar


class Foo2(Foo):
    """
    Foo2 is derived from Foo.

    Extends foo and adds get_foo. Also uppercases all values.
    """

    def __init__(self, baz):
        super().__init__(baz.upper())
        self.bar = "BAR"
        self.foo = "FOO"

    def get_foo(self):
        """Get foo from instance."""
        return self.foo

print('"Base class instance"')
foo = Foo('baz')
print(foo.get_baz())
print(foo.get_bar())
# baz
# bar

print('\n"Derived class instance"')
foo2 = Foo2('baz')
print(foo2.get_baz())
print(foo2.get_bar())
print(foo2.get_foo())
# BAZ
# BAR
# FOO

print('\n"Test if instance of"')
print(isinstance(foo, Foo))
print(isinstance(foo2, Foo))
print(isinstance(foo, Foo2))
print(isinstance(foo2, Foo2))
# True
# True
# False
# True

print('\n"Use classmethod"')
# Notice this changes class definition!
Foo.change_bar('new_bar')
print(foo.get_bar())
print(foo2.get_bar())
new_foo = Foo('baz')
print(new_foo.get_bar())
# new_bar
# BAR
# new_bar

print('\n"Use static method"')
Foo.hello()
foo.hello()
foo2.hello()
# hello
# hello
# hello
