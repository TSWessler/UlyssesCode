'''
Name:
    SKIP_TYP.py

Version:
    wessler
    2024 November 10
    version 1

Description:
    *designed to run on Ulee's TI-84 Plus CE
    *just sees if you typed numbers that are divisible by each other
    *Ulee wanted a program of this name to fit with the other program names, and he also wanted a program with frowning faces, so he made up this program.

Inputs:
    *NOTHING
    *(does have user input values when prompted)

Outputs/does:

        Enter:
            *skip_value
            *target_value
        Output:
            [either "YES!" or "NO :("]
            You do say the number
            [target_value]
            while counting by
            [skip_value]
            starting at
            [start_value]

Used by:
    *NOTHING--this is standalone code

Uses:
    *NOTHING--this is standalone code

NOTES:


'''


# =============================
# =============================
# algorithms
# =============================
# =============================

def say_number_or_no(skip_val, target_num):

    if (target_num % skip_val) < 1e-15:
        pass_check_mod=True
    else:
        pass_check_mod=False

    if ((target_num>0) and (skip_val>0)) or ((target_num<0) and (skip_val<0)):
        pass_check_IncDec=True
    else:
        pass_check_IncDec=False

    if pass_check_mod and pass_check_IncDec:
        print("\n:)")
        print("Good job typing numbers divisible by each other!")
        print(":)")
    else:
        print("\n:(")
        print("Sorry! Cannot type a number to count to that is not divisible by the number counting by!")
        print(":(")


# =============================
# =============================
# inputs
# =============================
# =============================

skip_value = None
target_number = None

KeepTrying = True
while KeepTrying:
    print('\n\nEnter number counting by:')
    try:
        skip_value = float(input())
        if skip_value==0:
            print("\nSorry, can't count by 0's :(\n")
        else:
            KeepTrying = False
    except:
        print('\n(Must be a number)\n')

KeepTrying = True
while KeepTrying:
    print("\n\nEnter number to count to:")
    try:
        target_number = float(input())
        KeepTrying = False
    except:
        print('\n(Must be a number)\n')

print('\n\n')

# =============================
# =============================
# run algorithms
# =============================
# =============================

say_number_or_no( skip_value, target_number)

print('\nTry again sometime!\n')