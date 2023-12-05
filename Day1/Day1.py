import re

my_file = open('firstProblem.txt', 'r')

data = my_file.read()

data_into_list = data.split("\n")

sanitizedList = []

sumOfNumbers = 0

for i in data_into_list:
    i = (
    i.replace("one", "one1one")
    .replace("two", "two2two")
    .replace("three", "three3three")
    .replace("four", "four4four")
    .replace("five", "five5five")
    .replace("six", "six6six")
    .replace("seven", "seven7seven")
    .replace("eight", "eight8eight")
    .replace("nine", "nine9nine")
)    
    newList = re.findall('\d', i)
    newList = str(newList[0] + newList[-1])
    sanitizedList.append(newList)

for n in sanitizedList:
    sumOfNumbers += int(n)
print(sumOfNumbers)

my_file.close()