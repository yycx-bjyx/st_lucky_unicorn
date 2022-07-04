import random
# main routine goes here

tokens = ["unicorn", "horse", "horse", "horse", "zebra", "zebra", "zebra", "donkey", "donkey", "donkey", "donkey"]
START_BALANCE = 100
# START_BALANCE is a constant, which sets a value that does not change throughout the program
balance = START_BALANCE
# testing loop to generate 20 tokens
for item in range(0, 500):
    chosen = random.choice(tokens)

    # Adjust balance
    if chosen == "unicorn":
        balance += 4
    elif chosen == "donkey":
        balance -= 1
    else:
        balance -= 0.5

    # output

print()
print("Starting balance: ${:.2f}".format(START_BALANCE))
print("Final balance: ${:.2f}".format(balance))
# :.2f = numbers with 2 decimal places at the end
