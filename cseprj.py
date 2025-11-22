print("HELLO USER")

num1 = float(input("Enter first number "))
num2 = float(input("Enter second number "))
opp = input("Enter opperator ")

if opp in ["add", "addition", "+"]:
    ans = num1 + num2
    print("Result =", ans)

elif opp in ["subtract", "minus", "difference", "-"]:
    ans2 = num1 - num2
    print("Result =", ans2)

elif opp in ["multiply", "product", "*"]:
    ans3 = num1 * num2
    print("Result =", ans3)

elif opp in ["divide", "division", "/"]:
    if num2 == 0:
        print("Cannot divide by zero!")
    else:
        ans4 = num1 / num2
        print("Result =", ans4)

else:
    print("error, enter a valid opperation (add , subtract, multiply or divide)")