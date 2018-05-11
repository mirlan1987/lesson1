x= input('Введите число от 1 до 9: ')
x= x[0]
print('Ваше число:',x)
if '1'<=x<='3':
    s= input('Введите строку: ')
    n= int(input('Сколько раз повторить строку? '))
    i= 0
    while i < n:
        print(s)
        i= i+1
elif '4'<=x<='6':
    m= int(input('Степень, в которую возвести число: '))
    x= int(x)
    print(x**m)
elif '7'<=x<='9':
    x= int(x)
    x2= x+10
    while x<x2:
        print(x)
        x= x+1
else:
    print('Ошибка ввода')
