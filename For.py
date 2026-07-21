# For loops is used to run a block of code repeatedly for each item in a collection

n = int(input("Enter the data :-"))
# We are taking a input(integer) from user and storing it in n 
a = 1
# a is storing the initial value from where the loop will start 
for i in range(1,n+1):
# the range of variable i will be from 1 to n+1(input number will increase by 1 everytime the loop runs)
 a = a+i
# the value of a will increment by i everytime means 1+1, 1+2, 1+3...
print(a)