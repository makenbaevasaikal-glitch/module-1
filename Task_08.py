# Получив строку, необходимо вернуть строку, в которой каждый символ (с учетом регистра) повторяется один раз.

# Примеры (Ввод -> Вывод):
# * "String"      -> "SSttrriinngg"
# * "Hello World" -> "HHeelllloo  WWoorrlldd"
# * "1234!_ "     -> "11223344!!__  "

def double_char(s):
    result = "" 
    for char in s:
        result += char * 2  
    return result    
print(double_char("Hello World"))