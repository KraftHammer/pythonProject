print('Привет! Это бот для внесения записей. Выберите, что хотите сделать:')
list = []
def write():
    while True:
        notes = input('Введите запись (или stop/стоп чтобы вернуться назад)\n')
        list.append(notes)
        if notes == 'stop' or notes == 'стоп':
            break
        else:
            print('Записано!')

def watch_list():
    if len(list) == 0:
        print('Записей ещё нет!')
    else:
        print('Список записей:')
        for i, note in enumerate(list, 1):
            print(f"{i}. {note}")
def main():
    while True:
        choice = input('1.Внести запись\n2.Просмотреть записи\n3.Выйти\n')
        if choice == '1':
            write()
        elif choice == '2':
            watch_list()
        else:
            break

if __name__ == "__main__":
    main()