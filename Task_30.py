# Напишите функцию для разделения строки слов, разделенных пробелами, и преобразования ее в массив слов. Слова во входном массиве будут разделены ровно одним пробелом. Входные слова не должны содержать пробелов в начале или конце. «Слово» — это любая непрерывная последовательность символов, не содержащая пробелов.

# Примеры (Ввод ==> Вывод):
# "string" ==> ["string"]
# "Robin Singh" ==> ["Robin", "Singh"]
# "I love arrays they are my favorite" ==> ["I", "love", "arrays", "they", "are", "my", "favorite"]

def string_to_array(s):
    return s.split(" ")
print(string_to_array("I love arrays they are my favorite"))