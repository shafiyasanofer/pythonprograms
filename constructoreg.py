class calculator:
    def __init__(self,a,b):
        self.n1=a
        self.n2=b

    def add(self):
        print("add",self.n1+self.n2)
    def sub(self):
        print("sub",self.n1-self.n2)
    def mul(self):
        print("mul",self.n1*self.n2)
    def div(self):
        print("div",self.n1%self.n2)
a=calculator(10,2)
a.add()
a.sub()
a.mul()
a.div()
