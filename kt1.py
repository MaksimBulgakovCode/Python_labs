#Писарев Максим ИТ-СИП-25-ПР
import random

def start():
    count = 0
    while True:
        say = input("Вы: ")
        if say == "ПОКА!":
            count += 1
        else:
            count = 0
        if count == 3:
            print("Бабушка: ДО СВИДАНИЯ, ДОРОГОЙ!")
            break
        elif say.isupper():
            print(f"Бабушка: НЕТ, НИ РАЗУ С {random.randint(1930, 1980)} ГОДА!")
        else:
            print("Бабушка: АСЬ?! ГОВОРИ ГРОМЧЕ, ВНУЧЕК")


start()
