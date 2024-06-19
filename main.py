import random

#Константы
MIN = 1
MAX = 3
QUIT = 'Exit'

def main():
    
    NEXT = 'sef'
    while NEXT != QUIT:
        RANDOM_NUM = random.randint(MIN,MAX)
        RANd = STROKA(RANDOM_NUM)
    
        NUM_USER = input(f'Введите то чем хотите сыграть\nКамень\nНожница\nБумага\nНапишите: ')
        print(f'\nСкрипт выбрал сыграть {RANd} а пользователь {NUM_USER}\n')
    
        Total = WIN(RANd,NUM_USER)
        print(Total)
        
        NEXT = input('Напишите Exit если хотите выйти.\nЛибо напишите любое другое значение: ')
    
    
    
def STROKA(RANDOM_NUM):
    if RANDOM_NUM == 1:
        RANDOM_NUM = 'Камень'
    elif RANDOM_NUM == 2:
        RANDOM_NUM = 'Ножницы'
    else:
        RANDOM_NUM = 'Бумага'
    return RANDOM_NUM



def WIN(RANd,NUM_USER):
    if RANd == 'Камень' and NUM_USER == 'Ножницы':
        return 'Скрипт победил'
    elif RANd == 'Ножницы' and NUM_USER == 'Бумага':
        return 'Скрипт победил'
    elif RANd == 'Бумага' and NUM_USER == 'Камень':
        return 'Скрипт победил'
    elif RANd == NUM_USER:
        return 'Ничья'
    #Победы игрока
    elif NUM_USER == 'Камень' and RANd == 'Ножницы':
        return 'Победил пользователь'
    elif NUM_USER == 'Ножницы' and RANd == 'Бумага':
        return 'Победил пользователь' 
    elif NUM_USER == 'Бумага' and RANd == 'Камень':
        return 'Победил пользователь'
    else:
        return 'Ничья'
        
main()