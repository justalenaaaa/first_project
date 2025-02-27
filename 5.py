#Программа по нахождениею расстояния между точками на Земле
import math
a1 = float(input('Введите первую координату широты: '))
b1 = float(input('Введите первую координату долготы: '))
a2 = float(input('Введите второю координату широты: '))
b2 = float(input('Введите вторую координату долготы: '))
a1 = math.radians(a1)
b1 = math.radians(b1)
a2 = math.radians(a2)
b2 = math.radians(b2)
#distance = 6371.01*across(sin(t1)*sin(t2)+cos(t1)*cos(t2)*cos(g1-g2))
R=6371.0
t = a2-a1
g=b2-b1
a = math.sin(t/2)**2+math.cos(a1)*math.cos(a2)*math.sin(g/2)**2
c= 2*math.atan2(math.sqrt(a),math.sqrt(1-a))
distance = R*c
print('Расстояния между точками = %.2f км' % distance)