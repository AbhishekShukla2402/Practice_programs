def prime(a,b):
    for i in range(a,b+1):
        if i>1 :
            for j in range(2,i):
                if i%j == 0:
                    break
            else:
                    print(i)
                
            
        
                    
    
a=int(input("Enter start value: "))
b=int(input("Enter end value: "))
prime(a,b)
