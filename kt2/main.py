from random import randint

print("Виселица. Угадай слово")
count = 0

def word():
    words = ["Мяч", "Турнир", "Машина", "Ипотека", "Ноутбук"]
    correctword = words[randint(0, 4)]
    return correctword

def hangman():
    stage = list("stage0.txt")
    stage[5] = str(count)
    stage = "".join(stage)

    with open(stage, 'r', encoding='utf-8') as file:
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
