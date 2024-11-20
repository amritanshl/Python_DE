
import TwoDShapes as t



exitIt = True
while(exitIt): 
    choice = input("""
please enter the choice as:
 + for addition
 - for substarction
 * multiplication
 / for divison
 1/x for dividing number by 1
 x2 for square of the number
 type exit() to exit out of calculator
""")
    num1 = int(input("enter your first number"))
    num2 = int(input("enter your second number"))
    
    if choice == "+":
        c.addition(num1,num2)
        
    elif choice == "-":
       c.subtraction(num1,num2)
    elif choice == "*":
        c.multiplication(num1,num2)
        
    elif choice == "/":
        c.division(num1,num2)
        
   
    else:
        print("Wrong choice")
        print("""
Please enter the choice as:
 + for addition
 - for subtraction
 * for multiplication
 / for division
 1/x for dividing number by 1
 x2 for square of the number
""")
    num1 = 0
    num2 = 0
    exitvar = input("If you want to exit() type exit else press enter")
    if(exitvar == "exit()"):
        exitIt = False

                        

def recur(num):
    if (num>0):
        cd = num + recur(num - 1) 
        print(cd)
    else:
        cd = 0
    return cd

recur(100)







