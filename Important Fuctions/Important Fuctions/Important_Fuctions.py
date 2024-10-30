# List of possible functions and trigonometric functions
functions = ["sin", "cos", "tan", "sec", "cosec", "cot", "log", "variable"]
trig_functions = ["sin", "cos", "tan", "sec", "cosec", "cot"]

# Prompt user for operation type: integration or differentiation
while True:
    operation = input("Do you want to integrate(int) or differentiate(diff): ").strip().lower()
    if operation == "int":
        operation = "integration"
        break
    elif operation == "diff":
        operation = "differentiation"
        break
    else:
        print("Choose integration or differentiation only.")

# Prompt user for the function type and validate input
while True:
    func = input("Provide function to perform " + operation + ": ").strip().lower()
    if func not in functions:
        print("Choose a valid function.")
    elif operation == "integration" and func == "log":
        print("Log function is not supported for integration. Choose another function.")
    else:
        break

# Collect variable information from the user and validate
while True:
    print("This is the variable: a(x)^n")
    coeff_a_str = input("Enter the value of coefficient a: ").strip()
    power_n_str = input("Enter the power n: ").strip()

    try:
        coeff_a = int(coeff_a_str)
        power_n = int(power_n_str)
    except ValueError:
        print("Invalid input for power or coefficient. Please enter a number.")
        continue
    
    # Confirm the variable format with the user
    if coeff_a_str != "1" and power_n_str != "1":
        variable_check = "Is this the variable: " + coeff_a_str + "x^" + power_n_str + " "
    elif coeff_a_str == "1":
        variable_check = "Is this the variable: x^" + power_n_str + " "
    elif power_n_str == "1":
        variable_check = "Is this the variable: " + coeff_a_str + "x "
    else:
        variable_check = "Is this the variable: x "
    
    confirmation = input(variable_check).strip().lower()
    if confirmation == "yes":
        break

# Set the variable expression and adjusted powers for calculation
variable = coeff_a_str + "x^" + power_n_str
power_inc = power_n + 1
power_dec = power_n - 1

# Define function to print differentiation result
def write_diff(expression):
    diff_expression = str(power_n * coeff_a) + "x^" + str(power_dec)
    result = "[" + expression + "] " + diff_expression
    print(result)

# Define function to print integration result
def write_int(expression):
    int_expression = str(coeff_a) + "x^" + str(power_inc) + "/" + str(power_inc)
    result = "[" + expression + "] " + int_expression
    print(result)

# Differentiation function based on user input
def differentiate():
    if func in trig_functions:
        if func == "sin":
            solution = "cos(" + variable + ")"
        elif func == "cos":
            solution = "-sin(" + variable + ")"
        elif func == "tan":
            solution = "sec(" + variable + ")^2"
        elif func == "sec":
            solution = "sec(" + variable + ") * tan(" + variable + ")"
        elif func == "cosec":
            solution = "-cosec(" + variable + ") * cot(" + variable + ")"
        elif func == "cot":
            solution = "cosec(" + variable + ")^2"
        write_diff(solution)
    elif func == "variable":
        solution = str(power_n * coeff_a) + "x^" + str(power_dec)
        print(solution)
    elif func == "log":
        solution = "1/" + variable
        write_diff(solution)

# Integration function based on user input
def integrate():
    if func in trig_functions:
        if func == "sin":
            solution = "-cos(" + variable + ")"
        elif func == "cos":
            solution = "sin(" + variable + ")"
        elif func == "tan":
            solution = "ln|sec(" + variable + ")|"
        elif func == "sec":
            solution = "ln|sec(" + variable + ") + tan(" + variable + ")|"
        elif func == "cosec":
            solution = "ln|cosec(" + variable + ") - cot(" + variable + ")|"
        elif func == "cot":
            solution = "ln|sin(" + variable + ")|"
        write_int(solution)
    elif func == "variable":
        solution = str(coeff_a) + "x^" + str(power_inc) + "/" + str(power_inc)
        print(solution)

# Perform the requested operation
if operation == "differentiation":
    differentiate()
elif operation == "integration":
    integrate()
