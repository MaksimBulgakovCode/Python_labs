from random import randint

print("Виселица. Угадай слово")
count = 0

def word():
    words = ["Мяч", "Турнир", "Машина", "Ипотека", "Ноутбук"]
    correctword = words[randint(0, 4)]
    return correctword

def hangman():
    if count == 0:
        with open('stage0.txt', 'r') as file:
            print(file.read())
    elif count == 1:
        with open('stage1.txt', 'r') as file:
            print(file.read())
    elif count == 2:
        with open('stage2.txt', 'r') as file:
            print(file.read())
    elif count == 3:
        with open('stage3.txt', 'r') as file:
            print(file.read())
    elif count == 4:
        with open('stage4.txt', 'r') as file:
            print(file.read())
    elif count == 5:
        with open('stage5.txt', 'r') as file:
            print(file.read())
    elif count == 6:
        with open('stage6.txt', 'r') as file:
            print(file.read())
    elif count == 7:
        with open('stage7.txt', 'r', encoding='utf-8') as file:
            print(file.read())

def start():
    
    global trueword, count
    guessed = ["*"] * len(trueword)

    while True:

        hangman()

        print("Слово:", "".join(guessed))
        letter = input("Введите букву: ").lower()
        
        if len(letter) >= 2:
            print("Введите одну букву!")
            continue
        
        if letter in trueword.lower():
            for i, ch in enumerate(trueword.lower()):
                if ch == letter:
                    guessed[i] = trueword[i]
        else:
            count += 1

        if "*" not in guessed:
            print("Победа! Слово:", trueword)
            break
        if count == 7:
            print("Проигрыш. Слово было:", trueword)
            hangman()
            break

trueword = word()
start()
