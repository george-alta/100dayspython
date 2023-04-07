from art import logo

def sum (a, b): return a+b
def substract (a, b): return a-b
def multiply (a, b): return a*b
def divide (a, b):
    # if b == 0: return "ERROR: cannot divide by zero"
    return a/b

operations = {
    "+":sum,
    "-":substract,
    "/":divide,
    "*":multiply}
first_run = True
while True:
    if first_run: 
        print (logo)
        num1 = float(input("enter first number: "))
    for symbol in operations: print(symbol)
    operation_symbol = input("enter a symbol from the line above: ")
    num2 = float(input("enter second number: "))
    if operation_symbol == "/" and num2 == 0:
        print ("cannot divide by zero, you need to choose again")
        continue
    first_run = False
    result = operations[operation_symbol](num1,num2)
    print(f"{num1} {operation_symbol} {num2} = {result}")
    num1 = result
    run_again = input(f"to continue calculating with {num1}, enter 'y', otherwise enter 'n' ")
    if run_again == "n": first_run = True 

    #there is another way to redefine the app, by using recursivity. 
    # for this, everything needs to be inside a calculator() function, and line 30 will run calculator() if true.
