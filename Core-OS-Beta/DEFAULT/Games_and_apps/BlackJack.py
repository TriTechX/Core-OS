
pinventory = []
P1Inventory = []
P2Inventory = []

cards = ["""
┌──── ─────┐
│1░░░░░░░░│
│░░░░░░░░░│
│░░░░1░░░░│
│░░░░░░░░░│
│░░░░░░░░1│
└─────────┘""",
                """
┌─────────┐
│2░░░░░░░░│
│░░░░░░░░░│
│░░░░2░░░░│
│░░░░░░░░░│
│░░░░░░░░2│
└─────────┘""",
                """
┌─────────┐
│3░░░░░░░░│
│░░░░░░░░░│
│░░░░3░░░░│
│░░░░░░░░░│
│░░░░░░░░3│
└─────────┘""",
                """
┌─────────┐
│4░░░░░░░░│
│░░░░░░░░░│
│░░░░4░░░░│
│░░░░░░░░░│
│░░░░░░░░4│
└─────────┘""",
                """
┌─────────┐
│5░░░░░░░░│
│░░░░░░░░░│
│░░░░5░░░░│
│░░░░░░░░░│
│░░░░░░░░5│
└─────────┘""",
                """
┌─────────┐
│6░░░░░░░░│
│░░░░░░░░░│
│░░░░6░░░░│
│░░░░░░░░░│
│░░░░░░░░6│
└─────────┘""",
                """
┌─────────┐
│7░░░░░░░░│
│░░░░░░░░░│
│░░░░7░░░░│
│░░░░░░░░░│
│░░░░░░░░7│
└─────────┘""",
                """
┌─────────┐
│8░░░░░░░░│
│░░░░░░░░░│
│░░░░8░░░░│
│░░░░░░░░░│
│░░░░░░░░8│
└─────────┘""",
"""
┌─────────┐
│9░░░░░░░░│
│░░░░░░░░░│
│░░░░9░░░░│
│░░░░░░░░░│
│░░░░░░░░9│
└─────────┘""",
                 """
┌─────────┐
│10░░░░░░░│
│░░░░░░░░░│
│░░░1░0░░░│
│░░░░░░░░░│
│░░░░░░░10│
└─────────┘""",
                 """
┌─────────┐
│1░░░░░░░░│
│░░░░░░░░░│
│░░░░1░░░░│
│░░░░░░░░░│
│░░░░░░░░1│
└─────────┘"""]


import time 
import colorama
import numpy as np
import random
import os
os.system("clear")
placv = "null"
TP1Cv = "null"
P2Cv = "null"
player = os.environ.get('REPL_OWNER')
wins = 0
losses = 0
draws = 0
playercardvals = []
player1cardvals = []
player2cardvals = []
aicardvals = []
f2 = open("wins.txt", "w")
bfb = open("balancer.txt", "r")
balancefb = bfb.read()
starter = int(balancefb)
bfb.close()

money = starter
if money == 0: 
    money = 100
s = os.path.getsize("wins.txt")
if s == 0:
    f2 = open("wins.txt", "w")
mode = 0
names = ["Dave", "Ben", "Lewis", "Cameron", "Theresa", "Johnson", "Jeff", "Matilda", "Fraser", "Jimmy", "Bob", "Kim", "Karl", "Darren", "Guy", "John", "Kevin", "Liam", "Oliver", "Olivia", "Emma", "Charlotte", "Amelia", "Charlie", "Charles", "Blake", "Joe", "Jon", "Jack", "Jemma", "Jermima", "Elijah", "Elliot", "Mayonnaise", "Helicopter", "Twitch", "Arse", "Kim Jong Un", "Donald Trump", "You", "Chris Wooller", "Rocky", "Jibbert", "Boris", "Kier Starmer", "Scott", "Scotty", "Michael", "The Twitter Bird", "Lorraine", "Kelly", "Lorraine Kelly", "Davina", "Devida", "McCall", "Davina McCall", "Nuts", "Square", "Table", "Shaun", "Sean", "Shaun Connery", "Callum", "Benjamin", "Josh", "Bell", "Jess", "Izzy", "Isabelle", "Jeffery", "Geoff", "Geoffery", "Lorraine Kelly", "Nons", "Gary Glitter", "Toby Maguire", "Tom Holland", "Social Credit Guy" , "Triangle", "Pea", "Blob", "3D Square", "Dining Table", "Office Chair", "Kelly", "Lorraine", "Lorraine", "Kelly", "Democracy", "Nigel", "Farage", "Nigel Farage TORY", "Brexit", "Brexit Means Brexit", "Kirby", "Mario", "Sonic", "Samus", "Link", "Zelda", "TikTok", "Tie", "Ashley", "Hello", "Anorexia", "Eat", "Clap", "Meals", "Windows", "2D Rectangle",  "Africa", "Jesus", "Jib Jib", "Far far away", "Star Wars", "Steven Spielburg", "God", "Theodore", "Name", "Surname", "Epic Chad Gamer", "Gigachad", "Lesser Chad", "Money", "Brexit MEANS Brexit", "Fudge", "What", "The", "Fudge", "NT", "Spacebar", "Clickety Clack", "File", "Nicely", "Formatted", "Code", "Floor", "Piano", "Cable", "GOD OF THE UNIVERSE", "Thanos", "Iron Man", "Thor", "Trees", "Tree", "Windows 8 Is Bad", "Windows 11 Is Also Bad", "Nigel Farage Hates Foreigners", "Astelea", "Osu!", "Poggers", "Peppy", "RobTop Games", "RubRub", ]


dealer = random.choice(names)
ai = random.choice(names)

##################################
def typebrainbow(text, nl):
    color = 0

    for char in text:
        color = color + 1
        if color > 7:
            color = 1
        if color == 1:
            color1 = colorama.Fore.RED
        if color == 2:
            color1 = "\033[33m"
        if color == 3:
            color1 = colorama.Fore.LIGHTYELLOW_EX
        if color == 4:
            color1 = colorama.Fore.LIGHTGREEN_EX
        if color == 5:
            color1 = colorama.Fore.LIGHTCYAN_EX
        if color == 6:
            color1 = colorama.Fore.BLUE
        if color == 7:
            color1 = colorama.Fore.LIGHTMAGENTA_EX
        print(color1, end="")
        print(char, end="", flush = True)
        time.sleep(0)
