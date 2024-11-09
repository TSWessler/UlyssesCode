'''
Name:
    CNT_1REP.py

Version:
    wessler
    2024 November 8
    update to: 2024 November 7
    changes:
        *cosmetic changes to be more consistent with other scripts

Description:
    *designed to run on Ulee's TI-84 Plus CE
    *counts up but only allowing the repeating any non-zero digits ONE time.
    *Ulee named this "counting by [I forget--I'll have to look up]" but we're calling it "counting by 1 repeats"

Inputs:
    *NOTHING
    *(does have user input values when prompted)

Outputs/does:

        Enter:
            *start_value
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

it takes a long time to see the pattern for this, so I've included a starting value (like 90 or 990).
due to laziness I just started the algorithm at 0 then run until it reaches the start value, at which time I start displaying

'''


# =============================
# =============================
# algorithms
# =============================
# =============================

def count_by_one_repeat(start_val, max_val, max_cnt_pause, max_num_of_nums):
    number_of_numbers = 0
    base_value = 0
    multiplier = 1

    display_number = base_value * multiplier
    flag_hit_start_val = False

    temp_count = 0
    keep_going = True
    while keep_going:
        if not flag_hit_start_val:
            if display_number >= start_val:
               flag_hit_start_val = True
               print(str(number_of_numbers) + ":   " + str(display_number))
               input("Press Enter to continue...")

        base_value = base_value + 1
        if base_value == 101:
            base_value = 11
            multiplier = 10 * multiplier
        display_number = base_value * multiplier

        if flag_hit_start_val:
            temp_count = temp_count + 1
            number_of_numbers = number_of_numbers + 1
            print(str(number_of_numbers) + ":   " + str(display_number))

        if (display_number >= max_val):
            print('\nDone!\n')
            break
        if (number_of_numbers == max_num_of_nums):
            print('\nToo much counting!\nTry a lower max value!\n')
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

start_value = None
max_value = None


KeepTrying = True
while KeepTrying:
    print('\n\nEnter start value:')
    try:
        start_value = float(input())
        if start_value >= 0:
            KeepTrying = False
        else:
            print('\n(start value must be non-negative)\n')
    except:
        print('\n(start value must be a number)\n')

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

count_by_one_repeat(start_value, max_value, max_count_with_pauses, max_number_of_numbers)

print('\nTry again sometime!\n')