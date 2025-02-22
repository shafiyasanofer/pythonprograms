class laptop:
    chargertype="c type"

    def __init__(self):
        self.brand=""
        self.price=34
    def setprice(self,price):
        self.price=price

    def getprice(self):
        print(self.price)
    @classmethod
    def changechargertype(cls):
        cls.chargertype="btype"
    @staticmethod
    def info ():
        print("this is laptop")

hp=laptop()
hp.setprice(3000)
hp.getprice()
laptop.changechargertype()
hp.info()
