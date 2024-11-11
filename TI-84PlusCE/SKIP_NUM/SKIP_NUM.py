'''
Name:
    SKIP_NUM.py

Version:
    wessler
    2024 November 10
    update to: 2024 November 8
    changes:
        *changed (a%b) == (c%d) to abs((a%b)-(c%d))<1e-15
        *made sure can't try counting by 0's

Description:
    *designed to run on Ulee's TI-84 Plus CE
    *checks to see if a number is said if counting by some other number.
        Ex: Is 7.5 said while counting by 1.5 starting at 0?
            0,1.5,3,4.5,6,7.5--YES! 7.5 is said while counting by 1.5 starting at 0

Inputs:
    *NOTHING
    *(does have user input values when prompted)

Outputs/does:

        Enter:
            *skip_value
            *start_value
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

def say_number_or_no(start_val, skip_val, target_num):
    if abs((target_num % skip_val) - (start_val % skip_val)) < 1e-15:
        pass_check_mod = True
    else:
        pass_check_mod = False

    if ((target_num > start_val) and (skip_val > 0)) or ((target_num < start_val) and (skip_val < 0)):
        pass_check_IncDec = True
    else:
        pass_check_IncDec = False

    if pass_check_mod and pass_check_IncDec:
        print("\nYES!")
        print("You do say the number ")
    else:
        print("\nNO :(")
        print("You do NOT say the number ")
    print(target_num)
    print("while counting by")
    print(skip_val)
    print("starting at")
    print(start_val)


# =============================
# =============================
# inputs
# =============================
# =============================

start_value = None
skip_value = None
target_number = None

KeepTrying = True
while KeepTrying:
    print('\n\nEnter number counting by:')
    try:
        skip_value = float(input())
        if skip_value == 0:
            print("\n\nSorry, can't count by 0's :(\n\n")
        else:
            KeepTrying = False
    except:
        print('\n(Must be a number)\n')

KeepTrying = True
while KeepTrying:
    print('\n\nEnter starting number:')
    try:
        start_value = float(input())
        KeepTrying = False
    except:
        print('\n(Must be a number)\n')

KeepTrying = True
while KeepTrying:
    print("\n\nEnter number you're wondering\nif you say while counting by")
    print(skip_value)
    print('starting at')
    print(str(start_value) + ":")
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

say_number_or_no(start_value, skip_value, target_number)

print('\nTry again sometime!\n')
