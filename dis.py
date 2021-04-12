import time
import math
import colorama
from colorama import Fore, Back, Style, init
colorama.init()
print(Fore.GREEN)
print('██████╗░██╗░██████╗░█████╗░')
print('██╔══██╗██║██╔════╝██╔══██╗')
print('██║░░██║██║╚█████╗░██║░░╚═╝')
print('██║░░██║██║░╚═══██╗██║░░██╗')
print('██████╔╝██║██████╔╝╚█████╔╝')
print('╚═════╝░╚═╝╚═════╝░░╚════╝░')
print('')
print('██████╗░██╗███╗░░░███╗██╗')
print('██╔══██╗██║████╗░████║██║')
print('██████╔╝██║██╔████╔██║██║')
print('██╔══██╗██║██║╚██╔╝██║██║')
print('██║░░██║██║██║░╚═╝░██║██║')
print('╚═╝░░╚═╝╚═╝╚═╝░░░░░╚═╝╚═╝')
print('')
print('███╗░░██╗░█████╗░███╗░░██╗████████╗')
print('████╗░██║██╔══██╗████╗░██║╚══██╔══╝')
print('██╔██╗██║███████║██╔██╗██║░░░██║░░░')
print('██║╚████║██╔══██║██║╚████║░░░██║░░░')
print('██║░╚███║██║░░██║██║░╚███║░░░██║░░░')
print('╚═╝░░╚══╝╚═╝░░╚═╝╚═╝░░╚══╝░░░╚═╝░░░')




ok1 = 0
ok2 = 0
ok3 = 0

def check(x):
    try:
        int(x) or float(x)
    except:
        print('Введите корректное число!')














colorama.init()

print(Fore.GREEN)



lolqw = -1
print('░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░')
while lolqw == -1:

    #a*x^2+b*x+c=0
    print(Fore.GREEN)
    
    while True:
        print(Fore.GREEN)
        ok1 = 0
        time.sleep(0.1)
        a = input('Введите старший коэффицент: ')
        ok1 = a
        try:
            int(ok1)
            float(a)
        except:
            print(Fore.RED)
            time.sleep(0.1)
            print('Введите корректное число!')
            time.sleep(0.1)
        else: 
            break
        
    while True:
        print(Fore.GREEN)
        time.sleep(0.1)
        ok2 = 0
        b = input('Введите младший коэффицент: ')
        ok2 = b
        try:
            int(ok2)
            float(b)
        except:
            print(Fore.RED)
            time.sleep(0.1)
            print('Введите корректное число!')
            time.sleep(0.1)
        else: 
            break

    while True:
        print(Fore.GREEN)
        time.sleep(0.1)
        ok3 = 0
        c = input('Введите свободный член: ')
        ok3 = c
        print(c)
        try:
            int(ok3)
            float(c)
        except:
            print(Fore.RED)
            time.sleep(0.1)
            print('Введите корректное число!')
            time.sleep(0.1)
        else: 
            break
    
    
           
    a = float(a)
    b = float(b)
    c = float(c)

    D = b*b-4*a*c
    time.sleep(0.1)
    print(Fore.RED)
    print("Дискриминант = " + str(D))

    if D > 0:
        print(Fore.GREEN)
        print('Выражение имеет 2 корня')
        time.sleep(0.01)
        print('Найдём x')
        
        kd = math.sqrt(D)

        x1 = ((-b) + float(kd))/(2*a)
        x2 = ((-b) - float(kd))/(2*a)
        time.sleep(0.1)
        print("x1 = " + str(x1))
        time.sleep(0.1)
        print("x2 = " + str(x2))

    elif D == 0:
        print(Fore.GREEN)
        print('Выражение имеет 1 корень')
        time.sleep(0.1)
        x = -b/(2*a)
        print("x = " + str(x))

    elif D < 0:
        time.sleep(0.1)
        print(Fore.RED)
        print('Выражение не имеет корней')
    
    print(Fore.GREEN)
    print('░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░')