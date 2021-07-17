class A:

    def __init__(self):
        self.a = "A"

    def hello(self):
        print(self.a)


class B:
    def __init__(self):
        self.b = "B"

    def hello(self):
        print(self.b)


class C(A, B):

    def __init__(self):
        A.__init__(self)
        B.__init__(self)

    def hello(self):
        A.hello(self)
        B.hello(self)
        print("C")


obj = C()
obj.hello()
