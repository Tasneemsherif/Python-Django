# ask the user to enter 2 numbers
num1 = int(input("Please enter the FIRST number: "))
num2 = int(input("Please enter the SECOND number: "))

# performing operations
sum_result = num1 + num2
diff_result = num2 - num1
mul_result = num1 * num2
div_result = num1 / num2

# print the results
print (f'the first number you entered is {num1}, the second number you entered is  {num2}')
print (f'Sum = {sum_result}, difference = {diff_result}, multiplication = {mul_result}, division = {div_result}')

# check if num1 > num2
if (num1 > num2) :
    print (f'First number {num1} greater than second number{num2}')
print(f"Second number: {num2} is greater than first number: {num1}")

# check sum is even or odd
if (sum_result % 2 == 0):
    print ("Sum of the two numbers is even")
else:
    print("Sum of the two numbers is odd")

# comparing num1 to num2
if (num1 > num2):
    print ("First number is greater than the second number")
elif (num1 < num2):
    print("Second number is greater than the first number")
else:
    print("First number is equal the second number")
