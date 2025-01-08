status = 'в процессе'
print('Текущий статус: ', status)
new_status = input('''Введите новый статус: 
1. выполнено
2. в процессе
3. отложено
''')
if new_status == 1:
    status = 'выполнено'
elif new_status == 2:
    status = 'в процессе'
elif new_status == 3:
    status = 'отложено'
else: print('Введено неверное значение')

print('Новый статус: ', status)