from math import sqrt


print('Добро пожаловать в самую лучшую программу для вычисления '
      'квадратного корня из заданного числа')


def CalculateSquareRoot(Number):
    """ Вычисляет квадратный корень"""
    return sqrt(Number)


def calc(your_number):
    if your_number <= 0:
        return
    print(f"Мы вычислили квадратный корень из введённого вами числа."
          f"Это будет: {CalculateSquareRoot(your_number)}")


calc(25.5)
