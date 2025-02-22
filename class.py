class phone():
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def display(self):
        print("brand:",self.brand)
        print("price:",self.price)
apple=phone("apple","1000000")
apple.display()
