# Demonstrating Logical Operators
Age = int(input("Enter your age: "))
has_id = input("Do you have an ID? (yes/no): ") == "yes"
#And Oparator
can_enter = Age >= 18 and has_id
print("Can Enter restricted area (age >= 18 and has ID)?", can_enter)
#Or Oparator
discount = (Age < 12 or Age >= 60) and has_id
print("Eligible for discount (age < 12 or age >= 60):", discount)
#Not Oparator
print("Is not eligible for discount:", not discount)
