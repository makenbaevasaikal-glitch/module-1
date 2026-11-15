# Напишите функцию parse_float, которая принимает строку/список и возвращает число или «none», если преобразование невозможно.
def parse_float(string):
    try:
        return float(string)
    except (ValueError, TypeError):
        return None
print(parse_float("1.0")) 