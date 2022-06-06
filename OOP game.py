from time import sleep
import random


class Stats:
    def __init__(self, name, power, health, crit_chance, crit_amplifier):
        self.alive = True
        self.name = name
        self.power = power
        self.hp = health
        self.crit_chance = crit_chance
        self.hp_at_start = self.hp
        self.power_at_start = self.power
        self.crit_amplifier = crit_amplifier
        self.deaths = 0
        self.level = 0

    def print_info(self):
        print(f"Name: {self.name}")
        sleep(0.3)
        print(f"Hit power: {self.power}")
        sleep(0.3)
        print(f"Health: {self.hp}")
        sleep(0.3)
        print(f"Crit chance: {self.crit_chance}")
        sleep(0.3)
        print(f"Crit power: {int(self.crit_amplifier * 100)}%")
        sleep(0.3)
        print(f"Level: {self.level}")
        sleep(0.3)

    def set_power_at_start(self, new):
        self.power_at_start = new

    def power_default(self):
        self.power = self.power_at_start

    def dies(self):
        self.alive = False
        self.deaths += 1


class Heroes(Stats):
    def first_print_info(self):
        print("\nThe new hero appears:")
        super().print_info()

    def print_info(self):
        super().print_info()


class Enemies(Stats):
    def print_info(self):
        print("\nNew enemy spawned:")
        super().print_info()


knight = Heroes("Knight", 13, 105, 24, 1.5)
wolf = Enemies("wolf", 8, 65, 36, 1.2)
golem = Enemies("Golem", 12, 120, 6, 1.3)


# main attack func (looped till one dies)
def attacking(att, deff):
    while att.hp > 0 or deff.hp > 0:
        att.power_default()
        crit_check(att)
        sleep(0.3)
        print(f"{att.name} attacks \n  {int(att.power)} damage!")
        deff.hp -= int(att.power)
        print(f"{deff.name} has {deff.hp} hp\n")
        crit_check(deff)
        sleep(0.3)
        print(f"    {deff.name} attacks \n  {int(deff.power)} damage!")
        att.hp -= int(deff.power)
        print(f"    {att.name} has {att.hp} hp\n")
        sleep(0.2)
        if att.hp <= 0 and deff.hp <= 0:
            print(f"{deff.name} dies")
            deff.dies()
            print(f"{att.name} dies")
            att.dies()
            break
        elif att.hp <= 0:
            print(f"{att.name} dies")
            att.dies()
            break
        elif deff.hp <= 0:
            print(f"{deff.name} dies")
            deff.dies()
            break


# mult power bt crit amplifier if rand (1-100) in crit chance
def crit_check(att):
    if random.randint(1, 100) in range(1, att.crit_chance):
        att.power *= att.crit_amplifier


def door_picking():
    print("\nU have 3 doors")
    print("which door to open? (1/2/3)")
    choose = None
    # incorrect type check
    while True:
        try:
            sleep(0.2)
            choose = int(input("Door number: "))
            break
        except ValueError:
            print("it seems you've typed something wrong. Try again")
        if choose not in rand_picks:
            print("Error. Type (1/2/3)")

    # shuffling list to pick from
    random.shuffle(rand_picks)

    # heal
    if rand_picks[choose - 1] == 1:
        print("\nYou've got an hp potion, grab your 30 hp")
        print("A nice moment. Enjoy ^-^")
        sleep(1.5)
        for _ in range(30):
            # healed to max
            if knight.hp_at_start == knight.hp:
                print("healed to max")
                break
            print(f"\nYour health: {knight.hp}")
            knight.hp += 1
            sleep(0.15)

        print("Your hp:", knight.hp)

    # wolf
    elif rand_picks[choose - 1] == 2:
        print("\nYou've got an enemy: Wolf!.\nFight for your life!")
        wolf.hp = wolf.hp_at_start
        lucky_pick(knight, wolf)

        if knight.hp > 0:
            level_up()
    # golem
    elif rand_picks[choose - 1] == 3:
        print("\nYou've got an enemy: Golem!.\nFight for your life!")
        golem.hp = golem.hp_at_start
        lucky_pick(knight, golem)

        if knight.hp > 0:
            level_up()
            level_up()

    print("\n\nDoors have been shuffled")


# finding first hit
def lucky_pick(hero, enemy):
    lucky = random.randint(0, 1)
    user_num = None
    while True:
        try:
            print("Roll for first hit. 0/1")
            user_num = int(input())
            if user_num > 1:
                print("it seems you've typed wrong number. Try again")
                continue
            break
        except ValueError:
            print("it seems you've typed something wrong. Try again")
    print()
    if user_num == lucky:
        print("Lucky pick!")
        attacking(hero, enemy)
    else:
        print("Unlucky =(")
        attacking(enemy, hero)
    sleep(1.5)


def level_up():
    stats = {"Healthushechka": 10,
             "Domogarov": 5,
             "CC": 3,
             "CA": 10
             }
    knight.level += 1
    print()
    print("Level up!\nYou can choose one stat to upgrade")
    sleep(0.5)
    print(f"Healthushechka: +{stats['Healthushechka']}")
    sleep(0.5)
    print(f"Domogarov: +{stats['Domogarov']}")
    sleep(0.5)
    print(f"5 kritov podryad sukaaaaaaaaaaaaaaaaaaa (Crit chance: +{stats['CC']})")
    sleep(0.5)
    print(f"НЫЫЫЫЫЫЫЫААААААА!!!!!! (Crit amplifier: +{stats['CA']})")
    sleep(0.5)

    print("Which one?", list(stats.keys()))
    stat = input()
    while stat not in stats.keys():
        print("You have typed something wrong. Try again")
        stat = input()
    print("\nNice choise!")
    if stat == "Healthushechka":
        knight.hp += stats[stat]
    elif stat == "Domogarov":
        knight.power += stats[stat]
        knight.set_power_at_start()
    elif stat == "CC":
        knight.crit_chance += stats[stat]
    elif stat == "CA":
        knight.crit_amplifier += stats[stat] / 100
    knight.print_info()


# results of deaths for the end
def results():
    knight.print_info()
    print()
    print(f"Wolf: {wolf.deaths} deaths" if wolf.deaths != 1 else f"Wolf: {wolf.deaths} death")
    print(f"Golem: {golem.deaths} deaths" if golem.deaths != 1 else f"Golem: {golem.deaths} death")


def end_speech():
    print("\n\nYour journey has ended.")
    print()
    if wolf.deaths < 1 and golem.deaths < 1:
        print("Your stats.. Em.. Not bad I think..")
    elif wolf.deaths > 0 and golem.deaths < 1:
        print("Good journey. Not really lucky thought")
    elif wolf.deaths > 0 and golem.deaths < 1:
        print("A great journey it was!")
    print("\nResults:")
    knight.hp = knight.hp_at_start
    results()


# prep picks to random
rand_picks = [1, 2, 3]

print("\nHello, traveler. Guide your hero to the win!")

print("Firstly, pick the name for your hero:")
knight.name = input()

sleep(0.2)
knight.first_print_info()
sleep(0.2)

while knight.hp > 0:
    door_picking()

end_speech()
input("press something to out")
