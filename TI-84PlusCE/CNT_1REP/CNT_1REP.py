# =============================
# algorithms
# =============================

def count_by_one_repeat():
    number_of_numbers = 0
    base_value = 0
    multiplier = 1

    display_number = base_value * multiplier
    flag_hit_start_val = False

    temp_count = 0
    keep_going = True
    while keep_going:
        if not flag_hit_start_val:
            if display_number >= start_value:
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

        if (display_number >= max_value):
            print('\nDone!\n')
            break
        if (number_of_numbers == max_number_of_numbers):
            print('\nToo much counting!\nTry a lower max value!\n')
            break

        if (temp_count > 9) and (number_of_numbers < max_count_with_pauses):
            input("Press Enter to continue...")
            temp_count = 0


# =============================
# inputs
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
        if start_value < 0:
            raise ValueError
        KeepTrying = False
    except ValueError:
        print('\n(start value must be a non-negative number)\n')

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

count_by_one_repeat()

print('\nTry again sometime!\n')
