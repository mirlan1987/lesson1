def qualifier(s):
    if 0<=s<7:
        print("Вам в детский сад")
    elif 7<=s<=18:
        print("Вам в школу")
    elif 19<=s<25:
        print("Вам в профессиональное учебное заведение")
    elif 25<=s<60:
        print("Вам на работу")
    elif 60<=s<=120:
        print("Вам на пенсию")
    elif s<0 or s>120:
        print("ОШИБКА! Это программа для людей!"*5)
        print('Общество в начале XXI века')
 
user_old= int(input('Сколько вам лет? '))
qualifier(user_old)
