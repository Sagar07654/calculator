num1 = int(input("enter a first number: "))
operator = input("option of operator is *,+,/,-: ")
num2 = int(input("enter a second number: "))
if operator == "+":
    result = num1+num2
elif operator == "*":
    result = num1*num2
elif operator == "-":
    result = num1-num2
elif operator == "/":
    if num2 != 0:
        result = num1/num2
    else:
        result = 'undifiened (not devisible by zero)'
else:
    result = 'invlaid operator'

print(f"this is {num1} {operator} {num2} = {result}.")

