import re

my_file = open('firstProblem.txt', 'r')

data = my_file.read()

data_into_list = data.split("\n")

sanitizedList = []

sumOfNumbers = 0

for i in data_into_list:
    newList = list(map(int, re.findall('\d+', i)))
    newList = str(newList[0]) + str(newList[-1])
    sanitizedList.append(newList)

for n in sanitizedList:
    sumOfNumbers += int(n)
print(sumOfNumbers)

my_file.close()