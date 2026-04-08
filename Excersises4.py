# 1. Write a Python program to sum all the items in a list:
x = [1,2,4,8,5,3]
print('The Sum Of List: ',sum(x))

# 2. Write a Python program to multiply all the items in a list:
x = [1,2,4,8,5,3]
mul = 1
for i in x:
    mul*=i
print(f"The multiplection of elements:{mul}")

#3.	Write a Python program to count the number of strings where the string length is 2 or more and the first
# and last character are same from a given list of strings:
text = ['abcd' , 'cvnc' , 'mnam' ,'xyz']
text_count = 0
for n in text:
    if len(n) >=2 and n[0]==n[-1]:
        text_count+=1
print('Expected Result: ',text_count)

#4.	Write a Python program to clone or copy a list:
list1 = [2,4,6,8]
list2 = []
for n in list1:
    list2.append(n)
print(list2)

#5.	Write a Python program to find the index of an item in a specified list:
list = [2,4,6,8]
for n , item in enumerate(list):
    if item == 6:
        print(f"The position of item 6 is : {n} ")

#6.	Write a Python function that takes two lists and returns True if they have at least one common member:
list1 = ['Ahmed','Sara','Noor','Noha','Hadi']
list2 = ['Noor','Saja','Noha','Ahmed','Dana']
def common_member(list1,list2):
    for n in list1:
        if n in list2:
            return True
    return False

print(common_member(list1,list2))

#7.	Write a Python program to print a specified list after removing the 0th, 4th and 5th elements:
list = ['Ahmed','Sara','Noor','Noha','Hadi','Doha','Shahed']
list2 = []
for index,name in enumerate(list):
    if index not in [0 ,4 ,5]:
        list2.append(name)
print(list2)

#8.	Write a Python program to print the numbers of a specified list after removing even numbers from it:
numbers = [12,8,6,0,1,4,3,6,5]
number2=[]
for n in numbers:
    if n%2 != 0:
        number2.append(n)
print(number2)

#9.	Write a Python program to convert a list of characters into a string:
list_of_characters = ['H','e','l','l','o']
String = ""
for n in list_of_characters:
    String+=n
print(String)

#10. Write a Python program to get unique values from a list:
number = [12,8,6,12,1,6,3,6,3]
print(set(number))
# Second Solution:
number_else = []
for n in number:
    if n not in number_else:
        number_else.append(n)
print(number_else)

#11. Write a Python program to count the number of elements in a list within a specified range:
values = [10,20,15,30,70,45,90,40,50,99,88,56]
number_count=0
for v in values:
    if 10<=v<=50:
        number_count+=1
print(f"The count of numbers in a values list that between 10 to 50 is : {number_count}")










