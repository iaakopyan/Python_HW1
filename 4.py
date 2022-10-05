# Создайте программу с классом Algebra. Создайте два атрибута — х и у.
# Напишите методы add, mult, divis, subtr, sqrt, pov — основные математические операции.
# Для sqrt входным параметром будет только атрибут х, квадратный корень для которого нужно и найти
# При передаче в методы параметров x и y с ними нужно производить соответствующие действия и печатать ответ.
class Algebra:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(x, y):
        c = x + y
        return c

    def mult(x, y):
        c = x * y
        return c

    def divis(x, y):

        if y == 0:
            c = 'Деление невозможно'
        else:
            c = x / y
        return c

    def subtr(x, y):
        c = x - y
        return c

    def sqrt(x):
        c = x ** (0.5)
        return c

    def pov(x, y):
        c = x ** y
        return c


x = int(input())
y = int(input())

print(Algebra.add(x, y))
print(Algebra.mult(x, y))
print(Algebra.divis(x, y))
print(Algebra.subtr(x, y))
print(Algebra.sqrt(x))
print(Algebra.pov(x, y))
