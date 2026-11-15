# Эта ката посвящена умножению заданного числа на восемь, если оно четное, и на девять в противном случае.

def simple_multiplication(number) :
    if number % 2 == 0:
        return number * 8 
    else:
        return number * 9
print(simple_multiplication(5))