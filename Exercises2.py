#Exercises #2 :
# Q1
temp= int(input('Enter the temperature: '))
if temp<0:
    print('Freezing weather')
elif 0<temp<10:
    print('Very cold weather')
elif 10<temp<20:
    print('Cold weather')
elif 20<temp<30:
    print('Normal in Temp')
elif 30<temp<40:
    print('Hot weather')
elif temp>=40:
    print('Very Hot')
else:
    print('Invalid input')
print('*******************************************')

#Q2:
n1 = int(input('Enter first number:'))
n2 = int(input('Enter second number:'))
n3 = int(input('Enter third number:'))
if n1>=n2 and n1>=n3:
    print('The 1st Number is the greatest among three ')
elif n2>=n1 and n2>=n3:
    print('The 2nd Number is the greatest among three ')
elif n3>=n1 and n3>=n2:
    print('The 3rd Number is the greatest among three ')    
else:
    print('all three number are equal')    
print('*******************************************')

# Q3:
num1 = int(input('Enter first number:'))
num2 = int(input('Enter second number:'))
num3 = int(input('Enter third number:')) 
num_list= [num1,num2,num3]   
print(f'The ascending order for list is :{sorted(num_list)}')


    