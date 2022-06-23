# Functions
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
            print("please answer yes / no")


def instructions():
    print("*** How to Play***")
    print()
    print("The rules of the game go here")
    print()
    return ""
# Main Routine...


show_instructions = yes_no("Have you played this game before")

if show_instructions == "no" or show_instructions == "n":
    show_instructions = "no"
    print(instructions())
else:
    print("program continues")

# for blank line, extra spacing
having_fun = yes_no("are you having fun?")
print("you said {} to having fun".format(having_fun))
