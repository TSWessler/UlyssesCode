'''
Name:
    NUM_TYPE.py

Version:
    wessler
    2024 November 8
    update to: 2024 October 31
    changes:
        *cosmetic changes to be more consistent with other scripts

Description:
    *designed to run on Ulee's TI-84 Plus CE
    *takes in a string of characters, then classifies whether or not it's a complex number, real or imaginary, rational or irrational, integer or not, whole number or not, natural or not

Inputs:
    *NOTHING
    *(reads an input)

Outputs/does:
        Enter:
            *"number"
        Outputs:
            Whether the "number":
            *is or is not a complex number
            *is a real or imaginary number
            *is a rational or irrational number
            *is or is not an integer
            *is or is not a whole number
            *is or is not a natural number


Used by:
    *NOTHING--this is standalone code

Uses:
    *NOTHING--this is standalone code

NOTES:


'''


def yes_or_no(Y_or_N):
    if Y_or_N:
        print("YES!")
    else:
        print("NO :(")


# =============================
# =============================
# inputs
# =============================
# =============================

print('\n\nEnter "number" to classify:')
print('Note: "j" is for imaginary part')
test_string = input()

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
except:
    is_complex = False
    is_real = False
    is_imaginary = False
    is_rational = False
    is_integer = False
    is_whole = False
    is_natural = False

# =============================
# =============================
# run algorithm
# =============================
# =============================

KeepGoing = True
while KeepGoing:
    KeepGoing = False
    print("\n\nIs " + test_string + " a Complex Number?")
    input()
    if is_complex:
        print("It is a complex number!")
    else:
        print("It is NOT a complex number!")
        print("...at least according to this program :(")
        print("...so, it is not a number :(")
        break

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

    print("\n\nTry again sometime!\n\n")
