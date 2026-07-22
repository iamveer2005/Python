#WAP to check if a number is prime or not

n = int (input("Enter the Number :- "))
count = 0 
for i in range(1,n+1):
    if n%i == 0:
        count = count + 1 #it will count the number and increment by one 
if count == 2: # if the counted number(factorials) are 2 then print prime else not prime
 print("The number is a Prime Number")
else:
 print("not a Prime Number")