#######################################################
def typeb(text, color, nl):
    if color != None:
        print(color, end = "")

    for char in text:
        print(char, end="", flush = True)
        time.sleep(0.03)
    print(colorama.Style.RESET_ALL)

    if nl == True:
        print()
    else:
        None
###################################################

typebrainbow('''
██████╗░██╗░░░░░░█████╗░░█████╗░██╗░░██╗  
██╔══██╗██║░░░░░██╔══██╗██╔══██╗██║░██╔╝  
██████╦╝██║░░░░░███████║██║░░╚═╝█████═╝░  
██╔══██╗██║░░░░░██╔══██║██║░░██╗██╔═██╗░  
██████╦╝███████╗██║░░██║╚█████╔╝██║░╚██╗  
╚═════╝░╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝  

░░░░░██╗░█████╗░░█████╗░██╗░░██╗
░░░░░██║██╔══██╗██╔══██╗██║░██╔╝
░░░░░██║███████║██║░░╚═╝█████═╝░
██╗░░██║██╔══██║██║░░██╗██╔═██╗░
╚█████╔╝██║░░██║╚█████╔╝██║░╚██╗
░╚════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝''', True)

print("   Redux\n")
typeb("Please answer with NUMBERS ONLY - (1/2 for stand/hit, any number for bets.)", colorama.Fore.LIGHTRED_EX, True)
time.sleep(0.7)
typeb("By Xytrophico", colorama.Fore.LIGHTCYAN_EX, True)
typeb("Press [ENTER] to start\n", colorama.Fore.LIGHTBLACK_EX, False)
print(colorama.Fore.LIGHTBLACK_EX, end = "", flush = True)
null = input(">>> ")
os.system("clear")
time.sleep(1)
typeb("Starting game...", None, False)
time.sleep(1)
os.system("clear")
wins = 0
print(colorama.Style.RESET_ALL, end = "", flush = True)
print("What mode would you like to play?")
print("(1) - 1P")
print("(2) - 2P")
mode = "null"
print(colorama.Fore.LIGHTBLACK_EX, end = "", flush = True)
while mode != "1" or mode != "2":
    mode = input(">>> ")
    if mode == "1" or mode == "2":
        break
