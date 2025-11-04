def calculator(a, b, operation):
    if operation == 1:
        return a + b
    elif operation == 2:
        return a - b
    elif operation == 3:
        return a * b
    elif operation == 4:
        if b!= 0:
            return a / b
        else:
            return "Error! Divided by zero!"
    else:
        return "Invalid operation!"
    
a = int(input("Enter first number: "))
b = int(input("Enter Second number: "))

print("\nSelect operation: ")
print("1. Addition")
print("2. Subtraction")
print("3. multipication")
print("4. division")

choice = int(input("Choice the operation (1-4): "))

result = calculator(a, b, choice)

print("The ans is: ", result)