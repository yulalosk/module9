def apply_all_func(int_list, *functions):
    results = {}
    for func in functions:
        results[func.__name__] = func(int_list)
    return results

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))

# def adder(args):
#     res = 0
#     for i in args:
#         res += i
#     return res
# def multiplier(args):
#     res = 1
#     for i in args:
#         res *= i
#     return res
#
# def process_numbers(numbers, function):
#     result = function(numbers)
#     print(f'Получилось {result}')
#
# my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
# process_numbers(my_numbers, adder)
# process_numbers(my_numbers, multiplier)