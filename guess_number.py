import random


def number():
    num1 = int(input("Enter a number to start between "))
    num2 = int(input("Enter a second number "))
    num_range = random.randint(num1, num2)
    print(f"Then number you have choosen is between {num1} - {num2}")
    play_game(int(num_range))

def play_game(num_range):
    guesses = True
    print(num_range)
    guess = input('Please choose a number: ')
    while guesses:
        if guess > str(num_range):
            print("Your number is too high")
            guess = input('Please choose a number: ')
        elif guess < str(num_range):
            print("Your number is too low ")
            guess = input('Please choose a number: ')
        else:
            guesses == False
    print('hello')





#Interactive Loop
while True:
    play = input("p to play / q to quit ")
    if play == 'p':
        number()
    elif play == 'q':
        False
    else:
        print("Pleas enter p or q")


