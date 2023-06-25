
# 5.62.
# Известны оценки по физике каждого ученика двух классов. Определить
# среднюю оценку в каждом классе. Количество учащихся в каждом классе одинаковое

import random

lenList = int(input('Enter student grades of first class: '))
lenList2 = int(input('Enter student grades of second class: '))

someList = []
someList2 = []

for grades in range(lenList):
    someList.append(random.randint(4,10))

for grades in range(lenList2):
    someList2.append(random.randint(4,10))

srGrade = sum(someList) / lenList
srGrade2 = sum(someList2) / lenList2

print(srGrade)
print(srGrade2)



# 2.43.
# Даны два целых числа a и b. Если a делится на b или b делится на a, то вывести 1,
# иначе — любое другое число. Условные операторы и операторы цикла не использовать.

# import random
#
# a = random.randint(1, 100)
# b = random.randint(1, 100)
ИЛИ

# a = int(input())
# b = int(input())
#
# isTrue = True
#
# isTrue = a % b or b % a == 0
#
# print(int(isTrue))


# 17.7.
# Известны стоимости 12 марок телевизоров (все значения разные).
# Определить стоимость телевизора, являющегося "пятым из самых дешевых моделей".

import random

lenList = int(input('Enter TVs: '))

someList = []

for TV in range(lenList):
    someList.append(random.randint(500, 3000))

result = sorted(someList)
priceFive = result[4]

print(result)
print(priceFive)


# 6.97.
# Известно количество очков, набранных каждой из 20-ти команд-участниц
# первенства по футболу. Перечень очков дан в порядке убывания.
# Определить, какое место заняла команда, набравшая "N" очков
# (значение "N" имеется в перечне). Условный оператор не использовать.

import random

lenList = int(input('Enter points: '))

someList = []

for i in range(lenList):
    someList.append(random.randint(1, 50))

result = sorted(someList)[::-1]
print(result)

for index in range(len(result)):

    print(index+1, result[index])




