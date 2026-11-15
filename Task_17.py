# Напишите функцию, которая принимает в качестве параметров неотрицательное целое число nи строку sи возвращает строку, содержащую sровно повторяющихся nзначений.

# Примеры (вход -> выход)
# 6, "I"     -> "IIIIII"
# 5, "Hello" -> "HelloHelloHelloHelloHello"

def repeat_str(repeat, string):
    return string * repeat
print(repeat_str(3, "World"))