# Arithmetic Sequence Algorithm (A. S. Algorithm)
# [Multi Operator Calculator 2.0]
# @maleenrox ft. @OminduD & @sanjulap

# Importing Modules
import math

# Variables

a = 0       # First Number in Calculation
b = 0       # Second Number in Calculation
d = "y"     # Main Command Storage
e = 0       # External First Number Storage
f = 0       # Assignment Loop Counter
g = 0       # External First Number Storage
h = 0       # Pi Input Detector
i = 0       # Degree Value Store in Inverse Operator
j = 0       # Inverse Value Generator
o = 0       # Main Operator Storage
p = 0       # External Operator Storage
q = 0       # Division Zero Error Detector
k = 0       # First Loop Ender
s = 0       # Loop Count Memorise Storage in Assignment Operators
z = 0       # Main Final Value Store

# Welcome Message & Command , Operator List
print('''.............................................
<<<<<<< Arithmatic Sequence Algorithm >>>>>>>
:::::::::::::::::::::::::::::::::::::::::::::
--------------------------------------------------------------------------
Welcome to Arithmatic Sequence Algorithm (M. O. Calculator 2.0) !!!
Developed By :- @maleenrox
--------------------------------------------------------------------------

*** Use the Following Commands & Inputs for Your Calculations...

*$$ Codes of Irrational Real Numbers
>> pi = (Pi) | 3.141592653589793...
>> -pi = (Negative Pi) | -3.141592653589793...
>> e = (e) | 2.718281828459045...
>> -e = (Negative e) | -2.718281828459045...
>> inf = Infinity
>> -inf = Negative Infinity

*$$ Operator Numbers & Symbols List
$ Arithmetic Operators                          $ Assignment Operators
    > 1: Addition (+)                               > 27: Addition Assignment (+=)
    > 2: Subtraction (-)                            > 28: Subtraction Assignment (-=)
    > 3: Multiplication (*)                         > 29: Multiplication Assignment (*=)
    > 4: Division (/)                               > 30: Division Assignment (/=)
    > 5: Modulus (%)				                > 31: Remainder Assignment (%=)
    > 6: Exponent (**)				                > 32: Exponent Assignment (**=)
    > 7: Floor Division (//)			            > 33: Floor Division Assignment (//=)
    > 8: Square Root (-(**))
                                                $ Bitwise Operators
$ Trigonometrical Operators				            > 34: Binary AND (&)
    > 9: Convert Radians to Degrees (rad)		    > 35: Binary OR (|)
    > 10: Convert Degrees to Radians (deg)		    > 36: Binary XOR (^)
    > 11: Sine Function (sin)                       > 37: Binary NOT / Binary Ones Complement (~)
    > 12: Cosine Function (cos)			            > 38: Binary Left Shift (<<)
    > 13: Tangent Function (tan)			        > 39: Binary Right Shift (>>)
    > 14: Cosec Function (cosec)
    > 15: Sec Function (sec)			        $ Logical Operators
    > 16: Cot Function (cot)				        > 40: Logical AND (and)
                                                    > 41: Logical OR (or)
    > 17: Sine Inverse Function (asin)              > 42: Logical Not (not)
    > 18: Cosine Inverse Function (acos)
    > 19: Tangent Inverse Function (atan)	    $ Comparison Operators
    > 20: Cosec Inverse Function (acosec)		    > 43: Equal (==)
    > 21: Sec Inverse Function (asec)		        > 44: Not Equal (!=)
    > 22: Cot Inverse Function (acot)		        > 45: Greater Than (>)
                                                    > 46: Less Than (<)
$ Logarithmic Operators					            > 47: Greater than or Equal to (>=)
    > 23: Log Equation (log)			            > 48: Less than or Equal to (<=)
    > 24: Log [Base = 10] (log10/lg)
    > 25: Log [Base = 2] (log2)
    > 26: Log [Base = e] (loge/ln)

*$$ Other Commands in Algorithm
>> y = Yes
.....(Input Location - "Do You want Another Operator to Final Value :- ")
>> n = No
.....(Input Location - "Do You want Another Operator to Final Value :- ")
>> new = New Calculation
.....(Input Location - "Do You want Another Operator to Final Value :- ")
>> arin/areinput = Re Enter Your First Number in Calculation
.....(Input Location - "Choose Your Operator :- ")
>> brin/breinput = Re Enter Your Second Number in Calculation
.....(Input Location - "Do You want Another Operator to Final Value :- ")
>> clist = Re Print the Command List
.....(Input Location - "Choose Your Operator :- ")
''')

