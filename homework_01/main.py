"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*nums):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел    
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    results=[]
    for num in nums:
        results.append(num * num)
    return results

# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def get_odd(nums):
    result = []
    for num in nums:
        if num % 2 != 0:
            result.append(num)
    return result


def get_even(nums):
    result = []
    for num in nums:
        if num % 2 == 0:
            result.append(num)
    return result


def is_num_prime(check_num):
    result = True
    if check_num == 0:
        return False
    for num in range(2, check_num):
        if check_num % num == 0:
            return False
    return result


def get_prime(nums):
    result = []
    for num in nums:
        is_prime = is_num_prime(num)
        if is_prime:
            result.append(num)
    return result


def filter_numbers(nums, filter_type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)
    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if filter_type == 'odd':
        return get_odd(nums)
    
    elif filter_type == 'even':
        return get_even(nums)
    
    elif filter_type == 'prime':
        return get_prime(nums)


if __name__ == '__main__':

    # out_list = power_numbers(1, 2, 5, 7, 9, 6)
    # print(out_list)
    #
    num_list = [0, 1, 2, 22, 9, 6, 14, 15, 17, 5, 7]

    # odd_nums = filter_numbers(num_list, ODD)
    # print(odd_nums)
    #
    # even_list = filter_numbers(num_list, EVEN)
    # print(even_list)

    prime_list = filter_numbers(num_list, PRIME)
    print(prime_list)
