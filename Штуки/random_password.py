import random

word = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def random_word():
    i = random.randint(2, 26)
    i = chr(i + ord('a'))
    return i


def generate():
    random_number_1 = random.randint(1000, 9999)
    random_number = (str(random_word()) + str(random_word()) + str(random_number_1) + str(random_word()) +
                     str(random_word()))
    print(random_number)


def main():
    while True:
        print('print accept to generate a random password, or exit to exit')
        x = input()
        if x == "accept":
            generate()
        elif x == 'exit':
            print('ok bye')
            break



if __name__ == "__main__":
    main()
