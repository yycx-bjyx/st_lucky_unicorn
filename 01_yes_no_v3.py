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
# Main Routine...


instructions = yes_no("Have you played this game before")

print("you chose {}".format(instructions))
print()
# for blank line, extra spacing
having_fun = yes_no("are you having fun?")
print("you said {} to having fun".format(having_fun))
