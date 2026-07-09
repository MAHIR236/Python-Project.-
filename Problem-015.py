# Swapping two variables using a temporary variable
first_num = int(input("Please provide the first number: "))
second_num = int(input("Please provide the second number: "))
print("Before swapping: first_num =", first_num, ", second_num =", second_num)

temp = first_num
first_num = second_num
second_num = temp

print("After swapping: first_num =", first_num, ", second_num =", second_num)