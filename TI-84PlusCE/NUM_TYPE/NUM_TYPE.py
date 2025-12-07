# =============================
# helper funcs
# =============================

def yes_or_no(Y_or_N):
    if Y_or_N:
        print("YES!")
    else:
        print("NO :(")

# =============================
# algorithms
# =============================

def classify_number():
    global is_complex, is_imaginary, is_real, is_rational, is_integer, is_whole, is_natural
    
    try:
        complex_val = complex(test_string)
        is_complex = True
        is_imaginary = False
        is_real = False
        is_rational = False
        is_integer = False
        is_whole = False
        is_natural = False
        if complex_val.imag == 0:
            float_val = complex_val.real
            is_real = True
            is_rational = True
            if float_val == round(float_val):
                is_integer = True
                if float_val >= 0:
                    is_whole = True
                    if float_val > 0:
                        is_natural = True
        else:
            if complex_val.real == 0:
                is_imaginary = True
    except ValueError:
        is_complex = False
        is_real = False
        is_imaginary = False
        is_rational = False
        is_integer = False
        is_whole = False
        is_natural = False

def display_results():
    print("\n\nIs " + test_string + " a Complex Number?")
    input()
    if is_complex:
        print("It is a complex number!")
    else:
        print("It is NOT a complex number!")
        print("...at least according to this program :(")
        print("...so, it is not a number :(")
        return
    
    print("\n\nIs " + test_string + " Real or Imaginary?")
    input()
    if is_real and not is_imaginary:
        print("Real!")
    elif is_imaginary and not is_real:
        print("Imaginary!")
    else:
        print("Actually, both!")
    
    print("\n\nIs " + test_string + " Rational or Irrational?")
    input()
    if is_rational:
        print("Rational!")
        print("...at least according to computers")
    else:
        print("Actually, neither!")
    
    print("\n\nIs " + test_string + " an Integer?")
    input()
    yes_or_no(is_integer)
    
    print("\n\nIs " + test_string + " a Whole Number?")
    input()
    yes_or_no(is_whole)
    
    print("\n\nIs " + test_string + " a Natural Number?")
    input()
    yes_or_no(is_natural)


# =============================
# inputs
# =============================

test_string = None

print('\n\nEnter "number" to classify:')
print('Note: "j" is for imaginary part')
test_string = input()

# =============================
# run algorithms
# =============================

classify_number()

display_results()

print("\n\nTry again sometime!\n\n")
