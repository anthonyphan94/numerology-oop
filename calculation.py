# 99123
from datetime import date


# calculate the sum of each digit
def total_digit(number):
    total = 0
    number = str(number)
    for i in range(len(number)):
        total += int(number[i])
    return total


def simplify(total_number):
    if str(total_number) == '11' or str(total_number) == '22' or str(total_number) == '33':
        return total_number
    my_number = total_digit(total_number)
    my_number = str(my_number)

    if my_number == '11' or my_number == '22' or my_number == '33':
        return my_number
    else:
        while len(my_number) > 1:
            temp = int(total_digit(my_number))
            # print(temp)
            my_number = str(temp)
    return my_number


today = str(date.today())

today = today.split('-')
this_year = today[0]
this_month = today[1]
this_date = today[2]
# print(simplify('34'))
