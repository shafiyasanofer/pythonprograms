salary=int(input())
age=int(input())
if(salary>=20000 or age<=25):
    loan=int(input())
    if(loan<=50000):
        print("eligible")
    else:
        print("maximum amount is 50000")
else:
    print("not eligible")
        
        
