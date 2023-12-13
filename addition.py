def addition(polynomial1, polynomial2):
    #Check Param
    if not isinstance(polynomial1, list) or not isinstance(polynomial2, list):
        raise TypeError("Unexpected parameter.")
    if not polynomial1 and not polynomial2:
        return []
    if not all(isinstance(e, (int, float)) for e in polynomial1) or not all(isinstance(e, (int, float)) for e in polynomial2):
        raise TypeError("Unexpected parameter.")

    lenPolynomial1 = len(polynomial1)
    lenPolynomial2 = len(polynomial2)
    finalPolynomial = []                 # ella es condicional de otro if :(
    i = 0
    while True:
        try:
            finalPolynomial.append(polynomial1[i] + polynomial2[i])
        except:
            if lenPolynomial1 == lenPolynomial2:
                break
            elif lenPolynomial1 >= i + 1:
                for j in range (i, lenPolynomial1):
                    finalPolynomial.append(polynomial1[j])
            else:
                for j in range (i, lenPolynomial2):
                    finalPolynomial.append(polynomial2[j])
            break
        i += 1
    return finalPolynomial


print(addition([4, 5, 9.87], []))
