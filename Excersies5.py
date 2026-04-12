# 1. Write a Python script to generate and print a dictionary that contains a number
# (between 1 and n) in the form (x, x*x).
n= 7
dict = {}
for i in range(n):
    if i == 0:
        continue
    dict[i]=i*i
print(dict)

# 2. Write a Python script that takes a list of integers and returns a dictionary whose keys are the list
# integers and whose values are "even" or "odd" depending on the number parity.
list = [1,6,8,9,6,0,3,5]
even_odd_dict = {}
for n in list:
    if n%2==0:
        even_odd_dict[n] = 'even'
    else:
        even_odd_dict[n]='odd'
print(even_odd_dict)

#3.	Write a Python program that asks the user to enter a text and return a dictionary whose keys are the words
# of the text entered and the values are the lengths of the words that make up the text.
text = input("Enter a text that contains more than one word:")
word_length_dict = {}
text_split = text.split()
for word in text_split:
    word_length_dict[word]= len(word)
print(word_length_dict)

# 4. Write a program (function!) that takes a list and returns a new list that contains all the elements of the
# first list without all the duplicates.
list = ['Samar','Nada','Mena','Nada','Mena','Ahmed','Noor','Ahmed']
def copy_list_without_duplicetion(list):
    list2= []
    for name in list:
        if name not in list2:
            list2.append(name)
    return list2
print(f"Copy Result without repeated:{copy_list_without_duplicetion(list)}")

# 5. Given a .txt file that has a list of a bunch of names, count how many of each name there are in the file,
# and print out the results to the screen as a dictionary [key is the name, value is the count].
file = open("D:\\name.txt")
lines = file.readlines()
name_count_dict={}
for name in lines:
    name_count_dict[name.strip()]=lines.count(name)

print(name_count_dict)

