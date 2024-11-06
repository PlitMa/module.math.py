from math import inf

def divide(first, second):
    if second != 0:
        f = first/second
        return f
    else:
        return inf

# float('inf') указывает на положительную бесконечность
# для проверки верности неравенства используется != или is not
# return завершает выполнение функции и «возвращает» результат вызывающему коду.