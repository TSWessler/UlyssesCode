# =============================
# algorithms
# =============================

def count_by_no_repeats():
    number_of_numbers = 0
    base_value = 0
    multiplier = 1

    display_number = base_value * multiplier
    print(str(number_of_numbers) + ":   " + str(display_number))
    input("Press Enter to continue...")

    temp_count = 0
    keep_going = True
    while keep_going:
        number_of_numbers = number_of_numbers + 1
        base_value = base_value + 1
        if base_value == 11:
            base_value = 2
            multiplier = 10 * multiplier
        display_number = base_value * multiplier
        print(str(number_of_numbers) + ":   " + str(display_number))

        if (display_number >= max_value):
            print('\nDone!\n')
            break
        if (number_of_numbers == max_number_of_numbers):
            print('\nToo much counting!\nTry a lower max value!\n')
            break
        temp_count = temp_count + 1
        if (temp_count > 9) and (number_of_numbers < max_count_with_pauses):
            input("Press Enter to continue...")
            temp_count = 0


# =============================
# inputs
# =============================

max_number_of_numbers = 1e3
max_count_with_pauses = 101

max_value = None

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

count_by_no_repeats()

print('\nTry again sometime!\n')
