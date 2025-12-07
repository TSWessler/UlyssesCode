# =============================
# algorithms
# =============================

def say_number_or_no():
    pass_check_mod = abs((target_number % skip_value) - (start_value % skip_value)) < 1e-15
    pass_check_IncDec = (target_number == start_value) or ((target_number > start_value) and (skip_value > 0)) or ((target_number < start_value) and (skip_value < 0))
    
    if pass_check_mod and pass_check_IncDec:
        print("\nYES!")
        print("You do say the number ")
    else:
        print("\nNO :(")
        print("You do NOT say the number ")
    print(target_number)
    print("while counting by")
    print(skip_value)
    print("starting at")
    print(start_value)


# =============================
# inputs
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
            raise ValueError
        KeepTrying = False
    except ValueError:
        print("\n(must be a non-zero number)\n")

KeepTrying = True
while KeepTrying:
    print('\n\nEnter starting number:')
    try:
        start_value = float(input())
        KeepTrying = False
    except ValueError:
        print('\n(must be a number)\n')

KeepTrying = True
while KeepTrying:
    print("\n\nEnter number you're wondering\nif you say while counting by")
    print(skip_value)
    print('starting at')
    print(str(start_value) + ":")
    try:
        target_number = float(input())
        KeepTrying = False
    except ValueError:
        print('\n(must be a number)\n')

print('\n\n')

# =============================
# run algorithms
# =============================

say_number_or_no()

print('\nTry again sometime!\n')
