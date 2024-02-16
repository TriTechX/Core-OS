import time
import os
import random
import colorama
from datetime import datetime

now = datetime.now()
date_time = now.strftime("%d/%m/%Y, %H:%M:%S")


def type(text):
    for x in text:
        print(x, end="", flush=True)
        time.sleep(0.03)
    print()


def clear():
    os.system("cls" if os.name in ["nt", "dos"] else "clear")


for x in range(0, random.randint(1, 3)):
    clear()
    print(
        f"Loading {colorama.Fore.LIGHTMAGENTA_EX}'Tic Tac Toe'{colorama.Style.RESET_ALL}"
    )
    time.sleep(0.2)
    clear()
    print(
        f"Loading {colorama.Fore.LIGHTMAGENTA_EX}'Tic Tac Toe'{colorama.Style.RESET_ALL}."
    )
    time.sleep(0.2)
    clear()
    print(
        f"Loading {colorama.Fore.LIGHTMAGENTA_EX}'Tic Tac Toe'{colorama.Style.RESET_ALL}.."
    )
    time.sleep(0.2)
    clear()
    print(
        f"Loading {colorama.Fore.LIGHTMAGENTA_EX}'Tic Tac Toe'{colorama.Style.RESET_ALL}..."
    )
    time.sleep(0.2)

print(colorama.Fore.LIGHTGREEN_EX + "Complete!" + colorama.Style.RESET_ALL)
time.sleep(1)
clear()
type("Welcome to " + colorama.Fore.LIGHTCYAN_EX + "Tic Tac Toe" +
     colorama.Style.RESET_ALL + " for " + colorama.Fore.LIGHTMAGENTA_EX +
     "Core OS" + colorama.Style.RESET_ALL + "!")
