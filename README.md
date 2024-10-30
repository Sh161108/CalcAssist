# CalcFunctions

This repository provides a command-line tool for performing basic symbolic differentiation and integration of single-variable functions. It supports trigonometric, logarithmic, and simple polynomial functions. The program prompts the user to input parameters, including function type, operation type, and variable format, and then displays the result.

## Features
- **Differentiate** or **integrate** single-variable functions
- Supports basic trigonometric functions: `sin`, `cos`, `tan`, `sec`, `cosec`, and `cot`
- Supports logarithmic function and polynomial expressions of the form `a * x^n`
- Input validation and guided prompts for an easy-to-use interface

## Usage
1. Run the script.
2. Choose an operation: integration (`int`) or differentiation (`diff`).
3. Specify the function type (e.g., `sin`, `cos`, `log`, or `variable` for general polynomial expressions).
4. Enter the coefficient and exponent for `a * x^n`.
5. Receive the symbolic result for the specified operation.

## Example
Below is an example usage session:
```shell
Do you want to integrate(int) or differentiate(diff): diff
Provide function to perform differentiation: sin
Enter the value of coefficient a: 2
Enter the power n: 3
Is this the variable: 2x^3? yes
Result: [sin(2x^3)] 2 * cos(2x^3)
