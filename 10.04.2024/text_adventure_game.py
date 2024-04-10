import json
from race_description import human_description, elf_description, anitur_description, venif_description
from class_description import knight_description, mage_description, archer_description, fighter_description
import time
import sys
import json
from the_beginning_1 import the_beginning


def parts(description):
    description_parts = description.split('\n')
    for part in description_parts:
        print(part)
        time.sleep(0)
    print("")


def parts2(description):
    description_parts = description.split('\n')
    for part in description_parts:
        print(part)
        time.sleep(2)
    print("     ")


with open("game_data.json", "r") as file:
    dane_json = json.load(file)

while True:
    print("\nMENU\n1. New Game\n2. Load Game\n3. Exit")
    try:
        n = int(input("Choose an option: \n"))
        print("")
        break
    except ValueError:
        continue

race_set = True
new_race = 0
choosing_race = True

class_set = True
new_class = 0
choosing_class = True

while True:

    if n == 1:
        p = 6
        print("NEW GAME")
        new_save = input("Input the name of the save file: \n")
        print("")
        new_name = input("Input your name: \n")
        print("")
        print("It's time to choose the race of your character. After choosing the race, there will be the description displayed.")
        while race_set is True:
            choosing_race = True
            print("\n1. Human\n2. Elf\n3. Anitur\n4. Venif")
            try:
                print("")
                race_number = int(input("Input the number.\n"))
                race_list = [1, 2, 3, 4]
                print("")
                if race_number not in race_list:
                    continue
                else:
                    race_set = False
                    while choosing_race is True:
                        if race_number == 1:
                            parts(human_description)
                            question = input("Do you want to choose this race? (y)es or (n)o\n")
                            if question == "y":
                                new_race = "human"
                                choosing_race = False
                            elif question == "n":
                                choosing_race = False
                                race_set = True

                        elif race_number == 2:
                            parts(elf_description)
                            question = input("Do you want to choose this race? (y)es or (n)o\n")
                            if question == "y":
                                new_race = "elf"
                                choosing_race = False
                            elif question == "n":
                                choosing_race = False
                                race_set = True

                        elif race_number == 3:
                            parts(anitur_description)
                            question = input("Do you want to choose this race? (y)es or (n)o\n")
                            if question == "y":
                                new_race = "anitur"
                                choosing_race = False
                            elif question == "n":
                                choosing_race = False
                                race_set = True

                        elif race_number == 4:
                            parts(venif_description)
                            question = input("Do you want to choose this race? (y)es or (n)o\n")
                            if question == "y":
                                new_race = "venif"
                                choosing_race = False
                            elif question == "n":
                                choosing_race = False
                                race_set = True

            except ValueError:
                print("Choose the correct number.")
                continue

        print("")
        print("It's time to choose the class of your character. After choosing the race, there will be the description displayed.")

        while class_set is True:
            choosing_class = True
            print("\n1. Knight\n2. Archer\n3. Mage\n4. Fighter")
            try:
                print("")
                class_number = int(input("Input the number.\n"))
                class_list = [1, 2, 3, 4]
                print("")
                if class_number not in class_list:
                    continue
                else:
                    class_set = False
                    while choosing_class is True:
                        if class_number == 1:
                            parts(knight_description)
                            question = input("Do you want to choose this class? (y)es or (n)o\n")
                            if question == "y":
                                new_class = "knight"
                                choosing_class = False
                            elif question == "n":
                                choosing_class = False
                                class_set = True

                        elif class_number == 2:
                            parts(archer_description)
                            question = input("Do you want to choose this class? (y)es or (n)o\n")
                            if question == "y":
                                new_class = "archer"
                                choosing_class = False
                            elif question == "n":
                                choosing_class = False
                                class_set = True

                        elif class_number == 3:
                            parts(mage_description)
                            question = input("Do you want to choose this class? (y)es or (n)o\n")
                            if question == "y":
                                new_class = "mage"
                                choosing_class = False
                            elif question == "n":
                                choosing_class = False
                                class_set = True

                        elif class_number == 4:
                            parts(fighter_description)
                            question = input("Do you want to choose this class? (y)es or (n)o\n")
                            if question == "y":
                                new_class = "fighter"
                                choosing_class = False
                            elif question == "n":
                                choosing_class = False
                                class_set = True

            except ValueError:
                print("Choose the correct number.")
                continue
        data1 = dict(save_file=new_save, name=new_name, race=new_race, class1=new_class, game_level=0)
        dane_json.append(data1)
        with open("game_data.json", "w") as file1:
            json.dump(dane_json, file1, indent=2)
        n = 2
        continue

    if n == 2:
        p = 5
        with open("game_data.json", "r") as file1:
            data = json.load(file1)
        print("")
        print("LOAD GAME")
        your_save = input("Input your save file name: ")
        print()

        found_user = None
        for save in data:
            if save.get("save_file") == your_save:
                found_user = save
                break

        if found_user is not None:
            your_name = input("Input your name: ")
            print()
            if save.get("name") != your_name:
                print("INVALID NAME")

            else:
                break
        else:
            print("Save file not found, you create a new game.")
            print()
            answer = input("Do you want to create a new game?\nyes or no?\n")
            print()
            if answer == "yes":
                p = 4
                new_save = input("Input the name of the save file: \n")
                print("")
                new_name = input("Input your name: \n")
                print("")
                print("It's time to choose the race of your character. After choosing the race, there will be the description displayed.")
                while race_set is True:
                    choosing_race = True
                    print("\n1. Human\n2. Elf\n3. Anitur\n4. Venif")
                    try:
                        print("")
                        race_number = int(input("Input the number.\n"))
                        race_list = [1, 2, 3, 4]
                        print("")
                        if race_number not in race_list:
                            continue
                        else:
                            race_set = False
                            while choosing_race is True:
                                if race_number == 1:
                                    parts(human_description)
                                    question = input("Do you want to choose this race? (y)es or (n)o\n")
                                    if question == "y":
                                        new_race = "human"
                                        choosing_race = False
                                    elif question == "n":
                                        choosing_race = False
                                        race_set = True

                                elif race_number == 2:
                                    parts(elf_description)
                                    question = input("Do you want to choose this race? (y)es or (n)o\n")
                                    if question == "y":
                                        new_race = "elf"
                                        choosing_race = False
                                    elif question == "n":
                                        choosing_race = False
                                        race_set = True

                                elif race_number == 3:
                                    parts(anitur_description)
                                    question = input("Do you want to choose this race? (y)es or (n)o\n")
                                    if question == "y":
                                        new_race = "anitur"
                                        choosing_race = False
                                    elif question == "n":
                                        choosing_race = False
                                        race_set = True

                                elif race_number == 4:
                                    parts(venif_description)
                                    question = input("Do you want to choose this race? (y)es or (n)o\n")
                                    if question == "y":
                                        new_race = "venif"
                                        choosing_race = False
                                    elif question == "n":
                                        choosing_race = False
                                        race_set = True

                    except ValueError:
                        print("Choose the correct number.")
                        continue

                print("")
                print("It's time to choose the class of your character. After choosing the race, there will be the description displayed.")

                while class_set is True:
                    choosing_class = True
                    print("\n1. Knight\n2. Archer\n3. Mage\n4. Fighter")
                    try:
                        print("")
                        class_number = int(input("Input the number.\n"))
                        class_list = [1, 2, 3, 4]
                        print("")
                        if class_number not in class_list:
                            continue
                        else:
                            class_set = False
                            while choosing_class is True:
                                if class_number == 1:
                                    parts(knight_description)
                                    question = input("Do you want to choose this class? (y)es or (n)o\n")
                                    if question == "y":
                                        new_class = "knight"
                                        choosing_class = False
                                    elif question == "n":
                                        choosing_class = False
                                        class_set = True

                                elif class_number == 2:
                                    parts(archer_description)
                                    question = input("Do you want to choose this class? (y)es or (n)o\n")
                                    if question == "y":
                                        new_class = "archer"
                                        choosing_class = False
                                    elif question == "n":
                                        choosing_class = False
                                        class_set = True

                                elif class_number == 3:
                                    parts(mage_description)
                                    question = input("Do you want to choose this class? (y)es or (n)o\n")
                                    if question == "y":
                                        new_class = "mage"
                                        choosing_class = False
                                    elif question == "n":
                                        choosing_class = False
                                        class_set = True

                                elif class_number == 4:
                                    parts(fighter_description)
                                    question = input("Do you want to choose this class? (y)es or (n)o\n")
                                    if question == "y":
                                        new_class = "fighter"
                                        choosing_class = False
                                    elif question == "n":
                                        choosing_class = False
                                        class_set = True
                        continue

                    except ValueError:
                        print("Choose the correct number.")
                        continue
                data1 = dict(save_file=new_save, name=new_name, race=new_race, class1=new_class, game_level=0)
                dane_json.append(data1)
                with open("game_data.json", "w") as file1:
                    json.dump(dane_json, file1, indent=2)
    if n == 3:
        sys.exit()
print("GAME LOADED")

with open("game_data.json", "r") as file2:
    data = json.load(file2)

if p == 6 or p == 4:
    the_name = new_name
elif p == 5:
    the_name = your_name

print(parts2(the_beginning))
print(f"")

