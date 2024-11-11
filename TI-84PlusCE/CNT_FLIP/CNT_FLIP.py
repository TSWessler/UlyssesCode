'''
Name:
    CNT_FLIP.py

Version:
    wessler
    2024 November 10
    update to: 2024 November 8
    changes:
        *fixed error with displaying: "0: 0" which should be "0: 1"

Description:
    *designed to run on Ulee's TI-84 Plus CE
    *counts by 2^n, but first says the number then flips the last 2 digits of the number and says it again.
    *Ulee named this "counting by [I forget--I'll have to look up]" but we're calling it "count by flip-the-end"

Inputs:
    *NOTHING
    *(does have user input values when prompted)

Outputs/does:

        Enter:
            *max_value
        Output:
            0: 0
            1: 2
            2: 4
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

because this is exponential, it gets big very fast.

this pattern (switching the last 2 digits) can be used for other counting methods (other than 2^n), but Ulee did it with 2^n when making it up, so that's what this script is based on. Obviously, the algorithm can easily be repurposed for other counting methods.

'''


# =============================
# =============================
# algorithms
# =============================
# =============================

def count_by_flip_the_end(max_val, max_cnt_pause, max_num_of_nums):
    number_of_numbers = 0
    base_value = 2
    exponent = 0

    display_number = base_value ** exponent
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
            print('\nToo much counting! Try a lower max value!\n')
            break

        temp_count = temp_count + 1
        if (temp_count > 9) and (number_of_numbers < max_cnt_pause):
            input("Press Enter to continue...")
            temp_count = 0

        if display_number >= 10:
            number_of_numbers = number_of_numbers + 1

            temp_str = str(display_number)
            display_End = temp_str[-1]
            display_NextToEnd = temp_str[-2]
            display_number_str = temp_str[:-2] + display_End + display_NextToEnd
            display_number_temp = int(display_number_str)

            print(str(number_of_numbers) + ":   " + str(display_number_temp))

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

count_by_flip_the_end(max_value, max_count_with_pauses, max_number_of_numbers)

print('\nTry again sometime!\n')