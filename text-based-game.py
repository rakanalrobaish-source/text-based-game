import random

#   1. Functions
def enemy_attack(health):
    enemy_damage = random.randint(5, 15)
    health -= enemy_damage
    print(f"The enemy dealt {enemy_damage} to you. You have {health} health left")
    return health

#   2. Variables
Stats = {"health": 100, "energy": 0, "enemy_health": 150, "escaped": False,}

#   3. Main Loop
while Stats["health"] > 0 and Stats["enemy_health"] > 0:
    Stats["energy"] += 1
    if Stats["energy"] > 6:
        Stats["energy"] = 6

    print(f"\n [YOU]: HP: {Stats['health']} | EN: {Stats['energy']} ")
    print(f"[ENEMY]: HP: {Stats['enemy_health']} \n")
    print("1. Attack | 2. Heal | 3. Abilities | 4. Escape \n")
    choice = input("Enter 1, 2, 3, or 4: ")

    if choice == "1":
        damage = random.randint(10, 20)
        if random.randint(1, 5) == 1:
            damage *= 2
            print("Critical hit!")
        Stats["enemy_health"] -= damage
        print(f"You dealt {damage} to the enemy. the enemy has {Stats['enemy_health']} health left")

    elif choice == "2":
        heal = random.randint(10, 20)
        Stats["health"] += heal
        if Stats["health"] > 100:
            Stats["health"] = 100
        print(f"You healed yourself for {heal} health")

    elif choice == "3":
        print("1. Barrage (1 energy)")
        print("2. Fireball (2 energy)")
        ability_choice = input("Enter 1 or 2: ")
        
        if ability_choice == "1":
            if Stats["energy"] < 1:
                print("Not enough energy to use Barrage")
            else:
                Stats["energy"] -= 1
                damage = random.randint(20, 25)
                if random.randint(1, 5) == 1:
                    damage *= 2
                    print("Critical hit!")
                Stats["enemy_health"] -= damage
                print(f"You dealt {damage} to the enemy with barrage. the enemy has {Stats['enemy_health']} health left")

        elif ability_choice == "2":
            if Stats["energy"] < 2:
                print("Not enough energy to use Fireball")
            else:
                Stats["energy"] -= 2
                damage = random.randint(10, 40)
                if random.randint(1, 5) == 1:
                    damage *= 2
                    print("Critical hit!")
                Stats["enemy_health"] -= damage
                print(f"You dealt {damage} to the enemy with fireball. the enemy has {Stats['enemy_health']} health left")
        else:
            print("Invalid ability choice, try again.") 
            continue

    elif choice == "4":
        escape_chance = random.randint(1, 3)
        if escape_chance == 1:
            Stats["escaped"] = True
            break
        else:
            print("Your escape failed!")

    else:
        print("Invalid choice, try again.")
        pass

    if Stats["enemy_health"] > 0:
        Stats["health"] = enemy_attack(Stats["health"])

#   4. Results
if Stats["escaped"]:
    print("You escaped successfully!")
elif Stats["health"] <= 0:
    print("You died! Game over.")
else:
    print("You defeated the enemy! You win!")
