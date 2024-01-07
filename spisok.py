#ПРОГРАММА ЧТОБЫ СДЕЛАТЬ СПИСОК ВЕЩЕЙ ЭТО TODO-ЛИСТ

notes = []  # список для хранения заметок
def add_note():
    note = input("Введите заметку: ")
    notes.append(note)
    print("Заметка добавлена!")

def view_notes():
    if len(notes) == 0:
        print("Заметок пока нет.")
    else:
        print("Список заметок:")
        for i, note in enumerate(notes, 1):
            print(f"{i}. {note}")

def main():
    while True:
        choice = input("Выберите действие:\n1. Добавить заметку\n2. Просмотреть заметки\n3. Выйти\n")

        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            break
        else:
            print("Неправильный ввод. Попробуйте еще раз.")

if __name__ == "__main__":
    main()
