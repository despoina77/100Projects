def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mult(a, b):
    return a * b


def div(a, b):
    return a / b


operations = {"+": add,
              "-": sub,
              "*": mult,
              "/": div}

num1 = float(input("What's the first number?: "))

for key in operations:
    print(key)
should_continue = True

while should_continue:
    operation_symb = input("Pick an operation: ")
    num2 = float(input("What's the second number?: "))
    calc_function = operations[operation_symb]
    answer = calc_function(num1, num2)
    print(f"{num1} {operation_symb} {num2} = {answer}")

    if input("Type 'yes' to continue calc with {answer}, or type 'no' to exit.: ") == 'yes':
        num1 = answer
    else:
        should_continue = False

