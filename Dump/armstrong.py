def armstrong(n):
 ctr=0
 sum=0
 tmp=n
 while tmp>0:
    ctr=ctr+1
    tmp=tmp//10
 digits=ctr
 print("Number of digits: ",digits)
 tmp2=n
 while(tmp2>0):
     tmp3=tmp2%10
     sum=sum+pow(tmp3,digits)
     tmp2=tmp2//10
 print("Sum is: ",sum)    
 if sum==n:
     print(n," is an armstong number")
 else:
     print(n, " is not an armstrong number")

val=int(input("Enter number: "))
armstrong(val)
