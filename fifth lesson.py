#num1 = 4
#num2 = 5

#print(num1 >= num2)

#age = int(input('Enter your age: '))

#a = age % 10 == 0 or age >= 50
#print(a)

#age = int(input('Enter your age: '))

#a = age % 10 == 0 and age >= 50
#print(a)

#name = 'Sara'
#if name == 'Bob':
    #print('It is male' )
#else:
    #print ('It is female')

#if 1+1 >= 2:
    #print('Good job')
#else:
    #print('Fail')

#a = int(input('Enter your number'))
#if a > 0:
    #print('Postitve')
#elif a == 0:
    #print('Zero')
#else:
    #print('Negative')

#a = int(input('Enter your number'))
#if (a>0) and (a==5):
    #print('Positive')
#else:
    #print('Negative')


#a = int(input('Enter your number '))

#person = input('Status of the person ')
#if person == 'student' or person == 'school 10th' or person == 'school 11h':
    #print(f'This person is more than 15 because he is a {person}')
#else:
    #print(f'This person is under the 15 because he is a {person}')


age_input = input('Enter your age or category: ')

try:
    age = int(age_input)
    if age <= 11:
        print('Kids')
    elif age <= 20:
        print('Teens')
    elif age <= 30:
        print('Young')
    elif age <= 50:
        print('Adult')
    else:
        print('Elder')
except ValueError:
    if age_input in ['Kid', 'Kids']:
        print('Kids')
    elif age_input in ['Teen', 'Teens']:
        print('Teens')
    elif age_input == 'Young':
        print('Young')
    elif age_input == 'Adult':
        print('Adult')
    elif age_input == 'Elder':
        print('Elder')
    else:
        print('Unknown category')

