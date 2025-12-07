# =============================
# algorithms
# =============================

def calculate_prime_factors(N):
    if N <= 1:
        return set()
    prime_factors = set()
    if N % 2 == 0:
        prime_factors.add(2)
    while N % 2 == 0:
        N = N // 2
        if N == 1:
            return prime_factors
    for factor in range(3, N + 1, 2):
        if N % factor == 0:
            prime_factors.add(factor)
            while N % factor == 0:
                N = N // factor
                if N == 1:
                    return prime_factors

def form_of_1():
    FullCharList = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    num_chars = 20
    return_string1 = "1." + num_chars * str(0) + "..."
    if base_value < 37:
        return_string2 = "0." + num_chars * FullCharList[base_value-1] + "..."
    else:
        return_string2 = "0." + round(num_chars / 3) * ("(" + str(base_value - 1) + ")") + "..."
    
    if n_value == 0:
        return_string = "UNDEFINED!\n(cannot divide by 0)"
    elif base_value == 1:
        return_string = return_string1
    else:
        list_multiples_base = calculate_prime_factors(base_value)
        list_multiples_n = calculate_prime_factors(n_value)
        return_string = return_string1
        for temp_multiple in list_multiples_n:
            if temp_multiple not in list_multiples_base:
                return_string = return_string2
                break
    
    print(str(n_value) + "/" + str(n_value) + " in base-" + str(base_value) + " is:")
    print(return_string)


# =============================
# inputs
# =============================

n_value = None
base_value = None

KeepTrying = True
while KeepTrying:
    print('\n\nEnter value of numerator/denominator:')
    try:
        float_val = float(input())
        n_value = round(float_val)
        if n_value != float_val:
            print('\n(rounded to ' + str(n_value) + ')\n')
        KeepTrying = False
    except ValueError:
        print('\n(numerator/denominator must be a number)\n')

KeepTrying = True
while KeepTrying:
    print('\n\nEnter base value:')
    try:
        float_val = float(input())
        base_value = round(float_val)
        if base_value <= 0:
            raise ValueError
        if base_value != float_val:
            print('\n(rounded to ' + str(base_value) + ')\n')
        KeepTrying = False
    except ValueError:
        print('\n(base value must be a positive number)\n')

print('\n\n')

# =============================
# run algorithms
# =============================

form_of_1()

print('\nTry again sometime!\n')
