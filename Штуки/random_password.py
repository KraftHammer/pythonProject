import random

word = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def random_book_1():
    i = random.randint(2, 26)
    i = chr(i + ord('a'))
    return i


def random_book_2():
    i = random.randint(2, 26)
    i = chr(i + ord('a'))
    return i


def generate():
    random_number_1 = random.randint(1000, 9999)
    random_double_word_1 = str(random_book_1() + random_book_2())
    random_double_word_2 = str(random_book_2() + random_book_1())
    random_number = random_double_word_1 + str(random_number_1) + random_double_word_2
    words = random_number.split()
    for i, word in enumerate(map(list, words)):
        random.shuffle(word)
        words[i] = ''.join(word)
    print(*words)
def main():
    while True:
        print('print accept to generate a random password, or exit')
        x = input()
        if x == "accept":
            generate()
        elif x == 'exit':
            print('ok bye')
            break


if __name__ == "__main__":
    main()
