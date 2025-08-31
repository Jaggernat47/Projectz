print("CALCULATOR 3.1.1")

while True:
    try:
        menu = float(input("\nMenu:\n 1. Start\n 2. Exit\n\nEnter here: "))
        if menu < 1 or menu > 2:
            print("[Error: Select one of the given choices]")
            menu_restart = input("Do you want to restart? [Y][N]: ")
            if menu_restart.upper() == "Y":
                continue
            elif menu_restart.upper() == "N":
                print("Goodbye")
                break
            else:
                print("Error")
        elif menu == 2:
            print("Goodbye")
            break
        
        num1 = float(int(input("Enter 1st number: ")))
        operator = input("Select an operator [+][-][*][/]: ")
        if operator != '+' and operator != '-' and operator != '*' and operator != '/':
            print("[Error: Select one of the given operators]")
            operator_restart = input("Do you want to restart? [Y][N]: ")
            if operator_restart.upper() == "Y":
                continue
            elif div_restart.upper() == "N":
                print("Goodbye")
                break
            else:
                print("Error")
                break
            
        num2 = float(int(input("Enter 2nd number: ")))
        equal = input("Type [=]: ")
        if equal != '=':
            print("[Error: That's not an equal sign]")
            equal_restart = input("Do you want to restart? [Y][N]: ")
            if equal_restart.upper() == "Y":
                continue
            elif div_restart.upper() == "N":
                print("Goodbye")
                break
            else:
                print("Error")
                break

        if operator == '+':
            add = num1 + num2
            print(f"Answer: {add}\n")
        elif operator == '-': 
            sub = num1 - num2
            print(f"Answer: {sub}\n")
        elif operator == '*':
            mul = num1 * num2 
            print(f"Answer: {mul}\n")
        elif operator == '/':
            if num2 == 0:
                print("[Error: You can't divide any number by zero]")
                div_restart = input("Do you want to restart? [Y][N]: ")
                if div_restart.upper() == "Y":
                    continue
                elif div_restart.upper() == "N":
                    print("Goodbye")
                    break
                else:
                    print("Error")
                    break
            div = num1 / num2
            print(f"Answer: {div}")

    except ValueError:
        print("[Error: numbers only]")
        menu_restart2 = int(input("Do you want to restart? [Y][N]: "))
        if menu_restart2.upper() == "Y":
            continue 
        elif menu_restart2.upper() == "N":
            print("Goodbye")
            break
        else:
            print("Error")
            break