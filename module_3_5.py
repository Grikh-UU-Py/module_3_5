# Рекурсивное умножение цифр
def get_multiplied_digits(number):
    str_number = str(number).lstrip('0').rstrip('0')
    if len(str_number) > 1:
        first = int(str_number[:1])
        multiplied = first * get_multiplied_digits(int(str_number[1:]))
    else:
        return number
    return multiplied

result = get_multiplied_digits(40203)
print(result)
