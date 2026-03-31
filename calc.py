num1 = int(input("enter number1: "))
num2 = int(input("enter number2: "))

choice = int(input("0. exit\n1. add\n2. subtract\nenter choice: "))

if choice == 0:
    print("bye!")
elif choice == 1:
    result = num1 + num2
    print("add result =", result)
elif choice == 2:
    result = num1 - num2
    print("subtract result =", result)
else:
    print("invalid choice!")
