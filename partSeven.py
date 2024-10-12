num1 = float(input("Choose a number."))
num2 = float(input("Choose a number."))
operation = input("Choose an operation.")

if operation == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operation == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operation == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operation == "/":
    result = num1/num2
    print(f"{num1} / {num2} = {result}")
elif operation == "^":
    result = num1^num2
    print(f"{num1} ^ {num2} = {result}")
elif operation == "%":
    result = num1 % num2
    print(f"{num1} % {num2} = {result}")