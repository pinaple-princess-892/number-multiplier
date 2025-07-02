print("-------------------------------------------------------")
print("Welcome to Marvellous Multiplacation Machine")
print("-------------------------------------------------------")
def multiply(a, b):
    return a * b 
def input_numbers():
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        return a, b
    except ValueError:
        print("Invalid input. Please enter integers only.")
        return None, None
def do_multiply():
    a, b = input_numbers()
    if a is not None and b is not None:
        result = multiply(a, b)
        print(f"The result of {a} * {b} is: {result}")
    else:
        print("Multiplication could not be performed due to invalid input.")
do_multiply()
print("-------------------------------------------------------")
print("Thank you for using Marvellous Multiplacation Machine")
print("-------------------------------------------------------")
