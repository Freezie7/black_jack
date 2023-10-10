import random


def give(rand_card):
    rand = random.randint(1, 52) - 1
    return list(cards.keys())[rand]

    
cards = {
    "Туз Пик": 11, "2 Пик": 2, "3 Пик": 3, "4 Пик:": 4, "5 Пик": 5,
    "6 Пик": 6, "7 Пик": 7, "8 Пик":8, "9 Пик": 9, "10 Пик": 10, "Валет Пик:": 10,
    "Дама Пик": 10, "Король Пик": 10,
    "Туз Черви": 11, "2 Черви": 2, "3 Черви": 3, "4 Черви:": 4, "5 Черви": 5,
    "6 Черви": 6, "7 Черви": 7, "8 Черви":8, "9 Черви": 9, "10 Черви": 10, "Валет Черви:": 10,
    "Дама Черви": 10, "Король Черви": 10,
    "Туз Бубни": 11, "2 Бубни": 2, "3 Бубни": 3, "4 Бубни:": 4, "5 Бубни": 5,
    "6 Бубни": 6, "7 Бубни": 7, "8 Бубни":8, "9 Бубни": 9, "10 Бубни": 10, "Валет Бубни:": 10,
    "Дама Бубни": 10, "Король Бубни": 10,
    "Туз Крести": 11, "2 Крести": 2, "3 Крести": 3, "4 Крести": 4, "5 Крести": 5,
    "6 Крести": 6, "7 Крести": 7, "8 Крести":8, "9 Крести": 9, "10 Крести": 10, "Валет Крести": 10,
    "Дама Крести": 10, "Король Крести": 10
    }

point1 = 0
point2 = 0
rand_card = 0


name_card = " "
print("ВЫ:")

name_card = give(name_card)
point1 += cards[name_card]
print(name_card)
name_card = give(name_card)
point1 += cards[name_card]
print(name_card)
print("Сумма очков: ", point1)

print("        ")

print("ДИЛЕР:")
name_card = give(name_card)
point2 += cards[name_card]
print(name_card)
name_card = give(name_card)
point2 += cards[name_card]
print(name_card)
print("Сумма очков: ", point2)

choice = input("1 - Hold/ 2 - Hit: ")
while choice != "1":
    if choice == "2":
        name_card = give(name_card)
        point1 += cards[name_card]
        print(name_card)
        print("Сумма очков: ", point1)
        if point1 > 21:
            break
    choice = input("1 - Hold/ 2 - Hit: ")

while point2 <= point1 and point1 <= 21 and point2 != 20:
    print("      ")
    print("ДИЛЕР ВЫТАЩИЛ КАРТУ:")
    name_card = give(name_card)
    point2 += cards[name_card]
    print(name_card)
    print("Сумма очков: ", point2)


if point1 > 21:
    print("ВЫ проиграли. Перебор")
if point1 <= 21 and point2 > 21:
    print("Вы победили!")
if point2 > point1 and point2 <= 21:
    print("ВЫ проиграли")
