'''
Name:
    CNT_BAS1.py

Version:
    wessler
    2024 November 8
    update to: 2024 November 6
    changes:
        *added max_count_with_pauses
        *cosmetic changes to be more consistent with other scripts

Description:
    *designed to run on Ulee's TI-84 Plus CE
    *counts in "base 1" up to a max number of numbers
    *gives the number and then text for saying the number aloud

Inputs:
    *NOTHING
    *(does have user input values when prompted)

Outputs/does:

        Enter:
            *max_number_of_numbers
        Output:
            0: +
            1: +0
            2: +00
            .
            .
            .
            i: j

            output_string

            it ends when i==max_number_of_numbers, then outpyts how the last number is said aloud

Used by:
    *NOTHING--this is standalone code

Uses:
    *NOTHING--this is standalone code

NOTES:

I kind of want to add commas to "display_string" in "count_numbers" but haven't yet

'''


# =============================
# =============================
# algorithms
# =============================
# =============================

def count_numbers(max_cnt_pause, max_num_of_nums):
    temp_count = -1
    number_of_numbers = -1
    while number_of_numbers < max_num_of_nums:
        temp_count += 1
        number_of_numbers += 1

        display_string = '0' * number_of_numbers
        print(str(number_of_numbers) + ":   +" + display_string)
        if temp_count < max_cnt_pause:
            input()


def say_number(number):
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
    len_number = len(number)
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
# =============================
# inputs
# =============================
# =============================

max_count_with_pauses = 21

max_allowed = 129

max_number_of_numbers = None

KeepTrying = True
while KeepTrying:
    print('\n\nEnter how many numbers to count:')
    try:
        float_val = float(input())
        if float_val < 0:
            print('\n(Sorry, must be >= 0)')
        elif float_val > max_allowed:
            print('\n(Sorry, must be <= ' + str(max_allowed) + ')')
        else:
            KeepTrying = False
            max_number_of_numbers = round(float_val)
            if float_val != max_number_of_numbers:
                print('\nNOTE:\n' + str(float_val) + '\nchanged to\n' + str(max_number_of_numbers) + '\n')
    except:
        print('\n(Sorry, must be a number)\n')

print('\n')

# =============================
# =============================
# run algorithms
# =============================
# =============================

count_numbers(max_count_with_pauses, max_number_of_numbers)
number_to_say = '0' * max_number_of_numbers
if number_to_say == '':
    print("Can't say this number :(")
else:
    print('Out loud this is:')
    say_number(number_to_say)

print('\nTry again sometime!\n')
