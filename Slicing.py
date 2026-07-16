# Slicing is a imp part of ML it means accessing parts of string the format of slicing is     a[start:stop:steps] the default value of starting value is 0 and ending value is the last value of variable.

str = "Pranjul Gupta"
print(str[1:4])
# it is used to print a certain part or slice of string in this case it would print form 1 to 4th part 

print(str[5:])
# or
print(str[5:len(str)])

# if you want to print or count backwards just use negative (-)

print(str[-5:])

# Suppose you have to print pajl means there is a gap in between in that case we use a format like a[start: stop: steps]
print(str[0:7:2])