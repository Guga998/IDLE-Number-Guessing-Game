import random

difficulty_easy = random.randint(2, 99)
difficulty_mid = random.randint(2, 999)
difficulty_hard = random.randint(2, 9999)

def main():
    print("Choose the difficulty(1-3): ")
    choice = int(input("Choice: "))
    if choice == 1:
        number = difficulty_easy
        num_game(number)
    elif choice == 2:
            number = difficulty_mid
            num_game(number)
    elif choice == 3:
            number = difficulty_hard
            num_game(number)

def num_game(number):
    guesses = 0

    if number == difficulty_easy:
        print("Choose a Number Between 1 and 100")
        choice1 = int(input("Choice: "))
    if number == difficulty_mid:
        print("Choose a Number Between 1 and 1000")
        choice1 = int(input("Choice: "))
    if number == difficulty_hard:
        print("Choose a Number Between 1 and 10000")
        choice1 = int(input("Choice: "))

    while choice1 != number:
        guesses += 1
        if choice1 > number:
            print("To High")
            choice1 = int(input("Choice: "))
        elif choice1 < number:
            print("To Low")
            choice1 = int(input("Choice: "))

    print("You Won!!")
    print("The Number was ", number)
    print("You tried ", guesses, " Times!")

main()