# Напишите функцию для преобразования имени в инициалы. Это задание строго принимает два слова, разделённых одним пробелом.

# В результате должны быть выведены две заглавные буквы, разделённые точкой.

# Это должно выглядеть примерно так:

# Sam Harris=>S.H

# patrick feeney=>P.F

def abbrev_name(name):
    words = name.split(" ")
    first_initial = words[0][0].upper()
    second_initial = words[1][0].upper()
    return f"{first_initial}.{second_initial}"
print(abbrev_name("Saikal Belesovna"))