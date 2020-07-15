def prime(a):
    flag=0
    for i in range(2,a):
        if (a%i)==0:
            flag=1
    return flag

val=int(input("Enter number: "))
chk=prime(val)
if chk==1:
    print(val,"is not a prime number")
else:
    print(val,"is a prime number")      
          
            
