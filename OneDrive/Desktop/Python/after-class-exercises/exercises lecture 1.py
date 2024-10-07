# session 1

#exercise 1
greeting='Hello world!'
print(greeting)

#exercise 2
a=3
b=7
print(a+b)
print(a-b)
print(a*b)
print(a/b)

#exercise 3
name='Monica'
print(f'Hello {name}!')

#exercise 4
universities=['ESADE','RSM','ESSEC','IE','Bocconi']
print(universities)
print(universities[0])
print(universities[-1])

#exercise 5
student={'name':'Monica','age':20,'grade':9}
for key in student:
    print(f'{key}:{student[key]}')

#exercise 6
coordinates=(14,60)
print(coordinates[0])
print(coordinates[1])

#exercise 7
colors={'red','green','blue'}
colors.add('pink')
colors.add('green')
print(colors)
colors.discard('red')
light_colors={'light blue','pastel green','lilac','butter yellow','pink'}
merged_colors=colors|light_colors
print(merged_colors)

#exercise 8
num=8
if num>0:
    print(f'{num} is positive')
elif num<0:
    print(f'{num} is negative')
elif num==0:
    print(f'{num} is zero')

#exercise 9
list_numbers=[number for number in range(1,6)]
for n in list_numbers:
    print(n)

#exercise 10
i=1
while i<6:
    print(i)
    i+=1

#exercise 11
