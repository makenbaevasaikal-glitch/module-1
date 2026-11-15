# Определите функцию, которая удаляет дубликаты из массива неотрицательных чисел и возвращает их в качестве результата.

# Порядок следования должен оставаться неизменным.

# Примеры:

# Input -> Output
# [1, 1, 2] -> [1, 2]
# [1, 2, 1, 1, 3, 2] -> [1, 2, 3]

def distinct(seq):
    result = []  
    for number in seq:
        if number not in result:
            result.append(number) 
    return result 
print(distinct([1, 2, 3, 3, 2, 2, 1,]))