num1 = float(input("enter the num1"))
num2 = float(input("enter the num2"))
operator = input("enter the operator (+,-,*,/):")
if operator == "+":
    print ("result=", num1 + num2)
elif operator == "-":
    print("result=", num1 - num2)
elif operator == "*":
    print("result=", num1 * num2)    
else:
    print("invalid")
