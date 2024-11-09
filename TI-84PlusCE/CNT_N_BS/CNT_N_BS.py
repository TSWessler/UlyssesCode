'''
Name:
    CNT_N_BS.py

Version:
    wessler
    2024 November 8
    update to: 2024 November 7
    changes:
        *cosmetic changes to be more consistent with other scripts

Description:
    *designed to run on Ulee's TI-84 Plus CE
    *counts "n-base" which Ulee made up (and I helped finalize rules), which is kind of backwards of counting in "base-n"
    *Ex: 3-base skips all numbers with 3's, 2's, and 1's in them, so:
        4,5,6,7,8,9,40,44,45,46,47,48,49,50,54,55,56,57,58,59,...

Inputs:
    *NOTHING
    *(does have user input values when prompted)

Outputs/does:

        Enter:
            *base_value
            *max_value
        Output:
            0: 0
            1: ???
            2: ???
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

*base can only be an integer between 0 and 8 (inclusive)
*base 0 is regular counting

'''


# =============================
# =============================
# algorithms
# =============================
# =============================

def n_base_counting(base_val, max_val, max_cnt_pause, max_num_of_nums):
    list_not_allowed = []
    ii = 1
    while ii <= base_val:
        list_not_allowed.append(str(ii))
        ii += 1

    number_of_numbers = 0
    display_number = 0
    display_string = str(display_number)
    print(str(number_of_numbers) + ":   " + display_string)
    input("Press Enter to continue...")

    temp_count = 0
    keep_going_IncreaseValue = True
    while keep_going_IncreaseValue:
        display_number += 1
        display_string = str(display_number)
        flag_print = True
        for char in list_not_allowed:
            if char in display_string:
                flag_print = False
                break
        if flag_print:
            temp_count = temp_count + 1
            number_of_numbers = number_of_numbers + 1
            print(str(number_of_numbers) + ":   " + display_string)

        if (display_number >= max_val):
            print('\nDone!\n')
            break
        if (number_of_numbers == max_num_of_nums):
            print('\nToo much counting! Try a lower max value!\n')
            break

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

base_value = None
max_value = None

KeepTrying = True
while KeepTrying:
    print('\n\nEnter base:')
    try:
        float_val = float(input())
        if float_val < 0:
            print('\n(base must be >= 0)')
        elif float_val > 8:
            print('\n(base must be <= 8)')
        else:
            KeepTrying = False
            base_value = round(float_val)
            if float_val != base_value:
                print('\nNOTE:\n' + str(float_val) + '\nchanged to\n' + str(base_value) + '\n')
    except:
        print('\n(base must be a number)\n')

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

n_base_counting(base_value, max_value, max_count_with_pauses, max_number_of_numbers)

print('\nTry again sometime!\n')