if mode == "1":
    aic = "null"
    plac = "null"
    os.system("clear")
    while True:
        try:

            print("--------------------------")

            dealer = random.choice(names)
            ai = random.choice(names)
            typeb("The dealer: " + dealer, colorama.Fore.LIGHTGREEN_EX, False)
            typeb("The competition: " + ai, colorama.Fore.RED, False)
            print("----")
            typeb("Current money: £" + str(money), colorama.Fore.LIGHTYELLOW_EX, False)


            print("--------------------------")


            typeb(dealer + ": 'Here are your cards.'", colorama.Fore.LIGHTCYAN_EX, True)
            ptotal = 0
            atotal = 0
            playertwist = True
            turn = "player"


            pvalue = random.randint(1, 11)

            if pvalue != 11 and pvalue != 1:
                playercardvals.append(pvalue) 
                ptotal = ptotal + pvalue
                typeb(player + " ~ Recieved one card\n Value: " + str(pvalue), colorama.Fore.LIGHTGREEN_EX, False)
                print(colorama.Style.RESET_ALL)

                print(cards[pvalue - 1])
                pinventory.append(cards[pvalue - 1])
                print()
                typeb("Current total: " + str(ptotal), colorama.Fore.LIGHTGREEN_EX, True)
                turn = "ai"
            else:
                typeb(player + " ~ Recieved one card\n", colorama.Fore.LIGHTGREEN_EX, False)
                print(colorama.Style.RESET_ALL, end = "", flush = True)
                print(cards[pvalue - 1])
                print()

                while placv != "1" or placv != "2":
                    typeb("*It's an ace! What value should it have?", colorama.Fore.LIGHTCYAN_EX, False)
                    typeb("(1) 1", colorama.Fore.LIGHTCYAN_EX, False)
                    typeb("(2) 11", colorama.Fore.LIGHTCYAN_EX, False)
                    print(colorama.Fore.LIGHTBLACK_EX, end = "", flush = True)
                    placv = input(">>> ")
                    if placv == "1" or placv == "2":
                        break
                if placv == "1":
                    pvalue = 1
                    playercardvals.append(pvalue) 
                    ptotal = ptotal + pvalue
                    typeb("\n" + "Recieved one card\n Value: " + str(pvalue), colorama.Fore.LIGHTGREEN_EX, False)
                    print(colorama.Style.RESET_ALL)
                    print(cards[pvalue - 1])
                    print()
                    pinventory.append(cards[pvalue - 1])
                    typeb("Current total: " + str(ptotal), colorama.Fore.LIGHTGREEN_EX, True)
                    turn = "ai"
                elif placv == "2":
                    pvalue = 11
                    playercardvals.append(pvalue) 
                    ptotal = ptotal + pvalue
                    typeb("\n" + player + " ~ Recieved one card\n Value: " + str(pvalue), colorama.Fore.LIGHTGREEN_EX, False)
                    print(colorama.Style.RESET_ALL)
                    print(cards[pvalue - 1])
                    print()
                    pinventory.append(cards[pvalue - 1])
                    typeb("Current total: " + str(ptotal), colorama.Fore.LIGHTGREEN_EX, True)
                    turn = "ai"

            avalue = random.randint(1,11)
            atotal = atotal + avalue
            aicardvals.append(avalue)
            typeb(ai + " ~ Recieved one card", colorama.Fore.RED, True)
            plac = "null"
            aic = "null"
            turn = "player"
            if plac != "1":

                inttesting = False
                typeb(dealer + ": 'How much do you bet that you will win? You currently have £" + str(money) + " available.'", colorama.Fore.LIGHTCYAN_EX, False)

                while not inttesting:
                    print(colorama.Fore.LIGHTBLACK_EX, end = "", flush = True)

                    bet = input(">>> ")
                    try:		
                        int(bet)
                        if int(bet) <= money and int(bet) > 0:
                            int(bet)
                            print()
                            inttesting = True
                        else:
                            l = "l"
                            int(l)
                    except:
                        typeb(dealer + ": 'Please can you choose a *number* that you can also afford-'", colorama.Fore.LIGHTCYAN_EX, False)
                        inttesting = False

                while plac != "1":
                    if plac == "1":
                        break
                    if aic == "1":
                            break
                    if ptotal > 21 or ptotal == 21:
                        break
                    if atotal > 21 or atotal == 21:
                        break
                    while atotal < 21 and ptotal < 21:
                        if plac == "1":
                            break
                        if ptotal > 21 or ptotal == 21:
                            break
                        if atotal > 21 or atotal == 21:
                            break

                        if turn == "player" and plac != "1":
                            if plac == "1":
                                break
                            while plac != "1" and plac != "2":

                                print(colorama.Style.RESET_ALL, end = "", flush = True)
                                print("Inventory:")
                                print(*pinventory, sep = " ")
                                print()
                                print("--------------------")
                                print()
                                typeb(dealer + ": 'What do you want to do? Your current total is " + str(ptotal) + "'", colorama.Fore.LIGHTCYAN_EX, False)
                                typeb("(1) Stand", colorama.Fore.LIGHTCYAN_EX, False)
                                typeb("(2) Hit", colorama.Fore.LIGHTCYAN_EX, False)
                                print(colorama.Fore.LIGHTBLACK_EX, end = "", flush = True)
                                plac = input(">>> ")

                                if plac == "1":
                                    typeb(player + ": 'I Stand'", colorama.Fore.LIGHTGREEN_EX, True)
                                    turn = "null"
                                    plac = "1"
                                    break



                                elif plac == "2":
                                    typeb(player + ": 'Hit me'", colorama.Fore.LIGHTGREEN_EX, False)
                                    pvalue = random.randint(1, 11)


                                    if pvalue != 11 and pvalue != 1:
                                        playercardvals.append(pvalue) 
                                        ptotal = ptotal + pvalue
                                        typeb(player + " ~ Recieved one card\n Value: " + str(pvalue), colorama.Fore.LIGHTGREEN_EX, False)
                                        print(colorama.Style.RESET_ALL)
                                        print(cards[pvalue - 1])
                                        print()
                                        pinventory.append(cards[pvalue - 1])

                                        typeb("Current total: " + str(ptotal), colorama.Fore.LIGHTGREEN_EX, True)
                                        turn = "ai"
                                    else:
                                        typeb(player + " ~ Recieved one card\n", colorama.Fore.LIGHTGREEN_EX, False)
                                        print(colorama.Style.RESET_ALL)
                                        print(cards[pvalue - 1])
                                        while placv != "1" or placv != "2":
                                            typeb("*It's an ace! What value should it have?", colorama.Fore.LIGHTCYAN_EX, False)
                                            typeb("(1) 1", colorama.Fore.LIGHTCYAN_EX, False)
                                            typeb("(2) 11", colorama.Fore.LIGHTCYAN_EX, False)
                                            print(colorama.Fore.LIGHTBLACK_EX, end = "", flush = True)
                                            placv = input(">>> ")
                                            if placv == "1" or placv == "2":
                                                break
                                        if placv == "1":
                                            pvalue = 1
                                            playercardvals.append(pvalue) 
                                            pinventory.append(cards[pvalue - 1])
                                            ptotal = ptotal + pvalue
                                            typeb("\n" + "Recieved one card\n Value: " + str(pvalue), colorama.Fore.LIGHTGREEN_EX, False)
                                            typeb("Current total: " + str(ptotal), colorama.Fore.LIGHTGREEN_EX, True)
                                            turn = "ai"
                                        elif placv == "2":
                                            pvalue = 11
                                            playercardvals.append(pvalue) 
                                            pinventory.append(cards[pvalue - 1])
                                            ptotal = ptotal + pvalue
                                            typeb("\n" + player + " ~ Recieved one card\n Value: " + str(pvalue), colorama.Fore.LIGHTGREEN_EX, False)
                                            typeb("Current total: " + str(ptotal), colorama.Fore.LIGHTGREEN_EX, True)
                                            turn = "ai"




                                    if ptotal == 21:
                                        break
                                        typeb(ai + ": 'I Stand at 21.'", colorama.Fore.LIGHTGREEN_EX, False)
                                    if ptotal > 21:
                                        break
                                        typeb(ai + ": 'I'm bust.'", colorama.Fore.LIGHTGREEN_EX, False)
                        if ptotal == 21:
                            break
                        if ptotal > 21:
                            break






                        elif turn == "ai":
                            if atotal != range(random.randint(14,18),20) and atotal != 21 and atotal < 21:
                                aic = "2"
                                typeb(ai + ": 'Hit me'", colorama.Fore.RED, False)
                                avalue = random.randint(1,11)
                                atotal = atotal + avalue
                                aicardvals.append(avalue)
                                typeb(ai + " ~ Recieved one card", colorama.Fore.RED, True)
                                turn = "player"
                                plac = "null"
                            elif atotal == 21:
                                break
                            elif atotal > 21:
                                break
                            if atotal == range(random.randint(14,18),20) or atotal == 21 or atotal > 21:
                                if atotal == 21:
                                    typeb(ai + ": 'I Stand at 21.'", colorama.Fore.RED, False)
                                    aic = "1"
                                elif atotal > 21:
                                    typeb(ai + ": 'I'm bust.'", colorama.Fore.RED, False)
                                    aic = "1"
                                else:
                                    if turn == "ai" and aic != "1":
                                        typeb(ai + ": 'I Stand'", colorama.Fore.RED, False)
                                        aic = "1"
                                        break
                                    elif aic == "1":
                                        turn = "player"
                                        plac = "null"



                        elif turn == "null":
                            plac = "1"
                            break

                    if atotal == 21:
                        break
                    if atotal > 21:
                        break







            if plac == "1":
                while atotal != range(random.randint(14,18),20) and atotal != 21 and atotal < 21:
                    aic = "2"
                    typeb(ai + ": 'Hit me'", colorama.Fore.RED, False)
                    avalue = random.randint(1,11)
                    atotal = atotal + avalue
                    aicardvals.append(avalue)
                    typeb(ai + " ~ Recieved one card", colorama.Fore.RED, True)
                    if atotal == range(random.randint(14,18),20):
                        if random.randint(1,2) == 1:
                            typeb(ai + ": 'I stand.'", colorama.Fore.RED, False)
                            aic = "1"
                            break

                        if atotal == range(random.randint(14,18),20) or atotal == 21 or atotal > 21:
                            break

                if atotal == range(random.randint(14,18),20) or atotal == 21 or atotal > 21:
                    if atotal == 21:
                        typeb(ai + ": 'I Stand at 21.'", colorama.Fore.RED, False)
                        aic = "1"
                    elif atotal > 21:
                        typeb(ai + ": 'I'm bust.'", colorama.Fore.RED, False)
                        aic = "1"
                    if atotal == range(random.randint(14,18),20):
                        if turn == "ai":
                            if random.randint(1,2) == 1:
                                typeb(ai + ": 'I Stand'", colorama.Fore.RED, False)
                                aic = "1"


            print()
            typeb("Ending game...", colorama.Fore.LIGHTCYAN_EX, False)
            typeb(player + " total: " + str(ptotal), colorama.Fore.LIGHTCYAN_EX, False)
            pinventory.clear()
            typeb(ai + " total: " + str(atotal), colorama.Fore.LIGHTCYAN_EX, False)


            if ptotal > atotal and ptotal <= 21:
                diff = ptotal - atotal
                typeb("You win by " + str(diff) + " points!", colorama.Fore.LIGHTGREEN_EX, False)
                wins = wins + 1
                money = money + int(bet)
                typeb("Total wins: " + str(wins), colorama.Fore.LIGHTGREEN_EX, False)
                typeb("+ £" + str(bet) + ":\n Balance: £" + str(money), colorama.Fore.LIGHTGREEN_EX, True)
                time.sleep(2)
            elif ptotal < atotal and atotal <= 21:
                diff = atotal - ptotal
                typeb("You lose by " + str(diff) + " points!", colorama.Fore.RED, False)
                losses = losses + 1
                money = money - int(bet)

                typeb("Total wins: " + str(wins), colorama.Fore.LIGHTGREEN_EX, False)
                typeb("- £" + str(bet) + ":\n Balance: £" + str(money), colorama.Fore.RED, True)
                time.sleep(2)

            elif ptotal == atotal and ptotal <= 21 and atotal <= 21:
                typeb("It's a draw! You both had " + str(ptotal) + " points!", colorama.Fore.LIGHTCYAN_EX, False)
                draws = draws + 1
                typeb("Total wins: " + str(wins), colorama.Fore.LIGHTGREEN_EX, True)
                typeb("Balance: £" + str(money), colorama.Fore.LIGHTCYAN_EX)
                time.sleep(2)
            elif ptotal > 21 and atotal <= 21:
                diff = ptotal - 21
                typeb("You lose! You went over 21 by " + str(diff) + " points!", colorama.Fore.RED, False)
                losses = losses + 1
                money = money - int(bet)
                typeb("Total wins: " + str(wins), colorama.Fore.LIGHTGREEN_EX, False)
                typeb("- £" + str(bet) + ":\n Balance: £" + str(money), colorama.Fore.RED, True)

                time.sleep(2)
            elif atotal > 21 and ptotal <= 21:
                diff = atotal - 21
                typeb("You win! " + ai + " went over 21 by " + str(diff) + " points!", colorama.Fore.LIGHTGREEN_EX, False)
                wins = wins + 1
                money = money + int(bet)
                typeb("Total wins: " + str(wins), colorama.Fore.LIGHTGREEN_EX, False)
                typeb("+ £" + str(bet) + ":\n Balance: £" + str(money), colorama.Fore.LIGHTGREEN_EX, True)
                time.sleep(2)
            os.system("clear")
            if money <= 0:
                typeb("You're broke!", colorama.Fore.RED, False)
                print(colorama.Style.RESET_ALL)

                print("Saving data...")

                from datetime import date
                today = date.today()

                todaya = today.strftime("%d/%m/%Y")

                f3 = open("balancer.txt", "r")
                testera = f3.read()
                testera = int(testera)
                f3.close()

                f2 = open("balancer.txt", "w")
                f2.write(str(money))
                f2.close()
                print("Ending session...")



                os.remove("balancer.txt")
                f2 = open("balancer.txt", "w+")
                f2.write(str(money))

                f2.close()

                os.remove("balancer.txt")
                f2 = open("balancer.txt", "w+")
                f2.write(str(money))
                f2.close()
                break


                print("--------------------------")

                try:
                    tot = draws + wins + losses
                    y = np.array([draws, wins, losses])
                    mylabels = ["Draws: " + str((draws/tot)*100) + "%", "Wins: " + str((wins/tot)*100) + "%", "Losses: " + str((losses/tot)*100) + "%"]

                except:
                    quit()

        except KeyboardInterrupt:
            print(colorama.Style.RESET_ALL)

            print("Saving data...")


            f3 = open("balancer.txt", "r")
            testera = f3.read()
            testera = int(testera)
            f3.close()

            f2 = open("balancer.txt", "w")
            f2.write(str(money))
            f2.close()
            print("Ending session...")



            os.remove("balancer.txt")
            f2 = open("balancer.txt", "w+")
            f2.write(str(money))

            f2.close()

            os.remove("balancer.txt")
            f2 = open("balancer.txt", "w+")
            f2.write(str(money))
            f2.close()
            break

            print("--------------------------")

            try:
                tot = draws + wins + losses
                y = np.array([draws, wins, losses])
                mylabels = ["Draws: " + str((draws/tot)*100) + "%", "Wins: " + str((wins/tot)*100) + "%", "Losses: " + str((losses/tot)*100) + "%"]

            except:
                quit()
