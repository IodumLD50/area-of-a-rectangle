#Задание №1

#Пользователь вводит стороны прямоугольника, выведите его площадь и периметр. На вход программе могут подаваться как целые числа,
# так и вещественные

a, b =  map(float,input('Введите стороны прямоугольника в одну строчку, через запятую: ').split(', ')) # map позволяет принимать сразу несколько знвчений,  split делит строчку.
square = a * b
print(f'Площадь прямоугольника = {square}. ')
