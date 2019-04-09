import random as rand
print(
    "Welcome to The Legion of Zolder!"
    "\nYou got lost on your way home from the New Moon Festival, and you're now alone in a dark forest. "
    "\nYou should probably look around for something useful.\nWhat do you want to do?")

enemy_count = 0
player_health = 25


class Item:
    def __init__(self, name, text):
        self.name = name
        self.text = text


class Enemy:
    def __init__(self, name, health, attack_min, attack_max):
        self.health = health
        self.name = name
        self.attack_min = attack_min
        self.attack_max = attack_max
        global enemy_count
        enemy_count += 1


class Weapon:
    def __init__(self, name, attack_min, attack_max):
        self.name = name
        self.attack_min = attack_min
        self.attack_max = attack_max


Sword = Weapon("sword", 4, 8)
Scroll_text = "So you finally got here!\nI bet you've been looking for this treasure for decades " \
              "and you're not even halfway through your journey!\nHow did you like all those puzzles?" \
              "\nI bet they completely stumped you! Yeah... I'm smart like that.\nOh, you just got lost and " \
              "found this scroll by chance?\nI see. \n... " \
              "\nForget what I wrote about the treasure, alright?\nThere's no treasure here, only trees." \
              "\nAnd a goblin.\nOh, right, be careful about the goblin!\n"

Goblin = Enemy("goblin", 18, 4, 7)
Scroll = Item("scroll", Scroll_text)
has_sword = False
has_scroll = False
has_searched = False
is_out = False
has_map = False
knows_goblin = False


def get_input():
    global has_scroll
    global has_sword
    global has_searched
    global is_out
    global has_map
    global knows_goblin
    command = input(": ").split()
    if 3 > len(command) > 0:
        action = command[0]
        action.lower()
        if action == "say":
            if len(command) <= 1:
                print("You said nothing.\n")
            else:
                print("You said", command[1])
        elif action == "attack":
            if len(command) <= 1 and has_sword is True:
                print("You attacked nothing.\n")
            elif has_sword is True:
                target = command[1]
                target.lower()
                if target == "goblin" and enemy_count >= 1:
                    damage = rand.randint(Sword.attack_min, Sword.attack_max)
                    Goblin.health -= damage
                    print("You attacked the", target,)
                    print("You dealt {} damage!\n".format(damage))
                    if damage == Sword.attack_max:
                        print("Critical Strike!\n")
                    return Goblin.health
                elif target == "goblin":
                    print("You already killed the goblin!\n")
                else:
                    print("You can't attack that!\n")
            else:
                print("You can't attack without a weapon!\n")

        elif action == "search" or action == "look":
            if len(command) >= 2:
                if command[1] == "treasure" and has_map is False:
                    print("You found the treasure map!\n")
                    has_map = True

                else:
                    if has_searched is False:
                        print("You looked around.\nYou found a scroll and a sword!\n"
                              "And something is lurking in the shadows...\n")
                        has_sword = True
                        has_scroll = True
                        has_searched = True
                    elif has_searched is True:
                        print("You looked around again.\nYou found nothing new.\n")
            elif has_searched is False:
                print("You looked around.\nYou found a scroll and a sword!\n"
                      "And something is lurking in the shadows...\n")
                has_sword = True
                has_scroll = True
                has_searched = True
            elif has_searched is True:
                print("You looked around again.\nYou found nothing new.\n")
        elif action == "read":
            if len(command) <= 1:
                print("You read nothing.\n")
            else:
                if command[1] == "scroll" and has_scroll is True:
                    print(Scroll_text)
                    knows_goblin = True
                elif command[1] == "treasure" or command[1] == "map" and has_map is True:
                    print("You tried to read the treasure map, but it's unreadable.\n "
                          "Look like it's been out for too long."
                          "\n Hiding it in a bush wasn't the best idea..."
                          "\n Hopefully that treasure wasn't really important...\n")
                elif command[1][0] in "aeiuo":
                    print("You don't have an {} to read!\n".format(command[1]))
                else:
                    print("You don't have a {} to read!\n".format(command[1]))
        elif action == "move":
            if enemy_count >= 1:
                print("You walked towards the edge of the forest.\n")
            elif enemy_count <= 1:
                print("You walked towards the light...\n")
                is_out = True
        else:
            print("You can't do that.\n")
    elif len(command) >= 3:
        print("I can't read that many words!")
    else:
        print("You do nothing.\n")


respawn = 0
i = 0
while True:
    i += 1
    if 0 < player_health <= 8:
        print("Your wounds are severe... You should hurry up...\n")
    elif player_health <= 0:
        print("You died.\n")
        break
    get_input()
    if is_out is True:
        print("And now, you got out of the forest!\nYour house is right here, you can finally go to bed"
              "but, wait, it's 9AM...\nWell...\nTime to go to school!\n")
        break
    if i >= 3:
        rng = rand.randint(0, 2)
        try:
            Goblin
        except NameError:
            if respawn <= 3:
                respawn += 1
            elif respawn > 3:
                Goblin = Enemy("goblin", 14, 4, 7)
                print("The goblin came back to life!\n")
        else:
            if rng == 1 or rng == 2:
                hit = rand.randint(Goblin.attack_min, Goblin.attack_max)
                player_health -= hit
                if knows_goblin is True and Goblin.health > 0:
                    print("You got it by the goblin!")
                    print("It dealt {} damage!\n".format(hit))
                    if hit == Goblin.attack_max:
                        print("Critical Strike! Ouch...\n")
                elif Goblin.health > 0:
                    print("You got it by the shadowy figure!")
                    print("It dealt {} damage!\n".format(hit))
                    if hit == Goblin.attack_max:
                        print("Critical Strike! Ouch...\n")
            else:
                if knows_goblin is True and Goblin.health > 0:
                    print("The goblin tried to hit you, but he ran into a tree!"
                          "\nYou got lucky this time...\n")
                elif Goblin.health > 0:
                    print("The shadowy figure tried to hit you, but he ran into a tree!"
                          "\nYou got lucky this time...\n")
            if Goblin.health <= 0:
                print("You killed the", Goblin.name, "!\n")
                del Goblin
                enemy_count -= 1
                respawn = 0
            if enemy_count <= 0:
                print("You defeated all the enemies!\nAll you have to do now is find your way out.")
                print("You see a shining light in front of you, the sun is rising, there's your way out!\n")

print("Thank you for playing The Legos of Zaldorg!")
