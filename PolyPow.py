from multiplication import multiplication


def PolyPow (Polynomial, n):
    # Check parameters
    if not isinstance(Polynomial, list) or not isinstance(n, (float, int)):
        raise TypeError("Unexpected parameter.")
    if not Polynomial or not n:
        return []
    if n == 0:
        return 1
    if isinstance(Polynomial, list):
        if not all(isinstance(e, int) for e in Polynomial):
            raise TypeError("Unexpected parameter.")

    finalPol = Polynomial
    for i in range (1, n):
        finalPol = multiplication(finalPol, Polynomial)
    return finalPol

print(PolyPow([10, 3, 4, 1], 1.5))
