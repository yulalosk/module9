first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']
first_result = (abs(len(f) - len(s)) for f, s in zip(first, second) if len(f) != len(s))
print(list(zip(first, second)))
print(list(first_result))
second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))
#second_result1 = ((x,y) for x in first for y in second if len(x) == len(y))
print(list(second_result))
#print(list(range(len(first))))


