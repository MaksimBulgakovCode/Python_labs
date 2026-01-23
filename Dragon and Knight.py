import random

language = input("ru/eng \n")

def start():

    player_hp = random.randint(40, 100)
    dragon_hp = 200

    if language == "eng":
        text = {
            'main': 'You need to defeat the dragon, he has {dragonHP} HP',
            'action': 'Player: {playerHP} HP | Dragon: {dragonHP} HP \nYou can attack or heal (a/h) \n',
            'player_damage': 'You dealt {dmg} damage to the dragon',
            'over100hp': 'You can not have over 100 HP',
            'heal': 'You have restored {heal} HP',
            'dragon_damage': 'The dragon attacked you and dealt {dmg} damage',
            'win': 'You win! Thank you for playing!',
            'defeat': 'Are you defeat :( \nRestart? (r)',
            }
        
    elif language == "ru":
        text = {
            'main': 'Тебе нужно победить дракона, у него {dragonHP} HP',
            'action': 'Игрок: {playerHP} HP | Дракон: {dragonHP} HP \nТы можешь атаковать или лечиться (a/h) \n',
            'player_damage': 'Ты нанёс {dmg} урона дракону',
            'over100hp': 'У тебя не может быть больше 100 HP',
            'heal': 'Ты восстановил {heal} HP',
            'dragon_damage': 'Дракон атаковал тебя, и нанёс {dmg} урона',
            'win': 'Ты победил! Спасибо за игру!',
            'defeat': 'Ты проиграл :( \nЗаново? (r)',
    }
    
    print(text['main'].format(dragonHP = dragon_hp))
    while True:
        action = input(text['action'].format(playerHP = player_hp, dragonHP = dragon_hp))
        print("=" * 20)
        
        if action == "a":
            damage = random.randint(0, 25)
            dragon_hp -= damage
            print(text['player_damage'].format(dmg = damage))
        
        if dragon_hp <= 0:
                print(text['win'])
                break
        
        elif action == "h":
            heal = random.randint(5, 30)
            if player_hp + heal >= 100:
                player_hp = 100
                print(text['over100hp'])
            else:
                player_hp += heal
            print(text['heal'].format(heal = heal))
        
        elif action == "exit":
            break
        
        damage = random.randint(0, 30)
        player_hp -= damage
        print(text['dragon_damage'].format(dmg = damage))

        if player_hp <= 0:
            end = input(text['defeat'])
            if end == "r":
                dragon_hp = 200
                player_hp = random.randint(40, 100)
                start()
            else:
                break

start()