#######################################################################
#######################################################################
#######################################################################
P1Wins = 0
P2Wins = 0
P1Total = 0
P2Total = 0
PTDraws = 0
TPDraws = 0
P1Cv = 0
P2Cv = 0
if mode == "2":
    P1C = "null"
    P2C = "null"

    P1Money = 100
    P2Money = 100
    os.system("clear")
    typeb("Starting 2 Player Mode...", colorama.Fore.LIGHTBLACK_EX, False)
    time.sleep(2)
    os.system("clear")

    while True:
        P1Inventory.clear()
        P2Inventory.clear()
        P1Total = 0

        P2Total = 0

        print("--------------------------")
        typeb("The dealer: " + dealer, colorama.Fore.LIGHTGREEN_EX, False)
        typeb("Competition: Player 1 V Player 2", colorama.Fore.RED, False)
        print("----")
        typeb("P1 Balance: £" + str(P1Money), colorama.Fore.LIGHTYELLOW_EX, False)
        print("----")
        typeb("P2 Balance: £" + str(P2Money), colorama.Fore.LIGHTYELLOW_EX, False)
        print("--------------------------")

        typeb(dealer + ": 'Here are your cards.'", colorama.Fore.LIGHTCYAN_EX, True)
        P1Total = 0
        P2Total = 0
        Player1Twist = True
        Player2Twist = True
        turn = "player1"
    ####################################################################
        print(colorama.Fore.LIGHTBLACK_EX, end = "", flush = True)
        null = input("Press [ENTER] to continue\n>>> ")
        os.system("clear")
        null = input("Player 1, press [ENTER] when you're ready.\n>>> ")
        os.system("clear")
        P1Value = random.randint(1, 11)
        if P1Value != 11 and P1Value != 1:
            player1cardvals.append(P1Value) 

            P1Total = P1Total + P1Value
            typeb("Player 1 ~ Recieved one card\n Value: " + str(P1Value), colorama.Fore.LIGHTGREEN_EX, False)
            print(colorama.Style.RESET_ALL)
            print(cards[P1Value - 1])
            print()
            P1Inventory.append(cards[P1Value - 1])
            typeb("Current total: " + str(P1Total), colorama.Fore.LIGHTGREEN_EX, True)
            turn = "player2"
        else:
            typeb("Player 1 ~ Recieved one card\n", colorama.Fore.LIGHTGREEN_EX, False)
            print(colorama.Style.RESET_ALL)
            print(cards[P1Value - 1])
            print()

