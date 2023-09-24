# To make collect a user input as a start
# For this project, we need the user's deposit and their bet as well
# Ctrl + F5
import random

MAXLINES = 3  # Constent variable all in capital
MAXBET = 100
MINBET = 1

ROWS = 3
COLS = 3

symbolCount = {
    "A": 2,
    "B": 3,
    "C": 4,
    "D": 1
}

symbolValue = {
    "A": 4,
    "B": 3,
    "C": 2,
    "D": 5
}


# A little confusing part, read as many times as necessary
# This is how we generate our itmes that gonna be in the machine

# Pick the row for each col
def getSlotSpin(rows, cols, symbols):
    # Create a full symbol list that we could select, and we choose 3 of them randomly
    allSymbols = []
    # Add all the symbols to the list
    for keys, values in symbolCount.items():
        for _ in range(values):   # so we don't have unused value
            allSymbols.append(keys)

    # Decide symbol in each col
    columns = []
    # We have three cols
    for _ in range(cols):
        column = []
        # Make a copy so we don't change the initial one
        currentSymbol = allSymbols[:]
        # We have three rows
        for _ in range(rows):
            # Pick a symbol from symbol list
            value = random.choice(currentSymbol)
            currentSymbol.remove(value)
            column.append(value)

        columns.append(column)
    return columns

# Formate our machine result

# This is confusing too


def printSlot(columns):
    # Spin our matrix and make the metrix presents by rows
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row])
        # A print() statement brings us down to the next line
        # Incrase line spacing
        print()

# Read deposit


def deposit():
    while True:  # a while loop with no restriction that will have an input
        amount = input("Please enter your deposit: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a solid number.")
    return amount


def getNumberOfLines():
    while True:  # a while loop with no restriction that will have an input
        lines = input(
            "Please enter the number of lines to bet on (1-" + str(MAXLINES) + "): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAXLINES:
                break
            else:
                print("Amount must be greater than 1 and smaller than 3.")
        else:
            print("Please enter a solid number.")
    return lines


# The amount I want to bet on each line


def getBet():
    while True:
        amount = input("Please enter your bet on each line: $")
        if amount.isdigit():
            amount = int(amount)
            if MINBET <= amount <= MAXBET:
                break
            else:
                print(f"Amount must be between ${MINBET} - ${MAXBET}.")
        else:
            print("Please enter a solid number.")
    return amount


def checkWinning(columns, lines, bet, values):
    winnings = 0
    winningsLines = []
    # Looping through every row
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbolCheck = column[line]
            if symbol != symbolCheck:
                break
        else:
            winnings += values[symbol] * bet
            winningsLines.append(lines + 1)
    return winnings, winningsLines


def main():
    balance = deposit()
    lines = getNumberOfLines()
    while True:
        bet = getBet()
        totalBet = bet * lines

        if totalBet > balance:
            print(
                f"Sorry, you do not have enough money to bet that amount, your current balance is ${balance}.")
        else:
            break
    # Main function
    print(
        f"You are betting ${bet} on {lines}.\n Total bet is equal to: ${totalBet}.")

    slots = getSlotSpin(ROWS, COLS, symbolCount)
    printSlot(slots)

    winnings, winningsLines = checkWinning(slots, lines, bet, symbolValue)
    print(f"You won ${winnings}.\nYou won on lines:", *winningsLines)


main()


# If you bet on one line, you just bet on top line
# If two, bet on top and middle
# If three, all lines
