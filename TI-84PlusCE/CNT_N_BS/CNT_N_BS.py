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

def n_base_counting():
    global temp_count, number_of_numbers
    list_not_allowed = []
    ii = 1
    while ii <= base_value:
        list_not_allowed.append(str(ii))
        ii += 1
    number_of_numbers = 0
    display_number = 0
    display_string = str(display_number)
    print(str(number_of_numbers) + ":   " + display_string)
    input("Press Enter to continue...")
    temp_count = 0
    while True:
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
            
            if check_termination(display_number):
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
    print('\n\nEnter base value:')
    try:
        float_val = float(input())
        base_value = round(float_val)
        if base_value < 0 or base_value > 8:
            raise ValueError
        if float_val != base_value:
            print('\nNOTE:\n' + str(float_val) + '\nchanged to\n' + str(base_value) + '\n')
        KeepTrying = False
    except ValueError:
        print('\n(base must be a number between 0 and 8)\n')

KeepTrying = True
while KeepTrying:
    print('\n\nEnter max value:')
    try:
        max_value = float(input())
        if max_value <= 0:
            raise ValueError
        KeepTrying = False
    except ValueError:
        print('\n(max value must be a positive number)\n')

print('\n\n')

# =============================
# run algorithms
# =============================

n_base_counting()

print('\nTry again sometime!\n')
