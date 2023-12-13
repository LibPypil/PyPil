# Lib PyPil
- A simple Python library that allows you to work with equations and 
  polynomials.
- Contact: [LibPypil@gmail.com](mailto:elcorreoquequieres@correo.com) 
- GitHub: [Pypil](https://github.com/LibPypil/PyPil?)

## Data Structure:
* ### Polynomials:
  - A polynomial can be represented as an array, where every index is the degree of the monomial:
  [1, 1.2, -2] > 1, 1.2x, -2x^2

* ### Equations:
  - 1rst degree:
    - Represented as an array. Items in the array can be a monomial
               or a special character, where the monomials without literal part;
               are integers or floats, and monomials with literal part; are strings.
    - Special Characters:
       - =
       - (
       - )
       - /
    - The coefficient must be only a number, without operators: 
       > ["1x+1x", "3(3x + 3)"] <- This is wrong.
    
       > ["2x", "9x", 9] <- This is perfect.
  - 2nd degree:
    - It must be an array that its length must be max 3 (it will use 
            the monomial rules). If the discriminant is negative, it will
            return a NaN (Not a Number). If 0, will return an array of one
            float, if < 0, will return an array of 2.
          
  - 3rd and more degrees:
    - The input must be an array, following the instructions for a polynomial.
      The method will return an array of all the possibles answers.

## Methods:
 - ### Polynomials:
      - **PolyAddition**
        - <u>Parameters</u>: *polynomial1, polynomial2 (they must be lists, with int and float items).*
        - <u>Returns</u>: *Returns a polynomial*
        - <u>Description</u>: *The function adds 2 polynomials.*

      - **PolySubtraction**
        - <u>Parameters</u>: *polynomial1, polynomial2 (They must be lists, with int and float items).
        - <u>Returns</u>: *Returns a polynomial.*
        - <u>Description</u>: *The function subtracts 2 polynomials (the order is important!).*

      - **PolyMultiplication**
        - <u>Parameters</u>: *polynomial1, polynomial2. They can be both lists (with int and float items), or one of them a list and the other an int / float, but they cannot be only two numbers.*
        - <u>Returns</u>: *Returns a polynomial.*
        - <u>Description</u>: *Multiplicates 2 polynomials, or multiplicates a polynomial with a number.*

      - **PolyDivision**
        - <u>Parameters</u>: *polynomial1, polynomial2. They can be both lists (with int and float items), or one of them a list and the other an int / float, but they cannot be only two numbers. (Order is important!) (polynomial2 cannot be 0).*
        - <u>Returns</u>: *Returns a polynomial.*
        - <u>Description</u>: *Divides 2 polynomials, or divides a polynomial with a number.*

      - **PolyRoot**
        - <u>Parameters</u>: *polynomial. It must be a list, with int and float items.*
        - <u>Returns</u>: *Returns an array.*
        - <u>Description</u>: *It computes the roots of a given polynomial.*

      - **PolyRuffini**
        - <u>Parameters</u>: *polynomial, independentTerm. One must be a list and the other one must be an int or float item.*
        - <u>Returns</u>: *Returns a tuple with a polynomial (0) and rest (1).*
        - <u>Description</u>: *It computes the Ruffini rule.*

      - **PolyPow**
        - <u>Parameters</u>: *polynomial, n. One must be a list and the other one must be an int or float item.*
        - <u>Returns</u>: *Returns a polynomial.*
        - <u>Description</u>: *It powers the polynomial to "n".*

 - ### Equations:
      - **1rst Degree**
        - <u>Parameters</u>:**
        - <u>Returns</u>:**
        - <u>Description</u>:**

      - **2nd Degree**
        - <u>Parameters</u>: *Polynomial. It must be a list (with only int / float items).*
        - <u>Returns</u>: *Returns a tuple with the two results.*
        - <u>Description</u>: *It computes the quadratic formula, and returns x1 (+ result) and x2 (- result).*

      - **3rt Degree and more**
        - <u>Parameters</u>: *Polynomial. It must be a list (with only int / float items)*
        - <u>Returns</u>: *It returns an array with all the possible results.*
        - <u>Description</u>: *It computes it using ruffini and using custom index roots.*