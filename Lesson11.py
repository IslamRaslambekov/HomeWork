class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Точка с координатами {self.x} и {self.y}'

    def __str__(self):
        return f'Точка с координатами {self.x} и {self.y}'

    def __eq__(self, other):
        if (self.x == other.x) and (self.y == other.y):
            return True
        return False

    def __ne__(self, other):
        if (self.x is not other.x) and (self.y is not other.y):
            return True
        return False

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


if __name__ == "__main__":
    pnt1 = Point(1, 10)
    pnt2 = Point(1, 10)
    print(pnt1 == pnt2)
    print(pnt1 != pnt2)
    print(pnt1 + pnt2)
