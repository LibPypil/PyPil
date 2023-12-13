~·~·~·~·~·~·~·~·~·~·~·~·~·~·~·~·~·~·~·~·~·~·~·~·~·~·~·~·~·~·~·~·~·~·~
                                Lib PyPil
~·~·~·~·~·~·~·~·~·~·~·~·~·~·~·~·~·~·~·~·~·~·~·~·~·~·~·~·~·~·~·~·~·~·~
- A simple Python library that allows you to work with equations and 
  polynomials.
- Contact: LibPypil@gmail.com 
- GitHub: Pypil
# - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - #
Data Structure:
    - Polynomials:
        - A polynomial can be represented as an array, where every
          index is the degree of the monomial:
        - [1, 1.2, -2] -> 1, 1.2x, -2x^2
    Equations:
        - Special Characters:
            - =
            - (
            - )
            - /
        - 1rst degree:
            - Represented as an array. Items in the array can be a monomial
              or a special character, where the monomials without literal part;
              are integers or floats, and monomials with literal part; are strings.
            - The coefficient must be only a number, without operators: 
               * ["1x+1x", "3(3x + 3)"] <- This is wrong.
               * ["2x", "9x", 9] <- This is perfect.
        - 2nd degree:
            - It must be an array that its length must be max 3 (it will use 
              the monomial rules). If the discriminant is negative, it will
              return a NaN (Not a Number). If 0, will return an array of one
              float, if < 0, will return an array of 2.
        - 3rd and more degrees:
            - The input must be an array, following the instructions for a polynomial.
              The method will return an array of all the possibles answers.
Methods:
    - Polynomials:

        - PolyAddition
            Parameters: polynomial1, polynomial2 
                * They must be lists, with int and float items.
            Returns:
                * Returns a polynomial
            Description: The function adds 2 polynomials.

        - PolySubtraction
            Parameters: polynomial1, polynomial2
                * They must be lists, with int and float items.
            Returns:   
                * Returns a polynomial
            Description: The function subtracts 2 polynomials (the order is important!)

        - PolyMultiplication
            Parameters: polynomial1, polynomial2
                * They can be both lists (with int and float items), or one of them a list and the other an int / float
                  but they cannot be only two numbers.
            Returns:
                * Returns a polynomial
            Description: Multiplicates 2 polynomials, or multiplicates a polynomial with a number.

        - PolyDivision
            Parameters: polynomial1, polynomial2
                * They can be both lists (with int and float items), or one of them a list and the other an int / float
                  but they cannot be only two numbers. (Order is important!) (polynomial2 cannot be 0).
            Returns:
                * Returns a polynomial
            Description: Divides 2 polynomials, or divides a polynomial with a number.

        - PolyRoot
            Parameters: polynomial
                * It must be a list, with int and float items.
            Returns:  
                * Returns an array.
            Description: It computes the roots of a given polynomial

        - PolyRuffini
            Parameters: polynomial, independentTerm
                * One must be a list and the other one must be an int or float item
            Returns: 
                * Returns a tuple with a polynomial (0) and rest (1)
            Description: It computes the Ruffini rule.

        - PolyPow
            Parameters: polynomial, n
                * One must be a list and the other one must be an int or float item
            Returns: 
                * Returns a polynomial
            Description: it powers the polynomial to "n"

    - Equations:
        - 1rst Degree
            Parameters:
                *
            Returns:
                *
            Description:

        - 2nd Degree
            Parameters: Polynomial
                * It must be a list (with only int / float items)
            Returns:
                * Returns a tuple with the two results.
            Description: It computes the quadratic formula, and returns x1 (+ result) and x2 (- result)

        - 3rt Degree and more
            Parameters: Polynomial
                * It must be a list (with only int / float items)
            Returns:
                * It returns an array with all the possible results.
            Description: It computes it using ruffini and using custom index roots.