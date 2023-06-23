# Arithmetic Sequence Algorithm
# A. S. Algorithm

import math

a = 0
b = 0
d = "y"
e = 0
f = 0
g = 0
h = 0
i = 0
j = 0
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
        a = str(input("Input Your First Number :- "))
        if a == "pi":
            a = float(math.pi)
        elif a == "-pi":
            a = float((-1) * math.pi)
        elif a == "e":
            a = float(math.e)
        elif a == "-e":
            a = float((-1) * math.e)
        elif a == "inf":
            a = float(math.inf)
        elif a == "-inf":
            a = float(-math.inf)
        else:
            a = float(a)
        o = str(input("Choose Your Operator :- "))
        p = o
        g = a
        if o == "+" or o == "1":
            print(a, "+", "?")
            b = str(input("Input Your First Number :- "))
            if b == "pi":
                b = float(math.pi)
            elif b == "-pi":
                b = float((-1) * math.pi)
            elif b == "e":
                b = float(math.e)
            elif b == "-e":
                b = float((-1) * math.e)
            elif b == "inf":
                b = float(math.inf)
            elif b == "-inf":
                b = float(-math.inf)
            else:
                b = float(b)
            z = a + b
            print(a, "+", b, "=", z)
            print("___________________________")
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
        elif o == "-" or o == "2":
            print(a, "-", "?")
            b = str(input("Input Your First Number :- "))
            if b == "pi":
                b = float(math.pi)
            elif b == "-pi":
                b = float((-1) * math.pi)
            elif b == "e":
                b = float(math.e)
            elif b == "-e":
                b = float((-1) * math.e)
            elif b == "inf":
                b = float(math.inf)
            elif b == "-inf":
                b = float(-math.inf)
            else:
                b = float(b)
            z = a - b
            print(a, "-", b, "=", z)
            print("___________________________")
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
        elif o == "*" or o == "3":
            print(a, "*", "?")
            b = str(input("Input Your First Number :- "))
            if b == "pi":
                b = float(math.pi)
            elif b == "-pi":
                b = float((-1) * math.pi)
            elif b == "e":
                b = float(math.e)
            elif b == "-e":
                b = float((-1) * math.e)
            elif b == "inf":
                b = float(math.inf)
            elif b == "-inf":
                b = float(-math.inf)
            else:
                b = float(b)
            z = a * b
            print(a, "*", b, "=", z)
            print("___________________________")
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
        elif o == "/" or o == "4":
            print(a, "/", "?")
            b = str(input("Input Your First Number :- "))
            if b == "pi":
                b = float(math.pi)
            elif b == "-pi":
                b = float((-1) * math.pi)
            elif b == "e":
                b = float(math.e)
            elif b == "-e":
                b = float((-1) * math.e)
            elif b == "inf":
                b = float(math.inf)
            elif b == "-inf":
                b = float(-math.inf)
            else:
                b = float(b)
            z = a / b
            print(a, "/", b, "=", z)
            print("___________________________")
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
        elif o == "%" or o == "5":
            print(a, "%", "?")
            b = str(input("Input Your First Number :- "))
            if b == "pi":
                b = float(math.pi)
            elif b == "-pi":
                b = float((-1) * math.pi)
            elif b == "e":
                b = float(math.e)
            elif b == "-e":
                b = float((-1) * math.e)
            elif b == "inf":
                b = float(math.inf)
            elif b == "-inf":
                b = float(-math.inf)
            else:
                b = float(b)
            z = a % b
            print(a, "%", b, "=", z)
            print("___________________________")
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
        elif o == "**" or o == "6":
            print(a, "**", "?")
            b = str(input("Input Your First Number :- "))
            if b == "pi":
                b = float(math.pi)
            elif b == "-pi":
                b = float((-1) * math.pi)
            elif b == "e":
                b = float(math.e)
            elif b == "-e":
                b = float((-1) * math.e)
            elif b == "inf":
                b = float(math.inf)
            elif b == "-inf":
                b = float(-math.inf)
            else:
                b = float(b)
            z = a ** b
            print(a, "**", b, "=", z)
            print("___________________________")
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
        elif o == "//" or o == "7":
            print(a, "//", "?")
            b = str(input("Input Your First Number :- "))
            if b == "pi":
                b = float(math.pi)
            elif b == "-pi":
                b = float((-1) * math.pi)
            elif b == "e":
                b = float(math.e)
            elif b == "-e":
                b = float((-1) * math.e)
            elif b == "inf":
                b = float(math.inf)
            elif b == "-inf":
                b = float(-math.inf)
            else:
                b = float(b)
            z = a // b
            print(a, "//", b, "=", z)
            print("___________________________")
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
        elif o == "-**" or o == "8":
            z = math.sqrt(a)
            print("sqrt(", a, ")", "=", z)
            print("___________________________")
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
        elif o == "rad" or o == "9":
            z = math.radians(a)
            h += 0
            print(a, u'\N{DEGREE SIGN}', "----->", z, "rad")
            print("___________________________")
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
        elif o == "deg" or o == "10":
            z = math.degrees(a)
            print(a, "rad", "----->", z, u'\N{DEGREE SIGN}')
            print("___________________________")
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
        elif o == "sin" or o == "11":
            if h == 0:
                z = math.sin(math.radians(a))
            else:
                z = math.sin(a)
            h = 0
            print(u'sin\N{DEGREE SIGN}' "(", a, ")", "=", z)
            print("___________________________")
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
        elif o == "cos" or o == "12":
            if h == 0:
                z = math.cos(math.radians(a))
            else:
                z = math.cos(a)
            h = 0
            print(u'cos\N{DEGREE SIGN}' "(", a, ")", "=", z)
            print("___________________________")
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
        elif o == "tan" or o == "13":
            if h == 0:
                z = math.tan(math.radians(a))
            else:
                z = math.tan(a)
            h = 0
            print(u'tan\N{DEGREE SIGN}' "(", a, ")", "=", z)
            print("___________________________")
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
        elif o == "cosec" or o == "14":
            if h == 0:
                j = math.sin(math.radians(a))
            else:
                j = math.sin(a)
            h = 0
            z = 1 / j
            print(u'cosec\N{DEGREE SIGN}' "(", a, ")", "=", z)
            print("___________________________")
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
        elif o == "sec" or o == "15":
            if h == 0:
                j = math.cos(math.radians(a))
            else:
                j = math.cos(a)
            h = 0
            z = 1 / j
            print(u'sec\N{DEGREE SIGN}' "(", a, ")", "=", z)
            print("___________________________")
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
        elif o == "cot" or o == "16":
            if h == 0:
                j = math.tan(math.radians(a))
            else:
                j = math.tan(a)
            h = 0
            z = 1 / j
            print(u'cot\N{DEGREE SIGN}' "(", a, ")", "=", z)
            print("___________________________")
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
        elif o == "asin" or o == "17":
            z = math.asin(a)
            i = math.degrees(z)
            print("asin", "(", a, ")", "----->", z, "rad", "|", i, u'\N{DEGREE SIGN}')
            z = i
            print("___________________________")
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
        elif o == "acos" or o == "18":
            z = math.acos(a)
            i = math.degrees(z)
            print("acos", "(", a, ")", "----->", z, "rad", "|", i, u'\N{DEGREE SIGN}')
            z = i
            print("___________________________")
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
        elif o == "atan" or o == "19":
            z = math.atan(a)
            i = math.degrees(z)
            print("atan", "(", a, ")", "----->", z, "rad", "|", i, u'\N{DEGREE SIGN}')
            z = i
            print("___________________________")
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
        elif o == "acosec" or o == "20":
            a = 1 / a
            z = math.asin(a)
            i = math.degrees(z)
            print("acosec", "(", a, ")", "----->", z, "rad", "|", i, u'\N{DEGREE SIGN}')
            z = i
            print("___________________________")
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
        elif o == "asec" or o == "21":
            a = 1 / a
            z = math.acos(a)
            i = math.degrees(z)
            print("asec", "(", a, ")", "----->", z, "rad", "|", i, u'\N{DEGREE SIGN}')
            z = i
            print("___________________________")
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
        elif o == "acot" or o == "22":
            a = 1 / a
            z = math.atan(a)
            i = math.degrees(z)
            print("acot", "(", a, ")", "----->", z, "rad", "|", i, u'\N{DEGREE SIGN}')
            z = i
            print("___________________________")
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
        elif o == "log" or o == "23":
            print("log", "?", a)
            b = str(input("Input Your First Number :- "))
            if b == "pi":
                b = float(math.pi)
            elif b == "-pi":
                b = float((-1) * math.pi)
            elif b == "e":
                b = float(math.e)
            elif b == "-e":
                b = float((-1) * math.e)
            elif b == "inf":
                b = float(math.inf)
            elif b == "-inf":
                b = float(-math.inf)
            else:
                b = float(b)
            z = math.log(a, b)
            print("log", b, a, "=", z)
            print("___________________________")
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
        elif o == "log10" or o == "lg" or o == "24":
            print("log", "10", a)
            z = math.log10(a)
            print("log", "10", a, "=", z)
            print("___________________________")
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
        elif o == "log2" or o == "25":
            print("log", "2", a)
            z = math.log2(a)
            print("log", "2", a, "=", z)
            print("___________________________")
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
        elif o == "loge" or o == "ln" or o == "26":
            print("log", "e", a)
            z = math.log(a, math.e)
            print("log", "e", a, "=", z)
            print("___________________________")
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
        elif o == "+=" or o == "27":
            print(a, "+=", "?")
            e = a
            b = str(input("Input Your First Number :- "))
            if b == "pi":
                b = float(math.pi)
            elif b == "-pi":
                b = float((-1) * math.pi)
            elif b == "e":
                b = float(math.e)
            elif b == "-e":
                b = float((-1) * math.e)
            elif b == "inf":
                b = float(math.inf)
            elif b == "-inf":
                b = float(-math.inf)
            else:
                b = float(b)
            s = int(input("Number of Loops required for Your Operator :- "))
            for f in range(s):
                print("Loop no.", f, "---", "x =", a, "+", b)
                a += b
                print("x =", a, "||", "y =", b)
            f = 0
            z = a
            print("___________________________")
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
        elif o == "-=" or o == "28":
            print(a, "-=", "?")
            e = a
            b = str(input("Input Your First Number :- "))
            if b == "pi":
                b = float(math.pi)
            elif b == "-pi":
                b = float((-1) * math.pi)
            elif b == "e":
                b = float(math.e)
            elif b == "-e":
                b = float((-1) * math.e)
            elif b == "inf":
                b = float(math.inf)
            elif b == "-inf":
                b = float(-math.inf)
            else:
                b = float(b)
            s = int(input("Number of Loops required for Your Operator :- "))
            for f in range(s):
                print("Loop no.", f, "---", "x =", a, "-", b)
                a -= b
                print("x =", a, "||", "y =", b)
            f = 0
            z = a
            print("___________________________")
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
        elif o == "*=" or o == "29":
            print(a, "*=", "?")
            e = a
            b = str(input("Input Your First Number :- "))
            if b == "pi":
                b = float(math.pi)
            elif b == "-pi":
                b = float((-1) * math.pi)
            elif b == "e":
                b = float(math.e)
            elif b == "-e":
                b = float((-1) * math.e)
            elif b == "inf":
                b = float(math.inf)
            elif b == "-inf":
                b = float(-math.inf)
            else:
                b = float(b)
            s = int(input("Number of Loops required for Your Operator :- "))
            for f in range(s):
                print("Loop no.", f, "---", "x =", a, "*", b)
                a *= b
                print("x =", a, "||", "y =", b)
            f = 0
            z = a
            print("___________________________")
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
        elif o == "/=" or o == "30":
            print(a, "/=", "?")
            e = a
            b = str(input("Input Your First Number :- "))
            if b == "pi":
                b = float(math.pi)
            elif b == "-pi":
                b = float((-1) * math.pi)
            elif b == "e":
                b = float(math.e)
            elif b == "-e":
                b = float((-1) * math.e)
            elif b == "inf":
                b = float(math.inf)
            elif b == "-inf":
                b = float(-math.inf)
            else:
                b = float(b)
            s = int(input("Number of Loops required for Your Operator :- "))
            for f in range(s):
                print("Loop no.", f, "---", "x =", a, "/", b)
                a /= b
                print("x =", a, "||", "y =", b)
            f = 0
            z = a
            print("___________________________")
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
        elif o == "%=" or o == "31":
            print(a, "%=", "?")
            e = a
            b = str(input("Input Your First Number :- "))
            if b == "pi":
                b = float(math.pi)
            elif b == "-pi":
                b = float((-1) * math.pi)
            elif b == "e":
                b = float(math.e)
            elif b == "-e":
                b = float((-1) * math.e)
            elif b == "inf":
                b = float(math.inf)
            elif b == "-inf":
                b = float(-math.inf)
            else:
                b = float(b)
            s = int(input("Number of Loops required for Your Operator :- "))
            for f in range(s):
                print("Loop no.", f, "---", "x =", a, "%", b)
                a %= b
                print("x =", a, "||", "y =", b)
            f = 0
            z = a
            print("___________________________")
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
        elif o == "**=" or o == "32":
            print(a, "**=", "?")
            e = a
            b = str(input("Input Your First Number :- "))
            if b == "pi":
                b = float(math.pi)
            elif b == "-pi":
                b = float((-1) * math.pi)
            elif b == "e":
                b = float(math.e)
            elif b == "-e":
                b = float((-1) * math.e)
            elif b == "inf":
                b = float(math.inf)
            elif b == "-inf":
                b = float(-math.inf)
            else:
                b = float(b)
            s = int(input("Number of Loops required for Your Operator :- "))
            for f in range(s):
                print("Loop no.", f, "---", "x =", a, "**", b)
                a **= b
                print("x =", a, "||", "y =", b)
            f = 0
            z = a
            print("___________________________")
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
        elif o == "//=" or o == "33":
            print(a, "//=", "?")
            e = a
            b = str(input("Input Your First Number :- "))
            if b == "pi":
                b = float(math.pi)
            elif b == "-pi":
                b = float((-1) * math.pi)
            elif b == "e":
                b = float(math.e)
            elif b == "-e":
                b = float((-1) * math.e)
            elif b == "inf":
                b = float(math.inf)
            elif b == "-inf":
                b = float(-math.inf)
            else:
                b = float(b)
            s = int(input("Number of Loops required for Your Operator :- "))
            for f in range(s):
                print("Loop no.", f, "---", "x =", a, "//", b)
                a //= b
                print("x =", a, "||", "y =", b)
            f = 0
            z = a
            print("___________________________")
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
        elif o == "&" or o == "34":
            a = int(a)
            print(a, "&", "?")
            b = int(input("Input Your Next Number :- "))
            z = a & b
            print(a, "&", b, "=", z)
            print("___________________________")
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
        elif o == "|" or o == "35":
            a = int(a)
            print(a, "|", "?")
            b = int(input("Input Your Next Number :- "))
            z = a | b
            print(a, "|", b, "=", z)
            print("___________________________")
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
        elif o == "^" or o == "36":
            a = int(a)
            print(a, "^", "?")
            b = int(input("Input Your Next Number :- "))
            z = a ^ b
            print(a, "^", b, "=", z)
            print("___________________________")
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
        elif o == "~" or o == "37":
            a = int(a)
            z = ~a
            print("~", a, "=", z)
            print("___________________________")
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
        elif o == "<<" or o == "38":
            a = int(a)
            print(a, "<<", "?")
            b = int(input("Input Your Next Number :- "))
            z = a << b
            print(a, "<<", b, "=", z)
            print("___________________________")
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
        elif o == ">>" or o == "39":
            a = int(a)
            print(a, ">>", "?")
            b = int(input("Input Your Next Number :- "))
            z = a >> b
            print(a, ">>", b, "=", z)
            print("___________________________")
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
        elif o == "and" or o == "40":
            print(a, "AND", "?")
            b = int(input("Input Your Next Number :- "))
            z = a and b
            print(a, "AND", b, "=", z)
            print("___________________________")
            print("Final Output :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
        elif o == "or" or o == "41":
            print(a, "OR", "?")
            b = int(input("Input Your Next Number :- "))
            z = a or b
            print(a, "OR", b, "=", z)
            print("___________________________")
            print("Final Output :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
        elif o == "not" or o == "42":
            z = not a
            print("NOT", a, "=", z)
            print("___________________________")
            print("Final Output :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
        elif o == "==" or o == "43":
            print(a, "==", "?")
            b = str(input("Input Your First Number :- "))
            if b == "pi":
                b = float(math.pi)
            elif b == "-pi":
                b = float((-1) * math.pi)
            elif b == "e":
                b = float(math.e)
            elif b == "-e":
                b = float((-1) * math.e)
            elif b == "inf":
                b = float(math.inf)
            elif b == "-inf":
                b = float(-math.inf)
            else:
                b = float(b)
            z = a == b
            print(a, "==", b, "---", z)
            print("___________________________")
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator (y/n/new) :- "))
        elif o == "!=" or o == "44":
            print(a, "!=", "?")
            b = str(input("Input Your First Number :- "))
            if b == "pi":
                b = float(math.pi)
            elif b == "-pi":
                b = float((-1) * math.pi)
            elif b == "e":
                b = float(math.e)
            elif b == "-e":
                b = float((-1) * math.e)
            elif b == "inf":
                b = float(math.inf)
            elif b == "-inf":
                b = float(-math.inf)
            else:
                b = float(b)
            z = a != b
            print(a, "!=", b, "---", z)
            print("___________________________")
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator (y/n/new) :- "))
        elif o == ">" or o == "45":
            print(a, ">", "?")
            b = str(input("Input Your First Number :- "))
            if b == "pi":
                b = float(math.pi)
            elif b == "-pi":
                b = float((-1) * math.pi)
            elif b == "e":
                b = float(math.e)
            elif b == "-e":
                b = float((-1) * math.e)
            elif b == "inf":
                b = float(math.inf)
            elif b == "-inf":
                b = float(-math.inf)
            else:
                b = float(b)
            z = a > b
            print(a, ">", b, "---", z)
            print("___________________________")
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator (y/n/new) :- "))
        elif o == "<" or o == "46":
            print(a, "<", "?")
            b = str(input("Input Your First Number :- "))
            if b == "pi":
                b = float(math.pi)
            elif b == "-pi":
                b = float((-1) * math.pi)
            elif b == "e":
                b = float(math.e)
            elif b == "-e":
                b = float((-1) * math.e)
            elif b == "inf":
                b = float(math.inf)
            elif b == "-inf":
                b = float(-math.inf)
            else:
                b = float(b)
            z = a < b
            print(a, "<", b, "---", z)
            print("___________________________")
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator (y/n/new) :- "))
        elif o == ">=" or o == "47":
            print(a, ">=", "?")
            b = str(input("Input Your First Number :- "))
            if b == "pi":
                b = float(math.pi)
            elif b == "-pi":
                b = float((-1) * math.pi)
            elif b == "e":
                b = float(math.e)
            elif b == "-e":
                b = float((-1) * math.e)
            elif b == "inf":
                b = float(math.inf)
            elif b == "-inf":
                b = float(-math.inf)
            else:
                b = float(b)
            z = a >= b
            print(a, ">=", b, "---", z)
            print("___________________________")
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator (y/n/new) :- "))
        elif o == "<=" or o == "48":
            print(a, "<=", "?")
            b = str(input("Input Your First Number :- "))
            if b == "pi":
                b = float(math.pi)
            elif b == "-pi":
                b = float((-1) * math.pi)
            elif b == "e":
                b = float(math.e)
            elif b == "-e":
                b = float((-1) * math.e)
            elif b == "inf":
                b = float(math.inf)
            elif b == "-inf":
                b = float(-math.inf)
            else:
                b = float(b)
            z = a <= b
            print(a, "<=", b, "---", z)
            print("___________________________")
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
        a = str(input("Input Your First Number :- "))
        if a == "pi":
            a = float(math.pi)
        elif a == "-pi":
            a = float((-1) * math.pi)
        elif a == "e":
            a = float(math.e)
        elif a == "-e":
            a = float((-1) * math.e)
        elif a == "inf":
            a = float(math.inf)
        elif a == "-inf":
            a = float(-math.inf)
        else:
            a = float(a)
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
        a = str(input("Input Your First Number :- "))
        if a == "pi":
            a = float(math.pi)
        elif a == "-pi":
            a = float((-1) * math.pi)
        elif a == "e":
            a = float(math.e)
        elif a == "-e":
            a = float((-1) * math.e)
        elif a == "inf":
            a = float(math.inf)
        elif a == "-inf":
            a = float(-math.inf)
        else:
            a = float(a)
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
    if o == "+" or o == "1":
        print(a, "+", "?")
        b = str(input("Input Your First Number :- "))
        if b == "pi":
            b = float(math.pi)
        elif b == "-pi":
            b = float((-1) * math.pi)
        elif b == "e":
            b = float(math.e)
        elif b == "-e":
            b = float((-1) * math.e)
        elif b == "inf":
            b = float(math.inf)
        elif b == "-inf":
            b = float(-math.inf)
        else:
            b = float(b)
        z = a + b
        print(a, "+", b, "=", z)
        print("___________________________")
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
    elif o == "-" or o == "2":
        print(a, "-", "?")
        b = str(input("Input Your First Number :- "))
        if b == "pi":
            b = float(math.pi)
        elif b == "-pi":
            b = float((-1) * math.pi)
        elif b == "e":
            b = float(math.e)
        elif b == "-e":
            b = float((-1) * math.e)
        elif b == "inf":
            b = float(math.inf)
        elif b == "-inf":
            b = float(-math.inf)
        else:
            b = float(b)
        z = a - b
        print(a, "-", b, "=", z)
        print("___________________________")
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
    elif o == "*" or o == "3":
        print(a, "*", "?")
        b = str(input("Input Your First Number :- "))
        if b == "pi":
            b = float(math.pi)
        elif b == "-pi":
            b = float((-1) * math.pi)
        elif b == "e":
            b = float(math.e)
        elif b == "-e":
            b = float((-1) * math.e)
        elif b == "inf":
            b = float(math.inf)
        elif b == "-inf":
            b = float(-math.inf)
        else:
            b = float(b)
        z = a * b
        print(a, "*", b, "=", z)
        print("___________________________")
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
    elif o == "/" or o == "4":
        print(a, "/", "?")
        b = str(input("Input Your First Number :- "))
        if b == "pi":
            b = float(math.pi)
        elif b == "-pi":
            b = float((-1) * math.pi)
        elif b == "e":
            b = float(math.e)
        elif b == "-e":
            b = float((-1) * math.e)
        elif b == "inf":
            b = float(math.inf)
        elif b == "-inf":
            b = float(-math.inf)
        else:
            b = float(b)
        z = a / b
        print(a, "/", b, "=", z)
        print("___________________________")
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
    elif o == "%" or o == "5":
        print(a, "%", "?")
        b = str(input("Input Your First Number :- "))
        if b == "pi":
            b = float(math.pi)
        elif b == "-pi":
            b = float((-1) * math.pi)
        elif b == "e":
            b = float(math.e)
        elif b == "-e":
            b = float((-1) * math.e)
        elif b == "inf":
            b = float(math.inf)
        elif b == "-inf":
            b = float(-math.inf)
        else:
            b = float(b)
        z = a % b
        print(a, "%", b, "=", z)
        print("___________________________")
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
    elif o == "**" or o == "6":
        print(a, "**", "?")
        b = str(input("Input Your First Number :- "))
        if b == "pi":
            b = float(math.pi)
        elif b == "-pi":
            b = float((-1) * math.pi)
        elif b == "e":
            b = float(math.e)
        elif b == "-e":
            b = float((-1) * math.e)
        elif b == "inf":
            b = float(math.inf)
        elif b == "-inf":
            b = float(-math.inf)
        else:
            b = float(b)
        z = a ** b
        print(a, "**", b, "=", z)
        print("___________________________")
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
    elif o == "//" or o == "7":
        print(a, "//", "?")
        b = str(input("Input Your First Number :- "))
        if b == "pi":
            b = float(math.pi)
        elif b == "-pi":
            b = float((-1) * math.pi)
        elif b == "e":
            b = float(math.e)
        elif b == "-e":
            b = float((-1) * math.e)
        elif b == "inf":
            b = float(math.inf)
        elif b == "-inf":
            b = float(-math.inf)
        else:
            b = float(b)
        z = a // b
        print(a, "//", b, "=", z)
        print("___________________________")
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
    elif o == "-**" or o == "8":
        z = math.sqrt(a)
        print("sqrt(", a, ")", "=", z)
        print("___________________________")
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
    elif o == "rad" or o == "9":
        z = math.radians(a)
        h += 0
        print(a, u'\N{DEGREE SIGN}', "----->", z, "rad")
        print("___________________________")
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
    elif o == "deg" or o == "10":
        z = math.degrees(a)
        print(a, "rad", "----->", z, u'\N{DEGREE SIGN}')
        print("___________________________")
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
    elif o == "sin" or o == "11":
        if h == 0:
            z = math.sin(math.radians(a))
        else:
            z = math.sin(a)
        h = 0
        print(u'sin\N{DEGREE SIGN}' "(", a, ")", "=", z)
        print("___________________________")
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
    elif o == "cos" or o == "12":
        if h == 0:
            z = math.cos(math.radians(a))
        else:
            z = math.cos(a)
        h = 0
        print(u'cos\N{DEGREE SIGN}' "(", a, ")", "=", z)
        print("___________________________")
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
    elif o == "tan" or o == "13":
        if h == 0:
            z = math.tan(math.radians(a))
        else:
            z = math.tan(a)
        h = 0
        print(u'tan\N{DEGREE SIGN}' "(", a, ")", "=", z)
        print("___________________________")
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
    elif o == "cosec" or o == "14":
        if h == 0:
            j = math.sin(math.radians(a))
        else:
            j = math.sin(a)
        h = 0
        z = 1 / j
        print(u'cosec\N{DEGREE SIGN}' "(", a, ")", "=", z)
        print("___________________________")
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
    elif o == "sec" or o == "15":
        if h == 0:
            j = math.cos(math.radians(a))
        else:
            j = math.cos(a)
        h = 0
        z = 1 / j
        print(u'sec\N{DEGREE SIGN}' "(", a, ")", "=", z)
        print("___________________________")
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
    elif o == "cot" or o == "16":
        if h == 0:
            j = math.tan(math.radians(a))
        else:
            j = math.tan(a)
        h = 0
        z = 1 / j
        print(u'cot\N{DEGREE SIGN}' "(", a, ")", "=", z)
        print("___________________________")
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
    elif o == "asin" or o == "17":
        z = math.asin(a)
        i = math.degrees(z)
        print("asin", "(", a, ")", "----->", z, "rad", "|", i, u'\N{DEGREE SIGN}')
        z = i
        print("___________________________")
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
    elif o == "acos" or o == "18":
        z = math.acos(a)
        i = math.degrees(z)
        print("acos", "(", a, ")", "----->", z, "rad", "|", i, u'\N{DEGREE SIGN}')
        z = i
        print("___________________________")
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
    elif o == "atan" or o == "19":
        z = math.atan(a)
        i = math.degrees(z)
        print("atan", "(", a, ")", "----->", z, "rad", "|", i, u'\N{DEGREE SIGN}')
        z = i
        print("___________________________")
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
    elif o == "acosec" or o == "20":
        a = 1 / a
        z = math.asin(a)
        i = math.degrees(z)
        print("acosec", "(", a, ")", "----->", z, "rad", "|", i, u'\N{DEGREE SIGN}')
        z = i
        print("___________________________")
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
    elif o == "asec" or o == "21":
        a = 1 / a
        z = math.acos(a)
        i = math.degrees(z)
        print("asec", "(", a, ")", "----->", z, "rad", "|", i, u'\N{DEGREE SIGN}')
        z = i
        print("___________________________")
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
    elif o == "acot" or o == "22":
        a = 1 / a
        z = math.atan(a)
        i = math.degrees(z)
        print("acot", "(", a, ")", "----->", z, "rad", "|", i, u'\N{DEGREE SIGN}')
        z = i
        print("___________________________")
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
    elif o == "log" or o == "23":
        print("log", "?", a)
        b = str(input("Input Your First Number :- "))
        if b == "pi":
            b = float(math.pi)
        elif b == "-pi":
            b = float((-1) * math.pi)
        elif b == "e":
            b = float(math.e)
        elif b == "-e":
            b = float((-1) * math.e)
        elif b == "inf":
            b = float(math.inf)
        elif b == "-inf":
            b = float(-math.inf)
        else:
            b = float(b)
        z = math.log(a, b)
        print("log", b, a, "=", z)
        print("___________________________")
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
    elif o == "log10" or o == "lg" or o == "24":
        print("log", "10", a)
        z = math.log10(a)
        print("log", "10", a, "=", z)
        print("___________________________")
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
    elif o == "log2" or o == "25":
        print("log", "2", a)
        z = math.log2(a)
        print("log", "2", a, "=", z)
        print("___________________________")
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
    elif o == "loge" or o == "ln" or o == "26":
        print("log", "e", a)
        z = math.log(a, math.e)
        print("log", "e", a, "=", z)
        print("___________________________")
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
    elif o == "+=" or o == "27":
        print(a, "+=", "?")
        e = a
        b = str(input("Input Your First Number :- "))
        if b == "pi":
            b = float(math.pi)
        elif b == "-pi":
            b = float((-1) * math.pi)
        elif b == "e":
            b = float(math.e)
        elif b == "-e":
            b = float((-1) * math.e)
        elif b == "inf":
            b = float(math.inf)
        elif b == "-inf":
            b = float(-math.inf)
        else:
            b = float(b)
        s = int(input("Number of Loops required for Your Operator :- "))
        for f in range(s):
            print("Loop no.", f, "---", "x =", a, "+", b)
            a += b
            print("x =", a, "||", "y =", b)
        f = 0
        z = a
        print("___________________________")
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
    elif o == "-=" or o == "28":
        print(a, "-=", "?")
        e = a
        b = str(input("Input Your First Number :- "))
        if b == "pi":
            b = float(math.pi)
        elif b == "-pi":
            b = float((-1) * math.pi)
        elif b == "e":
            b = float(math.e)
        elif b == "-e":
            b = float((-1) * math.e)
        elif b == "inf":
            b = float(math.inf)
        elif b == "-inf":
            b = float(-math.inf)
        else:
            b = float(b)
        s = int(input("Number of Loops required for Your Operator :- "))
        for f in range(s):
            print("Loop no.", f, "---", "x =", a, "-", b)
            a -= b
            print("x =", a, "||", "y =", b)
        f = 0
        z = a
        print("___________________________")
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
    elif o == "*=" or o == "29":
        print(a, "*=", "?")
        e = a
        b = str(input("Input Your First Number :- "))
        if b == "pi":
            b = float(math.pi)
        elif b == "-pi":
            b = float((-1) * math.pi)
        elif b == "e":
            b = float(math.e)
        elif b == "-e":
            b = float((-1) * math.e)
        elif b == "inf":
            b = float(math.inf)
        elif b == "-inf":
            b = float(-math.inf)
        else:
            b = float(b)
        s = int(input("Number of Loops required for Your Operator :- "))
        for f in range(s):
            print("Loop no.", f, "---", "x =", a, "*", b)
            a *= b
            print("x =", a, "||", "y =", b)
        f = 0
        z = a
        print("___________________________")
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
    elif o == "/=" or o == "30":
        print(a, "/=", "?")
        e = a
        b = str(input("Input Your First Number :- "))
        if b == "pi":
            b = float(math.pi)
        elif b == "-pi":
            b = float((-1) * math.pi)
        elif b == "e":
            b = float(math.e)
        elif b == "-e":
            b = float((-1) * math.e)
        elif b == "inf":
            b = float(math.inf)
        elif b == "-inf":
            b = float(-math.inf)
        else:
            b = float(b)
        s = int(input("Number of Loops required for Your Operator :- "))
        for f in range(s):
            print("Loop no.", f, "---", "x =", a, "/", b)
            a /= b
            print("x =", a, "||", "y =", b)
        f = 0
        z = a
        print("___________________________")
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
    elif o == "%=" or o == "31":
        print(a, "%=", "?")
        e = a
        b = str(input("Input Your First Number :- "))
        if b == "pi":
            b = float(math.pi)
        elif b == "-pi":
            b = float((-1) * math.pi)
        elif b == "e":
            b = float(math.e)
        elif b == "-e":
            b = float((-1) * math.e)
        elif b == "inf":
            b = float(math.inf)
        elif b == "-inf":
            b = float(-math.inf)
        else:
            b = float(b)
        s = int(input("Number of Loops required for Your Operator :- "))
        for f in range(s):
            print("Loop no.", f, "---", "x =", a, "%", b)
            a %= b
            print("x =", a, "||", "y =", b)
        f = 0
        z = a
        print("___________________________")
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
    elif o == "**=" or o == "32":
        print(a, "**=", "?")
        e = a
        b = str(input("Input Your First Number :- "))
        if b == "pi":
            b = float(math.pi)
        elif b == "-pi":
            b = float((-1) * math.pi)
        elif b == "e":
            b = float(math.e)
        elif b == "-e":
            b = float((-1) * math.e)
        elif b == "inf":
            b = float(math.inf)
        elif b == "-inf":
            b = float(-math.inf)
        else:
            b = float(b)
        s = int(input("Number of Loops required for Your Operator :- "))
        for f in range(s):
            print("Loop no.", f, "---", "x =", a, "**", b)
            a **= b
            print("x =", a, "||", "y =", b)
        f = 0
        z = a
        print("___________________________")
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
    elif o == "//=" or o == "33":
        print(a, "//=", "?")
        e = a
        b = str(input("Input Your First Number :- "))
        if b == "pi":
            b = float(math.pi)
        elif b == "-pi":
            b = float((-1) * math.pi)
        elif b == "e":
            b = float(math.e)
        elif b == "-e":
            b = float((-1) * math.e)
        elif b == "inf":
            b = float(math.inf)
        elif b == "-inf":
            b = float(-math.inf)
        else:
            b = float(b)
        s = int(input("Number of Loops required for Your Operator :- "))
        for f in range(s):
            print("Loop no.", f, "---", "x =", a, "//", b)
            a //= b
            print("x =", a, "||", "y =", b)
        f = 0
        z = a
        print("___________________________")
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
    elif o == "&" or o == "34":
        a = int(a)
        print(a, "&", "?")
        b = int(input("Input Your Next Number :- "))
        z = a & b
        print(a, "&", b, "=", z)
        print("___________________________")
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
    elif o == "|" or o == "35":
        a = int(a)
        print(a, "|", "?")
        b = int(input("Input Your Next Number :- "))
        z = a | b
        print(a, "|", b, "=", z)
        print("___________________________")
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
    elif o == "^" or o == "36":
        a = int(a)
        print(a, "^", "?")
        b = int(input("Input Your Next Number :- "))
        z = a ^ b
        print(a, "^", b, "=", z)
        print("___________________________")
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
    elif o == "~" or o == "37":
        a = int(a)
        z = ~a
        print("~", a, "=", z)
        print("___________________________")
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
    elif o == "<<" or o == "38":
        a = int(a)
        print(a, "<<", "?")
        b = int(input("Input Your Next Number :- "))
        z = a << b
        print(a, "<<", b, "=", z)
        print("___________________________")
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
    elif o == ">>" or o == "39":
        a = int(a)
        print(a, ">>", "?")
        b = int(input("Input Your Next Number :- "))
        z = a >> b
        print(a, ">>", b, "=", z)
        print("___________________________")
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
    elif o == "and" or o == "40":
        print(a, "AND", "?")
        b = int(input("Input Your Next Number :- "))
        z = a and b
        print(a, "AND", b, "=", z)
        print("___________________________")
        print("Final Output :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
    elif o == "or" or o == "41":
        print(a, "OR", "?")
        b = int(input("Input Your Next Number :- "))
        z = a or b
        print(a, "OR", b, "=", z)
        print("___________________________")
        print("Final Output :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
    elif o == "not" or o == "42":
        z = not a
        print("NOT", a, "=", z)
        print("___________________________")
        print("Final Output :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new) :- "))
    elif o == "==" or o == "43":
        print(a, "==", "?")
        b = str(input("Input Your First Number :- "))
        if b == "pi":
            b = float(math.pi)
        elif b == "-pi":
            b = float((-1) * math.pi)
        elif b == "e":
            b = float(math.e)
        elif b == "-e":
            b = float((-1) * math.e)
        elif b == "inf":
            b = float(math.inf)
        elif b == "-inf":
            b = float(-math.inf)
        else:
            b = float(b)
        z = a == b
        print(a, "==", b, "---", z)
        print("___________________________")
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator (y/n/new) :- "))
    elif o == "!=" or o == "44":
        print(a, "!=", "?")
        b = str(input("Input Your First Number :- "))
        if b == "pi":
            b = float(math.pi)
        elif b == "-pi":
            b = float((-1) * math.pi)
        elif b == "e":
            b = float(math.e)
        elif b == "-e":
            b = float((-1) * math.e)
        elif b == "inf":
            b = float(math.inf)
        elif b == "-inf":
            b = float(-math.inf)
        else:
            b = float(b)
        z = a != b
        print(a, "!=", b, "---", z)
        print("___________________________")
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator (y/n/new) :- "))
    elif o == ">" or o == "45":
        print(a, ">", "?")
        b = str(input("Input Your First Number :- "))
        if b == "pi":
            b = float(math.pi)
        elif b == "-pi":
            b = float((-1) * math.pi)
        elif b == "e":
            b = float(math.e)
        elif b == "-e":
            b = float((-1) * math.e)
        elif b == "inf":
            b = float(math.inf)
        elif b == "-inf":
            b = float(-math.inf)
        else:
            b = float(b)
        z = a > b
        print(a, ">", b, "---", z)
        print("___________________________")
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator (y/n/new) :- "))
    elif o == "<" or o == "46":
        print(a, "<", "?")
        b = str(input("Input Your First Number :- "))
        if b == "pi":
            b = float(math.pi)
        elif b == "-pi":
            b = float((-1) * math.pi)
        elif b == "e":
            b = float(math.e)
        elif b == "-e":
            b = float((-1) * math.e)
        elif b == "inf":
            b = float(math.inf)
        elif b == "-inf":
            b = float(-math.inf)
        else:
            b = float(b)
        z = a < b
        print(a, "<", b, "---", z)
        print("___________________________")
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator (y/n/new) :- "))
    elif o == ">=" or o == "47":
        print(a, ">=", "?")
        b = str(input("Input Your First Number :- "))
        if b == "pi":
            b = float(math.pi)
        elif b == "-pi":
            b = float((-1) * math.pi)
        elif b == "e":
            b = float(math.e)
        elif b == "-e":
            b = float((-1) * math.e)
        elif b == "inf":
            b = float(math.inf)
        elif b == "-inf":
            b = float(-math.inf)
        else:
            b = float(b)
        z = a >= b
        print(a, ">=", b, "---", z)
        print("___________________________")
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator (y/n/new) :- "))
    elif o == "<=" or o == "48":
        print(a, "<=", "?")
        b = str(input("Input Your First Number :- "))
        if b == "pi":
            b = float(math.pi)
        elif b == "-pi":
            b = float((-1) * math.pi)
        elif b == "e":
            b = float(math.e)
        elif b == "-e":
            b = float((-1) * math.e)
        elif b == "inf":
            b = float(math.inf)
        elif b == "-inf":
            b = float(-math.inf)
        else:
            b = float(b)
        z = a <= b
        print(a, "<=", b, "---", z)
        print("___________________________")
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
