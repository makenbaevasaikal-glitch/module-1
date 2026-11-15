# Завершите функцию, которая возвращает день недели в соответствии с введенным числом:

# 1возвращает"Sunday"
# 2возвращает"Monday"
# 3возвращает"Tuesday"
# 4возвращает"Wednesday"
# 5возвращает"Thursday"
# 6возвращает"Friday"
# 7возвращает"Saturday"
# В противном случае возвращает"Wrong, please enter a number between 1 and 7"

def whatday(num):
    days = {
        1: "Sunday",
        2: "Monday",
        3: "Tuesday",
        4: "Wednesday",
        5: "Thursday",
        6: "Friday",
        7: "Saturday"
    }
    return days.get(num, "Wrong, please enter a number between 1 and 7")
print(whatday(2))