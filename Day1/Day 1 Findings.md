Day 1 Findings

#Part 1

I kept on getting errors in my initial code because numbers next to each counted as one, rather than seperate characters. 
This is because my initial regular expression `re.findall('\d+', i)` consumed as many integers as it could, meaning the first index of my array was more than one number. 
more about the use of `+` operator in regex can be found here: https://stackoverflow.com/questions/3850217/what-is-the-meaning-of-in-a-regex

#Part 2

I couldn't figure out the solution to this one by myself, so I had to view fuglede's solution here: https://github.com/fuglede/adventofcode/blob/master/2023/day01/solutions.py

First thing I learned about implementing fuglede's solution was the exitence of `replace()` method in python. The way the method is used in this solution is it replaces a string with a string and an integer. This makes it so that regex picks up any string occurrence and replaces it with the desired integer.

more about `replace()` method here: https://www.w3schools.com/python/ref_string_replace.asp

