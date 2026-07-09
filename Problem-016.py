# Swapping two variables without using a temporary variable
first_num = int(input("Please provide the first number: "))
second_num = int(input("Please provide the second number: "))
print("Before swapping: first_num =", first_num, ", second_num =", second_num)

# Pythonic way of swapping (no temp variable needed!)
first_num, second_num = second_num, first_num

print("After swapping: first_num =", first_num, ", second_num =", second_num)