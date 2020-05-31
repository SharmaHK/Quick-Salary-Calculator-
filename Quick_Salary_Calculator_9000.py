wage = 0
#define mult, which gives a approximate yearly salary from hourly wage 
def eqn_mult (a):
    return float(a) * 40 * 52
#define div, which gives approximate hourly wage from yearly salary
def eqn_div (a):
    return float(a)/(40*52)
#Since I use a 101-key keyboard with a numpad, I chose the divide (/), multiply (*), and decimal (.) 
#keys to help facilitate quicker typing
while wage != ".":
    wage = input("divide(/) or multiply(*): ")
    if wage == "/":
        wage = input("Enter the yearly salary: ")
        print("The hourly wage with this salary would be {:.2f} USD.".format(eqn_div(wage)))
#formatting the print statement so eqn_div and eqn_mult only return a floating point number with
#two decimal places
    elif wage == "*":
        wage = input("Enter hourly wage: ")
        print("Yearly salary with this wage would be {:.2f} USD.".format(eqn_mult(wage)))
