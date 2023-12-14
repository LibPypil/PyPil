def EQ1(Equation):
    # Check parameters
    if not isinstance(Equation, list):
        raise TypeError("Unexpected parameter.")
    if not all(isinstance(e, (int, float, str)) for e in Equation):
        raise TypeError("Unexpected parameter.")

    leftPol = []
    rightPol = []
    leftPointer = True
    for e in Equation:
        if e == "=":
            leftPointer = False
        elif leftPointer:
            leftPol.append(e)
        else:
            rightPol.append(e)

    sumStr = 0
    sumInt = 0
    for e in leftPol:
        if isinstance(e, str):
            if e == "x":
                e = "1"
            elif e == "-x":
                e = "-1"
            e = e.replace("x", "")
            sumStr += int(e)
        else:
            sumInt += e
    leftPol.clear()
    leftPol.append(sumInt)
    leftPol.append(sumStr)

    sumStr = 0
    sumInt = 0
    for e in rightPol:
        if isinstance(e, str):
            if e == "x":
                e = "1"
            elif e == "-x":
                e = "-1"
            e = e.replace("x", "")
            sumStr += int(e)
        else:
            sumInt += e
    rightPol.clear()
    rightPol.append(sumInt)
    rightPol.append(sumStr)

    left = leftPol[1] - rightPol[1]
    right = - leftPol[0] + rightPol[0]

    return right / left

print(EQ1(["2x", -8, "4x", "-x", "=", 16, "-8x"]))