'''
Name:
    CNT_BASE.py

Version:
    wessler
    2024 November 8
    update to: 2024 October 18
    changes:
        *improved user-input error-handling
        *cosmetic changes to be more consistent with other scripts

Description:
    *designed to run on Ulee's TI-84 Plus CE
    *counts from 0 to a max value in a given base (between 2 and 36)

Inputs:
    *NOTHING
    *(does have user input values when prompted)

Outputs/does:

        Enter:
            *base_value (must be between 2 and 36--see CNT_BAS1.py for base-1)
            *max_value (value in base that counts to--e.g., in base 2 max_value=2 displays 0,1,10 then stops)
        Output:
            0: 0
            1: 1
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

the order of digits is:
0  1  2  3  4  5  6  7  8  9  A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z
0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35

'''


# =============================
# =============================
# algorithms
# =============================
# =============================


# -----------------------------
# base is <10
# -----------------------------

def base_counting_base_less_than_10(base_val, max_val, max_cnt_pause, max_num_of_nums):
    number_of_numbers = 0
    temp_count = 0
    display_number = 0
    print(str(number_of_numbers) + ":   " + str(display_number))
    input("Press Enter to continue...")

    keep_going_IncreaseValue = True
    while keep_going_IncreaseValue:
        number_of_numbers = number_of_numbers + 1

        display_number = display_number + 1
        display_string = str(display_number)
        length_string = len(display_string)
        position = length_string
        keep_going_ConvertToBaseValue = True
        while keep_going_ConvertToBaseValue:
            if int(display_string[position - 1]) == base_val:
                if position == 1:
                    display_string = "1" + "0" + display_string[position:length_string]
                else:
                    temp_val = int(display_string[position - 2])
                    temp_val = temp_val + 1
                    if position == 2:
                        display_string = str(temp_val) + "0" + display_string[position:length_string]
                    elif position == length_string:
                        display_string = display_string[0:length_string - 2] + str(temp_val) + "0"
                    else:
                        display_string = display_string[0:position - 2] + str(temp_val) + "0" + display_string[
                                                                                                position:length_string]
                position = position - 1
            else:
                keep_going_ConvertToBaseValue = False

        display_number = int(display_string)
        print(str(number_of_numbers) + ":   " + str(display_number))

        if display_number >= max_val:
            print('\nDone!\n')
            break
        if number_of_numbers >= max_num_of_nums:
            print('\nToo much counting!\nTry a lower max value!\n')
            break

        temp_count = temp_count + 1
        if (temp_count > 9) and (number_of_numbers < max_cnt_pause):
            input("Press Enter to continue...")
            temp_count = 0


# -----------------------------
# base is =10
# -----------------------------

def base_counting_base_is_10(max_val, max_cnt_pause, max_num_of_nums):
    number_of_numbers = 0
    display_number = 0
    temp_count = 0
    print(str(number_of_numbers) + ":   " + str(display_number))
    input("Press Enter to continue...")

    keep_going_IncreaseValue = True
    while keep_going_IncreaseValue:
        number_of_numbers = number_of_numbers + 1
        display_number = display_number + 1
        print(str(number_of_numbers) + ":   " + str(display_number))
        if display_number >= max_val:
            print('\nDone!\n')
            break
        if number_of_numbers >= max_num_of_nums:
            print('\nToo much counting!\nTry a lower max value!\n')
            break
        temp_count = temp_count + 1
        if (temp_count > 9) and (number_of_numbers < max_cnt_pause):
            input("Press Enter to continue...")
            temp_count = 0


# -----------------------------
# base is >10
# -----------------------------

def base_counting_base_is_more_than_10(base_val, max_val, max_cnt_pause, max_num_of_nums):
    max_val_str = str(max_val)
    FullCharList = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    number_of_numbers = 0
    temp_count = 0
    display_string = "0"
    print(str(number_of_numbers) + ":   " + display_string)
    input("Press Enter to continue...")

    keep_going_IncreaseValue = True
    while keep_going_IncreaseValue:
        number_of_numbers = number_of_numbers + 1
        length_string = len(display_string)
        position = length_string - 1
        value_at_position_NUMBER = FullCharList.find(
            display_string[position]) + 1  # this is the increase in value--done at last "digit"
        need_to_convert_to_char = True
        keep_going_ConvertToBaseValue = True
        while keep_going_ConvertToBaseValue:
            if value_at_position_NUMBER == base_val:
                if position == 0:
                    display_string = "1" + "0" + display_string[position + 1:]
                    length_string = len(display_string)
                    need_to_convert_to_char = False
                    break
                else:
                    need_to_convert_to_char = True
                    if position == 1:
                        display_string = display_string[0] + "0" + display_string[position + 1:length_string]
                    elif position == length_string - 1:
                        display_string = display_string[:length_string - 1] + "0"
                    else:
                        display_string = display_string[:position] + "0" + display_string[position + 1:]
                    position = position - 1
                    value_at_position_NUMBER = FullCharList.find(display_string[position]) + 1
            else:
                keep_going_ConvertToBaseValue = False
                if need_to_convert_to_char:
                    if length_string == 1:
                        display_string = FullCharList[value_at_position_NUMBER]
                    elif length_string == 2:
                        if position == 0:
                            display_string = FullCharList[value_at_position_NUMBER] + display_string[1]
                        else:
                            display_string = display_string[0] + FullCharList[value_at_position_NUMBER]
                    else:
                        if position == 0:
                            display_string = FullCharList[value_at_position_NUMBER] + display_string[position + 1:]
                        elif position == length_string - 1:
                            display_string = display_string[:length_string - 1] + FullCharList[value_at_position_NUMBER]
                        else:
                            display_string = display_string[:position] + FullCharList[
                                value_at_position_NUMBER] + display_string[position + 1:]

        print(str(number_of_numbers) + ":   " + display_string)

        if (display_string == max_val_str):
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

base_value = None
max_value = None

KeepTrying = True
while KeepTrying:
    print('\n\nEnter base number:')
    try:
        float_val = float(input())
        if float_val < 2:
            print("\n\nSorry, can't do bases less than 2 :(")
            print("(Try CNT_BAS1 for base-1)\n\n")
        elif float_val > 36:
            print("\n\nSorry, can't do bases greater than 36 right now :(\n\n")
        else:
            base_value = round(float_val)
            if float_val != base_value:
                print('\nNOTE:\n' + str(float_val) + '\nchanged to\n' + str(base_value) + '\n')
            KeepTrying = False
    except:
        print('\n(Sorry, must be a number)\n')

while KeepTrying:
    print('\n\nEnter max value to count to:')
    try:
        max_value = float(input())
        if max_value < 2:
            print('\n\nChoose a number greater than 1\n\n')
        else:
            KeepTrying = False
    except:
        print('\n(Sorry, must be a number)\n')

print('\n\n')

# =============================
# =============================
# run algorithms
# =============================
# =============================

if base_value < 10:
    base_counting_base_less_than_10(base_value, max_value, max_count_with_pauses, max_number_of_numbers)
elif base_value == 10:
    base_counting_base_is_10(max_value, max_count_with_pauses, max_number_of_numbers)
else:
    base_counting_base_is_more_than_10(base_value, max_value, max_count_with_pauses, max_number_of_numbers)

print('\nTry again sometime!\n')