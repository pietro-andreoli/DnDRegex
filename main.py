from regex import *
def print_class_intro():
    with open("ClassIntro.txt", 'r') as intro:
        print(intro.read())


def get_classes():
    num_of_classes = 0
    class_list = []
    with open("Classes.txt", 'r') as class_file:
        for dnd_class in class_file.readlines():
            num_of_classes += 1
            class_list.append(dnd_class.strip())
    return num_of_classes, class_list


def select_level():
    lvl_choice = 0
    while True:
        try:
            lvl_choice = int(input("Select a level between 2 and 20\n"))
        except ValueError:
            print("Invalid input.")
            continue
        if 20 < lvl_choice or lvl_choice < 2:
            continue
        else:
            break
    return lvl_choice




num_classes = 0
classes = []
choice = -1
num_classes, classes = get_classes()
level_choice = 0

print_class_intro()


while True:
    try:
        choice = int(input("Enter the corresponding number between 0 and 11.\n"))
    except ValueError:
        print("Invalid input. Please select a number between 0 and " + str(num_classes) + ".")
        print_class_intro()
        continue
    if 0 <= choice <= num_classes-1:
        break
    else:
        print("Invalid input. Please select a number between 0 and " + str(num_classes) + ".")
        print_class_intro()

print(classes[choice] + " chosen.")

level_choice = select_level()

print(str(level_choice) + "selected.")
strip_file("Sorcerer")
