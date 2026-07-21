# WAP to check if a number is perfect (sum of factors = the number itself)

n= int(input("Enter the number :-"))
a = 0
for i in range(1,n): #here we are using n instead of n+1 as we don't want the number itself to be added
    if n%i == 0: 
        a = a+i
        
if a == n:
    print("Perfect Number")
else:
    print("Not a perfect number")