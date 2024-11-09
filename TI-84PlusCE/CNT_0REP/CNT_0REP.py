'''
Name:
    CNT_0REP.py

Version:
    wessler
    2024 November 8
    update to: 2024 November 7
    changes:
        *cosmetic changes to be more consistent with other scripts

Description:
    *designed to run on Ulee's TI-84 Plus CE
    *counts up but without repeating any non-zero digits
    *Ulee named this "counting by dees" but we're calling it "counting by no-repeats" or "counting by 0 repeats"

Inputs:
    *NOTHING
    *(does have user input values when prompted)

Outputs/does:

        Enter:
            *max_value
        Output:
            0: 0
            1: 1
            2: 2
            .
            .
            .
            i: j

            it ends when either i==max_number_of_numbers (hard-coded) or j>=max_value

Used by:
    *NOTHING--this is standalone code

Uses:
    *NOTHING--this is standalone code

NOTES:

these values get big fast--value is on the order of 10^(number_of_numbers/10)

'''


# =============================
# =============================
# algorithms
# =============================
# =============================

def count_by_no_repeats(max_val, max_cnt_pause, max_num_of_nums):
    number_of_numbers = 0
    base_value = 0
    multiplier = 1

    display_number = base_value * multiplier
    print(str(number_of_numbers) + ":   " + str(display_number))
    input("Press Enter to continue...")

    temp_count = 0
    keep_going = True
    while keep_going:
        number_of_numbers = number_of_numbers + 1
        base_value = base_value + 1
        if base_value == 11:
            base_value = 2
            multiplier = 10 * multiplier
        display_number = base_value * multiplier
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

count_by_no_repeats(max_value, max_count_with_pauses, max_number_of_numbers)

print('\nTry again sometime!\n')