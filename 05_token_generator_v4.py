import random
# main routine goes here

tokens = ["unicorn", "horse", "horse", "horse", "zebra", "zebra", "zebra", "donkey", "donkey", "donkey", "donkey"]
START_BALANCE = 100
# START_BALANCE is a constant, which sets a value that does not change throughout the program
balance = START_BALANCE
# testing loop to generate 20 tokens
for item in range(0, 10):
    chosen_num = random.randint(1, 100)

    # Adjust balance
    if 1 <= chosen_num <= 5:
        chosen = "unicorn"
        balance += 4
    elif 6 <= chosen_num <= 36:
        chosen = "donkey"
        balance -= 1
    else:
        if chosen_num % 2 == 0:
            # % finds the remainder when the number is divided.
            # if the number divided by 2 and the remainder is 0, the number is even
            chosen = "zebra"
        else:
            chosen = "horse"
        balance -= 0.5

    # output
    print("You got a {}. Your balance is ${:.2f}".format(chosen, balance))

# :.2f = numbers with 2 decimal places at the end
print()
print("Starting Balance: ${:.2f}".format(START_BALANCE))
print("Final Balance: ${:.2f}".format(balance))
