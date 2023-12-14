from math import lcm
from EQ2 import EQ2


def deleteItemsBetween(list, start, end):
    startIndex = list.index(start) if end in list else None
    lastIndex = list.index(end) if end in list else None
    if startIndex is not None and lastIndex is not None:
        del list[startIndex:lastIndex + 1]
    return list


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
                sumStr += float(e)
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
                sumStr += float(e)
            else:
                sumInt += e
        rightPol.clear()
        rightPol.append(sumInt)
        rightPol.append(sumStr)

        left = leftPol[1] - rightPol[1]
        right = - leftPol[0] + rightPol[0]

        return right / left
    elif fractions == 1:
        # Encontrar el tipo de fracción:
        numerator = 0
        denominator = 0
        parentesisLeft = True
        typeOf = 0
        foundParentesis = False
        foundEqual = False
        foundSlash = False
        moreX = False
        index = -1
        for e in Equation:
            index += 1
            doNothing = False
            if e == "(" and not doNothing:
                foundParentesis = True
                if foundEqual:
                    parentesisLeft = False
                doNothing = True
            if e == ")" and not doNothing:
                foundParentesis = False
                doNothing = True
            if e == "/" and not doNothing:
                foundSlash = True
                doNothing = True
            if e == "=" and not doNothing:
                foundEqual = True
                doNothing = True
            if foundParentesis and not foundSlash and not doNothing:
                numerator = e
                if isinstance(e, str):
                    typeOf = 1
            if foundParentesis and foundSlash and not doNothing:
                denominator = e
                if isinstance(e, str):
                    if typeOf == 1:
                        typeOf = 4
                    else:
                        typeOf = 3
            if not foundParentesis and not doNothing:
                if isinstance(e, str) and not e == "=":
                    moreX = True
        if typeOf == 3 and moreX:
            typeOf = 2

        if typeOf == 1:
            left = []
            right = []
            returnLeft = []
            returnRight = []
            deleteItemsBetween(leftPol, "(", ")")
            deleteItemsBetween(rightPol, "(", ")")
            left.append(numerator)
            for e in leftPol:
                if isinstance(e, str):
                    e = float(e.strip("x"))
                    e = str(e * denominator) + "x"
                    left.append(e)
                else:
                    left.append(e * denominator)
            for e in rightPol:
                if isinstance(e, str):
                    e = float(e.strip("x"))
                    e = str(e * denominator) + "x"
                    right.append(e)
                else:
                    right.append(e * denominator)

            sumStr = 0
            sumInt = 0
            for e in left:
                if isinstance(e, str):
                    if e == "x":
                        e = "1"
                    elif e == "-x":
                        e = "-1"
                    e = e.replace("x", "")
                    sumStr += float(e)
                else:
                    sumInt += e
            left.clear()
            returnLeft.append(sumInt)
            returnLeft.append(sumStr)

            sumStr = 0
            sumInt = 0
            for e in right:
                if isinstance(e, str):
                    if e == "x":
                        e = "1"
                    elif e == "-x":
                        e = "-1"
                    e = e.replace("x", "")
                    sumStr += float(e)
                else:
                    sumInt += e
            right.clear()
            returnRight.append(sumInt)
            returnRight.append(sumStr)

            left = returnLeft[1] - returnRight[1]
            right = - returnLeft[0] + returnRight[0]
            return right / left

        elif typeOf == 2:
            left = [0, 0, 0]
            right = [0, 0, 0]
            deleteItemsBetween(leftPol, "(", ")")
            deleteItemsBetween(rightPol, "(", ")")
            if parentesisLeft:
                left[0] = numerator
            else:
                right[0] = numerator

            for e in leftPol:
                if isinstance(e, str):
                    left[2] = left[2] + float(e.strip("x"))
                else:
                    left[1] = e
            for e in rightPol:
                if isinstance(e, str):
                    right[2] = right[2] + float(e.strip("x"))
                else:
                    right[1] = e
            left[0] -= right[0]
            left[1] -= right[1]
            left[2] -= right[2]
            return EQ2(left)

        elif typeOf == 3:
            left = [0, 0]
            right = [0, 0]
            deleteItemsBetween(leftPol, "(", ")")
            deleteItemsBetween(rightPol, "(", ")")
            if parentesisLeft:
                left[0] = numerator
            else:
                right[0] = numerator
            for e in leftPol:
                left[1] += e
            for e in rightPol:
                right[1] += e

            return (left[0] - right[0]) / (right[1] - left[1])

        else:
            numerator = int(numerator.strip("x"))
            denominator = int(denominator.strip("x"))
            if numerator / denominator >= 1:
                finalEquation = []
                if parentesisLeft:
                    finalEquation.append(str(numerator / denominator) + "x")
                for e in deleteItemsBetween(leftPol, "(", ")"):
                    finalEquation.append(e)
                finalEquation.append("=")
                for e in deleteItemsBetween(rightPol, "(", ")"):
                    finalEquation.append(e)
                if not parentesisLeft:
                    finalEquation.append(str(numerator / denominator) + "x")
                return EQ1(finalEquation)
            else:
                fraction = ["(", 1, "/", str(abs(numerator - denominator)) + "x", ")"]
                finalEquation = []
                if parentesisLeft:
                    for e in fraction:
                        finalEquation.append(e)
                for e in deleteItemsBetween(leftPol, "(", ")"):
                    finalEquation.append(e)
                finalEquation.append("=")
                for e in deleteItemsBetween(rightPol, "(", ")"):
                    finalEquation.append(e)
                if not parentesisLeft:
                    for e in fraction:
                        finalEquation.append(e)
                return EQ1(finalEquation)
    else:
        print("más de 2 fracs")
        #Algoritmo con 2 o más fracciones


print(EQ1(["(", "x", "/", 3, ")", -8, "=", 23]))