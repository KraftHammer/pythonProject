# Требования:
# 2. Блоб имеет 10% шанс умереть (в течении дня)
# 3. Блоб живёт только в том случае, если имеется 1 ед. пищи на день
# 4. Каждый день блобам выдаётся случайное число пищи (от 0 до 100), которое съедается, а затем складируется
from random import randint
def must_born(blob_population, blob_food, blob_count):
    while blob_population >= 2 and blob_food >= 4:
        blob_population -= 2
        blob_food -= 4
        blob_count += 1
    if blob_count > 0:
        print(f"{' new' if blob_count == 1 else ' new'} {blob_count} blob{' has' if blob_count == 1 else 's have'}"
              f" arrived to this world!")
    else:
        print("Not enough resources to give birth to new blobs.")
    return blob_count

def watch_my_blobs(blob_count, blob_population):
    blobs_count = blob_count + blob_population
    if blob_count == 0:
        print("No Blob's :(")
    else:
        print(f"You have {blobs_count} blob's! Congratulations!")

def random_blob_population(blob_population):
    blob_population = randint(1, 10)
    return blob_population
def random_blob_food(blob_food):
    blob_food = randint(1, 25)
    return blob_food

def main():
    blob_population = 0
    blob_count = 0
    blob_food = 0
    while True:
        print("\nNeed more Blob's?\n")
        choice = input("1.Yes, please!\n2.Watch my blob's ( ͡° ͜ʖ ͡°)\n3.No, i dont want a blob.\n")
        if choice == "1":
            blob_population = random_blob_population(blob_population)
            blob_food = random_blob_food(blob_food)
            print(f"Your blob's count now is... {blob_population} blob's!")
            print(f"Your blob's food now is... {blob_food} stuff's! Not bad?")
        elif choice == "2":
            watch_my_blobs(blob_count, blob_population)
        elif choice == "3":
            print("ok bye")
            break

if __name__ == "__main__":
    main()
