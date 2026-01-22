import random

player_hp = random.randint(40, 100)
dragon_hp = 200

start_stop = True
language = input("ru/eng \n")

if language == "eng":
    text = {
        'main' : f'You need to defeat the dragon, he has {dragon_hp} HP',
        'action' : f'You have {player_hp} HP \nDragon has {dragon_hp} HP \nYou can attack or heal (a/h) \n',
        'player_damage' : f'You dealt {player_damage} damage to the dragon',
        'over100hp' : f'You can not have over 100 HP',
        'heal' : f'You have restored {heal} HP',
        'dragon_damage' : f'The dragon attacked you and dealt {dragon_damage} damage',
        'win' : 'You win! Thank you for playing!',
        'defeat' : 'Are you defeat :( \nRestart? (r))',
        }
elif language == "ru":
    text = {
        'main' : f'Тебе нужно победить дракона, у него {dragon_hp} HP',
        'action' : f'Игрок: {player_hp} HP | Дракон: {dragon_hp} HP \nТы можешь атаковать или лечиться (a/h) \n',
        'player_damage' : f'Ты нанёс {player_damage} урона дракону',
        'over100hp' : 'У тебя не может быть больше 100 HP',
        'heal' : f'Ты восстановил {heal} HP',
        'dragon_damage' : f'Дракон атаковал тебя, и нанёс {dragon_damage} урона',
        'win' : 'Ты победил! Спасибо за игру!',
        'defeat' : 'Ты проиграл :( \nЗаново? (r))',
    }

def start():
    
    print(text['main'])
    while start_stop:
        action = input(text['action'])
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
            if player_hp + heal == 100:
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
        
        dragon_damage = random.randint(0, 30)
        player_hp = player_hp - dragon_damage
        if language == "eng":
            print(f"The dragon attacked you and dealt {dragon_damage} damage")
        elif language == "ru":
            print(f"Дракон атаковал тебя, и нанёс {dragon_damage} урона")

        if dragon_hp <= 0 or player_hp <= 0:
            restart()

        
def restart():
    global dragon_hp, player_hp, start_stop
    if dragon_hp < 0:
        if language == "eng":
            print("You win! Thank you for playing!")
            start_stop = False
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
            start_stop = False

start()

