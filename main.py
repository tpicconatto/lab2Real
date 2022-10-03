
def mul(x,y): #multiplication
    return x*y
def dev(x,y): #devision
    return x/y
def add(x,y): #addition
    return x+y
def subtract(x,y): #subtraction
    return x-y
def mod(x,y): #module
    return x%y
def expon(x,y): #exponents
    return x**y

number1 = float(input("Enter a number:"))
operator = str(input("Enter an operator:"))
number2 = float(input("Enter a number:"))
caldict = { #dictionary access functions
    "+":add(number1, number2),
    "-":subtract(number1, number2),
    "*":mul(number1, number2),
    "/":dev(number1, number2),
    "%":mod(number1, number2),
    "^":expon(number1, number2)
}
if operator in caldict: #using a valid operator
    print(caldict.get(operator))
else: #not using a valid operator
    print("Error, & is not a valid operator")

