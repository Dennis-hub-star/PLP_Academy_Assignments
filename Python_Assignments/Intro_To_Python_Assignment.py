num1 = input("Input the your first number: ")
operator = input("Input an operator of your choice: ")
num2 = input("Input the second number: ")


results = f"{num1} {operator} {num2}"

# For displaying all the numbers and an operator used
print(results)    

# Displays the results of the mathematical operation
print(eval(results))