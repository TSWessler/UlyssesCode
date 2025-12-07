# =============================
# helper funcs
# =============================

def handle_pause():
    global temp_count, number_of_numbers
    temp_count = temp_count + 1
    if (temp_count > 9) and (number_of_numbers < max_count_with_pauses):
        input("Press Enter to continue...")
        temp_count = 0

def check_termination(current_value, is_string=False):
    if is_string:
        if current_value == str(max_value):
            print('\nDone!\n')
            return True
    else:
        if current_value >= max_value:
            print('\nDone!\n')
            return True
    if number_of_numbers >= max_number_of_numbers:
        print('\nToo much counting!\nTry a lower max value!\n')
        return True
    return False
    
# =============================
# algorithms
# =============================

# -----------------------------
# base is <10
# -----------------------------

def base_counting_base_less_than_10():
    global temp_count, number_of_numbers
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
            if int(display_string[position - 1]) == base_value:
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

        if check_termination(display_number):
            break

        handle_pause()


# -----------------------------
# base is =10
# -----------------------------

def base_counting_base_is_10():
    global temp_count, number_of_numbers
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
        
        if check_termination(display_number):
            break
            
        handle_pause()


# -----------------------------
# base is >10
# -----------------------------

def base_counting_base_is_more_than_10():
    global temp_count, number_of_numbers
    max_val_str = str(max_value)
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
            if value_at_position_NUMBER == base_value:
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

        if check_termination(display_string, is_string=True):
            break

        handle_pause()


# =============================
# inputs
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
        base_value = round(float_val)
        if base_value < 2:
            print("\n\nSorry, can't do bases less than 2 :(")
            print("(Try CNT_BAS1 for base-1)\n\n")
        elif base_value > 36:
            print("\n\nSorry, can't do bases greater than 36 right now :(\n\n")
        else:
            if float_val != base_value:
                print('\nNOTE:\n' + str(float_val) + '\nchanged to\n' + str(base_value) + '\n')
            KeepTrying = False
    except ValueError:
        print('\n(base must be a number between 2 and 36)\n')

KeepTrying = True
while KeepTrying:
    print('\n\nEnter max value to count to:')
    try:
        max_value = float(input())
        if max_value < 2:
            raise ValueError
        KeepTrying = False
    except ValueError:
        print('\n(max value must be a number greater than 1)\n')

print('\n\n')

# =============================
# run algorithms
# =============================

if base_value < 10:
    base_counting_base_less_than_10()
elif base_value == 10:
    base_counting_base_is_10()
else:
    base_counting_base_is_more_than_10()

print('\nTry again sometime!\n')
