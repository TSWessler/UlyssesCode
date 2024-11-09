'''
Name:
    CNT_SKIP.py

Version:
    wessler
    2024 November 8
    update to: 2024 October 18
    changes:
        *cosmetic changes to be more consistent with other scripts

Description:
    *designed to run on Ulee's TI-84 Plus CE
    *counts from "start_value" until reaching (at least) "max_value" while skipping "skip_value"-1 numbers inbetween
    *e.g.: start_value = 0; max_value = 15; skip_value = 2;
        goes: 0, 2, 4, 6, 8, 10, 12, 14, 16

Inputs:
    *NOTHING
    *(does have user input values when prompted)

Outputs/does:

        Enter:
            *skip_value
            *start_value
            *max_value (value that counts to with skipping)
        Output:
            0: start_value
            1: 1*skip_value+start_value
            .
            .
            .
            i: j*skip_value+start_value

            it ends when either i==max_number_of_numbers (hard-coded) or j*skip_value+start_value>=max_value

Used by:
    *NOTHING--this is standalone code

Uses:
    *NOTHING--this is standalone code

NOTES:

for floating-point addition reasons can mess up after a while

'''


# =============================
# =============================
# algorithm
# =============================
# =============================


def skip_counting(start_val, skip_val, max_val, max_cnt_pause, max_num_of_nums):
    if (abs(round(skip_val) - skip_val)) > 1e-10 or (abs(round(start_val) - start_val)) > 1e-10:
        temp_str=str(start_val)
        temp_int=temp_str.find('.')
        temp_int1=len(temp_str[temp_int+1:])
        temp_str = str(skip_val)
        temp_int = temp_str.find('.')
        temp_int2 = len(temp_str[temp_int+1:])
        dig_after_dec=max(temp_int1,temp_int2)
        ten_to_the=10**dig_after_dec
        is_int = False
    else:
        is_int = True
    number_of_numbers = 0
    temp_count = 0
    display_number = start_val
    print(str(number_of_numbers) + ":   " + str(display_number))
    input("Press Enter to continue...")
    
    keep_going_IncreaseValue = True
    while keep_going_IncreaseValue:
        number_of_numbers = number_of_numbers + 1
        if is_int:
            display_number = int(display_number + skip_val)
            print(str(number_of_numbers) + ":   " + str(display_number))
        else:
            display_number = display_number + skip_val
            temp_str=str(round(display_number*ten_to_the))
            temp_int=len(temp_str)
            if temp_int>dig_after_dec:
                display_number_str=temp_str[:(temp_int-dig_after_dec)]+'.'+temp_str[(temp_int-dig_after_dec):]
            else:
                display_number_str='.'+'0'*(dig_after_dec-temp_int)+temp_str
            print(str(number_of_numbers) + ":   " + display_number_str)

        if (display_number >= max_val):
            print('\nDone!\n')
            break
        elif (number_of_numbers == max_num_of_nums):
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

max_number_of_numbers = 1e3  # max number of numbers to display before aborting
max_count_with_pauses = 200  # max number of numbers to display requiring periodic pauses before just running to end

start_value = None
skip_value = None
max_value = None

KeepTrying = True
while KeepTrying:
    print('\n\nEnter value to count by:')
    skip_value = float(input())
    if skip_value == 0:
        print("\n\nSorry, can't count by 0's :(\n\n")
    elif skip_value < 0:
        print("\n\nSorry, can't count by negative numbers :(\n\n")
    elif skip_value > 0:
        break

while KeepTrying:
    print('\n\nEnter value to start at:')
    start_value = round(float(input()))
    if (start_value < 0) or (start_value >= 0):
        break

while KeepTrying:
    print('\n\nEnter max value to count to:')
    max_value = round(float(input()))
    if (max_value <= start_value):
        print('\n\nChoose a number greater than "Start Value"\n\n')
    if (max_value > start_value):
        break

print('\n\n')

# =============================
# =============================
# run algorithm
# =============================
# =============================

skip_counting(start_value, skip_value, max_value, max_count_with_pauses, max_number_of_numbers)

print('\nTry again sometime!\n')