try:
    while True:
        mode = ""
        validia = False
        winner = None
        board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        colour_board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        valid = False

        type("------")

        if os.path.exists("endings.log"):
            type(colorama.Fore.LIGHTCYAN_EX + "Previous" +
                 colorama.Style.RESET_ALL + " game...")
            type("------")
            f = open("endings.log", "r")
            contents = f.read()
            for character in contents:
                if character == "O":
                    print(colorama.Fore.BLUE + "O" + colorama.Style.RESET_ALL,
                          end="")
                if character == "X":
                    print(colorama.Fore.RED + "X" + colorama.Style.RESET_ALL,
                          end="")
                elif character != "O" and character != "X":
                    print(character, end="")
            print()
            print("------")
        while valid == False:

            mode = input("Which mode?\n(1) " + colorama.Fore.LIGHTGREEN_EX +
                         "2 player" + colorama.Style.RESET_ALL + "\n(2) " +
                         colorama.Fore.LIGHTMAGENTA_EX + "Vs AI?" +
                         colorama.Style.RESET_ALL + "\n>>> ")
            if mode.strip(" ") == "1" or mode.strip(" ") == "2":
                valid = True
                time.sleep(0.5)
                clear()
            else:
                valid = False
                type("Please enter '1' or '2'...")
                time.sleep(0.5)
                clear()

        def check():
            global board, won, winner, validia
            #horizontal
            if board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X":
                won = True
                winner = "X"
            elif board[1][0] == "X" and board[1][1] == "X" and board[1][
                    2] == "X":
                won = True
                winner = "X"
            elif board[2][0] == "X" and board[2][1] == "X" and board[2][
                    2] == "X":
                won = True
                winner = "X"
            #diagonal
            elif board[0][0] == "X" and board[1][1] == "X" and board[2][
                    2] == "X":
                won = True
                winner = "X"
            elif board[2][0] == "X" and board[1][1] == "X" and board[0][
                    2] == "X":
                won = True
                winner = "X"
            #vertical
            elif board[0][0] == "X" and board[1][0] == "X" and board[2][
                    0] == "X":
                won = True
                winner = "X"
            elif board[0][1] == "X" and board[1][1] == "X" and board[2][
                    1] == "X":
                won = True
                winner = "X"
            elif board[0][2] == "X" and board[1][2] == "X" and board[2][
                    2] == "X":
                won = True
                winner = "X"

            #horizontal
            elif board[0][0] == "O" and board[0][1] == "O" and board[0][
                    2] == "O":
                won = True
                winner = "O"
            elif board[1][0] == "O" and board[1][1] == "O" and board[1][
                    2] == "O":
                won = True
                winner = "O"
            elif board[2][0] == "O" and board[2][1] == "O" and board[2][
                    2] == "O":
                won = True
                winner = "O"

            #diagonal
            elif board[0][0] == "O" and board[1][1] == "O" and board[2][
                    2] == "O":
                won = True
                winner = "O"
            elif board[2][0] == "O" and board[1][1] == "O" and board[0][
                    2] == "O":
                won = True
                winner = "O"

            #vertical
            elif board[0][0] == "O" and board[1][0] == "O" and board[2][
                    0] == "O":
                won = True
                winner = "O"
            elif board[0][1] == "O" and board[1][1] == "O" and board[2][
                    1] == "O":
                won = True
                winner = "O"
            elif board[0][2] == "O" and board[1][2] == "O" and board[2][
                    2] == "O":
                won = True
                winner = "O"

            elif " " not in board[0] and " " not in board[
                    1] and " " not in board[2] and won != True:
                won = True
                winner = None
                validia = True

        def layout():
            print(f"  1   2   3  ")
            print(
                f"| {colour_board[0][0]} | {colour_board[0][1]} | {colour_board[0][2]} | 1"
            )
            print(f"| - | - | - |")
            print(
                f"| {colour_board[1][0]} | {colour_board[1][1]} | {colour_board[1][2]} | 2"
            )
            print(f"| - | - | - |")
            print(
                f"| {colour_board[2][0]} | {colour_board[2][1]} | {colour_board[2][2]} | 3"
            )

        def save_layout():
            global board

            top_layer = f"  1   2   3  "
            second_layer = f"| {board[0][0]} | {board[0][1]} | {board[0][2]} | 1"
            third_layer = f"| - | - | - |"
            fourth_layer = f"| {board[1][0]} | {board[1][1]} | {board[1][2]} | 2"
            fifth_layer = f"| - | - | - |"
            sixth_layer = f"| {board[2][0]} | {board[2][1]} | {board[2][2]} | 3"
            if os.environ["REPL_OWNER"] != "TriTech":
                f = open("endings.log", "w+")
                f.write(date_time + "\n")
                f.write(top_layer + "\n" + second_layer + "\n" + third_layer +
                        "\n" + fourth_layer + "\n" + fifth_layer + "\n" +
                        sixth_layer)
                f.close()

        def ai_O():
            global board, placement, placementChecker
            placementChecker = True
            placement = ""

            if board[0][0] == "O" and board[0][1] == "O" and board[0][2] == " ":
                placement = [0, 2]
            elif board[0][1] == "O" and board[0][2] == "O" and board[0][
                    0] == " ":
                placement = [0, 0]

            elif board[1][0] == "O" and board[1][1] == "O" and board[1][
                    2] == " ":
                placement = [1, 2]
            elif board[1][1] == "O" and board[1][2] == "O" and board[1][
                    0] == " ":
                placement = [1, 0]

            elif board[2][0] == "O" and board[2][1] == "O" and board[2][
                    2] == " ":
                placement = [2, 2]
            elif board[2][1] == "O" and board[2][2] == "O" and board[2][
                    0] == " ":
                placement = [2, 0]
            ######################
            #Blocks setups such as
            # [X, " ", X]
            ######################
            elif board[0][0] == "O" and board[0][2] == "O" and board[0][
                    1] == " ":
                placement = [0, 1]
            elif board[1][0] == "O" and board[1][2] == "O" and board[1][
                    1] == " ":
                placement = [1, 1]
            elif board[2][0] == "O" and board[2][2] == "O" and board[2][
                    1] == " ":
                placement = [2, 1]
            ######################
            #Blocks setups such as
            # [X, " ", " "]
            # ["", " ", " "]
            # [X, " ", " "]
            ######################
            elif board[0][0] == "O" and board[2][0] == "O" and board[1][
                    0] == " ":
                placement = [1, 0]
            elif board[0][1] == "O" and board[2][1] == "O" and board[1][
                    1] == " ":
                placement = [1, 1]
            elif board[0][2] == "O" and board[2][2] == "O" and board[1][
                    2] == " ":
                placement = [1, 2]
            ######################
            #Blocks setups such as
            # [X, " ", " "]
            # [" ", " ", " "]
            # [" ", " ", X]
            elif board[0][0] == "O" and board[2][2] == "O" and board[1][
                    1] == " ":
                placement = [1, 1]
            elif board[0][2] == "O" and board[2][0] == "O" and board[1][
                    1] == " ":
                placement = [1, 1]
            ######################
            #Blocks setups such as
            # [X, " ", " "]
            # [X, " ", " "]
            # [" ", " ", " "]
            ######################
            elif board[0][0] == "O" and board[1][0] == "O" and board[2][
                    0] == " ":
                placement = [2, 0]
            elif board[1][0] == "O" and board[2][0] == "O" and board[0][
                    0] == " ":
                placement = [0, 0]

            elif board[0][1] == "O" and board[1][1] == "O" and board[2][
                    1] == " ":
                placement = [2, 1]
            elif board[1][1] == "O" and board[2][1] == "O" and board[0][
                    1] == " ":
                placement = [0, 1]

            elif board[0][2] == "O" and board[1][2] == "O" and board[2][
                    2] == " ":
                placement = [2, 2]
            elif board[1][2] == "O" and board[2][2] == "O" and board[0][
                    2] == " ":
                placement = [0, 2]
            ######################
            #Blocks setups such as
            # [X , " ", " "]
            # [" ", X , " "]
            # [" ", " ", X ]
            ######################
            elif board[0][0] == "O" and board[1][1] == "O" and board[2][
                    2] == " ":
                placement = [2, 2]
            elif board[1][1] == "O" and board[2][2] == "O" and board[0][
                    0] == " ":
                placement = [0, 0]
            elif board[0][2] == "O" and board[1][1] == "O" and board[2][
                    0] == " ":
                placement = [2, 0]
            elif board[2][0] == "O" and board[1][1] == "O" and board[0][
                    2] == " ":
                placement = [0, 2]
            ######################
            #Blocks setups such as
            # [X, X, " "]
            # and
            # [" ", X, X]
            ######################
            elif board[0][0] == "X" and board[0][1] == "X" and board[0][
                    2] == " ":
                placement = [0, 2]
            elif board[0][1] == "X" and board[0][2] == "X" and board[0][
                    0] == " ":
                placement = [0, 0]

            elif board[1][0] == "X" and board[1][1] == "X" and board[1][
                    2] == " ":
                placement = [1, 2]
            elif board[1][1] == "X" and board[1][2] == "X" and board[1][
                    0] == " ":
                placement = [1, 0]

            elif board[2][0] == "X" and board[2][1] == "X" and board[2][
                    2] == " ":
                placement = [2, 2]
            elif board[2][1] == "X" and board[2][2] == "X" and board[2][
                    0] == " ":
                placement = [2, 0]
            ######################
            #Blocks setups such as
            # [X, " ", X]
            ######################
            elif board[0][0] == "X" and board[0][2] == "X" and board[0][
                    1] == " ":
                placement = [0, 1]
            elif board[1][0] == "X" and board[1][2] == "X" and board[1][
                    1] == " ":
                placement = [1, 1]
            elif board[2][0] == "X" and board[2][2] == "X" and board[2][
                    1] == " ":
                placement = [2, 1]
            ######################
            #Blocks setups such as
            # [X, " ", " "]
            # ["", " ", " "]
            # [X, " ", " "]
            ######################
            elif board[0][0] == "X" and board[2][0] == "X" and board[1][
                    0] == " ":
                placement = [1, 0]
            elif board[0][1] == "X" and board[2][1] == "X" and board[1][
                    1] == " ":
                placement = [1, 1]
            elif board[0][2] == "X" and board[2][2] == "X" and board[1][
                    2] == " ":
                placement = [1, 2]
            ######################
            #Blocks setups such as
            # [X, " ", " "]
            # [" ", " ", " "]
            # [" ", " ", X]
            elif board[0][0] == "X" and board[2][2] == "X" and board[1][
                    1] == " ":
                placement = [1, 1]
            elif board[0][2] == "X" and board[2][0] == "X" and board[1][
                    1] == " ":
                placement = [1, 1]
            ######################
            #Blocks setups such as
            # [X, " ", " "]
            # [X, " ", " "]
            # [" ", " ", " "]
            ######################
            elif board[0][0] == "X" and board[1][0] == "X" and board[2][
                    0] == " ":
                placement = [2, 0]
            elif board[1][0] == "X" and board[2][0] == "X" and board[0][
                    0] == " ":
                placement = [0, 0]

            elif board[0][1] == "X" and board[1][1] == "X" and board[2][
                    1] == " ":
                placement = [2, 1]
            elif board[1][1] == "X" and board[2][1] == "X" and board[0][
                    1] == " ":
                placement = [0, 1]

            elif board[0][2] == "X" and board[1][2] == "X" and board[2][
                    2] == " ":
                placement = [2, 2]
            elif board[1][2] == "X" and board[2][2] == "X" and board[0][
                    2] == " ":
                placement = [0, 2]
            ######################
            #Blocks setups such as
            # [X , " ", " "]
            # [" ", X , " "]
            # [" ", " ", X ]
            ######################
            elif board[0][0] == "X" and board[1][1] == "X" and board[2][
                    2] == " ":
                placement = [2, 2]
            elif board[1][1] == "X" and board[2][2] == "X" and board[0][
                    0] == " ":
                placement = [0, 0]
            elif board[0][2] == "X" and board[1][1] == "X" and board[2][
                    0] == " ":
                placement = [2, 0]
            elif board[2][0] == "X" and board[1][1] == "X" and board[0][
                    2] == " ":
                placement = [0, 2]

            else:
                temporaryChoice = random.randint(1, 3)
                if temporaryChoice == 1:
                    placement = [1, 1]
                elif temporaryChoice == 2:
                    placement = [0, 0]
                elif temporaryChoice == 3:
                    placement = [2, 2]
                else:
                    placement = [random.randint(1, 3), random.randint[1, 3]]

                while board[placement[0]][placement[1]] != " ":
                    placement = [random.randint(0, 2), random.randint(0, 2)]

        def ai_X():
            global board, placement, placementChecker
            placementChecker = True
            placement = ""
            if board[0][0] == "X" and board[0][1] == "X" and board[0][2] == " ":
                placement = [0, 2]
            elif board[0][1] == "X" and board[0][2] == "X" and board[0][
                    0] == " ":
                placement = [0, 0]

            elif board[1][0] == "X" and board[1][1] == "X" and board[1][
                    2] == " ":
                placement = [1, 2]
            elif board[1][1] == "X" and board[1][2] == "X" and board[1][
                    0] == " ":
                placement = [1, 0]

            elif board[2][0] == "X" and board[2][1] == "X" and board[2][
                    2] == " ":
                placement = [2, 2]
            elif board[2][1] == "X" and board[2][2] == "X" and board[2][
                    0] == " ":
                placement = [2, 0]
            ######################
            #Blocks setups such as
            # [X, " ", X]
            ######################
            elif board[0][0] == "X" and board[0][2] == "X" and board[0][
                    1] == " ":
                placement = [0, 1]
            elif board[1][0] == "X" and board[1][2] == "X" and board[1][
                    1] == " ":
                placement = [1, 1]
            elif board[2][0] == "X" and board[2][2] == "X" and board[2][
                    1] == " ":
                placement = [2, 1]
            ######################
            #Blocks setups such as
            # [X, " ", " "]
            # ["", " ", " "]
            # [X, " ", " "]
            ######################
            elif board[0][0] == "X" and board[2][0] == "X" and board[1][
                    0] == " ":
                placement = [1, 0]
            elif board[0][1] == "X" and board[2][1] == "X" and board[1][
                    1] == " ":
                placement = [1, 1]
            elif board[0][2] == "X" and board[2][2] == "X" and board[1][
                    2] == " ":
                placement = [1, 2]
            ######################
            #Blocks setups such as
            # [X, " ", " "]
            # [" ", " ", " "]
            # [" ", " ", X]
            elif board[0][0] == "X" and board[2][2] == "X" and board[1][
                    1] == " ":
                placement = [1, 1]
            elif board[0][2] == "X" and board[2][0] == "X" and board[1][
                    1] == " ":
                placement = [1, 1]
            ######################
            #Blocks setups such as
            # [X, " ", " "]
            # [X, " ", " "]
            # [" ", " ", " "]
            ######################
            elif board[0][0] == "X" and board[1][0] == "X" and board[2][
                    0] == " ":
                placement = [2, 0]
            elif board[1][0] == "X" and board[2][0] == "X" and board[0][
                    0] == " ":
                placement = [0, 0]

            elif board[0][1] == "X" and board[1][1] == "X" and board[2][
                    1] == " ":
                placement = [2, 1]
            elif board[1][1] == "X" and board[2][1] == "X" and board[0][
                    1] == " ":
                placement = [0, 1]

            elif board[0][2] == "X" and board[1][2] == "X" and board[2][
                    2] == " ":
                placement = [2, 2]
            elif board[1][2] == "X" and board[2][2] == "X" and board[0][
                    2] == " ":
                placement = [0, 2]
            ######################
            #Blocks setups such as
            # [X , " ", " "]
            # [" ", X , " "]
            # [" ", " ", X ]
            ######################
            elif board[0][0] == "X" and board[1][1] == "X" and board[2][
                    2] == " ":
                placement = [2, 2]
            elif board[1][1] == "X" and board[2][2] == "X" and board[0][
                    0] == " ":
                placement = [0, 0]
            elif board[0][2] == "X" and board[1][1] == "X" and board[2][
                    0] == " ":
                placement = [2, 0]
            elif board[2][0] == "X" and board[1][1] == "X" and board[0][
                    2] == " ":
                placement = [0, 2]

            ######################
            #Blocks setups such as
            # [X, X, " "]
            # and
            # [" ", X, X]
            ######################
            elif board[0][0] == "O" and board[0][1] == "O" and board[0][
                    2] == " ":
                placement = [0, 2]
            elif board[0][1] == "O" and board[0][2] == "O" and board[0][
                    0] == " ":
                placement = [0, 0]

            elif board[1][0] == "O" and board[1][1] == "O" and board[1][
                    2] == " ":
                placement = [1, 2]
            elif board[1][1] == "O" and board[1][2] == "O" and board[1][
                    0] == " ":
                placement = [1, 0]

            elif board[2][0] == "O" and board[2][1] == "O" and board[2][
                    2] == " ":
                placement = [2, 2]
            elif board[2][1] == "O" and board[2][2] == "O" and board[2][
                    0] == " ":
                placement = [2, 0]
            ######################
            #Blocks setups such as
            # [X, " ", X]
            ######################
            elif board[0][0] == "O" and board[0][2] == "O" and board[0][
                    1] == " ":
                placement = [0, 1]
            elif board[1][0] == "O" and board[1][2] == "O" and board[1][
                    1] == " ":
                placement = [0, 1]
            elif board[2][0] == "O" and board[2][2] == "O" and board[2][
                    1] == " ":
                placement = [0, 1]
            ######################
            #Blocks setups such as
            # [X, " ", " "]
            # ["", " ", " "]
            # [X, " ", " "]
            ######################
            elif board[0][0] == "O" and board[2][0] == "O" and board[1][
                    0] == " ":
                placement = [1, 0]
            elif board[0][1] == "O" and board[2][1] == "O" and board[1][
                    1] == " ":
                placement = [1, 1]
            elif board[0][2] == "O" and board[2][2] == "O" and board[1][
                    2] == " ":
                placement = [1, 2]
            ######################
            #Blocks setups such as
            # [X, " ", " "]
            # [" ", " ", " "]
            # [" ", " ", X]
            elif board[0][0] == "O" and board[2][2] == "O" and board[1][
                    1] == " ":
                placement = [1, 1]
            elif board[0][2] == "O" and board[2][0] == "O" and board[1][
                    1] == " ":
                placement = [1, 1]
            ######################
            #Blocks setups such as
            # [X, " ", " "]
            # [X, " ", " "]
            # [" ", " ", " "]
            ######################
            elif board[0][0] == "O" and board[1][0] == "O" and board[2][
                    0] == " ":
                placement = [2, 0]
            elif board[1][0] == "O" and board[2][0] == "O" and board[0][
                    0] == " ":
                placement = [0, 0]

            elif board[0][1] == "O" and board[1][1] == "O" and board[2][
                    1] == " ":
                placement = [2, 1]
            elif board[1][1] == "O" and board[2][1] == "O" and board[0][
                    1] == " ":
                placement = [0, 1]

            elif board[0][2] == "O" and board[1][2] == "O" and board[2][
                    2] == " ":
                placement = [2, 2]
            elif board[1][2] == "O" and board[2][2] == "O" and board[0][
                    2] == " ":
                placement = [0, 2]
            ######################
            #Blocks setups such as
            # [X , " ", " "]
            # [" ", X , " "]
            # [" ", " ", X ]
            ######################
            elif board[0][0] == "O" and board[1][1] == "O" and board[2][
                    2] == " ":
                placement = [2, 2]
            elif board[1][1] == "O" and board[2][2] == "O" and board[0][
                    0] == " ":
                placement = [0, 0]
            elif board[0][2] == "O" and board[1][1] == "O" and board[2][
                    0] == " ":
                placement = [2, 0]
            elif board[2][0] == "O" and board[1][1] == "O" and board[0][
                    2] == " ":
                placement = [0, 2]

            else:
                temporaryChoice = random.randint(1, 3)
                if temporaryChoice == 1:
                    placement = [1, 1]
                elif temporaryChoice == 2:
                    placement = [0, 0]
                elif temporaryChoice == 3:
                    placement = [2, 2]
                else:
                    placement = [random.randint(1, 3), random.randint[1, 3]]

                while board[placement[0]][placement[1]] != " ":
                    placement = [random.randint(0, 2), random.randint(0, 2)]

        go = 1
        valid = False
        won = False

        if mode.strip(" ") == "1":
            while won == False:
                if " " not in board[0] and " " not in board[
                        1] and " " not in board[2]:
                    break
                    validia = True
                check()
                if won == True:
                    clear()
                    break

                try:
                    if go == 1:

                        #X's go
                        valid = False
                        while valid == False:
                            go = 1
                            clear()
                            layout()
                            print()
                            columnRow = input(
                                colorama.Fore.RED + "X's go" +
                                colorama.Style.RESET_ALL +
                                " (column (or x), row (or y))\n>>> ")
                            coordinates = columnRow.split(",")
                            if len(coordinates) != 2:
                                valid = False
                            else:

                                index = -1
                                for x in coordinates:
                                    index = +1
                                    if x.strip(" ") == "":
                                        coordinates.pop(index)

                                for coordinate in coordinates:
                                    try:
                                        coordinate = int(coordinate)
                                    except:
                                        valid = False
                                        break

                                    if coordinate > 3 or coordinate < 1:
                                        valid2 = False
                                        break
                                    else:
                                        valid2 = True

                                if valid2 == True:
                                    if board[int(coordinates[1]) - 1][int(
                                            coordinates[0]
                                    ) - 1] == " " and coordinate < 4 or coordinate > 0:
                                        if board[int(coordinates[1]) -
                                                 1][int(coordinates[0]) -
                                                    1] == " ":
                                            if int(coordinates[0]) + int(
                                                    coordinates[1]
                                            ) < 7 and int(
                                                    coordinates[0]) + int(
                                                        coordinates[1]) > 1:
                                                valid = True
                                else:
                                    valid = False
                                    type("Please enter a valid coordinate.")
                                    input(colorama.Fore.LIGHTBLACK_EX +
                                          "[ENTER] to continue..." +
                                          colorama.Style.RESET_ALL)

                                if valid == True:
                                    break

                        if valid == True:
                            board[int(coordinates[1]) -
                                  1][int(coordinates[0]) - 1] = "X"
                            colour_board[int(coordinates[1]) - 1][
                                int(coordinates[0]) -
                                1] = colorama.Fore.RED + "X" + colorama.Style.RESET_ALL
                            layout()
                            go = go + 1
                        elif valid == False:
                            type("Please enter a valid coordinate.")
                            input(colorama.Fore.LIGHTBLACK_EX +
                                  "[ENTER] to continue..." +
                                  colorama.Style.RESET_ALL)
                        print()

                    check()
                    if won == True:
                        clear()
                        break

                    if go == 2:
                        #O's go
                        valid = False
                        while valid == False:
                            go = 2
                            clear()
                            layout()
                            print()
                            columnRow = input(
                                colorama.Fore.BLUE + "O's go  " +
                                colorama.Style.RESET_ALL +
                                "(column (or x), row (or y))\n>>> ")
                            coordinates = columnRow.split(",")
                            if len(coordinates) != 2:
                                valid = False
                            else:

                                index = -1
                                for x in coordinates:
                                    index = +1
                                    if x.strip(" ") == "":
                                        coordinates.pop(index)

                                for coordinate in coordinates:
                                    try:
                                        coordinate = int(coordinate)
                                    except:
                                        valid = False
                                        break

                                    if coordinate > 3 or coordinate < 1:
                                        valid2 = False
                                        break
                                    else:
                                        valid2 = True

                                if valid2 == True:
                                    if board[int(coordinates[1]) - 1][int(
                                            coordinates[0]
                                    ) - 1] == " " and coordinate < 4 or coordinate > 0:
                                        if board[int(coordinates[1]) -
                                                 1][int(coordinates[0]) -
                                                    1] == " ":
                                            if int(coordinates[0]) + int(
                                                    coordinates[1]
                                            ) < 7 and int(
                                                    coordinates[0]) + int(
                                                        coordinates[1]) > 1:
                                                valid = True
                                else:
                                    valid = False
                                    type("Please enter a valid coordinate.")
                                    input(colorama.Fore.LIGHTBLACK_EX +
                                          "[ENTER] to continue..." +
                                          colorama.Style.RESET_ALL)

                                if valid == True:
                                    break

                        if valid == True:
                            board[int(coordinates[1]) -
                                  1][int(coordinates[0]) - 1] = "O"
                            colour_board[int(coordinates[1]) - 1][
                                int(coordinates[0]) -
                                1] = colorama.Fore.BLUE + "O" + colorama.Style.RESET_ALL
                            layout()
                            go = go - 1
                        elif valid == False:
                            type("Please enter a valid coordinate.")
                            input(colorama.Fore.LIGHTBLACK_EX +
                                  "[ENTER] to continue..." +
                                  colorama.Style.RESET_ALL)
                            go = 2
                        print()
                except IndexError:
                    type("Please follow the formatting stated.")
                    input(colorama.Fore.LIGHTBLACK_EX +
                          "[ENTER] to continue..." + colorama.Style.RESET_ALL)
                except ValueError:
                    type("Please use an integer input.")
                    input(colorama.Fore.LIGHTBLACK_EX +
                          "[ENTER] to continue..." + colorama.Style.RESET_ALL)
            if winner != None:
                layout()
                save_layout()
                print()
                type(f"{winner} wins!")
                type("------")
                input(colorama.Fore.LIGHTBLACK_EX + "[ENTER] to continue..." +
                      colorama.Style.RESET_ALL)
                clear()
            elif validia != True:
                layout()
                save_layout()
                print()
                type("No-one won.")
                type("------")
                input(colorama.Fore.LIGHTBLACK_EX + "[ENTER] to continue..." +
                      colorama.Style.RESET_ALL)
                clear()
            elif validia == True:
                layout()
                save_layout()
                print()
                type("The board filled up!")
                type("Stalemate.")
                type("------")
                input(colorama.Fore.LIGHTBLACK_EX + "[ENTER] to continue..." +
                      colorama.Style.RESET_ALL)
                clear()

        elif mode.strip(" ") == "2":

            valid = False
            while valid == False:

                version = input("Which type?\n(1) " + colorama.Fore.RED + "X" +
                                colorama.Style.RESET_ALL + "\n(2) " +
                                colorama.Fore.BLUE + "O" +
                                colorama.Style.RESET_ALL + "\n>>> ")
                if version.strip(" ") == "1" or version.strip(" ") == "2":
                    valid = True
                    time.sleep(0.5)
                    clear()
                else:
                    valid = False
                    type("Please enter '1' or '2'...")
                    time.sleep(0.5)
                    clear()

                hardMode = input("Which difficulty?\n(1) " +
                                 colorama.Fore.RED + "Hard" +
                                 colorama.Style.RESET_ALL + "\n(2) " +
                                 colorama.Fore.BLUE + "Easy?" +
                                 colorama.Style.RESET_ALL + "\n>>> ")

                if hardMode.strip(" ") == "1" or hardMode.strip(" ") == "2":
                    valid = True
                    if hardMode == "1":
                        hardMode = True
                    else:
                        hardMode = False
                    time.sleep(0.5)
                    clear()
                else:
                    valid = False
                    type("Please enter '1' or '2'...")
                    time.sleep(0.5)
                    clear()

            if version.strip(" ") == "1":
                while won == False:
                    if " " not in board[0] and " " not in board[
                            1] and " " not in board[2]:
                        break
                        validia = True
                    check()
                    if won == True:
                        clear()
                        break

                    try:
                        if go == 1:

                            #X's go
                            valid = False
                            while valid == False:
                                go = 1
                                clear()
                                layout()
                                print()
                                columnRow = input(
                                    colorama.Fore.RED + "X's go" +
                                    colorama.Style.RESET_ALL +
                                    " (column (or x), row (or y))\n>>> ")
                                coordinates = columnRow.split(",")
                                if len(coordinates) != 2:
                                    valid = False
                                else:

                                    index = -1
                                    for x in coordinates:
                                        index = +1
                                        if x.strip(" ") == "":
                                            coordinates.pop(index)

                                    for coordinate in coordinates:
                                        try:
                                            coordinate = int(coordinate)
                                        except:
                                            valid = False
                                            break

                                        if coordinate > 3 or coordinate < 1:
                                            valid2 = False
                                            break
                                        else:
                                            valid2 = True

                                    if valid2 == True:
                                        if board[int(coordinates[1]) - 1][int(
                                                coordinates[0]
                                        ) - 1] == " " and coordinate < 4 or coordinate > 0:
                                            if board[int(coordinates[1]) -
                                                     1][int(coordinates[0]) -
                                                        1] == " ":
                                                if int(coordinates[0]) + int(
                                                        coordinates[1]
                                                ) < 7 and int(
                                                        coordinates[0]
                                                ) + int(coordinates[1]) > 1:
                                                    valid = True
                                    else:
                                        valid = False
                                        type(
                                            "Please enter a valid coordinate.")
                                        input(colorama.Fore.LIGHTBLACK_EX +
                                              "[ENTER] to continue..." +
                                              colorama.Style.RESET_ALL)

                                    if valid == True:
                                        break

                            if valid == True:
                                board[int(coordinates[1]) -
                                      1][int(coordinates[0]) - 1] = "X"
                                colour_board[int(coordinates[1]) - 1][
                                    int(coordinates[0]) -
                                    1] = colorama.Fore.RED + "X" + colorama.Style.RESET_ALL
                                layout()
                                go = go + 1
                            elif valid == False:
                                type("Please enter a valid coordinate.")
                                input(colorama.Fore.LIGHTBLACK_EX +
                                      "[ENTER] to continue..." +
                                      colorama.Style.RESET_ALL)
                            print()

                        check()
                        if won == True:
                            clear()
                            break

                        #AI CODE#
                        if go == 2:
                            coordinates = []
                            coordinates = [
                                random.randint(0, 2),
                                random.randint(0, 2)
                            ]

                            if hardMode == False:
                                while board[coordinates[1]][
                                        coordinates[0]] != " ":
                                    coordinates = [
                                        random.randint(0, 2),
                                        random.randint(0, 2)
                                    ]
                            elif hardMode == True:
                                ai_O()
                                coordinates = placement

                            board[int(coordinates[0])][int(
                                coordinates[1])] = "O"
                            colour_board[int(coordinates[0])][int(
                                coordinates[1]
                            )] = colorama.Fore.BLUE + "O" + colorama.Style.RESET_ALL
                            clear()
                            layout()
                            go = 1
                        #AI CODE#
                    except IndexError:
                        type("Please follow the formatting stated.")
                        input(colorama.Fore.LIGHTBLACK_EX +
                              "[ENTER] to continue..." +
                              colorama.Style.RESET_ALL)
                    except ValueError:
                        type("Please use an integer input.")
                        input(colorama.Fore.LIGHTBLACK_EX +
                              "[ENTER] to continue..." +
                              colorama.Style.RESET_ALL)

                if winner != None:
                    layout()
                    save_layout()
                    print()
                    type(f"{winner} wins!")
                    type("------")
                    input(colorama.Fore.LIGHTBLACK_EX +
                          "[ENTER] to continue..." + colorama.Style.RESET_ALL)
                    clear()
                elif validia != True:
                    layout()
                    save_layout()
                    print()
                    type("No-one won.")
                    type("------")
                    input(colorama.Fore.LIGHTBLACK_EX +
                          "[ENTER] to continue..." + colorama.Style.RESET_ALL)
                    clear()
                elif validia == True:
                    layout()
                    save_layout()
                    print()
                    type("The board filled up!")
                    type("Stalemate.")
                    type("------")
                    input(colorama.Fore.LIGHTBLACK_EX +
                          "[ENTER] to continue..." + colorama.Style.RESET_ALL)
                    clear()

            elif version.strip(" ") == "2":
                while won == False:
                    layout()
                    try:
                        check()
                        if won == True:
                            clear()
                            break

                        if go == 1:
                            coordinates = []
                            coordinates = [
                                random.randint(0, 2),
                                random.randint(0, 2)
                            ]
                            if hardMode == False:
                                while board[coordinates[1]][
                                        coordinates[0]] != " ":
                                    coordinates = [
                                        random.randint(0, 2),
                                        random.randint(0, 2)
                                    ]
                            elif hardMode == True:
                                ai_X()
                                coordinates = placement
                            board[int(coordinates[0])][int(
                                coordinates[1])] = "X"
                            colour_board[int(coordinates[0])][int(
                                coordinates[1]
                            )] = colorama.Fore.RED + "X" + colorama.Style.RESET_ALL

                            clear()
                            layout()
                            go = 2

                        check()
                        if won == True:
                            clear()
                            break

                        if go == 2:

                            valid = False
                            while valid == False:
                                go = 2
                                clear()
                                layout()
                                print()
                                columnRow = input(
                                    colorama.Fore.BLUE + "O's go" +
                                    colorama.Style.RESET_ALL +
                                    " (column (or x), row (or y))\n>>> ")
                                coordinates = columnRow.split(",")
                                if len(coordinates) != 2:
                                    valid = False
                                else:

                                    index = -1
                                    for x in coordinates:
                                        index = +1
                                        if x.strip(" ") == "":
                                            coordinates.pop(index)

                                    for coordinate in coordinates:
                                        try:
                                            coordinate = int(coordinate)
                                        except:
                                            valid = False
                                            break

                                        if coordinate > 3 or coordinate < 1:
                                            valid2 = False
                                            break
                                        else:
                                            valid2 = True

                                    if valid2 == True:
                                        if board[int(coordinates[1]) - 1][int(
                                                coordinates[0]
                                        ) - 1] == " " and coordinate < 4 or coordinate > 0:
                                            if board[int(coordinates[1]) -
                                                     1][int(coordinates[0]) -
                                                        1] == " ":
                                                if int(coordinates[0]) + int(
                                                        coordinates[1]
                                                ) < 7 and int(
                                                        coordinates[0]
                                                ) + int(coordinates[1]) > 1:
                                                    valid = True
                                    else:
                                        valid = False
                                        type(
                                            "Please enter a valid coordinate.")
                                        input(colorama.Fore.LIGHTBLACK_EX +
                                              "[ENTER] to continue..." +
                                              colorama.Style.RESET_ALL)

                                    if valid == True:
                                        break

                            if valid == True:
                                board[int(coordinates[1]) -
                                      1][int(coordinates[0]) - 1] = "O"
                                colour_board[int(coordinates[1]) - 1][
                                    int(coordinates[0]) -
                                    1] = colorama.Fore.BLUE + "O" + colorama.Style.RESET_ALL
                                layout()
                                go = 1
                            elif valid == False:
                                type("Please enter a valid coordinate.")
                                input(colorama.Fore.LIGHTBLACK_EX +
                                      "[ENTER] to continue..." +
                                      colorama.Style.RESET_ALL)
                            print()

                        check()
                        if won == True:
                            clear()
                            break

                    except IndexError:
                        type("Please follow the formatting stated.")
                        input(colorama.Fore.LIGHTBLACK_EX +
                              "[ENTER] to continue..." +
                              colorama.Style.RESET_ALL)
                    except ValueError:
                        type("Please use an integer input.")
                        input(colorama.Fore.LIGHTBLACK_EX +
                              "[ENTER] to continue..." +
                              colorama.Style.RESET_ALL)

                if winner != None:
                    layout()
                    save_layout()
                    print()
                    type(f"{winner} wins!")
                    type("------")
                    input(colorama.Fore.LIGHTBLACK_EX +
                          "[ENTER] to continue..." + colorama.Style.RESET_ALL)
                    clear()
                elif validia != True:
                    layout()
                    save_layout()
                    print()
                    type("No-one won.")
                    type("------")
                    input(colorama.Fore.LIGHTBLACK_EX +
                          "[ENTER] to continue..." + colorama.Style.RESET_ALL)
                    clear()
                elif validia == True:
                    layout()
                    save_layout()
                    print()
                    type("The board filled up!")
                    type("Stalemate.")
                    type("------")
                    input(colorama.Fore.LIGHTBLACK_EX +
                          "[ENTER] to continue..." + colorama.Style.RESET_ALL)
                    clear()
        #end
except KeyboardInterrupt:
    print()
    print("------")
    type("Exiting...")
