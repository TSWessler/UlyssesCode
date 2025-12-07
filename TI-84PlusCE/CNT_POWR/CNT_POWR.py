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

def power_counting():
    global temp_count, number_of_numbers
    number_of_numbers = 0
    base_value = 0
    if power_value < 0:
        display_string = "undefined!!!"
    elif power_value == 0:
        display_string = "indeterminate!!!"
    else:
        display_number = base_value ** power_value
        if power_value > 0 and power_value == int(power_value):
            display_string = str(int(display_number))
        else:
            display_string = str(display_number)
    print(str(number_of_numbers) + ":   " + display_string)
    input("Press Enter to continue...")
    temp_count = 0
    while True:
        number_of_numbers = number_of_numbers + 1
        base_value = base_value + 1
        display_number = base_value ** power_value
        display_string = str(display_number)
        print(str(number_of_numbers) + ":   " + display_string)
        
        if check_termination(display_number):
            break
            
        handle_pause()


# =============================
# inputs
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
    except ValueError:
        print('\n(power must be a number)\n')

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

power_counting()

print('\nTry again sometime!\n')
