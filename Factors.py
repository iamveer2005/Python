# WAP to find out factors of a number

n= int(input("Enter the number :- "))
a = 1
for i in range (1, n+1):
    if n% i == 0:
        print(i)