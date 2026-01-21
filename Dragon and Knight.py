import random

start_stop = True
dragon_hp = 200
dragon_mana = 300
language = input("ru/eng \n")

player_hp = random.randint(40, 100)

def start():
    global dragon_hp, player_hp, language
    if language == "eng":
        print(f"You need to defeat the dragon, he has {dragon_hp} HP")
    elif language == "ru":
        print(f"Тебе нужно победить дракона, у него {dragon_hp} HP")
    
    while start_stop:
        if language == "eng":
            action = input(f"You have {player_hp} HP \nDragon has {dragon_hp} HP \nYou can attack or heal (a/h) \n")
        elif language == "ru":
            action = input(f"У тебя {player_hp} HP \nУ дракона {dragon_hp} HP \nТы можешь атаковать или лечиться (a/h) \n")
        print("=" * 20)
        
        if action == "a":
            player_damage = random.randint(0, 25)
            dragon_hp = dragon_hp - player_damage
            if language == "eng":
                print(f"You dealt {player_damage} damage to the dragon")
            elif language == "ru":
                print(f"Ты нанёс {player_damage} урона дракону")
        
        elif action == "h":
            heal = random.randint(5, 30)
            if player_hp + heal > 100:
                player_hp = 100
                if language == "eng":
                    print("You can't have over 100 HP")
                elif language == "ru":
                    print("У тебя не может быть больше 100 HP")
            else:
                player_hp = player_hp + heal
            if language == "eng":
                print(f"You have restored {heal} HP")
            elif language == "ru":
                print(f"Ты восстановил {heal} HP")
        
        if action == "exit":
            break

        if dragon_hp or player_hp <= 0:
            restart()
        
        dragon_damage = random.randint(0, 30)
        player_hp = player_hp - dragon_damage
        if language == "eng":
            print(f"The dragon attacked you and dealt {dragon_damage} damage")
        elif language == "ru":
            print(f"Дракон атаковал тебя, и нанёс {dragon_damage} урона")

        
def restart():
    global dragon_hp, player_hp, start_stop
    if dragon_hp < 0:
        if language == "eng":
            print("You win! Thank you for playing!")
        elif language == "ru":
            print("Ты победил! Спасибо за игру!")
            start_stop = False

    elif player_hp < 0:
        if language == "eng":
            print("Are you defeat :( \nRestart? (r))")
        elif language == "ru":
            print("Ты проиграл :( \nЗаново? (r))")
        end = input()
        if end == "r":
            dragon_hp = 200
            player_hp = random.randint(40, 100)
            start()
        else:
            start_stop == False

start()

