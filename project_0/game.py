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


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов 
                угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    
    count_ls = []
    random_array = np.random.randint(1, 101, size=1000) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number, text=False))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    
    return score


if __name__ == "__main__":
    score_game(random_predict)