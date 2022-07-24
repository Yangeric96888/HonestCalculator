answer = 0  # Holding var for answer

def check(x, y, oper):
    '''
    Part of assignment, gives a message depending on various conditions set by the assignment

    :param x: first number in givenequation
    :param y: second number in given equation
    :param oper: operation in given equation
    :return: a not nice string, whose contents depend if the given equaiton fits diff. conditions
    '''

    possAns = 0
    msg = ""
    if is_one_digit(x) and is_one_digit(y):
        msg += " ... lazy"

    if (x == 1 or y == 1) and oper == "*":
        msg += " ... very lazy"

    if (x == 0 or y == 0) and (oper == "*" or oper == "+" or oper == "-"):
        msg += " ... very, very lazy"

    if msg != "":
        msg = "You are" + msg

    return msg

def is_one_digit(num):
    '''
    Checks if the input is one digit and is a proper integer (not necessarily if var type is int)

    :param num: the number being checked
    :return: true if num fits the above conditions or false otherwise
    '''
    if num.is_integer() and (num > -10 and num < 10):
        return True
    else:
        return False

def save_result(num):
    '''
    This functions confirms with the user if they want to save a single digit number
    This occurs only when the user says yes to number that happens to be one digit

    :param num: the number the user is trying to save
    :return: int, either the original num if user wants to save it OR the default holding answer
    '''
    index = 0
    msgIndex = ["Are you sure? It is only one digit! (y / n)",
                "Don't be silly! It's just one number! Add to the memory? (y / n)",
                "Last chance! Do you really want to embarrass yourself? (y / n)"]
    while index < 3:
        response = input(msgIndex[index])
        if response == "y":
            index += 1
        if response == "n":
            return answer
    else:
        return num


#####

while True:
    print("Enter an equation")
    calc = input().split()

    # Substitute number with var
    if calc[0] == "M":
        calc[0] = answer
    if calc[2] == "M":
        calc[2] = answer

    # Check input to make sure it is compatible
    try:
        calc[0] = float(calc[0])
        calc[2] = float(calc[2])
    except ValueError:
        print("Do you even know what numbers are? Stay focused!")
        continue

    if calc[1] == "+" or calc[1] == "-" or calc[1] == "*" or calc[1] == "/":
        pass
    else:
        print("Yes ... an interesting math operation. You've slept through all classes, haven't you?")
        continue

    # Honest remarks
    print(check(calc[0], calc[2], calc[1]))

    # Does the maths operation
    if calc[1] == "+":
        print (calc[0] + calc[2])
        possAns = calc[0] + calc[2]
    elif calc[1] == "-":
        print (calc[0] - calc[2])
        possAns = calc[0] - calc[2]
    elif calc[1] == "*":
        print (calc[0] * calc[2])
        possAns = calc[0] * calc[2]
    elif calc[1] == "/":
        # Try for zero exception
        try:
            print (calc[0] / calc[2])
            possAns = calc[0] / calc[2]
        except ZeroDivisionError:
            print("Yeah... division by zero. Smart move...")
            continue
    else:
        break

    # Save answer
    saveResult = input("Do you want to store the result? (y / n):" )
    if saveResult == "y":
        if is_one_digit(possAns):
            answer = save_result(possAns)
        else:
            answer = possAns

    # Continue calculations
    continueCalc = input("Do you want to continue calculations? (y / n):")
    if continueCalc == "y":
        continue
    else:
        break


