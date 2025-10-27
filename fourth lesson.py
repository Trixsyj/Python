import math as mt

num1 = 5.83
num2 = round(num1)
#print(num2)
#print(mt.ceil(num1))
#print(mt.floor(num1))

num3 = mt.radians(30)
num4 = mt.degrees(0.5235987755982988)
#print(num3 , num4)

num5 = mt.pow(3, 3) # 3 ** 3 = 27
#print(num5)

num6 = mt.sqrt(81)
#print(num6) # 81 ** 0.5

name1, name2, name3 = 'Jack', 'Alice', 'Bob'
#print(name2)

#print(max(2, 4, 984, 93, 78, 9643, 90))
#print(min(1098, 98, 547, -0.6, 75, 0.0000001, -0,876))

#student1 = ['Tom' , 29, True, 'male', 'bank']

#student1[0] = 'Bob'
#print(student1)

#student1[-1] = 500
#print(student1)
#print(len(student1))

#student1.append('Bob')
#people = student1[1:-1:2]
#people.reverse()
#print(people)

#student1[4:] = student1[0:2]

#student1[-1] = student1[0]
#student1[-2] = student1[1]

#student1[2] = 'Alex'

#student1.insert(0, 'Chris')


#student2 = ['Alice' , 'John' , 'Eva']
#student2.extend(student1)

#student2.remove('Alice')
#print(student2)

#student2.clear()
#print('this is student2' , student2)
#print('this is student1', student1)

student1 = ['Tom', 'Sam' , 'Jack', 'Hugh', 'Ross', 'Tim' , 'Sarah']

tim_index = student1.index('Tim')
student1[tim_index] = 'Timothy'
print(student1)















