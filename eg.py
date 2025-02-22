class employee():
    def __init__(self,name):
        self.name=name
        self.salary=salary
        
class manager(employee):
    def __init__(self,department,name,salary):
        super().__init__(name,salary)
        
        self.department=department
    def display(self):
        print(self.name,self.department,self.salary)
        
    
m1=manager("aids","hardik","1000000")
m1.display()