#############
            while P1Cv != "1" or P1Cv != "2":
                typeb("*It's an ace! What value should it have?", colorama.Fore.LIGHTCYAN_EX, False)
                typeb("(1) 1", colorama.Fore.LIGHTCYAN_EX, False)
                typeb("(2) 11", colorama.Fore.LIGHTCYAN_EX, False)
                print(colorama.Fore.LIGHTBLACK_EX, end = "", flush = True)
                P1Cv = input(">>> ")

                if P1Cv == "1" or P1Cv == "2":
                    break
##############
            if P1Cv == "1":
                P1Value = 1
                player1cardvals.append(P1Value) 
                P1Total = P1Total + P1Value
                typeb("\nPlayer 1 ~ Recieved one card\n Value: " + str(P1Value), colorama.Fore.LIGHTGREEN_EX, False)
                print(colorama.Style.RESET_ALL)
                print(cards[P1Value - 1])
                print()
                P1Inventory.append(cards[P1Value - 1])
                typeb("Current total: " + str(P1Total), colorama.Fore.LIGHTGREEN_EX, True)
                turn = "ai"
            elif P1Cv == "2":
                P1Value = 11
                player1cardvals.append(P1Value) 
                P1Total = P1Total + P1Value
                typeb("\nPlayer 1 ~ Recieved one card\n Value: " + str(P1Value), colorama.Fore.LIGHTGREEN_EX, False)
                print(colorama.Style.RESET_ALL)
                print(cards[P1Value - 1])
                print()
                P1Inventory.append(cards[P1Value - 1])
                typeb("Current total: " + str(P1Total), colorama.Fore.LIGHTGREEN_EX, True)
                turn = "player2"
        ##############
        print(colorama.Fore.LIGHTBLACK_EX, end = "", flush = True)
        null = input("Press [ENTER] to continue\n>>> ")
        os.system("clear")
        null = input("Player 2, press [ENTER] when you're ready.\n>>> ")
        os.system("clear")
        P2Value = random.randint(1, 11)
        if P2Value != 11 and P2Value != 1:
            player2cardvals.append(P1Value) 
            P2Total = P2Total + P2Value
            typeb("Player 2 ~ Recieved one card\n Value: " + str(P2Value), colorama.Fore.RED, False)
            print(colorama.Style.RESET_ALL)
            print(cards[P2Value - 1])
            print()
            P2Inventory.append(cards[P2Value - 1])
            typeb("Current total: " + str(P2Total), colorama.Fore.RED, True)
            turn = "player1"
        else:
            typeb("Player 2 ~ Recieved one card\n", colorama.Fore.RED, False)
            print(colorama.Style.RESET_ALL)
            print(cards[P2Value - 1])
            print()
#############
            while P2Cv != "1" or P2Cv != "2":
                typeb("*It's an ace! What value should it have?", colorama.Fore.LIGHTCYAN_EX, False)
                typeb("(1) 1", colorama.Fore.LIGHTCYAN_EX, False)
                typeb("(2) 11", colorama.Fore.LIGHTCYAN_EX, False)
                print(colorama.Fore.LIGHTBLACK_EX, end = "", flush = True)
                P2Cv = input(">>> ")

                if P2Cv == "1" or P2Cv == "2":
                    break
