s= input("Enter a string: ")
flag=0
r=s[::-1]
l=len(s)
for i in range(0,l):
    
    if s[i] != r[i]:
            flag=1
if flag==1:
    print("Not Palindrome")
else:
    print("Palindrome")
        
