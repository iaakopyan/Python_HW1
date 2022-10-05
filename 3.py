# Реализовать функцию со следующим функционалом: найти сумму цифр произвольного положительного числа.
def summ(a):
    summ = 0
    while a > 0:
        digit = a % 10
        if digit != 0:
            summ = summ + digit
        a = a // 10
    return summ


e = int(input())
print(summ(e))
