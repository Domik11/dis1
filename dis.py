import time
import math
import colorama
from colorama import Fore, Back, Style, init


colorama.init()




lolqw = -1

while lolqw == -1:
    colorama.init()
    #a*x^2+b*x+c=0
    print(Fore.GREEN)
    a = float(input('Введите старший коэфицент: '))
    b = float(input('Введите младший коэфицент: '))
    c = float(input('Введите свободный член: '))
    D = b*b-4*a*c
    print(Fore.RED)
    print("Дискриминант = " + str(D))

    if D > 0:
        print(Fore.GREEN)
        print('Выражение имеет 2 корня')
        time.sleep(1)
        print('Найдём x')

        kd = math.sqrt(D)

        x1 = ((-b) + float(kd))/(2*a)
        x2 = ((-b) - float(kd))/(2*a)
        print("x1 = " + str(x1))
        print("x2 = " + str(x2))

    elif D == 0:
        print(Fore.GREEN)
        print('Выражение имеет 1 корень')
        time.sleep(1)
        x = -b/(2*a)
        print("x = " + str(x))

    elif D < 0:
        print(Fore.RED)
        print('Выражение не имеет корней')
    





