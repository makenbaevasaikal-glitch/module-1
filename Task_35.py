# Создайте метод для проверки того, написана ли строка ЗАГЛАВНЫМИ БУКВАМИ.

# Примеры (вход -> выход)
# "c" -> False
# "C" -> True
# "hello I AM DONALD" -> False
# "HELLO I AM DONALD" -> True
# "ACSKLDFJSgSKLDFJSKLDFJ" -> False
# "ACSKLDFJSGSKLDFJSKLDFJ" -> True

def is_uppercase(inp):
    return inp == inp.upper()
print(is_uppercase("ACSKLDFJSgSKLDFJSKLDFJ"))