import random
while True:
    min,max = list(map(int,input("Enter the range for number to be choosen [min,max]: ").split(",")))
    number = random.randint(min,max)
    count = 0
    while True:
        num = int(input("Guess the number: "))
        count += 1
        if num == number:
            break
        elif num < number:
            print("You guessed a smaller number.")
        elif num > number:
            print("You guessed a larger number.")
        else:
            print("Enter a valid Number.")
    print(f"Great! you took {count} attemps to guess it correct.")
    choice = input("Do you want to continue playing this game[y/n]: ")
    if (choice[0] == "n" or choice[0] == "N"):
        break