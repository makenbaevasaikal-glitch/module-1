# Дано число n, верните количество положительных нечетных чисел, указанных ниже n. ЛЕГКО!

# Примеры (Ввод -> Вывод)
# 7  -> 3 (because odd numbers below 7 are [1, 3, 5])
# 15 -> 7 (because odd numbers below 15 are [1, 3, 5, 7, 9, 11, 13])

def odd_count(n):
    return n // 2
print(odd_count(9))  