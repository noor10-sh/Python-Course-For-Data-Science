#1.	Write a Python function to find the Max of three numbers:
def max_of_three_number(x,y,z):
    if x>=y and x>=z:
        return x
    elif y>=x and y>=z:
        return y
    elif z>=x and z>=y:
        return z
    else:
        return  'equal'
print(f'The maxmium number is: {max_of_three_number(4,9,1)}')

# 2. Write a Python function to print the even numbers from a given list:
def even_number(list):
    list2 = []
    for n in list:
        if n%2==0:
            list2.append(n)
    return list2
list = [1,6,0,9,4,7,5,3,2]
print(even_number(list))

#3.	Write a Python function to multiply all the numbers in a list:
def multiply_function(mul_list):
    mul = 1
    for n in mul_list:
        mul*=n
    return mul
print(multiply_function([1,4,6,5,2]))

#4.	Write a Python function to calculate the factorial of a number (a non-negative integer).
# The function accepts the number as an argument:
def fact_num(n):
    factorial = 1
    while n>=1:
        factorial*=n
        n = (n-1)
    return factorial

print(fact_num(5))

#5. Write a Python function that takes a file path as an argument and prints the sum of all numbers in the file:
def sum_numbers_file(myFile):
    f = open(myFile)
    sum = 0
    for line in f.readlines():
        line = int(line)
        sum+=line
    return sum
print(sum_numbers_file('D:\\numbers.txt'))

#6.	Imagine you have a file named data.txt. Open it for reading using Python, but make sure to use a try block to
# catch an exception that arises if the file doesn't exist. Once you've verified your solution works with an
# actual file, delete the file and see if your try block is able to handle it:
try:
    file = open("D:\\data.txt")
    line = f.readlines()
    print(line)
except Exception as e:
    print(f"The file does not exsits ==> {e}")

#7.	Create a Python function that prompts the user for a list of grades separated by commas. Split the string
# into individual grades and use a list comprehension to convert each string to an integer. You should use a
# try statement to inform the user when the values they entered cannot be converted:
def grades_list(grades):
    grades = grades.split(",")
    try:
        list=[int(i) for i in grades]
        print(list)
    except ValueError as e :
        print(f"Cannot convarted {e}")
    except Exception as e :
        print(f"Error {e}")
grades_list("60,80,?,90,88,95,83,na")
grades_list("60,80,90,88,95")

"""
8.	You're going to write an interactive calculator! User input is assumed to be a formula that consist of a number
 , an operator (at least + and -), and another number, separated by white space (e.g. 1 + 1). Split user input
 using str.split(), and check whether the resulting list is valid:
If the input does not consist of 3 elements, raise an error Exception.
Try to convert the first and third input to a float (like so: float_value = float(str_value)). Catch any ValueError
 that occurs If the second input is not '+' or '-', again raise an Exception
"""
formula = input("Enter the fotmula like (n + n) or any other operation: ")
splitting_formula = formula.split()
if len(splitting_formula)!=3:
    print(Exception)
else:
    splitting_formula[0]=float(splitting_formula[0])
    splitting_formula[-1]=float(splitting_formula[-1])
    print(splitting_formula[0],splitting_formula[-1])

    if splitting_formula[1] == '+' or splitting_formula[1] == '-':
        print("Vaild input")
    else:
        print(Exception)


"""
9.	Below you'll find a list which contains the relevant data about a selection of movies.
Each item in the list is a tuple containing a movie name and movie budget in that order:
movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]
For this project, your program should do the following:
•	Calculate the average budget of all movies in the data set.
•	Print out every movie that has a budget higher than the average you calculated. You should also print out 
how much higher than the average the movie's budget was.
•	Print out how many movies spent more than the average you calculated.
•	Create a function that takes the movies list and returns three the above three results in order.
"""
movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]
#1:
sum = 0
for m in movies:
    sum+=m[1]
avg = sum / (len(movies))
print(f"The avarge budget for all movies in list : {avg}")
#2:
high_budget = []
for b in movies:
    if b[1] > avg:
        high_budget.append(b[0])

print(high_budget)
#3:
print(f"No of movies that have a higher budget than avarge: {len(high_budget)} ")

#4:
def result_function(movies):
    return  avg , high_budget , len(high_budget)
print(result_function(movies))









