"""          Игра "Угадай число"
(Компьютер сам загадывает и сам угадывает число)
"""


import numpy as np


def random_predict(number: int=1, text:bool=True) -> int:
    """Угадываем число за количество попыток не более 7

    Args:
        number (int, optional): Загаданное число. Defaults to 1.
        text (bool, optional): 
                "True" - вывести сопровождающий текст вывода.
                "False" - без вывода сопровождающего текста.
                Defaults to True.

    Returns:
        int: Количество сделанных попыток.
    """    

    min = 1 # нижняя граница
    max = 100 # верхняя граница
    count = 0 # количество попыток
    predict_number = (max-min) // 2 # шаг первый (середина отрезка)
    
    if text:
        print(f"Загаданное число: {number}")
        print(f"{count}: {predict_number}") 
    
    while True:
        if number > predict_number:
            min = predict_number
            predict_number = max - (max-min) // 2
            
        elif number < predict_number:
            max = predict_number
            predict_number = min + (max-min) // 2
            
        else:
            break  # выход из цикла если угадали
        
        count += 1
        
        if text:
            print(f"{count}: {predict_number}")
            
    if text:
            print(f"Количество попыток: {count}")
            
    return count


if __name__ == "__main__":
    number = np.random.randint(1, 101) # рандомное число от 1 до 100
    random_predict(number, text=True)