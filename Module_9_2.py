first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']
first_result = [len(x) for x in first_strings]
second_result = [(x,y) for x in first_strings for y in second_strings if len(x) == len(y)]
third_result = {s: len(s)  for s in first_strings + second_strings if len(s) % 2 == 0}
#third_result = {(x: len(x), (y: len(y)) for x in first_strings for y in second_strings}
print(first_result)
print(second_result)
print(third_result)












# my_number = ['A', 1 ,4, 'B', 5, 'C', 2, 6]
# result = [x if type(x) == str else x *5 for x in my_number]
# print(result)
# my_numbers = [3, 1 ,4, 9, 5, 7, 2, 6]
# other_number = [7, 2 ,6, 5, 4, 1, 3, 8]
# result1 = [x * y for x in my_numbers for y in other_number if x % 2 and y // 2]
# print(result1)
# they_numbers = [3, 1, 4, 5, 9]
# result2 = {x: x ** 2 for x in they_numbers}
# print(result2)
# def by_3(x):
#     return x * 3
# def is_odd(x):
#     return x % 2
# result4 = map(by_3, filter(is_odd, my_numbers))
# print(list(result4))
