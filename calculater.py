def new_evil(strEvil):
    num = strEvil.split(" ")
    if num[1] == "+":
        return float(num[0]) + float(num[2])
    elif num[1] == "-":
        return float(num[0]) - float(num[2])
    elif num[1] == "*":
        return float(num[0]) * float(num[2])
    elif num[1] == "/":
        return float(num[0]) / float(num[2])
    elif num[1] == "%":
        return float(num[0]) % float(num[2])
    elif num[1] == "**":
        return float(num[0]) ** float(num[2])
    else:
        return "error operator"


if __name__ == "__main__":
    while True:
        strEvil = input("Please enter the eval(q to quit):")
        if strEvil.lower() == "q":
            break
        print("the result is : %d" % (new_evil(strEvil)))
