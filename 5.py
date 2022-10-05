# Создайте программу с классом Student и Starosta. Класс Starosta должен наследоваться от класса Student.
# Атрибутами класса Student должны быть bilnum - номер студбилета длинною 9 цифр,
# FIO - ФИО студента без цифр, знаков препинания, разрешены только пробелы,
# rating - рейтинг успеваемости от 0 до 100.

# Методы класса Student - printinf - выводит всю имеющуюся информацию по студенту,
# change_rating - при передаче отрицательного числа понижает рейтинг, а положительного увеличивает его.

# Атрибут класса Starosta - journal - словарь всех студентов, в котором ФИО указывается в виде ключа, а значение -
# как журнал оставшихся bilnim и rating, где ключ это bilnum, а rating это значение. Методы класса Starosta -
# addstudent (пополнение словаря), removestudent (удаление данных из словаря), showclass (вывод на экран всего списка
# студентов в по алфавиту).

class Student:
    def __init__(self, bilnum, FIO, rating):
        self.bilnum = bilnum
        self.FIO = FIO
        self.rating = rating

    @staticmethod
    def printinf(FIO, bilnum, rating):

        return FIO, bilnum, rating

    def change_rating(self, FIO, bilnum, rating):

        Starosta.journal.update({FIO: {bilnum: rating}})
        return Starosta.journal


class Starosta(Student):
    journal = {}

    def __dict__(self, journal):
        self.journal = journal

    def addstudent(FIO, bilnum, rating):
        Starosta.journal[FIO] = {bilnum: rating}
        return Starosta.journal

    def removestudent(FIO):
        del Starosta.journal[FIO]
        return Starosta.journal

    def showclass(journal):
        a = sorted(Starosta.journal.items())
        a=dict(a)
        for i in a:
            print(i,':', a[i])


FIO1 = str(input())
bilnum1 = -1
rating1 = -1
while bilnum1 < 100000000 or bilnum1 > 999999999:
    bilnum1 = int(input())
while rating1 < 0 or rating1 > 100:
    rating1 = int(input())
fir = Student(FIO1, bilnum1, rating1)

Starosta.addstudent(FIO1, bilnum1, rating1)

FIO2 = str(input())

bilnum2 = -1
rating2 = -1
while bilnum2 < 100000000 or bilnum2 > 999999999:
    bilnum2 = int(input())
while rating2 < 0 or rating2 > 100:
    rating2 = int(input())
sec = Student(FIO2, bilnum2, rating2)

print(Student.printinf(FIO1, bilnum1, rating1))

x = int(input())

rating1 = rating1 + x

if rating1 >= 100:
    rating1 = 100
elif rating1 <= 0:
    rating1 = 0

Student.change_rating(x, FIO1, bilnum1, rating1)

print(Student.printinf(FIO1, bilnum1, rating1))

print(Student.printinf(FIO2, bilnum2, rating2))

Starosta.showclass(Starosta.journal)

Starosta.addstudent(FIO2, bilnum2, rating2)

Starosta.showclass(Starosta.journal)

Starosta.removestudent(FIO1)

Starosta.showclass(Starosta.journal)

