# =============================
# algorithms
# =============================

def say_number_or_no():
    remainder = target_number % skip_value
    pass_check_mod = (remainder < 1e-15) or (abs(remainder - skip_value) < 1e-15)
    pass_check_IncDec = (target_number == 0) or ((target_number > 0) and (skip_value > 0)) or ((target_number < 0) and (skip_value < 0))
    
    if pass_check_mod and pass_check_IncDec:
        print("\n:)")
        print("Good job typing numbers divisible by each other!")
        print(":)")
    else:
        print("\n:(")
        print("Sorry! Cannot type a number to count to that is not divisible by the number counting by!")
        print(":(")


# =============================
# inputs
# =============================

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
    print("\n\nEnter number to count to:")
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
