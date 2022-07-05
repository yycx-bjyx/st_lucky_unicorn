# Functions
import random


def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()
        # .lower() at the end of statement input indicates that the variable is being put as a lower case, and is not case-sensitive
        if response == "yes" or response == "y":
            response = "yes"
            return response
        elif response == "no" or response == "n":
            response = "no"
            return response
        else:
            print("Please answer yes / no")


def instructions():
    print("*** How to Play***")
    print()
    print("The rules of the game go here")
    print()
    return ""


def num_check(question, low, high, answer):
    error = "Please enter an integer between 1 and 10\n"
    error_msg = "This is not an integer!!"
    # \n give line break
    valid = False
    while not valid:
        # ask the question
        try:
            response = int(input(question))
            if low < response <= high:
                print(answer.format(response))
                return response
            # output an error if the number is not appropriate.
            else:
                print(error)

        except ValueError:
            print(error_msg)
        # if the amount is appropriate

# Main Routine...


show_instructions = yes_no("Have you played this game before")

if show_instructions == "no" or show_instructions == "n":
    print(instructions())

how_much = num_check("How much would you like to play with? ", 0, 10, "You wil be spending ${}")

# print() for blank line, extra spacing

balance = how_much

rounds_played = 0

play_again = input("Press <Enter> to play").lower()
while play_again == "":

    # increase num of rounds played
    rounds_played += 1

    # print round number
    print()
    print("*** Round #{} ***".format(rounds_played))

    chosen_num = random.randint(1, 100)

    # Adjust balance
    # if the random num is between 1 and 5,
    # user gets a unicorn (add $4 to balance)
    if 1 <= chosen_num <= 5:
        chosen = "unicorn"
        balance += 4
    # if the random num is between 6 and 36,
    # user gets a donkey (subtract $1 from balance)
    elif 6 <= chosen_num <= 36:
        chosen = "donkey"
        balance -= 1
    # the token is either a horse or zebra
    # subtract $0.5 from balance
    else:
        # if the number is even, set the chosen item to a zebra
        if chosen_num % 2 == 0:
            # % finds the remainder when the number is divided.
            # if the number divided by 2 and the remainder is 0, the number is even
            chosen = "zebra"
        # otherwise set it to a zebra
        else:
            chosen = "horse"
        balance -= 0.5
    # output
    print("You got a {}. Your balance is ${:.2f}".format(chosen, balance))
    # :.2f = numbers with 2 decimal places at the end (2 floats)

    if balance < 1:
        play_again = "xxx"
        print("Sorry you have run out of money")
    else:
        play_again = input("Press Enter to play again or 'xxx' to quit")

print()
print("Final balance", balance)
