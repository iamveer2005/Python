# WAP that Takes total food bill, GST, number of students and then 
# Calculates: final bill after GST and amount each student has to pay

# Taking input from user
Food = float(input("Enter Total Food Bill: "))
GST = float(input("Enter GST percentage: "))
Student = int(input("Enter Number of Students: "))

# Calculating GST amount
GST_amount = Food * GST /100

# Calculating final bill
final_bill = Food + GST_amount

# Calculating per student contribution
per_student = final_bill / Student

# Printing Bill
print("----------RIG Hostel----------")
print("\n----------Bill Details----------")

# This statement will calculate and print the result

print("Food Bill :", Food)
print("GST Amount :", GST)
print("Final Amount:", final_bill)
print("Each Students pays:", per_student)
