# Проверить является ли число простым.
# Реализовать в виде функции, принимающей один аргумент и возвращающей True или False.
def pros(n):
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return d * d > n


e = int(input())
print(pros(e))
