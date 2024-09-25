def print_usage_message():
    usage_message = "usage: add|sub|mul|div v0 v1 \n       quit"
    print(usage_message)

def is_valid_input(user_input):
    inputs_array = user_input.split()

    # User input is 3 elements long
    if len(inputs_array) != 3:
        return False

    operation, v1, v2 = inputs_array

    # Operation is a string
    if not isinstance(operation, str):
        return False

    # User input is not blank
    if operation == "":
        return False

    # Variables are numbers
    try:
        float(v1)
        float(v2)
    except ValueError:
        return False

    # User is not dividing by 0
    if operation == "div" and v2 == 0:
        print("Can't divide by zero.")
        return False

    return True

while True:
    user_input = input("SuperMathyBot> ")
    if user_input == "quit":
        quit()

    while not is_valid_input(user_input):
        print_usage_message()

        user_input = input("SuperMathyBot> ")
        if user_input == "quit":
            quit()

    operation, v1, v2 = user_input.split()
    v1 = float(v1)
    v2 = float(v2)

    match operation:
        case "add":
            print(v1 + v2)
        case "sub":
            print(v1 - v2)
        case "mul":
            print(v1 * v2)
        case "div":
            print(v1 / v2)
        case _:
            print_usage_message()
