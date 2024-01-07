# Узнаем время! (подсмотрел на яндекс практикуме)
for current_hour in range(0,24):
    print(f"На часах: {current_hour}:00")
    if current_hour >= 8 and current_hour <= 11:
        print('Доброе утро!')
    elif current_hour > 11 and current_hour <= 17:
        print('Добрый день!')
    elif current_hour > 17 and current_hour <= 21:
        print('Добрый вечер!')
    else:
        print('Доброй ночи!')

