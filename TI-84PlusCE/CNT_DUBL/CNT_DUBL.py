'''
Name:
    CNT_DUBL.py

Version:
    wessler
    2024 November 8
    1st version

Description:
    *designed to run on Ulee's TI-84 Plus CE
    *counts 2^0, 2^1, 2^2, ...

Inputs:
    *NOTHING
    *(does have user input values when prompted)

Outputs/does:

        Enter:
            *max_value
        Output:
            0: 2^0
            1: 2^1
            2: 2^2
            .
            .
            .
            i: 2^i

            it ends when either i==max_number_of_numbers (hard-coded) or 2^i>=max_value

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

def count_doubling(max_val, max_cnt_pause, max_num_of_nums):
    number_of_numbers = 0
    base_value = 2
    exponent = 0

    display_number = 0
    print(str(number_of_numbers) + ":   " + str(display_number))
    input("Press Enter to continue...")

    temp_count = 0
    keep_going = True
    while keep_going:
        number_of_numbers = number_of_numbers + 1
        exponent = exponent + 1

        display_number = base_value ** exponent
        print(str(number_of_numbers) + ":   " + str(display_number))

        if (display_number >= max_val):
            print('\nDone!\n')
            break
        if (number_of_numbers == max_num_of_nums):
            print('\nToo much counting!\nTry a lower max value!\n')
            break

        temp_count = temp_count + 1
        if (temp_count > 9) and (number_of_numbers < max_cnt_pause):
            input("Press Enter to continue...")
            temp_count = 0


# =============================
# =============================
# inputs
# =============================
# =============================

max_number_of_numbers = 1e3
max_count_with_pauses = 101

max_value = None

KeepTrying = True
while KeepTrying:
    print('\n\nEnter max value:')
    try:
        max_value = float(input())
        if max_value > 0:
            KeepTrying = False
        else:
            print('\n(max value must be positive)\n')
    except:
        print('\n(max value must be a number)\n')

print('\n\n')

# =============================
# =============================
# run algorithms
# =============================
# =============================

count_doubling(max_value, max_count_with_pauses, max_number_of_numbers)

print('\nTry again sometime!\n')