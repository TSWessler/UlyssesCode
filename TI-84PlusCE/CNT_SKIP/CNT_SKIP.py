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
# algorithm
# =============================

def skip_counting():
    global temp_count, number_of_numbers
    if (abs(round(skip_value) - skip_value)) > 1e-10 or (abs(round(start_value) - start_value)) > 1e-10:
        temp_str=str(start_value)
        temp_int=temp_str.find('.')
        temp_int1=len(temp_str[temp_int+1:])
        temp_str = str(skip_value)
        temp_int = temp_str.find('.')
        temp_int2 = len(temp_str[temp_int+1:])
        dig_after_dec=max(temp_int1,temp_int2)
        ten_to_the=10**dig_after_dec
        is_int = False
    else:
        is_int = True
    number_of_numbers = 0
    temp_count = 0
    display_number = start_value
    print(str(number_of_numbers) + ":   " + str(display_number))
    input("Press Enter to continue...")
    
    while True:
        number_of_numbers = number_of_numbers + 1
        if is_int:
            display_number = int(display_number + skip_value)
            print(str(number_of_numbers) + ":   " + str(display_number))
        else:
            display_number = display_number + skip_value
            temp_str=str(round(display_number*ten_to_the))
            temp_int=len(temp_str)
            if temp_int>dig_after_dec:
                display_number_str=temp_str[:(temp_int-dig_after_dec)]+'.'+temp_str[(temp_int-dig_after_dec):]
            else:
                display_number_str='.'+'0'*(dig_after_dec-temp_int)+temp_str
            print(str(number_of_numbers) + ":   " + display_number_str)
        
        if check_termination(display_number):
            break
            
        handle_pause()


# =============================
# inputs
# =============================

max_number_of_numbers = 1e3
max_count_with_pauses = 200
start_value = None
skip_value = None
max_value = None

KeepTrying = True
while KeepTrying:
    print('\n\nEnter value to count by:')
    try:
        skip_value = float(input())
        if skip_value <= 0:
            raise ValueError
        KeepTrying = False
    except ValueError:
        print("\n(must be a positive number)\n")

KeepTrying = True
while KeepTrying:
    print('\n\nEnter value to start at:')
    try:
        start_value = float(input())
        KeepTrying = False
    except ValueError:
        print('\n(must be a number)\n')

KeepTrying = True
while KeepTrying:
    print('\n\nEnter max value to count to:')
    try:
        max_value = float(input())
        if max_value <= start_value:
            raise ValueError
        KeepTrying = False
    except ValueError:
        print('\n(must be greater than start value)\n')

print('\n\n')

# =============================
# run algorithm
# =============================

skip_counting()

print('\nTry again sometime!\n')
