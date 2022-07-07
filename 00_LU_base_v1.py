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
    print()
    statement_generator("How to Play", "*")
    print()
    print("Choose a starting amount (minimum $1, maximum $10).")
    print()
    print("Then press <enter> to play. You will get either a horse, a zebra, a donkey or a unicorn.")
    print()
    print("It costs a $1 per round. Depending on your prize you might win some money back. Here's the payout amounts...")
    print("Unicorn: balance increases by $4")
    print("Horse: balance decreases by $0.50")
    print("Zebra: balance decreases by $0.50")
    print("Donkey: balance decreases by $1")
    return ""


def num_check(question, low, high):
    error = "Please enter an integer between 1 and 10\n"
    error_msg = "This is not an integer!!\n"
    # \n give line break
    valid = False
    while not valid:
        # ask the question
        try:
            response = int(input(question))
            if low < response <= high:
                return response
            # output an error if the number is not appropriate.
            else:
                print(error)

        except ValueError:
            print(error_msg)
        # if the amount is appropriate


def statement_generator(statement, decoration):

    sides = decoration * 3

    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""


# Main Routine...
statement_generator("Welcome to the Lucky Unicorn Game", "*")
print()

show_instructions = yes_no("Have you played this game before? ")

if show_instructions == "no" or show_instructions == "n":
    print(instructions())

print("Can you avoid the donkeys, get the unicorns and walk home with the money? ")

statement_generator("Let's get Started", "-")

how_much = num_check("How much would you like to play with? ", 0, 10)

# print() for blank line, extra spacing

balance = how_much

rounds_played = 0

play_again = input("Press <Enter> to play").lower()
while play_again == "":

    # increase num of rounds played
    rounds_played += 1

    # print round number
    print()
    statement_generator("Round #{}".format(rounds_played), "·")

    chosen_num = random.randint(1, 100)

    # Adjust balance
    # if the random num is between 1 and 5,
    # user gets a unicorn (add $4 to balance)
    if 1 <= chosen_num <= 5:
        chosen = "unicorn"
        prize_decoration = "!"
        balance += 4
    # if the random num is between 6 and 36,
    # user gets a donkey (subtract $1 from balance)
    elif 6 <= chosen_num <= 36:
        chosen = "donkey"
        balance -= 1
        prize_decoration = "D"
    # the token is either a horse or zebra
    # subtract $0.5 from balance
    else:
        # if the number is even, set the chosen item to a zebra
        if chosen_num % 2 == 0:
            # % finds the remainder when the number is divided.
            # if the number divided by 2 and the remainder is 0, the number is even
            chosen = "zebra"
            prize_decoration = "Z"
        # otherwise set it to a zebra
        else:
            chosen = "horse"
            print()
            prize_decoration = "H"
        balance -= 0.5
    # output
    outcome = "You got a {}. Your balance is ${:.2f}".format(chosen, balance)
    statement_generator(outcome, prize_decoration)
    # :.2f = numbers with 2 decimal places at the end (2 floats)

    if balance < 1:
        play_again = "xxx"
        print("Sorry you have run out of money")
    else:
        play_again = input("Press Enter to play again or 'xxx' to quit")

print()
statement_generator("Results", "=")
print("Final balance: $", balance)
print("Thank your for playing:))")
