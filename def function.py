s_username="emc"
s_password="123"



uname=input()
password=input()

def validate():
    if(s_username==uname and s_password==password):
        return True
        
    else:
        return False
a=validate()
print(a)

