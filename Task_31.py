# Если задано число в диапазоне от до 0-9, верните его прописью. Обратите внимание, что входные данные гарантированно находятся в пределах диапазона от до 0-9.

# Ввод:1

# Выход: "One".

def switch_it_up(number):
    words = {
        0: "Zero",
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine"
    }
    return words[number]
print(switch_it_up(5))