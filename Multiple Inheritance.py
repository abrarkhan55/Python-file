#multiple inheritance
class A:
    def dis(self):
        print("This is A class")
class B:
    def dis(self):
        print("This is B class")
class C (B,A):
    pass

o=C()
o.dis()