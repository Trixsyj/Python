#products1 = ['melon' , 23 , 76.6 , True , 9>4]
#print(products1[3])

#products2 = ['banana,' , 'icecream,' , 'cake,']
#print('I bought: ' , products2[0], products2[1], 'and ' , products2[2])
#question = input('How much did you pay? ')
#print('I paid: ' , question)


#price = int (input('Enter the price of the product: '))
#print('Change is: ' , 500-price)


#products = ['banana' , 'icecream,' , 'cake']
#print('I bought:' , products[0], products[-1])
#print('Did you bought' , products[1] , '?')
#print('No')
#question = int(input('How much did you pay? '))
#print('I paid: ' , question)
#price = int(input('How much does a iceram cost? '))
#print('Icecream costs: ' , price)
#print('So you saved:' , question - price)

#a = 5
#b = 2
#c = 10

#print(a * b /c)

#1
a = 2
b = 3
c = 1

print(a * (b - c))

#2
a = 5
b = 1

print((a - b) * (a + b))

#3
a = 0.3
b = 4
c = 1

print(a * (b - c))

#4
a = 91
b = 1
c = 2

print((a - b) / (c + b))

#5
a = 5
b = 4
c = 3

print(((a * b) / 3) ** 0.5)

#6
a = 1
b = 3
c = 5
d = 0.2
e = 0.001
f = 91

print((a / b) + (c * ((d - e) / f)))

#7
a = 40
b = 4.25
c = 7.08
d = 6.768
e = 0.75
f = 2050

print(((a - (b * c)) + (d / e)) * f)

#8
print((0.16 * (3.2 - 3/40) + (2 + 3/11) * 4.125 / (3 + 3/4)) / ((5 + 1/6) * 0.3 - 0.3 * 4.5 + (1/3) * 0.3))

#9
x = 24
y = 31.4

print(type(x))
print(type(y))


#10
a = 23
b = 56
diff = 23-56
print(abs(diff))

#11
a = 290
b = 25
dif = 290/25
dif2 = 290%25
print(dif)
print(dif2)

#12
h_1 = 13
m_1 = 25

h_2 = 19
m_2 = 40
time1 = h_2 - h_1
time2 = m_2 - m_1

print(time1 , ':' , time2)

#13

#old_price = int(input('Write old price: '))
#new_price = int(input('Write new price: '))

#res = round((new_price - old_price) / old_price * 100 , 1)
#print('Цена изменилась на' , res, '%')

#14

import math as mt
x = 2
y = mt.e ** (1/(1+mt.cos(x) ** 2))
print(y)

#15

prod = 1500
operator = 45

res = round(1500/45)
print(f'Для выполнения заказа необходимо задействовать {res} поста')

#16
import math

katet_1 = int(input('Введите длину катета: '))
katet_2 = int(input('Введите длину катета: '))
gip = int(input('Введите длину гипотенузы: '))

mniejshiy_katet = min(katet_1, katet_2)
sin_angle = mniejshiy_katet / gip

print('Синус наименьшего угла равен:', sin_angle)

#17
import math

katet_1 = int(input('Введите длину катета: '))
katet_2 = int(input('Введите длину катета: '))
gip = int(input('Введите длину гипотенузы: '))

mniejshiy_katet = min(katet_1, katet_2)
sin_angle = mniejshiy_katet / gip

angle_rad = math.asin(sin_angle)
angle_deg = angle_rad * 180 / math.pi

print('Меньший острый угол равен:', round(angle_deg, 2), 'градусов')
