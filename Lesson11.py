class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Точка с координатами {self.x} и {self.y}'

    def __str__(self):
        return f'Точка с координатами {self.x} и {self.y}'

    def __eq__(self, other):
        if (self.x is other.x) and (self.y is other.y):
            return True
        return False

    def __ne__(self, other):
        if (self.x is not other.x) or (self.y is not other.y):
            return True
        return False

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Point(self.x * other.x, self.y * other.y)

    def __truediv__(self, other):
        return Point(self.x / other.x, self.y / other.y)

    def __floordiv__(self, other):
        return Point(self.x // other.x, self.y // other.y)

    def __mod__(self, other):
        return Point(self.x % other.x, self.y % other.y)

    def __pow__(self, other):
        return Point(self.x ** other.x, self.y ** other.y)


if __name__ == "__main__":
    pnt1 = Point(1, 10)
    pnt2 = Point(2, 10)  # Перегрузка:
    print(pnt1 == pnt2)  # равенства
    print(pnt1 != pnt2)  # неравенства
    print(pnt1 + pnt2)  # сложения
    print(pnt1 - pnt2)  # вычитания
    print(pnt1 * pnt2)  # умножения
    print(pnt1 / pnt2)  # деления
    print(pnt1 // pnt2)  # деления без плавающей точки
    print(pnt1 % pnt2)  # остатка от деления
    print(pnt1 ** pnt2)  # возведения в степень