# Main Loop
while d != "n":
    # Beginning Loop
    while k == 0:
        a = str(input("Input Your First Number :- "))
        if a == "pi":
            a = float(math.pi)
            h += 1
        elif a == "-pi":
            a = float((-1) * math.pi)
            h += 1
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
        o = str(input("Choose Your Operator (operator/arin) :- "))
        p = o
        g = a
        # Arithmetic Operators
        if o == "+" or o == "1":
            print(a, "+", "?")
            b = str(input("Input Your Second Number :- "))
            if b == "pi":
                h += 1
                b = float(math.pi)
            elif b == "-pi":
                b = float((-1) * math.pi)
                h += 1
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
            d = str(input("Do You want Another Operator to Final Value (y/n/new/brin/clist) :- "))
        elif o == "-" or o == "2":
            print(a, "-", "?")
            b = str(input("Input Your Second Number :- "))
            if b == "pi":
                b = float(math.pi)
                h += 1
            elif b == "-pi":
                b = float((-1) * math.pi)
                h += 1
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
            d = str(input("Do You want Another Operator to Final Value (y/n/new/brin/clist) :- "))
        elif o == "*" or o == "3":
            print(a, "*", "?")
            b = str(input("Input Your Second Number :- "))
            if b == "pi":
                b = float(math.pi)
                h += 1
            elif b == "-pi":
                b = float((-1) * math.pi)
                h += 1
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
            d = str(input("Do You want Another Operator to Final Value (y/n/new/brin/clist) :- "))
        elif o == "/" or o == "4":
            print(a, "/", "?")
            b = str(input("Input Your Second Number :- "))
            if b == "pi":
                b = float(math.pi)
                h += 1
            elif b == "-pi":
                b = float((-1) * math.pi)
                h += 1
            elif b == "e":
                b = float(math.e)
            elif b == "-e":
                b = float((-1) * math.e)
            elif b == "inf":
                b = float(math.inf)
            elif b == "-inf":
                b = float(-math.inf)
            elif b == "0":
                q += 1
            else:
                b = float(b)
            if q != 0:
                z = math.inf
            else:
                z = a / b
            q = 0
            print(a, "/", b, "=", z)
            print("___________________________")
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new/brin/clist) :- "))
        elif o == "%" or o == "5":
            print(a, "%", "?")
            b = str(input("Input Your Second Number :- "))
            if b == "pi":
                b = float(math.pi)
                h += 1
            elif b == "-pi":
                b = float((-1) * math.pi)
                h += 1
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
            d = str(input("Do You want Another Operator to Final Value (y/n/new/brin/clist) :- "))
        elif o == "**" or o == "6":
            print(a, "**", "?")
            b = str(input("Input Your Second Number :- "))
            if b == "pi":
                b = float(math.pi)
                h += 1
            elif b == "-pi":
                b = float((-1) * math.pi)
                h += 1
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
            d = str(input("Do You want Another Operator to Final Value (y/n/new/brin/clist) :- "))
        elif o == "//" or o == "7":
            print(a, "//", "?")
            b = str(input("Input Your Second Number :- "))
            if b == "pi":
                b = float(math.pi)
                h += 1
            elif b == "-pi":
                b = float((-1) * math.pi)
                h += 1
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
            d = str(input("Do You want Another Operator to Final Value (y/n/new/brin/clist) :- "))
        elif o == "-**" or o == "8":
            z = math.sqrt(a)
            print("sqrt(", a, ")", "=", z)
            print("___________________________")
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new/brin/clist) :- "))

        # Trigonometrical Operators
        elif o == "rad" or o == "9":
            z = math.radians(a)
            h += 0
            print(a, u'\N{DEGREE SIGN}', "----->", z, "rad")
            print("___________________________")
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new/brin/clist) :- "))
        elif o == "deg" or o == "10":
            z = math.degrees(a)
            print(a, "rad", "----->", z, u'\N{DEGREE SIGN}')
            print("___________________________")
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new/brin/clist) :- "))
        elif o == "sin" or o == "11":
            if h == 0:
                z = math.sin(math.radians(a))
            else:
                z = math.sin(a)
            h = 0
            print(u'sin\N{DEGREE SIGN}' "(", a, ")", "=", z)
            print("___________________________")
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new/brin/clist) :- "))
        elif o == "cos" or o == "12":
            if h == 0:
                z = math.cos(math.radians(a))
            else:
                z = math.cos(a)
            h = 0
            print(u'cos\N{DEGREE SIGN}' "(", a, ")", "=", z)
            print("___________________________")
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new/brin/clist) :- "))
        elif o == "tan" or o == "13":
            if h == 0:
                z = math.tan(math.radians(a))
            else:
                z = math.tan(a)
            h = 0
            print(u'tan\N{DEGREE SIGN}' "(", a, ")", "=", z)
            print("___________________________")
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new/brin/clist) :- "))
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
            d = str(input("Do You want Another Operator to Final Value (y/n/new/brin/clist) :- "))
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
            d = str(input("Do You want Another Operator to Final Value (y/n/new/brin/clist) :- "))
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
            d = str(input("Do You want Another Operator to Final Value (y/n/new/brin/clist) :- "))

        elif o == "asin" or o == "17":
            z = math.asin(a)
            i = math.degrees(z)
            print("asin", "(", a, ")", "----->", z, "rad", "|", i, u'\N{DEGREE SIGN}')
            z = i
            print("___________________________")
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new/brin/clist) :- "))
        elif o == "acos" or o == "18":
            z = math.acos(a)
            i = math.degrees(z)
            print("acos", "(", a, ")", "----->", z, "rad", "|", i, u'\N{DEGREE SIGN}')
            z = i
            print("___________________________")
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new/brin/clist) :- "))
        elif o == "atan" or o == "19":
            z = math.atan(a)
            i = math.degrees(z)
            print("atan", "(", a, ")", "----->", z, "rad", "|", i, u'\N{DEGREE SIGN}')
            z = i
            print("___________________________")
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new/brin/clist) :- "))
        elif o == "acosec" or o == "20":
            a = 1 / a
            z = math.asin(a)
            i = math.degrees(z)
            print("acosec", "(", a, ")", "----->", z, "rad", "|", i, u'\N{DEGREE SIGN}')
            z = i
            print("___________________________")
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new/brin/clist) :- "))
        elif o == "asec" or o == "21":
            a = 1 / a
            z = math.acos(a)
            i = math.degrees(z)
            print("asec", "(", a, ")", "----->", z, "rad", "|", i, u'\N{DEGREE SIGN}')
            z = i
            print("___________________________")
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new/brin/clist) :- "))
        elif o == "acot" or o == "22":
            a = 1 / a
            z = math.atan(a)
            i = math.degrees(z)
            print("acot", "(", a, ")", "----->", z, "rad", "|", i, u'\N{DEGREE SIGN}')
            z = i
            print("___________________________")
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new/brin/clist) :- "))

        # Logarithmic Operators
        elif o == "log" or o == "23":
            print("log", "?", a)
            b = str(input("Input Your Second Number :- "))
            if b == "pi":
                b = float(math.pi)
                h += 1
            elif b == "-pi":
                b = float((-1) * math.pi)
                h += 1
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
            d = str(input("Do You want Another Operator to Final Value (y/n/new/brin/clist) :- "))
        elif o == "log10" or o == "lg" or o == "24":
            print("log", "10", a)
            z = math.log10(a)
            print("log", "10", a, "=", z)
            print("___________________________")
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new/brin/clist) :- "))
        elif o == "log2" or o == "25":
            print("log", "2", a)
            z = math.log2(a)
            print("log", "2", a, "=", z)
            print("___________________________")
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new/brin/clist) :- "))
        elif o == "loge" or o == "ln" or o == "26":
            print("log", "e", a)
            z = math.log(a, math.e)
            print("log", "e", a, "=", z)
            print("___________________________")
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new/brin/clist) :- "))

        # Assignment Operators
        elif o == "+=" or o == "27":
            print(a, "+=", "?")
            e = a
            b = str(input("Input Your Second Number :- "))
            if b == "pi":
                b = float(math.pi)
                h += 1
            elif b == "-pi":
                b = float((-1) * math.pi)
                h += 1
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
            d = str(input("Do You want Another Operator to Final Value (y/n/new/brin/clist) :- "))
        elif o == "-=" or o == "28":
            print(a, "-=", "?")
            e = a
            b = str(input("Input Your Second Number :- "))
            if b == "pi":
                b = float(math.pi)
                h += 1
            elif b == "-pi":
                b = float((-1) * math.pi)
                h += 1
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
            d = str(input("Do You want Another Operator to Final Value (y/n/new/brin/clist) :- "))
        elif o == "*=" or o == "29":
            print(a, "*=", "?")
            e = a
            b = str(input("Input Your Second Number :- "))
            if b == "pi":
                b = float(math.pi)
                h += 1
            elif b == "-pi":
                b = float((-1) * math.pi)
                h += 1
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
            d = str(input("Do You want Another Operator to Final Value (y/n/new/brin/clist) :- "))
        elif o == "/=" or o == "30":
            print(a, "/=", "?")
            e = a
            b = str(input("Input Your Second Number :- "))
            if b == "pi":
                b = float(math.pi)
                h += 1
            elif b == "-pi":
                b = float((-1) * math.pi)
                h += 1
            elif b == "e":
                b = float(math.e)
            elif b == "-e":
                b = float((-1) * math.e)
            elif b == "inf":
                b = float(math.inf)
            elif b == "-inf":
                b = float(-math.inf)
            elif b == "0":
                q += 1
            else:
                b = float(b)
            if q != 0:
                print("$ Can not Division Assignment with zero(0)")
                d = "new"
                break
            else:
                s = int(input("Number of Loops required for Your Operator :- "))
                for f in range(s):
                    print("Loop no.", f, "---", "x =", a, "/", b)
                    a /= b
                    print("x =", a, "||", "y =", b)
                f = 0
                z = a
            print("___________________________")
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new/brin/clist) :- "))
        elif o == "%=" or o == "31":
            print(a, "%=", "?")
            e = a
            b = str(input("Input Your Second Number :- "))
            if b == "pi":
                b = float(math.pi)
                h += 1
            elif b == "-pi":
                b = float((-1) * math.pi)
                h += 1
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
            d = str(input("Do You want Another Operator to Final Value (y/n/new/brin/clist) :- "))
        elif o == "**=" or o == "32":
            print(a, "**=", "?")
            e = a
            b = str(input("Input Your Second Number :- "))
            if b == "pi":
                b = float(math.pi)
                h += 1
            elif b == "-pi":
                b = float((-1) * math.pi)
                h += 1
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
            d = str(input("Do You want Another Operator to Final Value (y/n/new/brin/clist) :- "))
        elif o == "//=" or o == "33":
            print(a, "//=", "?")
            e = a
            b = str(input("Input Your Second Number :- "))
            if b == "pi":
                b = float(math.pi)
                h += 1
            elif b == "-pi":
                b = float((-1) * math.pi)
                h += 1
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
            d = str(input("Do You want Another Operator to Final Value (y/n/new/brin/clist) :- "))

        # Bitwise Operators
        elif o == "&" or o == "34":
            a = int(a)
            print(a, "&", "?")
            b = int(input("Input Your Next Number :- "))
            z = a & b
            print(a, "&", b, "=", z)
            print("___________________________")
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new/brin/clist) :- "))
        elif o == "|" or o == "35":
            a = int(a)
            print(a, "|", "?")
            b = int(input("Input Your Next Number :- "))
            z = a | b
            print(a, "|", b, "=", z)
            print("___________________________")
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new/brin/clist) :- "))
        elif o == "^" or o == "36":
            a = int(a)
            print(a, "^", "?")
            b = int(input("Input Your Next Number :- "))
            z = a ^ b
            print(a, "^", b, "=", z)
            print("___________________________")
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new/brin/clist) :- "))
        elif o == "~" or o == "37":
            a = int(a)
            z = ~a
            print("~", a, "=", z)
            print("___________________________")
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new/brin/clist) :- "))
        elif o == "<<" or o == "38":
            a = int(a)
            print(a, "<<", "?")
            b = int(input("Input Your Next Number :- "))
            z = a << b
            print(a, "<<", b, "=", z)
            print("___________________________")
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new/brin/clist) :- "))
        elif o == ">>" or o == "39":
            a = int(a)
            print(a, ">>", "?")
            b = int(input("Input Your Next Number :- "))
            z = a >> b
            print(a, ">>", b, "=", z)
            print("___________________________")
            print("Final Value :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new/brin/clist) :- "))

        # Logical Operators
        elif o == "and" or o == "40":
            print(a, "AND", "?")
            b = int(input("Input Your Next Number :- "))
            z = a and b
            print(a, "AND", b, "=", z)
            print("___________________________")
            print("Final Output :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new/brin/clist) :- "))
        elif o == "or" or o == "41":
            print(a, "OR", "?")
            b = int(input("Input Your Next Number :- "))
            z = a or b
            print(a, "OR", b, "=", z)
            print("___________________________")
            print("Final Output :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new/brin/clist) :- "))
        elif o == "not" or o == "42":
            z = not a
            print("NOT", a, "=", z)
            print("___________________________")
            print("Final Output :-", z)
            d = str(input("Do You want Another Operator to Final Value (y/n/new/brin/clist) :- "))

        #  Comparison Operators
        elif o == "==" or o == "43":
            print(a, "==", "?")
            b = str(input("Input Your Second Number :- "))
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
            d = str(input("Do You want Another Operator (y/n/new/brin/clist) :- "))
        elif o == "!=" or o == "44":
            print(a, "!=", "?")
            b = str(input("Input Your Second Number :- "))
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
            d = str(input("Do You want Another Operator (y/n/new/brin/clist) :- "))
        elif o == ">" or o == "45":
            print(a, ">", "?")
            b = str(input("Input Your Second Number :- "))
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
            d = str(input("Do You want Another Operator (y/n/new/brin/clist) :- "))
        elif o == "<" or o == "46":
            print(a, "<", "?")
            b = str(input("Input Your Second Number :- "))
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
            d = str(input("Do You want Another Operator (y/n/new/brin/clist) :- "))
        elif o == ">=" or o == "47":
            print(a, ">=", "?")
            b = str(input("Input Your Second Number :- "))
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
            d = str(input("Do You want Another Operator (y/n/new/brin/clist) :- "))
        elif o == "<=" or o == "48":
            print(a, "<=", "?")
            b = str(input("Input Your Second Number :- "))
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
            d = str(input("Do You want Another Operator (y/n/new/brin/clist) :- "))

        # Other Commands
        elif o == "areinput" or o == "arin":
            d = "areinput"
        elif o == "breinput" or o == "brin":
            d = "breinputerro"
        else:
            print("___________________________")
            print("$ Invalid Operator/Command Entry...")
            print("$ Re Enter Your Operator/Command...")
            d = "y"
            break
        k += 1
    # Main Carnal
    if d == "new":
        print("$ New Calculation...")
        print("___________________________")
        a = str(input("Input Your First Number :- "))
        if a == "pi":
            a = float(math.pi)
            h += 1
        elif a == "-pi":
            a = float((-1) * math.pi)
            h += 1
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
        o = str(input("Choose Your Operator (operator/arin) :- "))
        g = a
        p = o
    elif d == "y":
        print("Final Value :-", z)
        p = o
        o = str(input("Choose Your Operator (operator/arin) :- "))
        a = z
        g = z
    elif d == "areinput":
        print("$ Refresh Your First Number in Calculation...")
        a = str(input("Input Your First Number :- "))
        if a == "pi":
            a = float(math.pi)
            h += 1
        elif a == "-pi":
            a = float((-1) * math.pi)
            h += 1
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
        o = str(input("Choose Your Operator (operator/arin) :- "))
        p = o
    elif d == "breinput" or d == "brin":
        print("$ Refresh Your Second Number in Calculation...")
        a = g
        o = p
    elif d == "breinputerro":
        print("$ Second Value Not Found...")
        print("$ Re Enter Your Calculation...")
        d = "new"
        continue
    elif d == "clist":
        print('''
*** Use the Following Commands & Inputs for Your Calculations...

*$$ Codes of Irrational Real Number
>> pi = (Pi) | 3.14159265...
>> -pi = (Negative Pi) | -3.14159265...
>> e = (e) | 2.7182818...
>> -e = (Negative e) | -2.7182818...
>> inf = Infinity
>> -inf = Negative Infinity

*$$ Operator Numbers & Symbols List
$ Arithmetic Operators                          $ Assignment Operators
    > 1: Addition (+)                               > 27: Addition Assignment (+=)
    > 2: Subtraction (-)                            > 28: Subtraction Assignment (-=)
    > 3: Multiplication (*)                         > 29: Multiplication Assignment (*=)
    > 4: Division (/)                               > 30: Division Assignment (/=)
    > 5: Modulus (%)				                > 31: Remainder Assignment (%=)
    > 6: Exponent (**)				                > 32: Exponent Assignment (**=)
    > 7: Floor Division (//)			            > 33: Floor Division Assignment (//=)
    > 8: Square Root (-(**))
                                                $ Bitwise Operators
$ Trigonometrical Operators				            > 34: Binary AND (&)
    > 9: Convert Radians to Degrees (rad)		    > 35: Binary OR (|)
    > 10: Convert Degrees to Radians (deg)		    > 36: Binary XOR (^)
    > 11: Sine Function (sin)                       > 37: Binary NOT / Binary Ones Complement (~)
    > 12: Cosine Function (cos)			            > 38: Binary Left Shift (<<)
    > 13: Tangent Function (tan)			        > 39: Binary Right Shift (>>)
    > 14: Cosec Function (cosec)
    > 15: Sec Function (sec)			        $ Logical Operators
    > 16: Cot Function (cot)				        > 40: Logical AND (and)
                                                    > 41: Logical OR (or)
    > 17: Sine Inverse Function (asin)              > 42: Logical Not (not)
    > 18: Cosine Inverse Function (acos)
    > 19: Tangent Inverse Function (atan)	    $ Comparison Operators
    > 20: Cosec Inverse Function (acosec)		    > 43: Equal (==)
    > 21: Sec Inverse Function (asec)		        > 44: Not Equal (!=)
    > 22: Cot Inverse Function (acot)		        > 45: Greater Than (>)
                                                    > 46: Less Than (<)
$ Logarithmic Operators					            > 47: Greater than or Equal to (>=)
    > 23: Log Equation (log)			            > 48: Less than or Equal to (<=)
    > 24: Log [Base = 10] (log10/lg)
    > 25: Log [Base = 2] (log2)
    > 26: Log [Base = e] (loge/ln)

*$$ Other Commands in Algorithm
>> y = Yes
.....(Input Location - "Do You want Another Operator to Final Value :- ")
>> n = No
.....(Input Location - "Do You want Another Operator to Final Value :- ")
>> new = New Calculation
.....(Input Location - "Do You want Another Operator to Final Value :- ")
>> arin/areinput = Re Enter Your First Number in Calculation
.....(Input Location - "Choose Your Operator :- ")
>> brin/breinput = Re Enter Your Second Number in Calculation
.....(Input Location - "Do You want Another Operator to Final Value :- ")
>> clist = Re Print the Command List
.....(Input Location - "Choose Your Operator :- ")
''')
        d = str(input("Do You want Another Operator (y/n/new/brin/clist) :- "))
        continue
    elif d == "n":
        break
    else:
        print("___________________________")
        print("$ Invalid Operator Entry...")
        print("$ Re Enter Your Command...")
        d = str(input("Do You want Another Operator (y/n/new/brin/clist) :- "))
        continue

    # Arithmetic Operators
    if o == "+" or o == "1":
        print(a, "+", "?")
        b = str(input("Input Your Second Number :- "))
        if b == "pi":
            h += 1
            b = float(math.pi)
        elif b == "-pi":
            b = float((-1) * math.pi)
            h += 1
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
        d = str(input("Do You want Another Operator to Final Value (y/n/new/brin/clist) :- "))
    elif o == "-" or o == "2":
        print(a, "-", "?")
        b = str(input("Input Your Second Number :- "))
        if b == "pi":
            b = float(math.pi)
            h += 1
        elif b == "-pi":
            b = float((-1) * math.pi)
            h += 1
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
        d = str(input("Do You want Another Operator to Final Value (y/n/new/brin/clist) :- "))
    elif o == "*" or o == "3":
        print(a, "*", "?")
        b = str(input("Input Your Second Number :- "))
        if b == "pi":
            b = float(math.pi)
            h += 1
        elif b == "-pi":
            b = float((-1) * math.pi)
            h += 1
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
        d = str(input("Do You want Another Operator to Final Value (y/n/new/brin/clist) :- "))
    elif o == "/" or o == "4":
        print(a, "/", "?")
        b = str(input("Input Your Second Number :- "))
        if b == "pi":
            b = float(math.pi)
            h += 1
        elif b == "-pi":
            b = float((-1) * math.pi)
            h += 1
        elif b == "e":
            b = float(math.e)
        elif b == "-e":
            b = float((-1) * math.e)
        elif b == "inf":
            b = float(math.inf)
        elif b == "-inf":
            b = float(-math.inf)
        elif b == "0":
            q += 1
        else:
            b = float(b)
        if q != 0:
            z = math.inf
        else:
            z = a / b
        q = 0
        print(a, "/", b, "=", z)
        print("___________________________")
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new/brin/clist) :- "))
    elif o == "%" or o == "5":
        print(a, "%", "?")
        b = str(input("Input Your Second Number :- "))
        if b == "pi":
            b = float(math.pi)
            h += 1
        elif b == "-pi":
            b = float((-1) * math.pi)
            h += 1
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
        d = str(input("Do You want Another Operator to Final Value (y/n/new/brin/clist) :- "))
    elif o == "**" or o == "6":
        print(a, "**", "?")
        b = str(input("Input Your Second Number :- "))
        if b == "pi":
            b = float(math.pi)
            h += 1
        elif b == "-pi":
            b = float((-1) * math.pi)
            h += 1
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
        d = str(input("Do You want Another Operator to Final Value (y/n/new/brin/clist) :- "))
    elif o == "//" or o == "7":
        print(a, "//", "?")
        b = str(input("Input Your Second Number :- "))
        if b == "pi":
            b = float(math.pi)
            h += 1
        elif b == "-pi":
            b = float((-1) * math.pi)
            h += 1
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
        d = str(input("Do You want Another Operator to Final Value (y/n/new/brin/clist) :- "))
    elif o == "-**" or o == "8":
        z = math.sqrt(a)
        print("sqrt(", a, ")", "=", z)
        print("___________________________")
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new/brin/clist) :- "))

    # Trigonometrical Operators
    elif o == "rad" or o == "9":
        z = math.radians(a)
        h += 0
        print(a, u'\N{DEGREE SIGN}', "----->", z, "rad")
        print("___________________________")
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new/brin/clist) :- "))
    elif o == "deg" or o == "10":
        z = math.degrees(a)
        print(a, "rad", "----->", z, u'\N{DEGREE SIGN}')
        print("___________________________")
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new/brin/clist) :- "))
    elif o == "sin" or o == "11":
        if h == 0:
            z = math.sin(math.radians(a))
        else:
            z = math.sin(a)
        h = 0
        print(u'sin\N{DEGREE SIGN}' "(", a, ")", "=", z)
        print("___________________________")
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new/brin/clist) :- "))
    elif o == "cos" or o == "12":
        if h == 0:
            z = math.cos(math.radians(a))
        else:
            z = math.cos(a)
        h = 0
        print(u'cos\N{DEGREE SIGN}' "(", a, ")", "=", z)
        print("___________________________")
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new/brin/clist) :- "))
    elif o == "tan" or o == "13":
        if h == 0:
            z = math.tan(math.radians(a))
        else:
            z = math.tan(a)
        h = 0
        print(u'tan\N{DEGREE SIGN}' "(", a, ")", "=", z)
        print("___________________________")
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new/brin/clist) :- "))
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
        d = str(input("Do You want Another Operator to Final Value (y/n/new/brin/clist) :- "))
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
        d = str(input("Do You want Another Operator to Final Value (y/n/new/brin/clist) :- "))
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
        d = str(input("Do You want Another Operator to Final Value (y/n/new/brin/clist) :- "))

    elif o == "asin" or o == "17":
        z = math.asin(a)
        i = math.degrees(z)
        print("asin", "(", a, ")", "----->", z, "rad", "|", i, u'\N{DEGREE SIGN}')
        z = i
        print("___________________________")
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new/brin/clist) :- "))
    elif o == "acos" or o == "18":
        z = math.acos(a)
        i = math.degrees(z)
        print("acos", "(", a, ")", "----->", z, "rad", "|", i, u'\N{DEGREE SIGN}')
        z = i
        print("___________________________")
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new/brin/clist) :- "))
    elif o == "atan" or o == "19":
        z = math.atan(a)
        i = math.degrees(z)
        print("atan", "(", a, ")", "----->", z, "rad", "|", i, u'\N{DEGREE SIGN}')
        z = i
        print("___________________________")
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new/brin/clist) :- "))
    elif o == "acosec" or o == "20":
        a = 1 / a
        z = math.asin(a)
        i = math.degrees(z)
        print("acosec", "(", a, ")", "----->", z, "rad", "|", i, u'\N{DEGREE SIGN}')
        z = i
        print("___________________________")
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new/brin/clist) :- "))
    elif o == "asec" or o == "21":
        a = 1 / a
        z = math.acos(a)
        i = math.degrees(z)
        print("asec", "(", a, ")", "----->", z, "rad", "|", i, u'\N{DEGREE SIGN}')
        z = i
        print("___________________________")
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new/brin/clist) :- "))
    elif o == "acot" or o == "22":
        a = 1 / a
        z = math.atan(a)
        i = math.degrees(z)
        print("acot", "(", a, ")", "----->", z, "rad", "|", i, u'\N{DEGREE SIGN}')
        z = i
        print("___________________________")
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new/brin/clist) :- "))

    # Logarithmic Operators
    elif o == "log" or o == "23":
        print("log", "?", a)
        b = str(input("Input Your Second Number :- "))
        if b == "pi":
            b = float(math.pi)
            h += 1
        elif b == "-pi":
            b = float((-1) * math.pi)
            h += 1
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
        d = str(input("Do You want Another Operator to Final Value (y/n/new/brin/clist) :- "))
    elif o == "log10" or o == "lg" or o == "24":
        print("log", "10", a)
        z = math.log10(a)
        print("log", "10", a, "=", z)
        print("___________________________")
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new/brin/clist) :- "))
    elif o == "log2" or o == "25":
        print("log", "2", a)
        z = math.log2(a)
        print("log", "2", a, "=", z)
        print("___________________________")
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new/brin/clist) :- "))
    elif o == "loge" or o == "ln" or o == "26":
        print("log", "e", a)
        z = math.log(a, math.e)
        print("log", "e", a, "=", z)
        print("___________________________")
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new/brin/clist) :- "))

    # Assignment Operators
    elif o == "+=" or o == "27":
        print(a, "+=", "?")
        e = a
        b = str(input("Input Your Second Number :- "))
        if b == "pi":
            b = float(math.pi)
            h += 1
        elif b == "-pi":
            b = float((-1) * math.pi)
            h += 1
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
        d = str(input("Do You want Another Operator to Final Value (y/n/new/brin/clist) :- "))
    elif o == "-=" or o == "28":
        print(a, "-=", "?")
        e = a
        b = str(input("Input Your Second Number :- "))
        if b == "pi":
            b = float(math.pi)
            h += 1
        elif b == "-pi":
            b = float((-1) * math.pi)
            h += 1
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
        d = str(input("Do You want Another Operator to Final Value (y/n/new/brin/clist) :- "))
    elif o == "*=" or o == "29":
        print(a, "*=", "?")
        e = a
        b = str(input("Input Your Second Number :- "))
        if b == "pi":
            b = float(math.pi)
            h += 1
        elif b == "-pi":
            b = float((-1) * math.pi)
            h += 1
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
        d = str(input("Do You want Another Operator to Final Value (y/n/new/brin/clist) :- "))
    elif o == "/=" or o == "30":
        print(a, "/=", "?")
        e = a
        b = str(input("Input Your Second Number :- "))
        if b == "pi":
            b = float(math.pi)
            h += 1
        elif b == "-pi":
            b = float((-1) * math.pi)
            h += 1
        elif b == "e":
            b = float(math.e)
        elif b == "-e":
            b = float((-1) * math.e)
        elif b == "inf":
            b = float(math.inf)
        elif b == "-inf":
            b = float(-math.inf)
        elif b == "0":
            q += 1
        else:
            b = float(b)
        if q != 0:
            print("$ Can not Division Assignment with zero(0)")
            d = "new"
            break
        else:
            s = int(input("Number of Loops required for Your Operator :- "))
            for f in range(s):
                print("Loop no.", f, "---", "x =", a, "/", b)
                a /= b
                print("x =", a, "||", "y =", b)
            f = 0
            z = a
        print("___________________________")
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new/brin/clist) :- "))
    elif o == "%=" or o == "31":
        print(a, "%=", "?")
        e = a
        b = str(input("Input Your Second Number :- "))
        if b == "pi":
            b = float(math.pi)
            h += 1
        elif b == "-pi":
            b = float((-1) * math.pi)
            h += 1
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
        d = str(input("Do You want Another Operator to Final Value (y/n/new/brin/clist) :- "))
    elif o == "**=" or o == "32":
        print(a, "**=", "?")
        e = a
        b = str(input("Input Your Second Number :- "))
        if b == "pi":
            b = float(math.pi)
            h += 1
        elif b == "-pi":
            b = float((-1) * math.pi)
            h += 1
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
        d = str(input("Do You want Another Operator to Final Value (y/n/new/brin/clist) :- "))
    elif o == "//=" or o == "33":
        print(a, "//=", "?")
        e = a
        b = str(input("Input Your Second Number :- "))
        if b == "pi":
            b = float(math.pi)
            h += 1
        elif b == "-pi":
            b = float((-1) * math.pi)
            h += 1
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
        d = str(input("Do You want Another Operator to Final Value (y/n/new/brin/clist) :- "))

    # Bitwise Operators
    elif o == "&" or o == "34":
        a = int(a)
        print(a, "&", "?")
        b = int(input("Input Your Next Number :- "))
        z = a & b
        print(a, "&", b, "=", z)
        print("___________________________")
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new/brin/clist) :- "))
    elif o == "|" or o == "35":
        a = int(a)
        print(a, "|", "?")
        b = int(input("Input Your Next Number :- "))
        z = a | b
        print(a, "|", b, "=", z)
        print("___________________________")
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new/brin/clist) :- "))
    elif o == "^" or o == "36":
        a = int(a)
        print(a, "^", "?")
        b = int(input("Input Your Next Number :- "))
        z = a ^ b
        print(a, "^", b, "=", z)
        print("___________________________")
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new/brin/clist) :- "))
    elif o == "~" or o == "37":
        a = int(a)
        z = ~a
        print("~", a, "=", z)
        print("___________________________")
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new/brin/clist) :- "))
    elif o == "<<" or o == "38":
        a = int(a)
        print(a, "<<", "?")
        b = int(input("Input Your Next Number :- "))
        z = a << b
        print(a, "<<", b, "=", z)
        print("___________________________")
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new/brin/clist) :- "))
    elif o == ">>" or o == "39":
        a = int(a)
        print(a, ">>", "?")
        b = int(input("Input Your Next Number :- "))
        z = a >> b
        print(a, ">>", b, "=", z)
        print("___________________________")
        print("Final Value :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new/brin/clist) :- "))

    # Logical Operators
    elif o == "and" or o == "40":
        print(a, "AND", "?")
        b = int(input("Input Your Next Number :- "))
        z = a and b
        print(a, "AND", b, "=", z)
        print("___________________________")
        print("Final Output :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new/brin/clist) :- "))
    elif o == "or" or o == "41":
        print(a, "OR", "?")
        b = int(input("Input Your Next Number :- "))
        z = a or b
        print(a, "OR", b, "=", z)
        print("___________________________")
        print("Final Output :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new/brin/clist) :- "))
    elif o == "not" or o == "42":
        z = not a
        print("NOT", a, "=", z)
        print("___________________________")
        print("Final Output :-", z)
        d = str(input("Do You want Another Operator to Final Value (y/n/new/brin/clist) :- "))

    #  Comparison Operators
    elif o == "==" or o == "43":
        print(a, "==", "?")
        b = str(input("Input Your Second Number :- "))
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
        d = str(input("Do You want Another Operator (y/n/new/brin/clist) :- "))
    elif o == "!=" or o == "44":
        print(a, "!=", "?")
        b = str(input("Input Your Second Number :- "))
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
        d = str(input("Do You want Another Operator (y/n/new/brin/clist) :- "))
    elif o == ">" or o == "45":
        print(a, ">", "?")
        b = str(input("Input Your Second Number :- "))
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
        d = str(input("Do You want Another Operator (y/n/new/brin/clist) :- "))
    elif o == "<" or o == "46":
        print(a, "<", "?")
        b = str(input("Input Your Second Number :- "))
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
        d = str(input("Do You want Another Operator (y/n/new/brin/clist) :- "))
    elif o == ">=" or o == "47":
        print(a, ">=", "?")
        b = str(input("Input Your Second Number :- "))
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
        d = str(input("Do You want Another Operator (y/n/new/brin/clist) :- "))
    elif o == "<=" or o == "48":
        print(a, "<=", "?")
        b = str(input("Input Your Second Number :- "))
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
        d = str(input("Do You want Another Operator (y/n/new/brin/clist) :- "))

    # Other Commands
    elif o == "areinput" or o == "arin":
        d = "areinput"
    elif o == "breinput" or o == "brin":
        d = "breinputerro"
    else:
        print("___________________________")
        print("$ Invalid Operator/Command Entry...")
        print("$ Re Enter Your Operator/Command...")
        d = "y"

# Exit Part
print("--------------------------------------------------------------------------")
print("Final Value of Your Calculation :-", z)
print("--------------------------------------------------------------------------")
print("Arithmetic Sequence Algorithm from @maleenrox")
input("Press Enter to Continue...")
