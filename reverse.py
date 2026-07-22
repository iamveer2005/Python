# WAP to reverse a string 
a = "Pranjul"

# # METHOD 1 (Slicing)
print (a[::-1])

# METHOD 2 (For loop)
rev ="" # rev creates an empty string to store the reversed letters
for i in range(len(a)-1, -1, -1):
# START(len(a)-1):len(a) is 7, so 7-1 = 6. The loop starts at index 6.
# STOP(-1):The loop stops before reaching this number. Stopping before -1 means it ends exactly at index 0 (the letter P)
# STEP(-1):This tells the loop to count backward by 1 on every turn (6, 5, 4, 3, 2, 1, 0).
 rev = rev + a[i]
print(rev)