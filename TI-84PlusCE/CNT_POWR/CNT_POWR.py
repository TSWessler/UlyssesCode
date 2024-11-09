'''
Name:
    CNT_POWR.py

Version:
    wessler
    2024 November 8
    update to: 2024 November 7
    changes:
        *cosmetic changes to be more consistent with other scripts

Description:
    *designed to run on Ulee's TI-84 Plus CE
    *counts 0^power, 1^power, 2^power, 3^power, ...

Inputs:
    *NOTHING
    *(does have user input values when prompted)

Outputs/does:

        Enter:
            *power
            *max_value
        Output:
            0: 0^power
            1: 1^power
            2: 2^power
            .
            .
            .
            i: i^power

            it ends when either i==max_number_of_numbers (hard-coded) or i^power>=max_value

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

def power_counting(pow_val, max_val, max_cnt_pause, max_num_of_nums):
    number_of_numbers = 0
    base_value = 0
    if pow_val <= 0:
        display_string = "undefined!!!"
    else:
        display_number = base_value ** pow_val
        display_string = str(display_number)
    print(str(number_of_numbers) + ":   " + display_string)
    input("Press Enter to continue...")

    temp_count = 0
    keep_going_IncreaseValue = True
    while keep_going_IncreaseValue:
        number_of_numbers = number_of_numbers + 1
        base_value = base_value + 1
        display_number = base_value ** pow_val
        display_string = str(display_number)
        print(str(number_of_numbers) + ":   " + display_string)

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

power_value = None
max_value = None

KeepTrying = True
while KeepTrying:
    print('\n\nEnter power value:')
    try:
        power_value = float(input())
        KeepTrying = False
    except:
        print('\n(power must be a number)\n')

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

power_counting(power_value, max_value, max_count_with_pauses, max_number_of_numbers)

print('\nTry again sometime!\n')