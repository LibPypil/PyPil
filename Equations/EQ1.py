from math import lcm
def EQ1(Equation):
    # Check parameters
    if not isinstance(Equation, list):
        raise TypeError("Unexpected parameter.")
    if not all(isinstance(e, (int, float, str)) for e in Equation):
        raise TypeError("Unexpected parameter.")

    #detectar cuantas fracciones hay:
    fractions = 0
    isOpen = False
    for e in Equation:
        if e == "(":
            if isOpen:
                raise TypeError("Unexpected parameter")
            isOpen = True
        if e == ")":
            if not isOpen:
                raise TypeError("Unexpected parameter")
            isOpen = False
            fractions += 1
    if isOpen:
        raise TypeError("Unexpected parameter")
    print(fractions)

    #Separarlos
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

    if fractions == 0:
        #Algoritmo sin fracciones
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
    elif fractions == 1:
        #Algoritmo con 1 fracción
    else:
        #Algoritmo con 2 o más fracciones


print(EQ1(["(", "x", "/", 8, ")", 2, "=", 4]))