##############
            if P2Cv == "1":
                P2Value = 1
                player2cardvals.append(P2Value) 
                P2Total = P2Total + P2Value
                typeb("\nPlayer 2 ~ Recieved one card\n Value: " + str(P2Value), colorama.Fore.RED, False)
                print(colorama.Style.RESET_ALL)
                print(cards[P2Value - 1])
                print()
                P2Inventory.append(cards[P2Value - 1])
                typeb("Current total: " + str(P2Total), colorama.Fore.RED, True)
                turn = "player1"
            elif P2Cv == "2":
                P2Value = 11
                player2cardvals.append(P1Value) 
                P2Total = P2Total + P2Value
                typeb("\nPlayer 2 ~ Recieved one card\n Value: " + str(P2Value), colorama.Fore.RED, False)
                print(colorama.Style.RESET_ALL)
                print(cards[P2Value - 1])
                print()
                P2Inventory.append(cards[P2Value - 1])
                typeb("Current total: " + str(P2Total), colorama.Fore.RED, True)

                turn = "player1"


    #######################################################################
    #P1 BETS
        end = False
        inttesting = False
        print(colorama.Fore.LIGHTBLACK_EX, end = "", flush = True)
        null = input("Press [ENTER] to continue\n>>> ")
        os.system("clear")
        print(colorama.Fore.LIGHTBLACK_EX, end = "", flush = True)
        null = input("Player 1, press [ENTER] when you're ready.\n>>> ")
        os.system("clear")

        typeb(dealer + ": 'Player 1, how much do you bet that you will win? You currently have £" + str(P1Money) + " available.'", colorama.Fore.LIGHTCYAN_EX, False)
        while not inttesting:
            print(colorama.Fore.LIGHTBLACK_EX, end = "", flush = True)

            P1bet = input(">>> ")
            try:		
                int(P1bet)
                if int(P1bet) <= P1Money and int(P1bet) > 0:
                    int(P1bet)
                    print()
                    inttesting = True
                else:
                    l = "l"
                    int(l)
            except:
                typeb(dealer + ": 'Player 1, please can you choose a *number* that you can also afford-'", colorama.Fore.LIGHTCYAN_EX, False)
    ######################################################################
        print(colorama.Fore.LIGHTBLACK_EX, end = "", flush = True)
        null = input("Press [ENTER] to continue\n>>> ")
        os.system("clear")
        null = input("Player 2, press [ENTER] when you're ready.\n>>> ")
        os.system("clear")
    #######################################################################
    #P2 BETS
        end == False
        inttesting = False
        typeb(dealer + ": 'Player 2, how much do you bet that you will win? You currently have £" + str(P2Money) + " available.'", colorama.Fore.LIGHTCYAN_EX, False)
        while not inttesting:
            print(colorama.Fore.LIGHTBLACK_EX, end = "", flush = True)
            P2bet = input(">>> ")
            try:		
                int(P2bet)
                if int(P2bet) <= P2Money and int(P2bet) > 0:
                    int(P2bet)
                    print()
                    inttesting = True
                else:
                    l = "l"
                    int(l)
            except:
                typeb(dealer + ": 'Player 2, please can you choose a *number* that you can also afford-'", colorama.Fore.LIGHTCYAN_EX, False)
    #########################################################################
        end = False
        turn = "player1"
        while end == False:
            P1C = None
            P2C = None

            if P1Total == 21:
                typeb("Player 1: 'I Stand with 21'", colorama.Fore.LIGHTGREEN_EX, True)
                turn = "null"
                plac = "1"
                end = True
                break
            if P2Total == 21:
                typeb("Player 2: 'I Stand with 21'", colorama.Fore.RED, True)
                turn = "null"
                plac = "1"
                end = True
                break
            if P1Total > 21:
                typeb("Player 1: 'I'm bust'", colorama.Fore.LIGHTGREEN_EX, True)
                turn = "null"
                plac = "1"
                end = True
                break
            if P2Total > 21:
                typeb("Player 2: 'I'm bust.'", colorama.Fore.LIGHTGREEN_EX, True)
                turn = "null"
                plac = "1"
                end = True
                break

            if turn == "player1" and P1C != "1":
                print(colorama.Fore.LIGHTBLACK_EX, end = "", flush = True)
                null = input("Press [ENTER] to continue\n>>> ")
                os.system("clear")

                if P2C != "1":
                    null = input("Player 1, press [ENTER] when you're ready.\n>>> ")
                    os.system("clear")
                elif P2C == "1":
                        print("PLAYER 2 HAS STOOD")
                        null = input("Player 1, press [ENTER] when you're ready.\n>>> ")
                        os.system("clear")
                while P1C != "1" or P1C != "2":
                    print(colorama.Fore.LIGHTBLACK_EX, end = "", flush = True)
                    print(colorama.Style.RESET_ALL, end = "", flush = True)
                    print("Inventory:")
                    print(*P1Inventory, sep = " ")
                    print()
                    print("--------------------")
                    print()
                    typeb(dealer + ": 'Player 1, what do you want to do? Your current total is: " + str(P1Total) + "'", colorama.Fore.LIGHTCYAN_EX, False)
                    typeb("(1) Stand", colorama.Fore.LIGHTCYAN_EX, False)
                    typeb("(2) Hit", colorama.Fore.LIGHTCYAN_EX, False)
                    print(colorama.Fore.LIGHTBLACK_EX, end = "", flush = True)
                    P1C = input(">>> ")
                    if P1C == "1":
                        if P2C != "1":
                            turn = "player2"

                        else:
                            end = True
                        break
                    if P1C == "2":
                        turn = "player2"
                        break

    ####################################
    #If Player 1 Choses Stand
                if P1C == "1":
                    typeb("Player 1: 'I Stand'", colorama.Fore.LIGHTGREEN_EX, True)
                    turn = "player2"
    ####################################
    #If Player 1 Choses Hit
                elif P1C == "2":
                    typeb("Player 1: 'Hit me'", colorama.Fore.LIGHTGREEN_EX, False)
                    P1Value = random.randint(1, 11)
    #############			
                    if P1Value != 11 and P1Value != 1:
                        player1cardvals.append(P1Value) 
                        P1Total = P1Total + P1Value
                        typeb("Player 1 ~ Recieved one card\n Value: " + str(P1Value), colorama.Fore.LIGHTGREEN_EX, False)
                        print(colorama.Style.RESET_ALL)
                        print(cards[P1Value - 1])
                        print()
                        P1Inventory.append(cards[P1Value - 1])
                        typeb("Current total: " + str(P1Total), colorama.Fore.LIGHTGREEN_EX, True)
                        turn = "player2"
                    else:
                        typeb("Player 1 ~ Recieved one card\n", colorama.Fore.LIGHTGREEN_EX, False)
                        print(colorama.Style.RESET_ALL)
                        print(cards[P1Value - 1])
                        print()

    #############
                        while P1Cv != "1" or P1Cv != "2":
                            typeb("*It's an ace! What value should it have?", colorama.Fore.LIGHTCYAN_EX, False)
                            typeb("(1) 1", colorama.Fore.LIGHTCYAN_EX, False)
                            typeb("(2) 11", colorama.Fore.LIGHTCYAN_EX, False)
                            print(colorama.Fore.LIGHTBLACK_EX, end = "", flush = True)
                            P1Cv = input(">>> ")

                            if P1Cv == "1" or P1Cv == "2":
                                break
    ##############
                        if P1Cv == "1":
                            P1Value = 1
                            player1cardvals.append(P1Value) 
                            P1Total = P1Total + P1Value
                            typeb("\nPlayer 1 ~ Recieved one card\n Value: " + str(P1Value), colorama.Fore.LIGHTGREEN_EX, False)
                            print(colorama.Style.RESET_ALL)
                            print(cards[P1Value - 1])
                            print()
                            P1Inventory.append(cards[P1Value - 1])
                            typeb("Current total: " + str(P1Total), colorama.Fore.LIGHTGREEN_EX, True)
                            turn = "ai"
                        elif P1Cv == "2":
                            P1Value = 11
                            player1cardvals.append(P1Value) 
                            P1Total = P1Total + P1Value
                            typeb("\nPlayer 1 ~ Recieved one card\n Value: " + str(P1Value), colorama.Fore.LIGHTGREEN_EX, False)
                            print(colorama.Style.RESET_ALL)
                            print(cards[P1Value - 1])
                            print()
                            P1Inventory.append(cards[P1Value - 1])
                            typeb("Current total: " + str(P1Total), colorama.Fore.LIGHTGREEN_EX, True)
                            turn = "player2"
            else:
                turn = "player2"
                if P1C == "1" and P2C == "1":
                    break
    ##############
            if turn == "player2" and P2C != "1":
                print(colorama.Fore.LIGHTBLACK_EX, end = "", flush = True)
                null = input("Press [ENTER] to continue\n>>> ")
                os.system("clear")
                if P1C != "1":
                    null = input("Player 2, press [ENTER] when you're ready.\n>>> ")
                    os.system("clear")
                elif P1C == "1":
                    print("PLAYER 1 HAS STOOD")
                    null = input("Player 2, press [ENTER] when you're ready.\n>>> ")
                    os.system("clear")
                while P2C != "1" or P2C != "2":
                    print(colorama.Fore.LIGHTBLACK_EX, end = "", flush = True)
                    print(colorama.Style.RESET_ALL, end = "", flush = True)
                    print("Inventory:")
                    print(*P2Inventory, sep = " ")
                    print()
                    print("--------------------")
                    print()
                    typeb(dealer + ": 'Player 2, what do you want to do? Your current total is: " + str(P2Total) + "'", colorama.Fore.LIGHTCYAN_EX, False)
                    typeb("(1) Stand", colorama.Fore.LIGHTCYAN_EX, False)
                    typeb("(2) Hit", colorama.Fore.LIGHTCYAN_EX, False)
                    print(colorama.Fore.LIGHTBLACK_EX, end = "", flush = True)
                    P2C = input(">>> ")
                    if P2C == "1":
                        if P1C != "1":
                            turn = "player1"
                        else:
                            end = True
                        break
                    if P2C == "2":
                        turn = "player1"
                        break
    ####################################
    #If Player 1 Choses Stand
                if P2C == "1":
                    typeb("Player 2: 'I Stand'", colorama.Fore.RED, True)
                    turn = "player1"

    ####################################
    #If Player 1 Choses Hit
                elif P2C == "2":
                    typeb("Player 2: 'Hit me'", colorama.Fore.RED, False)
                    P2Value = random.randint(1, 11)
    #############			
                    if P2Value != 11 and P2Value != 1:
                        player2cardvals.append(P1Value) 
                        P2Total = P2Total + P2Value
                        typeb("Player 2 ~ Recieved one card\n Value: " + str(P2Value), colorama.Fore.RED, False)
                        print(colorama.Style.RESET_ALL)
                        print(cards[P2Value - 1])
                        print()
                        P2Inventory.append(cards[P2Value - 1])
                        typeb("Current total: " + str(P2Total), colorama.Fore.RED, True)
                        turn = "player1"
                    else:
                        typeb("Player 2 ~ Recieved one card\n", colorama.Fore.RED, False)
    #############
                        while P2Cv != "1" or P2Cv != "2":
                            typeb("*It's an ace! What value should it have?", colorama.Fore.LIGHTCYAN_EX, False)
                            typeb("(1) 1", colorama.Fore.LIGHTCYAN_EX, False)
                            typeb("(2) 11", colorama.Fore.LIGHTCYAN_EX, False)
                            print(colorama.Fore.LIGHTBLACK_EX, end = "", flush = True)
                            P2Cv = input(">>> ")

                            if P2Cv == "1" or P2Cv == "2":
                                break
    ##############
                        if P2Cv == "1":
                            P2Value = 1
                            player2cardvals.append(P2Value) 
                            P2Total = P2Total + P2Value
                            typeb("\nPlayer 2 ~ Recieved one card\n Value: " + str(P2Value), colorama.Fore.RED, False)
                            print(colorama.Style.RESET_ALL)
                            print(cards[P2Value - 1])
                            print()
                            P2Inventory.append(cards[P2Value - 1])
                            typeb("Current total: " + str(P2Total), colorama.Fore.RED, True)
                            turn = "player1"
                        elif P2Cv == "2":
                            P2Value = 11
                            player2cardvals.append(P1Value)
                            print(colorama.Style.RESET_ALL)
                            print(cards[P2Value - 1])
                            print()
                            P2Inventory.append(cards[P2Value - 1])
                            P2Total = P2Total + P2Value
                            typeb("\nPlayer 2 ~ Recieved one card\n Value: " + str(P2Value), colorama.Fore.RED, False)
                            typeb("Current total: " + str(P2Total), colorama.Fore.RED, True)

                            turn = "player1"
            else:
                turn = "player1"
                if P1C == "1" and P2C == "1":
                    break
    ##############
        typeb("Game ending...", None, True)
        if P1Total > P2Total and P1Total <= 21:
            diff = P1Total - P2Total
            typeb("P1 Points: " + str(P1Total), colorama.Fore.LIGHTGREEN_EX, False)
            typeb("P2 Points: " + str(P2Total), colorama.Fore.RED, False)
            typeb("Player 1 wins by " + str(diff) + " points!", colorama.Fore.LIGHTGREEN_EX, False)
            P1Money = P1Money + int(P2bet)
            P1Wins = P1Wins + 1
            P2Money = P2Money - int(P2bet)

        elif P1Total < P2Total and P2Total <= 21:
            typeb("P1 Points: " + str(P1Total), colorama.Fore.LIGHTGREEN_EX, False)
            typeb("P2 Points: " + str(P2Total), colorama.Fore.RED, False)
            diff = P2Total - P1Total
            typeb("Player 2 wins by " + str(diff) + " points!", colorama.Fore.RED, False)
            P2Wins = P2Wins + 1
            P1Money = P1Money - int(P1bet)
            P2Money = P2Money + int(P1bet)

        elif P1Total == P2Total and P2Total <= 21 and P1Total <= 21:
            typeb("P1 Points: " + str(P1Total), colorama.Fore.LIGHTGREEN_EX, False)
            typeb("P2 Points: " + str(P2Total), colorama.Fore.RED, False)
            typeb("It's a draw! You both had " + str(P1Total) + " points!", colorama.Fore.LIGHTCYAN_EX, False)
            TPDraws = TPDraws + 1

        elif P1Total > 21 and P2Total <= 21:
            typeb("P1 Points: " + str(P1Total), colorama.Fore.LIGHTGREEN_EX, False)
            typeb("P2 Points: " + str(P2Total), colorama.Fore.RED, False)
            diff = P1Total - 21
            typeb("Player 2 wins! Player 1 went over 21 by " + str(diff) + " points!", colorama.Fore.RED, False)
            P2Wins = P2Wins + 1
            P1Money = P1Money - int(P1bet)
            P2Money = P2Money + int(P1bet)


        elif P2Total > 21 and P1Total <= 21:
            typeb("P1 Points: " + str(P1Total), colorama.Fore.LIGHTGREEN_EX, False)
            typeb("P2 Points: " + str(P2Total), colorama.Fore.RED, False)
            diff = P2Total - 21
            typeb("Player 1 wins! Player 2 went over 21 by " + str(diff) + " points!", colorama.Fore.RED, False)
            P1Wins = P1Wins + 1
            P1Money = P1Money + int(P2bet)
            P2Money = P2Money - int(P2bet)
        time.sleep(2)
        os.system("clear")

        if P1Money <= 0:
            typeb("Player 1 went broke!", colorama.Fore.RED, False)
            print(colorama.Style.RESET_ALL)
            print("--------------------------")
            print(colorama.Fore.LIGHTBLACK_EX, end = "", flush = True)
            null = input("Press [ENTER] to end the game\n>>> ")
            os.system("clear")
            try:
                tot = TPDraws + P1Wins + P2Wins
                y = np.array([TPDraws, P1Wins, P2Wins])
                mylabels = ["Draws: " + str((TPDraws/tot)*100) + "%", "Player 1 Wins: " + str((P1Wins/tot)*100) + "%", "Player 2 Wins: " + str((P2Wins/tot)*100) + "%"]

            except:
                quit()
        if P2Money <= 0:
            typeb("Player 2 went broke!", colorama.Fore.RED, False)
            print(colorama.Style.RESET_ALL)
            print("--------------------------")
            print(colorama.Fore.LIGHTBLACK_EX, end = "", flush = True)
            null = input("Press [ENTER] to end the game\n>>> ")
            try:
                tot = TPDraws + P1Wins + P2Wins
                y = np.array([TPDraws, P1Wins, P2Wins])
                mylabels = ["Draws: " + str((TPDraws/tot)*100) + "%", "Player 1 Wins: " + str((P1Wins/tot)*100) + "%", "Player 2 Wins: " + str((P2Wins/tot)*100) + "%"]

            except:
                quit()


            #
            print("--------------------------")
            print(colorama.Fore.LIGHTBLACK_EX, end = "", flush = True)
            null = input("Press [ENTER] to continue the games\n>>> ")
            os.system("clear")
            tot = TPDraws + P1Wins + P2Wins
            y = np.array([TPDraws, P1Wins, P2Wins])
            try:
                mylabels = ["Draws: " + str((TPDraws/tot)*100) + "%", "Player 1 Wins: " + str((P1Wins/tot)*100) + "%", "Player 2 Wins: " + str((P2Wins/tot)*100) + "%"]

            except:
                quit()


os.remove("balancer.txt")
time.sleep(3)
f100 = open("wins.txt", "w")
f.close()
with open("balancer.txt", "w") as f9:
    print(money)
    f9.write(str(money))
    f9.close()





