def square_odd_numbers(*numbers):
    return [pow(number, 2) for number in numbers if number % 2 != 0]
