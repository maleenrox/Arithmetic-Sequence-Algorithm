# Arithmetic Sequence Algorithm
# A. S. Algorithm

import math

a = 0
b = 0
d = "y"
e = 0
f = 0
g = 0
o = 0
p = 0
k = 0
s = 0
t = 0
z = 0

print('''.............................................
####*** Arithmatic Sequence Algorithm ***####
---------------------------------------------

$$$ Operators & Algorithm Commands

Arithmetic Operators
> 1: Addition (+)
> 2: Subtraction (-)
> 3: Multiplication (*)
> 4: Division (/)
> 5: Modulus (%)
> 6: Exponent (**)
> 7: Floor Division (//)
> 8: Square Root (-(**))

Assignment Operators
> 9: Addition Assignment (+=)
> 10: Subtraction Assignment (-=)
> 11: Multiplication Assignment (*=)
> 12: Division Assignment (/=)
> 13: Remainder Assignment (%=)
> 14: Exponent Assignment (**=)
> 15: Floor Division Assignment (//=)

Bitwise Operators
> 16: Binary AND (&)
> 17: Binary OR (|)
> 18: Binary XOR (^)
> 19: Binary NOT / Binary Ones Complement (~)
> 20: Binary Left Shift (<<)
> 21: Binary Right Shift (>>)

Logical Operators
> 22: Logical AND (and)
> 23: Logical OR (or)
> 24: Logical Not (not)

Comparison Operators
> 25: Equal (==)
> 26: Not Equal (!=)
> 27: Greater Than (>)
> 28: Less Than (<)
> 29: Greater than or Equal to (>=)
> 30: Less than or Equal to (<=)
........................................
''')

