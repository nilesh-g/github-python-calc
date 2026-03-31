num1 = int(input("enter number1: "))
num2 = int(input("enter number2: "))

choice = int(input("0. exit\n1. add\n2. subtract\n3. multiply\n4. divide\nenter choice: "))

if choice == 0:
    print("bye!")
elif choice == 1:
    result = num1 + num2
    print("add result =", result)
elif choice == 2:
    result = num1 - num2
    print("subtract result =", result)
elif choice == 3:
    result = num1 * num2
    print("multiply result =", result)
elif choice == 4:
    result = num1 / num2
    print("divide result =", result)
else:
    print("invalid choice!")
