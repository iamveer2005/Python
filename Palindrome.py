# WAP to check whether a number is palindrome(word is same after been reversed) or not

a = "naman"
rev =""

for i in range (len(a)-1 , -1, -1):
    rev = rev + a[i]

if rev == a:
    print("The name is palindrome")
else:
    print("Not Palindrome") 