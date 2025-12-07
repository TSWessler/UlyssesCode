# =============================
# algorithms
# =============================

def count_numbers():
    temp_count = -1
    number_of_numbers = -1
    while number_of_numbers < max_number_of_numbers:
        temp_count += 1
        number_of_numbers += 1

        display_string = '0' * number_of_numbers
        print(str(number_of_numbers) + ":   +" + display_string)
        if temp_count < max_count_with_pauses:
            input()


def say_number():
    list_prefixes = ['thousand', 'million', 'billion', 'trillion', 'quadrillion', 'quintillion', 'sextillion',
                     'septillion', 'octillion', 'nonillion', 'decillion', 'undecillion', 'duodecillion', 'tredecillion',
                     'quattuordecillion', 'quindecillion', 'sexdecillion', 'septendecillion', 'octodecillion',
                     'novemdecillion', 'vigintillion', 'unvigintillion', 'duovigintillion', 'trevigintillion',
                     'quattuorvigintillion', 'quinvigintillion', 'sexvigintillion', 'septenvigintillion',
                     'octovigintillion', 'novemvigintillion', 'trigintillion', 'untrigintillion', 'duotrigintillion',
                     'tretrigintillion', 'quattuortrigintillion', 'quintrigintillion', 'sextrigintillion',
                     'septentrigintillion', 'octotrigintillion', 'novemtrigintillion', 'quadragintillion',
                     'unquadragintillion']
    list_numbers = ['zero ', 'zeroty ', 'zero hundred and ']
    len_number = len(number_to_say)
    after_prefix = (len_number % 3)
    if after_prefix == 0:
        max_prefix = round(len_number / 3) - 1
        after_prefix = 3
    elif after_prefix == 1:
        max_prefix = round(len_number / 3)
    else:
        max_prefix = round(len_number / 3) - 1

    id_prefix = max_prefix
    id_digit = len_number
    while id_digit > 0:
        print(list_numbers[after_prefix - 1], end='')
        if after_prefix > 1:
            after_prefix -= 1
        else:
            after_prefix = 3

        if after_prefix == 3:
            if id_prefix > 0:
                print('\n' + list_prefixes[id_prefix - 1], end='')
                input()
                id_prefix -= 1

        id_digit -= 1
    input()


# =============================
# inputs
# =============================

max_count_with_pauses = 21

max_allowed = 129

max_number_of_numbers = None

KeepTrying = True
while KeepTrying:
    print('\n\nEnter how many numbers to count:')
    try:
        float_val = float(input())
        max_number_of_numbers = round(float_val)
        if max_number_of_numbers < 0 or max_number_of_numbers > max_allowed:
            raise ValueError
        KeepTrying = False
        if float_val != max_number_of_numbers:
            print('\nNOTE:\n' + str(float_val) + '\nchanged to\n' + str(max_number_of_numbers) + '\n')
    except ValueError:
        print('\n(must be a number between 0 and ' + str(max_allowed) + ')\n')

print('\n')

# =============================
# run algorithms
# =============================

count_numbers()
number_to_say = '0' * max_number_of_numbers
if number_to_say == '':
    print("Can't say this number :(")
else:
    print('Out loud this is:')
    say_number()

print('\nTry again sometime!\n')
