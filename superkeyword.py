class a():
    def __init__(self):
        print("a")
    def display(self):
        print("you are in class a")
class b(a):
    def __init__(self):
        super().__init__()
        print("b")
    def display(self):
        print("you are in class b")
obj=b()