while d == "y" or d == "new" or d == "areinput" or d == "breinput" or d == "breinputerro" or d == "clist":
    while k == 0:
        a = int(input("Input Your First Number :- "))
        o = str(input("Choose Your Operator :- "))
        p = o
        g = a
        if o == "+":
            print(a, "+", "?")
            b = int(input("Input Your Next Number :- "))
            z = a + b
            print(a, "+", b, "=", z)
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
        elif o == "-":
            print(a, "-", "?")
            b = int(input("Input Your Next Number :- "))
            z = a - b
            print(a, "-", b, "=", z)
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
        elif o == "*":
            print(a, "*", "?")
            b = int(input("Input Your Next Number :- "))
            z = a * b
            print(a, "*", b, "=", z)
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
        elif o == "/":
            print(a, "/", "?")
            b = int(input("Input Your Next Number :- "))
            z = a / b
            print(a, "/", b, "=", z)
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
        elif o == "%":
            print(a, "%", "?")
            b = int(input("Input Your Next Number :- "))
            z = a % b
            print(a, "%", b, "=", z)
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
        elif o == "**":
            print(a, "**", "?")
            b = int(input("Input Your Next Number :- "))
            z = a ** b
            print(a, "**", b, "=", z)
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
        elif o == "//":
            print(a, "//", "?")
            b = int(input("Input Your Next Number :- "))
            z = a // b
            print(a, "//", b, "=", z)
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
        elif o == "-**":
            z = math.sqrt(a)
            print("sqrt(", a, ")", "=", z)
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
        elif o == "+=":
            print(a, "+=", "?")
            e = a
            b = int(input("Input Your Next Number :- "))
            s = int(input("Number of Loops required for Your Operator :- "))
            for f in range(s):
                print("Loop no.", f, "---", "x =", a, "+", b)
                a += b
                print("x =", a, "||", "y =", b)
            f = 0
            z = a
            print("___________________________")
            print("Final Value :-", a)
            d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
        elif o == "-=":
            print(a, "-=", "?")
            e = a
            b = int(input("Input Your Next Number :- "))
            s = int(input("Number of Loops required for Your Operator :- "))
            for f in range(s):
                print("Loop no.", f, "---", "x =", a, "-", b)
                a -= b
                print("x =", a, "||", "y =", b)
            f = 0
            z = a
            print("___________________________")
            print("Final Value :-", a)
            d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
        elif o == "*=":
            print(a, "*=", "?")
            e = a
            b = int(input("Input Your Next Number :- "))
            s = int(input("Number of Loops required for Your Operator :- "))
            for f in range(s):
                print("Loop no.", f, "---", "x =", a, "*", b)
                a *= b
                print("x =", a, "||", "y =", b)
            f = 0
            z = a
            print("___________________________")
            print("Final Value :-", a)
            d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
        elif o == "/=":
            print(a, "/=", "?")
            e = a
            b = int(input("Input Your Next Number :- "))
            s = int(input("Number of Loops required for Your Operator :- "))
            for f in range(s):
                print("Loop no.", f, "---", "x =", a, "/", b)
                a /= b
                print("x =", a, "||", "y =", b)
            f = 0
            z = a
            print("___________________________")
            print("Final Value :-", a)
            d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
        elif o == "%=":
            print(a, "%=", "?")
            e = a
            b = int(input("Input Your Next Number :- "))
            s = int(input("Number of Loops required for Your Operator :- "))
            for f in range(s):
                print("Loop no.", f, "---", "x =", a, "%", b)
                a %= b
                print("x =", a, "||", "y =", b)
            f = 0
            z = a
            print("___________________________")
            print("Final Value :-", a)
            d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
        elif o == "**=":
            print(a, "**=", "?")
            e = a
            b = int(input("Input Your Next Number :- "))
            s = int(input("Number of Loops required for Your Operator :- "))
            for f in range(s):
                print("Loop no.", f, "---", "x =", a, "**", b)
                a **= b
                print("x =", a, "||", "y =", b)
            f = 0
            z = a
            print("___________________________")
            print("Final Value :-", a)
            d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
        elif o == "//=":
            print(a, "//=", "?")
            e = a
            b = int(input("Input Your Next Number :- "))
            s = int(input("Number of Loops required for Your Operator :- "))
            for f in range(s):
                print("Loop no.", f, "---", "x =", a, "//", b)
                a //= b
                print("x =", a, "||", "y =", b)
            f = 0
            z = a
            print("___________________________")
            print("Final Value :-", a)
            d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
        elif o == "&":
            print(a, "&", "?")
            b = int(input("Input Your Next Number :- "))
            z = a & b
            print(a, "&", b, "=", z)
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
        elif o == "|":
            print(a, "|", "?")
            b = int(input("Input Your Next Number :- "))
            z = a | b
            print(a, "|", b, "=", z)
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
        elif o == "^":
            print(a, "^", "?")
            b = int(input("Input Your Next Number :- "))
            z = a ^ b
            print(a, "^", b, "=", z)
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
        elif o == "~":
            z = ~a
            print("~", a, "=", z)
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
        elif o == "<<":
            print(a, "<<", "?")
            b = int(input("Input Your Next Number :- "))
            z = a << b
            print(a, "<<", b, "=", z)
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
        elif o == ">>":
            print(a, ">>", "?")
            b = int(input("Input Your Next Number :- "))
            z = a >> b
            print(a, ">>", b, "=", z)
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
        elif o == "and":
            print(a, "AND", "?")
            b = int(input("Input Your Next Number :- "))
            z = a and b
            print(a, "AND", b, "=", z)
            print("Final Output :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
        elif o == "or":
            print(a, "OR", "?")
            b = int(input("Input Your Next Number :- "))
            z = a or b
            print(a, "OR", b, "=", z)
            print("Final Output :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
        elif o == "not":
            z = not a
            print("NOT", a, "=", z)
            print("Final Output :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
        elif o == "==":
            print(a, "==", "?")
            b = int(input("Input Your Next Number :- "))
            z = a == b
            print(a, "==", b, "---", z)
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator (y/n/new) :- "))
        elif o == "!=":
            print(a, "!=", "?")
            b = int(input("Input Your Next Number :- "))
            z = a != b
            print(a, "!=", b, "---", z)
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator (y/n/new) :- "))
        elif o == ">":
            print(a, ">", "?")
            b = int(input("Input Your Next Number :- "))
            z = a > b
            print(a, ">", b, "---", z)
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator (y/n/new) :- "))
        elif o == "<":
            print(a, "<", "?")
            b = int(input("Input Your Next Number :- "))
            z = a < b
            print(a, "<", b, "---", z)
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator (y/n/new) :- "))
        elif o == ">=":
            print(a, ">=", "?")
            b = int(input("Input Your Next Number :- "))
            z = a >= b
            print(a, ">=", b, "---", z)
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator (y/n/new) :- "))
        elif o == "<=":
            print(a, "<=", "?")
            b = int(input("Input Your Next Number :- "))
            z = a <= b
            print(a, "<=", b, "---", z)
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator (y/n/new) :- "))
        elif o == "1":
            print(a, "+", "?")
            b = int(input("Input Your Next Number :- "))
            z = a + b
            print(a, "+", b, "=", z)
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
        elif o == "2":
            print(a, "-", "?")
            b = int(input("Input Your Next Number :- "))
            z = a - b
            print(a, "-", b, "=", z)
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
        elif o == "3":
            print(a, "*", "?")
            b = int(input("Input Your Next Number :- "))
            z = a * b
            print(a, "*", b, "=", z)
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
        elif o == "4":
            print(a, "/", "?")
            b = int(input("Input Your Next Number :- "))
            z = a / b
            print(a, "/", b, "=", z)
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
        elif o == "5":
            print(a, "%", "?")
            b = int(input("Input Your Next Number :- "))
            z = a % b
            print(a, "%", b, "=", z)
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
        elif o == "6":
            print(a, "**", "?")
            b = int(input("Input Your Next Number :- "))
            z = a ** b
            print(a, "**", b, "=", z)
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
        elif o == "7":
            print(a, "//", "?")
            b = int(input("Input Your Next Number :- "))
            z = a // b
            print(a, "//", b, "=", z)
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
        elif o == "8":
            z = math.sqrt(a)
            print("sqrt(", a, ")", "=", z)
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
        elif o == "9":
            print(a, "+=", "?")
            e = a
            b = int(input("Input Your Next Number :- "))
            s = int(input("Number of Loops required for Your Operator :- "))
            for f in range(s):
                print("Loop no.", f, "---", "x =", a, "+", b)
                a += b
                print("x =", a, "||", "y =", b)
            f = 0
            z = a
            print("___________________________")
            print("Final Value :-", a)
            d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
        elif o == "10":
            print(a, "-=", "?")
            e = a
            b = int(input("Input Your Next Number :- "))
            s = int(input("Number of Loops required for Your Operator :- "))
            for f in range(s):
                print("Loop no.", f, "---", "x =", a, "-", b)
                a -= b
                print("x =", a, "||", "y =", b)
            f = 0
            z = a
            print("___________________________")
            print("Final Value :-", a)
            d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
        elif o == "11":
            print(a, "*=", "?")
            e = a
            b = int(input("Input Your Next Number :- "))
            s = int(input("Number of Loops required for Your Operator :- "))
            for f in range(s):
                print("Loop no.", f, "---", "x =", a, "*", b)
                a *= b
                print("x =", a, "||", "y =", b)
            f = 0
            z = a
            print("___________________________")
            print("Final Value :-", a)
            d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
        elif o == "12":
            print(a, "/=", "?")
            e = a
            b = int(input("Input Your Next Number :- "))
            s = int(input("Number of Loops required for Your Operator :- "))
            for f in range(s):
                print("Loop no.", f, "---", "x =", a, "/", b)
                a /= b
                print("x =", a, "||", "y =", b)
            f = 0
            z = a
            print("___________________________")
            print("Final Value :-", a)
            d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
        elif o == "13":
            print(a, "%=", "?")
            e = a
            b = int(input("Input Your Next Number :- "))
            s = int(input("Number of Loops required for Your Operator :- "))
            for f in range(s):
                print("Loop no.", f, "---", "x =", a, "%", b)
                a %= b
                print("x =", a, "||", "y =", b)
            f = 0
            z = a
            print("___________________________")
            print("Final Value :-", a)
            d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
        elif o == "14":
            print(a, "**=", "?")
            e = a
            b = int(input("Input Your Next Number :- "))
            s = int(input("Number of Loops required for Your Operator :- "))
            for f in range(s):
                print("Loop no.", f, "---", "x =", a, "**", b)
                a **= b
                print("x =", a, "||", "y =", b)
            f = 0
            z = a
            print("___________________________")
            print("Final Value :-", a)
            d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
        elif o == "15":
            print(a, "//=", "?")
            e = a
            b = int(input("Input Your Next Number :- "))
            s = int(input("Number of Loops required for Your Operator :- "))
            for f in range(s):
                print("Loop no.", f, "---", "x =", a, "//", b)
                a //= b
                print("x =", a, "||", "y =", b)
            f = 0
            z = a
            print("___________________________")
            print("Final Value :-", a)
            d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
        elif o == "16":
            print(a, "&", "?")
            b = int(input("Input Your Next Number :- "))
            z = a & b
            print(a, "&", b, "=", z)
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
        elif o == "17":
            print(a, "|", "?")
            b = int(input("Input Your Next Number :- "))
            z = a | b
            print(a, "|", b, "=", z)
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
        elif o == "18":
            print(a, "^", "?")
            b = int(input("Input Your Next Number :- "))
            z = a ^ b
            print(a, "^", b, "=", z)
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
        elif o == "19":
            z = ~a
            print("~", a, "=", z)
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
        elif o == "20":
            print(a, "<<", "?")
            b = int(input("Input Your Next Number :- "))
            z = a << b
            print(a, "<<", b, "=", z)
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
        elif o == "21":
            print(a, ">>", "?")
            b = int(input("Input Your Next Number :- "))
            z = a >> b
            print(a, ">>", b, "=", z)
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
        elif o == "22":
            print(a, "AND", "?")
            b = int(input("Input Your Next Number :- "))
            z = a and b
            print(a, "AND", b, "=", z)
            print("Final Output :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
        elif o == "23":
            print(a, "OR", "?")
            b = int(input("Input Your Next Number :- "))
            z = a or b
            print(a, "OR", b, "=", z)
            print("Final Output :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
        elif o == "24":
            z = not a
            print("NOT", a, "=", z)
            print("Final Output :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
        elif o == "25":
            print(a, "==", "?")
            b = int(input("Input Your Next Number :- "))
            z = a == b
            print(a, "==", b, "---", z)
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator (y/n/new) :- "))
        elif o == "26":
            print(a, "!=", "?")
            b = int(input("Input Your Next Number :- "))
            z = a != b
            print(a, "!=", b, "---", z)
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator (y/n/new) :- "))
        elif o == "27":
            print(a, ">", "?")
            b = int(input("Input Your Next Number :- "))
            z = a > b
            print(a, ">", b, "---", z)
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator (y/n/new) :- "))
        elif o == "28":
            print(a, "<", "?")
            b = int(input("Input Your Next Number :- "))
            z = a < b
            print(a, "<", b, "---", z)
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator (y/n/new) :- "))
        elif o == "29":
            print(a, ">=", "?")
            b = int(input("Input Your Next Number :- "))
            z = a >= b
            print(a, ">=", b, "---", z)
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator (y/n/new) :- "))
        elif o == "30":
            print(a, "<=", "?")
            b = int(input("Input Your Next Number :- "))
            z = a <= b
            print(a, "<=", b, "---", z)
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator (y/n/new) :- "))
        elif o == "areinput":
            d = "areinput"
        elif o == "breinput":
            d = "breinputerro"
        else:
            print("Invalid Operator Data Entry...")
            print("___________________________")
            o = str(input("Choose Your Operator :- "))
            d = "new"
            break
        k += 1
    # .................................................
    if d == "new":
        print("$ New Calculation...")
        print("___________________________")
        a = int(input("Input Your First Number :- "))
        o = str(input("Choose Your Operator :- "))
        g = a
        p = o
    elif d == "y":
        print("Final Value :-", z)
        p = o
        o = str(input("Choose Your Next Operator :- "))
        a = z
        g = z
    elif d == "areinput":
        print("$ Refresh Your First Number in Calculation...")
        a = int(input("Input Your First Number :- "))
        g = a
        o = str(input("Choose Your Operator :- "))
        p = o
    elif d == "breinput":
        print("$ Refresh Your Second Number in Calculation...")
        a = g
        o = p
    elif d == "breinputerro":
        print("$ Second Value Not Found...")
        print("$ Re Enter Your Calculation...")
        d = "new"
        continue
    elif d == "clist":
        print("Hi Hi Hi Hi Hi Hi")
        d = str(input("Do You want Another Operator (y/n/new) :- "))
        continue
    elif d == "n":
        break
    if o == "+":
        print(a, "+", "?")
        b = int(input("Input Your Next Number :- "))
        z = a + b
        print(a, "+", b, "=", z)
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
    elif o == "-":
        print(a, "-", "?")
        b = int(input("Input Your Next Number :- "))
        z = a - b
        print(a, "-", b, "=", z)
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
    elif o == "*":
        print(a, "*", "?")
        b = int(input("Input Your Next Number :- "))
        z = a * b
        print(a, "*", b, "=", z)
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
    elif o == "/":
        print(a, "/", "?")
        b = int(input("Input Your Next Number :- "))
        z = a / b
        print(a, "/", b, "=", z)
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
    elif o == "%":
        print(a, "%", "?")
        b = int(input("Input Your Next Number :- "))
        z = a % b
        print(a, "%", b, "=", z)
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
    elif o == "**":
        print(a, "**", "?")
        b = int(input("Input Your Next Number :- "))
        z = a ** b
        print(a, "**", b, "=", z)
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
    elif o == "//":
        print(a, "//", "?")
        b = int(input("Input Your Next Number :- "))
        z = a // b
        print(a, "//", b, "=", z)
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
    elif o == "-**":
        z = math.sqrt(a)
        print("sqrt(", a, ")", "=", z)
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
    elif o == "+=":
        print(a, "+=", "?")
        e = a
        b = int(input("Input Your Next Number :- "))
        s = int(input("Number of Loops required for Your Operator :- "))
        for f in range(s):
            print("Loop no.", f, "---", "x =", a, "+", b)
            a += b
            print("x =", a, "||", "y =", b)
        f = 0
        z = a
        print("___________________________")
        print("Final Value :-", a)
        d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
    elif o == "-=":
        print(a, "-=", "?")
        e = a
        b = int(input("Input Your Next Number :- "))
        s = int(input("Number of Loops required for Your Operator :- "))
        for f in range(s):
            print("Loop no.", f, "---", "x =", a, "-", b)
            a -= b
            print("x =", a, "||", "y =", b)
        f = 0
        z = a
        print("___________________________")
        print("Final Value :-", a)
        d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
    elif o == "*=":
        print(a, "*=", "?")
        e = a
        b = int(input("Input Your Next Number :- "))
        s = int(input("Number of Loops required for Your Operator :- "))
        for f in range(s):
            print("Loop no.", f, "---", "x =", a, "*", b)
            a *= b
            print("x =", a, "||", "y =", b)
        f = 0
        z = a
        print("___________________________")
        print("Final Value :-", a)
        d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
    elif o == "/=":
        print(a, "/=", "?")
        e = a
        b = int(input("Input Your Next Number :- "))
        s = int(input("Number of Loops required for Your Operator :- "))
        for f in range(s):
            print("Loop no.", f, "---", "x =", a, "/", b)
            a /= b
            print("x =", a, "||", "y =", b)
        f = 0
        z = a
        print("___________________________")
        print("Final Value :-", a)
        d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
    elif o == "%=":
        print(a, "%=", "?")
        e = a
        b = int(input("Input Your Next Number :- "))
        s = int(input("Number of Loops required for Your Operator :- "))
        for f in range(s):
            print("Loop no.", f, "---", "x =", a, "%", b)
            a %= b
            print("x =", a, "||", "y =", b)
        f = 0
        z = a
        print("___________________________")
        print("Final Value :-", a)
        d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
    elif o == "**=":
        print(a, "**=", "?")
        e = a
        b = int(input("Input Your Next Number :- "))
        s = int(input("Number of Loops required for Your Operator :- "))
        for f in range(s):
            print("Loop no.", f, "---", "x =", a, "**", b)
            a **= b
            print("x =", a, "||", "y =", b)
        f = 0
        z = a
        print("___________________________")
        print("Final Value :-", a)
        d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
    elif o == "//=":
        print(a, "//=", "?")
        e = a
        b = int(input("Input Your Next Number :- "))
        s = int(input("Number of Loops required for Your Operator :- "))
        for f in range(s):
            print("Loop no.", f, "---", "x =", a, "//", b)
            a //= b
            print("x =", a, "||", "y =", b)
        f = 0
        z = a
        print("___________________________")
        print("Final Value :-", a)
        d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
    elif o == "&":
        print(a, "&", "?")
        b = int(input("Input Your Next Number :- "))
        z = a & b
        print(a, "&", b, "=", z)
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
    elif o == "|":
        print(a, "|", "?")
        b = int(input("Input Your Next Number :- "))
        z = a | b
        print(a, "|", b, "=", z)
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
    elif o == "^":
        print(a, "^", "?")
        b = int(input("Input Your Next Number :- "))
        z = a ^ b
        print(a, "^", b, "=", z)
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
    elif o == "~":
        z = ~a
        print("~", a, "=", z)
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
    elif o == "<<":
        print(a, "<<", "?")
        b = int(input("Input Your Next Number :- "))
        z = a << b
        print(a, "<<", b, "=", z)
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
    elif o == ">>":
        print(a, ">>", "?")
        b = int(input("Input Your Next Number :- "))
        z = a >> b
        print(a, ">>", b, "=", z)
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
    elif o == "and":
        print(a, "AND", "?")
        b = int(input("Input Your Next Number :- "))
        z = a and b
        print(a, "AND", b, "=", z)
        print("Final Output :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
    elif o == "or":
        print(a, "OR", "?")
        b = int(input("Input Your Next Number :- "))
        z = a or b
        print(a, "OR", b, "=", z)
        print("Final Output :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
    elif o == "not":
        z = not a
        print("NOT", a, "=", z)
        print("Final Output :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
    elif o == "==":
        print(a, "==", "?")
        b = int(input("Input Your Next Number :- "))
        z = a == b
        print(a, "==", b, "---", z)
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator (y/n/new) :- "))
    elif o == "!=":
        print(a, "!=", "?")
        b = int(input("Input Your Next Number :- "))
        z = a != b
        print(a, "!=", b, "---", z)
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator (y/n/new) :- "))
    elif o == ">":
        print(a, ">", "?")
        b = int(input("Input Your Next Number :- "))
        z = a > b
        print(a, ">", b, "---", z)
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator (y/n/new) :- "))
    elif o == "<":
        print(a, "<", "?")
        b = int(input("Input Your Next Number :- "))
        z = a < b
        print(a, "<", b, "---", z)
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator (y/n/new) :- "))
    elif o == ">=":
        print(a, ">=", "?")
        b = int(input("Input Your Next Number :- "))
        z = a >= b
        print(a, ">=", b, "---", z)
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator (y/n/new) :- "))
    elif o == "<=":
        print(a, "<=", "?")
        b = int(input("Input Your Next Number :- "))
        z = a <= b
        print(a, "<=", b, "---", z)
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator (y/n/new) :- "))
    elif o == "1":
        print(a, "+", "?")
        b = int(input("Input Your Next Number :- "))
        z = a + b
        print(a, "+", b, "=", z)
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
    elif o == "2":
        print(a, "-", "?")
        b = int(input("Input Your Next Number :- "))
        z = a - b
        print(a, "-", b, "=", z)
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
    elif o == "3":
        print(a, "*", "?")
        b = int(input("Input Your Next Number :- "))
        z = a * b
        print(a, "*", b, "=", z)
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
    elif o == "4":
        print(a, "/", "?")
        b = int(input("Input Your Next Number :- "))
        z = a / b
        print(a, "/", b, "=", z)
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
    elif o == "5":
        print(a, "%", "?")
        b = int(input("Input Your Next Number :- "))
        z = a % b
        print(a, "%", b, "=", z)
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
    elif o == "6":
        print(a, "**", "?")
        b = int(input("Input Your Next Number :- "))
        z = a ** b
        print(a, "**", b, "=", z)
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
    elif o == "7":
        print(a, "//", "?")
        b = int(input("Input Your Next Number :- "))
        z = a // b
        print(a, "//", b, "=", z)
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
    elif o == "8":
        z = math.sqrt(a)
        print("sqrt(", a, ")", "=", z)
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
    elif o == "9":
        print(a, "+=", "?")
        e = a
        b = int(input("Input Your Next Number :- "))
        s = int(input("Number of Loops required for Your Operator :- "))
        for f in range(s):
            print("Loop no.", f, "---", "x =", a, "+", b)
            a += b
            print("x =", a, "||", "y =", b)
        f = 0
        z = a
        print("___________________________")
        print("Final Value :-", a)
        d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
    elif o == "10":
        print(a, "-=", "?")
        e = a
        b = int(input("Input Your Next Number :- "))
        s = int(input("Number of Loops required for Your Operator :- "))
        for f in range(s):
            print("Loop no.", f, "---", "x =", a, "-", b)
            a -= b
            print("x =", a, "||", "y =", b)
        f = 0
        z = a
        print("___________________________")
        print("Final Value :-", a)
        d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
    elif o == "11":
        print(a, "*=", "?")
        e = a
        b = int(input("Input Your Next Number :- "))
        s = int(input("Number of Loops required for Your Operator :- "))
        for f in range(s):
            print("Loop no.", f, "---", "x =", a, "*", b)
            a *= b
            print("x =", a, "||", "y =", b)
        f = 0
        z = a
        print("___________________________")
        print("Final Value :-", a)
        d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
    elif o == "12":
        print(a, "/=", "?")
        e = a
        b = int(input("Input Your Next Number :- "))
        s = int(input("Number of Loops required for Your Operator :- "))
        for f in range(s):
            print("Loop no.", f, "---", "x =", a, "/", b)
            a /= b
            print("x =", a, "||", "y =", b)
        f = 0
        z = a
        print("___________________________")
        print("Final Value :-", a)
        d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
    elif o == "13":
        print(a, "%=", "?")
        e = a
        b = int(input("Input Your Next Number :- "))
        s = int(input("Number of Loops required for Your Operator :- "))
        for f in range(s):
            print("Loop no.", f, "---", "x =", a, "%", b)
            a %= b
            print("x =", a, "||", "y =", b)
        f = 0
        z = a
        print("___________________________")
        print("Final Value :-", a)
        d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
    elif o == "14":
        print(a, "**=", "?")
        e = a
        b = int(input("Input Your Next Number :- "))
        s = int(input("Number of Loops required for Your Operator :- "))
        for f in range(s):
            print("Loop no.", f, "---", "x =", a, "**", b)
            a **= b
            print("x =", a, "||", "y =", b)
        f = 0
        z = a
        print("___________________________")
        print("Final Value :-", a)
        d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
    elif o == "15":
        print(a, "//=", "?")
        e = a
        b = int(input("Input Your Next Number :- "))
        s = int(input("Number of Loops required for Your Operator :- "))
        for f in range(s):
            print("Loop no.", f, "---", "x =", a, "//", b)
            a //= b
            print("x =", a, "||", "y =", b)
        f = 0
        z = a
        print("___________________________")
        print("Final Value :-", a)
        d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
    elif o == "16":
        print(a, "&", "?")
        b = int(input("Input Your Next Number :- "))
        z = a & b
        print(a, "&", b, "=", z)
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
    elif o == "17":
        print(a, "|", "?")
        b = int(input("Input Your Next Number :- "))
        z = a | b
        print(a, "|", b, "=", z)
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
    elif o == "18":
        print(a, "^", "?")
        b = int(input("Input Your Next Number :- "))
        z = a ^ b
        print(a, "^", b, "=", z)
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
    elif o == "19":
        z = ~a
        print("~", a, "=", z)
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
    elif o == "20":
        print(a, "<<", "?")
        b = int(input("Input Your Next Number :- "))
        z = a << b
        print(a, "<<", b, "=", z)
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
    elif o == "21":
        print(a, ">>", "?")
        b = int(input("Input Your Next Number :- "))
        z = a >> b
        print(a, ">>", b, "=", z)
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
    elif o == "22":
        print(a, "AND", "?")
        b = int(input("Input Your Next Number :- "))
        z = a and b
        print(a, "AND", b, "=", z)
        print("Final Output :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
    elif o == "23":
        print(a, "OR", "?")
        b = int(input("Input Your Next Number :- "))
        z = a or b
        print(a, "OR", b, "=", z)
        print("Final Output :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
    elif o == "24":
        z = not a
        print("NOT", a, "=", z)
        print("Final Output :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
    elif o == "25":
        print(a, "==", "?")
        b = int(input("Input Your Next Number :- "))
        z = a == b
        print(a, "==", b, "---", z)
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator (y/n/new) :- "))
    elif o == "26":
        print(a, "!=", "?")
        b = int(input("Input Your Next Number :- "))
        z = a != b
        print(a, "!=", b, "---", z)
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator (y/n/new) :- "))
    elif o == "27":
        print(a, ">", "?")
        b = int(input("Input Your Next Number :- "))
        z = a > b
        print(a, ">", b, "---", z)
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator (y/n/new) :- "))
    elif o == "28":
        print(a, "<", "?")
        b = int(input("Input Your Next Number :- "))
        z = a < b
        print(a, "<", b, "---", z)
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator (y/n/new) :- "))
    elif o == "29":
        print(a, ">=", "?")
        b = int(input("Input Your Next Number :- "))
        z = a >= b
        print(a, ">=", b, "---", z)
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator (y/n/new) :- "))
    elif o == "30":
        print(a, "<=", "?")
        b = int(input("Input Your Next Number :- "))
        z = a <= b
        print(a, "<=", b, "---", z)
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator (y/n/new) :- "))
    elif o == "areinput":
        d = "areinput"
    elif o == "breinput":
        d = "breinputerro"
    else:
        print("Invalid Operator Data Entry...")
        print("___________________________")
        o = str(input("Choose Your Operator :- "))
        d = "new"

print("Final Value :-", z)
print("Thank You")
input("Press Enter to Continue...")
