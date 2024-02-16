####################
import time
import socket
import random
import psutil
import shutil
from pathlib import Path
import os
from datetime import datetime
import colorama
import writer
import webbrowser
import requests
from contextlib import contextmanager
from io import StringIO
import sys
import subprocess
#Maybe you should define the colors instead of using them again and again.
#ugh fine
ogdir = os.getcwd()
black = colorama.Fore.LIGHTBLACK_EX
#not black
reset = colorama.Style.RESET_ALL
red = colorama.Fore.RED
blue = colorama.Fore.LIGHTCYAN_EX
purple = colorama.Fore.LIGHTMAGENTA_EX
green = colorama.Fore.LIGHTGREEN_EX
#done
newsActive = True
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '_']

old = os.getcwd()
os.chdir(old)
Date = str(datetime.now())[5:10]
holidays = [["Christmas Eve", "12-24"], ["Christmas", "12-25"], ["Hallow's Eve", "10-30"], ["Halloween", "10-31"], ["New Year's Eve", "12-31"], ["New Year's Day", "01-01"], ["Valentine's Day", "02-14"]]

for sublist in holidays:
    if Date in sublist:
        holiday = sublist[0]

try:
    if holiday == "Christmas Eve":
        hMessages = ["'Twas the night before Christmas...", "You better have left the sherry out.", "Merry not Christmas!", "1 day left...", "Is the table laid out?", "Quick, now's your chance, go wrap it all... or just use CoreOS."]
    elif holiday == "Christmas":
        hMessage = ["Merry Christmas!", "Did you get anything?", "You better have gotten your coal.", "Man. It's Jesus day.", "Did the fat man come?"]
    elif holiday == "Hallow's Eve":
        hMessage = ["Check your walls...", "Did you hear something?", "What... what was that?", "Did I hear someone say candy?", "I'm under your floorboards..."]
    elif holiday == "Halloween":
        hMessage = ["AGHHH!", "I've already scared you and you didn't even know it.", "Hallow - een?", "Halloween - een?"]
    elif holiday == "New Year's Eve":
        hMessage = ["It's almost over..."]
    elif holiday == "New Year's Day":
        hMessage = ["It's the day!", "The best day of the year so far. Objectively.", "One of the days of all time!", "Happy New Year!"]
    elif holiday == "Valentine's Day":
        hMessage = ["Who is it... just tell me.", "What's the gift?", "Shouldn't you be spending time with other humans or something like that today?"]
except:
    None

try:
    specialMessage= random.choice(hMessages)
except:
    None



systemdirs = ["Documents", "Games_and_apps", "Messages", "Notes", "System", "CORE_OS.zip", "main.py", "writer.py", "tree.py", "helpfile.txt", ".version", "logo.ascii", "balancer.txt", "Reminders.log", "DEFAULT"]

for x in range(0, random.randint(1, 5)):
    print(f"{purple}Core{reset} is starting up. [-----]")
    time.sleep(0.2)
    os.system("clear")
    print(f"{purple}Core{reset} is starting up. [•----]")
    time.sleep(0.2)
    os.system("clear")
    print(f"{purple}Core{reset} is starting up. [••---]")
    time.sleep(0.2)
    os.system("clear")
    print(f"{purple}Core{reset} is starting up. [•••--]")
    time.sleep(0.2)
    os.system("clear")
    print(f"{purple}Core{reset} is starting up. [••••-]")
    time.sleep(0.2)
    os.system("clear")
    print(f"{purple}Core{reset} is starting up. [•••••]")
    time.sleep(0.2)
    os.system("clear")
time.sleep(random.randint(1, 15)/10)

#user code#
valid = False
validionormous = False
while not validionormous:
    f = open("UWP.lock", "r")
    passdata = f.read().splitlines()
    f.close()
    try:
        while valid == False:
            username = input(f"Username: {black}Press [CTRL] and [C] to create new user...\n{reset}>>> ")
            if username not in systemdirs and username in os.listdir():
                for item in passdata:
                    if username in item.split(",")[0]:
                        correct = False
                        while correct == False:
                            if username in item:
                                inlist = True
                                passwordAttempt = input(f"Password:\n>>> ")
                                if passwordAttempt == item.split(",")[1]:
                                    valid = True
                                    correct = True
                                    validionormous = True
                                    break
                                else:
                                    correct = False
                                    print(f"{red}Incorrect password{reset}\n------")
                    else:
                        None
                correct = True
                valid = True
                validionormous = True
                break
            else:
                valid = False
                print(f"{red}Invalid username{reset}\n" + "------")
                time.sleep(2)
                os.system("clear")
    
    except KeyboardInterrupt:
        print("[CTRL]+[C]")
        time.sleep(1)
        os.system("clear")
        
        valid = False
        valid0 = True

        while valid == False and valid0 == True:
            valid1 = True
            done = 0
            username = input(f"New user username:\n>>> ")
            
            if username not in systemdirs and username in os.listdir():
                
                valid = False
                print(f"{red}User already exists, please sign in.{reset}\n" + "------")
                time.sleep(2)
                os.system("clear")
                valid0 = False
            for item in username:
                if item.lower() in alpha:
                    None
                else:
                    valid1 = False

            if valid1 ==False:
                valid = False
                print(f"{red}Username must only contain letters and underscores.{reset}")
                done = 1

            if len(username) >= 17:
                valid = False
                print(f"{red}Username must be less than 17 characters.{reset}")
                valid = False
                done+=1

            print(f"Please enter a password for your new user. {black}(Type nothing for no password.){reset}")
            newPass = input(">>> ")
            if newPass == "":
                None
            else:
                f=open("UWP.lock", "a")
                f.write(f"\n{username},{newPass}\n")
                f.close()
            
            ogdir = os.getcwd()
            if done >0:
                time.sleep(2)
                os.system("clear")

            

            else:   
                valid = True
                print("Creating user...")
                time.sleep(0.2)
                shutil.copytree(ogdir + "/DEFAULT", username)
                print("User created!")
                time.sleep(1)
                validionormous = True
                break



USER = username
home_directory = os.getcwd() + "/" + username
os.chdir(home_directory)
time.sleep(1)
os.system("clear")
#end user code#



def returnDir():
    return(home_directory)
old = os.getcwd()
dir()
url = 'https://newsapi.org/v2/top-headlines?country=gb&apiKey=d8b8ad3ec036441faedc41caeec7c1da'

def gettasks():
    global runningProcesses
    runningProcesses = psutil.pids()
    print("------")
    for item in runningProcesses:
        temp = psutil.Process(item)
        listwe = temp.cmdline()
        print(colorama.Fore.LIGHTCYAN_EX + str(item) + colorama.Style.RESET_ALL +" - " + colorama.Fore.LIGHTMAGENTA_EX + temp.name() + colorama.Style.RESET_ALL)
        time.sleep(0.02)
    print("------")

def printhelp():
    print(colorama.Fore.LIGHTBLACK_EX+"------"+colorama.Style.RESET_ALL)
    print("Press 'Ctrl + C' during any operation to cancel it.")
    print(colorama.Fore.LIGHTBLACK_EX+"------"+colorama.Style.RESET_ALL)
    blue = colorama.Fore.LIGHTCYAN_EX
    purple = colorama.Fore.LIGHTMAGENTA_EX
    green = colorama.Fore.LIGHTGREEN_EX
    reset = colorama.Style.RESET_ALL
    print(blue + 
        "Command 1:"+reset+" 'help' - This prints a list of commands with their descriptions."
    )
    print(colorama.Fore.LIGHTBLACK_EX+"------"+colorama.Style.RESET_ALL)
    print(purple+
        "Command 2:"+reset+" 'dirbk' - This command goes back a folder. For example, if you are in '/runner/Core-OS', then you will go back to '/runner'"
    )
    print(colorama.Fore.LIGHTBLACK_EX+"------"+colorama.Style.RESET_ALL)
    print(green+
        "Command 3:"+reset+" 'messages' - Prints a list of the developer messages that you have recieved, and allows you to read them."
    )
    print(colorama.Fore.LIGHTBLACK_EX+"------"+colorama.Style.RESET_ALL)
    print(blue+"Command 4:"+reset+" 'chdir' - This command goes into a folder.")
    print(colorama.Fore.LIGHTBLACK_EX+"------"+colorama.Style.RESET_ALL)
    print(purple+"Command 5:"+reset+" 'ls' - Lists all folders and files in your folder.")
    print(colorama.Fore.LIGHTBLACK_EX+"------"+colorama.Style.RESET_ALL)
    print(green+
        "Command 6:"+reset+" 'clear' OR 'cls' - Clears the screen, and reprints the welcome."
    )
    print(colorama.Fore.LIGHTBLACK_EX+"------"+colorama.Style.RESET_ALL)
    print(blue+"Command 7:"+reset+" 'date' - Prints the date and time.")
    print(colorama.Fore.LIGHTBLACK_EX+"------"+colorama.Style.RESET_ALL)
    print(purple+"Command 8:"+reset+" 'version' - Prints the version of Core OS.")
    print(colorama.Fore.LIGHTBLACK_EX+"------"+colorama.Style.RESET_ALL)
    print(green+
        "Command 9:"+reset+" 'location' - Prints the current specific latitude/longitude of the session."
    )
    print(colorama.Fore.LIGHTBLACK_EX+"------"+colorama.Style.RESET_ALL)
    print(blue+
        "Command 10:"+reset+" 'write' OR 'note' - Creates a note. (File extensions are not required.)"
    )
    print(colorama.Fore.LIGHTBLACK_EX+"------"+colorama.Style.RESET_ALL)
    print(purple+
        "Command 11:"+reset+" 'create' OR 'document' - Creates a file. (File extensions are required.)"
    )
    print(colorama.Fore.LIGHTBLACK_EX+"------"+colorama.Style.RESET_ALL)
    print(blue+"Command 12:"+reset+" 'read' - Reads a file.")
    print(colorama.Fore.LIGHTBLACK_EX+"------"+colorama.Style.RESET_ALL)
    print(purple+
        "Command 13:"+reset+" 'execute' OR 'run' - Runs a file if readable by the python compiler."
    )
    print(colorama.Fore.LIGHTBLACK_EX+"------"+colorama.Style.RESET_ALL)
    print(green+
        "Command 14:"+reset+" 'python' OR 'py' OR 'python3' - Opens the Python shell for Core OS."
    )
    print(colorama.Fore.LIGHTBLACK_EX+"------"+colorama.Style.RESET_ALL)
    print(blue+
        "Command 15:"+reset+" 'home' OR 'homedir' OR 'hd' - Navigates to the home directory; Goes to the folder where Core is running."
    )
    print(colorama.Fore.LIGHTBLACK_EX+"------"+colorama.Style.RESET_ALL)
    print(purple+
        "Command 16:"+reset+" 'tree' OR 'dtree' OR 'dirtree' - Prints a tree of files on the system."
    )
    print(colorama.Fore.LIGHTBLACK_EX+"------"+colorama.Style.RESET_ALL)
    print(green + "Command 17:"+reset+" 'whoami' OR 'username' - Prints the username.")
    print(colorama.Fore.LIGHTBLACK_EX+"------"+colorama.Style.RESET_ALL)
    print(blue+
        "Command 18:"+reset+" 'design' - Changes the terminal design. - Currently: '" +
        termdes + colorama.Style.RESET_ALL + "'")
    print(colorama.Fore.LIGHTBLACK_EX+"------"+colorama.Style.RESET_ALL)
    print(purple+"Command 19:"+reset+" 'properties' - Views the properties of a file/folder.")
    print(colorama.Fore.LIGHTBLACK_EX+"------"+colorama.Style.RESET_ALL)
    print(green+"Command 20:"+reset+" 'rename' - Renames a file/folder.")
    print(colorama.Fore.LIGHTBLACK_EX+"------"+colorama.Style.RESET_ALL)
    print(blue+
        "Command 21:"+reset+" 'rnr' OR 'runner' OR 'filewd' OR 'cwd' OR 'pwd' - Gets the current working directory."
    )
    print(colorama.Fore.LIGHTBLACK_EX+"------"+colorama.Style.RESET_ALL)
    print(purple+"Command 22:"+reset+" 'open' OR 'play' - Opens a game or app.")
    print(colorama.Fore.LIGHTBLACK_EX+"------"+colorama.Style.RESET_ALL)
    print(green+"Command 23:"+reset+" 'delete' OR 'remove' - Deletes/removes a file.")
    print(colorama.Fore.LIGHTBLACK_EX+"------"+colorama.Style.RESET_ALL)
    print(blue+
        "Command 24:"+reset+" 'view' - Opens a file in a seperate default application.")
    print(colorama.Fore.LIGHTBLACK_EX+"------"+colorama.Style.RESET_ALL)
    print(purple+
        "Command 25:"+reset+" 'chport' - Changes the source, destination and server ports."
    )
    print(colorama.Fore.LIGHTBLACK_EX+"------"+colorama.Style.RESET_ALL)
    print(green+
        "Command 26:"+reset+" 'port' - Views the source, destination and server ports.")
    print(colorama.Fore.LIGHTBLACK_EX+"------"+colorama.Style.RESET_ALL)
    print(blue+"Command 27:"+reset+" 'ip' OR 'ipconfig' - Views the device's IPv4 address.")
    print(colorama.Fore.LIGHTBLACK_EX+"------"+colorama.Style.RESET_ALL)
    print(purple+"Command 28:"+reset+" 'find' OR 'findstr' - Find a string in a text file.")
    print(colorama.Fore.LIGHTBLACK_EX+"------"+colorama.Style.RESET_ALL)
    print(green+
        "Command 29:"+reset+" 'battery' OR 'power' - View the battery level of the device."
    )
    print(colorama.Fore.LIGHTBLACK_EX+"------"+colorama.Style.RESET_ALL)
    print(blue+
        "Command 30:"+reset+" 'rmstr' - Removes the line from a file containing a specified string."
    )
    print(colorama.Fore.LIGHTBLACK_EX+"------"+colorama.Style.RESET_ALL)
    print(purple+"Command 31:"+reset+" 'rmline' - Removes a line from a file.")
    print(colorama.Fore.LIGHTBLACK_EX+"------"+colorama.Style.RESET_ALL)
    print(green+"Command 32:"+reset+" 'command' - Retrieves help for a certain command.")
    print(colorama.Fore.LIGHTBLACK_EX+"------"+colorama.Style.RESET_ALL)
    print(blue+
        "Command 33:"+reset+" 'sort' - BE CAREFUL: sorts all items in a folder in alphabetical order."
    )
    print(colorama.Fore.LIGHTBLACK_EX+"------"+colorama.Style.RESET_ALL)
    print(purple+"Command 34:"+reset+" 'duplicate' OR 'dup' - Duplicates a file in a folder.")
    print(colorama.Fore.LIGHTBLACK_EX+"------"+colorama.Style.RESET_ALL)
    print(green+"Command 35:"+reset+" 'rng' - Random number generation.")
    print(colorama.Fore.LIGHTBLACK_EX+"------"+colorama.Style.RESET_ALL)
    print(blue+"Command 36:"+reset+" 'system' - Runs system command prompt.")
    print(colorama.Fore.LIGHTBLACK_EX+"------"+colorama.Style.RESET_ALL)
    print(purple+"Command 37:"+reset+" 'diskchk' - Prints the disk usage.")
    print(colorama.Fore.LIGHTBLACK_EX+"------"+colorama.Style.RESET_ALL)
    print(green+
        "Command 38:"+reset+" 'health' OR 'performance' - Prints the memory and CPU usage until 'ctrl + c' is pressed."
    )
    print(colorama.Fore.LIGHTBLACK_EX+"------"+colorama.Style.RESET_ALL)
    print(blue+"Command 39:"+reset+" 'gpu' - Prints the specifications of the GPU.")
    print(colorama.Fore.LIGHTBLACK_EX+"------"+colorama.Style.RESET_ALL)
    print(purple+
        "Command 40:"+reset+" 'wiki' OR 'wikipedia' - Retrieves a summary off of wikipedia for a topic."
    )
    print(colorama.Fore.LIGHTBLACK_EX+"------"+colorama.Style.RESET_ALL)
    print(green+
        "Command 41:"+reset+" 'google' OR 'search' - Gets a collection of the top search results off of google."
    )
    print(colorama.Fore.LIGHTBLACK_EX+"------"+colorama.Style.RESET_ALL)
    print(blue+
        "Command 42:"+reset+" 'howdoi' OR 'how' - Assists with coding in Python, and provides snippets of code."
    )
    print(colorama.Fore.LIGHTBLACK_EX+"------"+colorama.Style.RESET_ALL)
    print(purple+
        "Command 43:"+reset+" 'dis' OR 'disassemble' - disassembles code into mneumonic-based bytecode."
    )
    print(colorama.Fore.LIGHTBLACK_EX+"------"+colorama.Style.RESET_ALL)
    print(green+
        "Command 44:"+reset+" 'scrape', 'retrieve', or 'ws' - Scrapes the HTML of any web page."
    )
    print(colorama.Fore.LIGHTBLACK_EX+"------"+colorama.Style.RESET_ALL)
    print(blue+
        "Command 45:"+reset+" 'pt' - Literally prints off a document through a printer."
    )
    print(colorama.Fore.LIGHTBLACK_EX+"------"+colorama.Style.RESET_ALL)
    print(purple+
        "Command 46:"+reset+" 'tutorial' - (Recommended) Teaches you how to use the Core Shell in a more in-depth way :)"
    )
    print(colorama.Fore.LIGHTBLACK_EX+"------"+colorama.Style.RESET_ALL)
    print(green+"Command 47:"+reset+" 'clrcache' - This clears the cache.")
    print(colorama.Fore.LIGHTBLACK_EX+"------"+colorama.Style.RESET_ALL)
    print(blue+"Command 48:"+reset+" 'text' - This prints text formatted to your desires.")
    print(colorama.Fore.LIGHTBLACK_EX+"------"+colorama.Style.RESET_ALL)
    print(purple+"Command 49:"+reset+" 'move' or 'mv' - Allows you to move a file from one place to another.")
    print(colorama.Fore.LIGHTBLACK_EX+"------"+colorama.Style.RESET_ALL)
    print(green+"Command 50:"+reset+" 'tasks' or 'pids' or 'running' - Shows you a list of running tasks and their IDs.")
    print(colorama.Fore.LIGHTBLACK_EX+"------"+colorama.Style.RESET_ALL)
    print(blue+"Command 51:"+reset+" 'cmdline' or 'tskline' - Shows you the command line of a task.")
    print(colorama.Fore.LIGHTBLACK_EX+"------"+colorama.Style.RESET_ALL)
    print(purple+"Command 52:"+reset+" 'wget' or 'download' or 'curl' - Downloads a file directly from a source link. This will be the site's HTML source if no redirect is provided.")
    print(colorama.Fore.LIGHTBLACK_EX+"------"+colorama.Style.RESET_ALL)
    print(green+"Command 53:"+reset+" 'makerm' - Creates a reminder.")
    print(colorama.Fore.LIGHTBLACK_EX+"------"+colorama.Style.RESET_ALL)
    print(blue+"Command 54:"+reset+" 'viewrm' or 'remind' - Views reminders.")
    print(colorama.Fore.LIGHTBLACK_EX+"------"+colorama.Style.RESET_ALL)
    print(purple+"Command 55:"+reset+" 'markrm' - Mark/tick off reminders.")
    print(colorama.Fore.LIGHTBLACK_EX+"------"+colorama.Style.RESET_ALL)
    print(green+"Command 56:"+reset+" 'news' - Enable/disable the news on the terminal startup.")
    print(colorama.Fore.LIGHTBLACK_EX+"------"+colorama.Style.RESET_ALL)
    print(blue+"Command 57:"+reset+" 'imgrun' or 'runimg' - Run an AppImage file.")
    print(colorama.Fore.LIGHTBLACK_EX+"------"+colorama.Style.RESET_ALL)
    print(purple+"Command 58:"+reset+" 'chuser' - Change the username of the current user.")
    print(colorama.Fore.LIGHTBLACK_EX+"------"+colorama.Style.RESET_ALL)
    print(green+"Command 59:"+reset+" 'rmdir' - Delete a directory.")
    print(colorama.Fore.LIGHTBLACK_EX+"------"+colorama.Style.RESET_ALL)
    print(blue+"Command 60:"+reset+" 'mkdir' - Create a directory.")
    print(colorama.Fore.LIGHTBLACK_EX+"------"+colorama.Style.RESET_ALL)

@contextmanager
def captureStdOut(output):
    stdout = sys.stdout
    sys.stdout = output
    try:
        yield
    finally:
        sys.stdout = stdout


response = requests.get(url)
listaaaa = response.json()
list2aaa = listaaaa['articles']
string = list2aaa[0]
dicti = string['title']

startms = [
    "You can press ctrl+c to cancel any operation?",
    "Playing games can earn you money! (Not real money, of course)",
    "You can spend money in the shop...",
    "Core OS was meant to be a simple OS that was easy to learn for the public...",
    "Ghostwriter keeps trying to autofill my list of hints and fails miserably...",
    "I'm not sure what this is, but I'm sure it's a game...",
    "You can read messages from the Developers? Type 'messages' to see them!",
    "Xytro originally decided to make a chat engine for all Core OS shells to interact with each other. That's why there's a 'port' command...",
    "This is the third time we've made an operating system... and the second major shell.",
    "This entire project was written in Python.",
    "Python is really easy to learn... why not give it a try?",
    "You can code in Python in Core OS... just try typing in 'python' and see what happens!",
    "ASCII art is cool. You should give it a try!",
    "Xytrophico is a Gaming YouTuber... You should check him out!",
    "The OfficialJibbert account on Twitter was temporarily shut down. Xytro decided to take control of a parody account to commemorate the original.",
    "Oura OS was made to be complex and more low level, whilst this is for everyone.",
    "Core OS is over 4000 lines of code, and the main program doesn't even start until over 1000 lines in!",
    "You might get a special message if you use Core on an international holiday...",
    "Core OS is FREE!",
    "This is a command-line shell... don't expect Windows to suddenly boot up... or do.",
    "Core OS was trending on Replit as of 2nd November 2023?",
    "The $PS1 (terminal design) is changable?"

]
messages2 = ["Rule 1: you're not allowed to delete other people's intro messages.",
    "Thanks so much for using Core OS :)",
    "Hop on Xytrophico's Twitter >>> twitter.com/Xytrophico",
    "Why are you using this?", "I hope you can hear me...",
    "Why not go outside?", "What files are we sorting today...?",
    "GET READY...", "Preparing awesomeness...",
    "I'm not sure what this is, but I think it's a game...", "What is this?",
    "You look great today :D", "Welcome back, good to see you again!",
    "Sup bro :D", "Ready to code?", "Hi there ^-^", "How's your day been?",
    "Welcome back...", "Omae wa mou, shindeiru...", "I'm not here.", "WHAT?!",
    "Do you even read this?", "I like your shirt :)", "Nice hairstyle today!",
    "Hey there.", "Hello, Jibbert.", "Hello, GrimPixelZ.", "Hello, Xytro.",
    "Hello.", "The WOOG is coming.", "How are your streaks going?", "What the winkle...", "Are you back yet?", "You're here!", "I'm bored :/", "I'm even better than ChatGPT. Trust.", "Why are you even here...?", "No Core, No Life.", "Why don't you go outside?", "What are we coding today...", "Programming AI interpreters...", "Implementing transdimentional confribulators...", "Installing hyperdrives...", "I wonder what Core in 4K 60FPS would look like...", "AppImage support when?", "Can Core run EXEs? The question is, can your computer run EXEs?", "Can... you hear me?", "Does anyone actually read these?", "Coding BlackJack...", "uwu", "I wrote this intro :)", "Need... more.. commands...", "nya~", "@everyone", "@everyone @everyone @everyone @everyone @everyone @ever...", "hi saffie", "No.", "Meme approved!", "Meme denied.", "LNs are bad", "Do you know THE way?", "Hop on Roblox a sec...", "Roblox support for Core when?", "Core OS ISN'T FREE!", "Stop trolling.", "no i don't want to", "These are messages that everyone will see on startup.", "but it's funny", "It'll seem so out of context...", "you're not allowed to remove messages, remember", "Yes but now you're just flooding the messages.", "people never read these it doesn't matter lol", "I fixed BlackJack!", "I swear you finished that ages ago?", "no i just played it with my friend and it had some stupid money bug, but it's fixed now :)"
]

message_choice = random.randint(1, 2)

old = os.getcwd()
os.chdir("Games_and_apps")
try:
    os.remove("wins.txt")
except:
    None
try:

    with open("balancer.txt", "r") as balk:
        coler = balk.read()
        balance = int(coler)
except:
    None
    balance = 0

if balance == 0:
    balance = 20
os.chdir(old)

colorama.init()
import geocoder

dsport = 50001
server_port = 55555

g = geocoder.ip('me')
latlng = g.latlng
os.chdir(home_directory)
#####################
if os.path.exists("Documents"):
    None
else:
    os.mkdir("Documents")

if os.path.exists(home_directory + "/Games_and_apps"):
    None
else:
    os.mkdir(home_directory + "/Games_and_apps")

if os.path.exists(home_directory + "/Notes"):
    None
else:
    os.mkdir(home_directory + "/Notes")


def write_version():
    f = open(".version", "w")
    contents = """Core OS, Version 1.2.3, Beta Replit QoL Release, Unix-based"""
    f.write(contents)
    f.close()
    os.chdir(old)


write_version()

if os.path.exists("System"):
    None
else:
    os.mkdir("System")
    old = os.getcwd()
    os.chdir("System")
    writer.write_version()
    writer.write_tree()

if os.path.exists("Messages"):
    None
else:
    os.mkdir("Messages")
    writer.write_message()


####################
def clear():
    os.system("cls" if os.name in ["nt", "dos"] else "clear")


def checkfile():
    global valid, filename
    valid = False
    while valid == False:
        filename = input(colorama.Style.RESET_ALL + termdes + " ")
        try:
            with open(filename) as f:
                None
            valid = True
        except:
            print(colorama.Fore.RED + "\033[1mError: file: '" + filename +
                  "' not found.")
            valid = False


def dirback():
    global parent
    parent = os.path.dirname(os.getcwd())
    os.chdir(parent)


def folderscan():
    DIR = os.getcwd()
    amount = len([
        name for name in os.listdir(DIR)
        if os.path.isfile(os.path.join(DIR, name))
    ])
    if amount == 0:
        print(colorama.Fore.LIGHTBLACK_EX + "This folder is empty." +
              colorama.Style.RESET_ALL)


def folderamount(folder):
    DIR = folder
    amount = len([
        name for name in os.listdir(DIR)
        if os.path.isfile(os.path.join(DIR, name))
    ])
    if amount == 0:
        print(colorama.Fore.LIGHTBLACK_EX + "This folder is empty." +
              colorama.Style.RESET_ALL)
    else:
        print("This folder contains " + colorama.Fore.LIGHTMAGENTA_EX +
              str(amount) + colorama.Style.RESET_ALL + " files")


DIR = 'Documents'
documents = len([
    name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))
])
DIR = 'Messages'
messages = len([
    name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))
])
DIR2 = 'Notes'
notes = len([
    name for name in os.listdir(DIR2)
    if os.path.isfile(os.path.join(DIR2, name))
])
####################
old = os.getcwd()
os.chdir("System")
with open(".version") as f:
    version = f.readlines()
f.close()
# path joining version for other paths
dirback()
os.chdir(old)


####################
def type(text):
    print(colorama.Style.RESET_ALL, end="")
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.03)
    print()


def typerainbow(text):
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
        print(char, end="", flush=True)
        time.sleep(0)
    print(colorama.Style.RESET_ALL)


####################
size = os.get_terminal_size()
columns = int(str(size)[25:27])

#####


def getdirectory():
    dir = os.getcwd()
    dlist = dir.split("/")
    print("------")
    if str(dlist[-1]) != "":
        print("Directory: '" + colorama.Fore.LIGHTMAGENTA_EX + str(dlist[-1]) +
              colorama.Style.RESET_ALL + "'")
    else:
        print("Directory: '" + colorama.Fore.LIGHTMAGENTA_EX + "replit" +
              colorama.Style.RESET_ALL + "'")


def ls():
    return os.listdir(os.getcwd())


def lista():
    files = os.listdir(os.getcwd())
    for location in files:
        sizea = int(os.path.getsize(str(os.getcwd()) + "/" + location))
        if sizea < 1000:
            size = str(
                os.path.getsize(str(os.getcwd()) + "/" + location)) + " B"
        if sizea < 1000000 and sizea > 1000:
            size = str(
                round(
                    os.path.getsize(str(os.getcwd()) + "/" + location) /
                    1000)) + " KB"
        if sizea >= 1000000 and sizea < 1000000000:
            size = str(
                round(
                    int(os.path.getsize(str(os.getcwd()) + "/" + location)) /
                    1000000)) + " MB"
        if sizea >= 1000000000 and sizea < 1000000000000:
            size = str(
                round(
                    int(os.path.getsize(str(os.getcwd()) + "/" + location)) /
                    1000000000)) + " GB"
        size = str(size)

        if location not in systemdirs:
            print(f"{'🗎' if os.path.isfile(location) else '🗀'}", end = "  ")    
            print("- '" + colorama.Fore.LIGHTMAGENTA_EX + location +colorama.Style.RESET_ALL + "'",end=" ")
        else:
            print(f"{'🗎' if os.path.isfile(location) else '🗀'}", end = "  ")    
            print("- '" + colorama.Fore.LIGHTCYAN_EX + location +colorama.Style.RESET_ALL + "'",end=" ")
        print(f"({'file' if os.path.isfile(location) else 'folder'})" + " - " +
              colorama.Fore.LIGHTGREEN_EX + size + colorama.Style.RESET_ALL)

        time.sleep(0.02)


def listfiles():
    files = os.listdir(os.getcwd())
    for location in files:
        sizea = int(os.path.getsize(str(os.getcwd()) + "/" + location))
        if sizea < 1000:
            size = str(
                os.path.getsize(str(os.getcwd()) + "/" + location)) + " B"
        if sizea < 1000000 and sizea > 1000:
            size = str(
                round(
                    os.path.getsize(str(os.getcwd()) + "/" + location) /
                    1000)) + " KB"
        if sizea >= 1000000 and sizea < 1000000000:
            size = str(
                round(
                    int(os.path.getsize(str(os.getcwd()) + "/" + location)) /
                    1000000)) + " MB"
        if sizea >= 1000000000 and sizea < 1000000000000:
            size = str(
                round(
                    int(os.path.getsize(str(os.getcwd()) + "/" + location)) /
                    1000000000)) + " GB"
        size = str(size)

        if os.path.isfile(location):
            if location not in systemdirs:
                print(f"{'🗎' if os.path.isfile(location) else '🗀'}", end = "  ")    
                print("- '" + colorama.Fore.LIGHTMAGENTA_EX + location +colorama.Style.RESET_ALL + "'",end=" ")
            else:
                print(f"{'🗎' if os.path.isfile(location) else '🗀'}", end = "  ")    
                print("- '" + colorama.Fore.LIGHTCYAN_EX + location +colorama.Style.RESET_ALL + "'",end=" ")
            print(f"({'file' if os.path.isfile(location) else 'folder'})" +
                  " - " + colorama.Fore.LIGHTGREEN_EX + size +
                  colorama.Style.RESET_ALL)

            time.sleep(0.02)

def listfilesExt(ext):
    filesO = os.listdir(os.getcwd())
    files = []
    for item in filesO:
        if item.endswith(ext):
            files.append(item)
        else:
            None
    if len(files) > 0:
        for location in files:
            sizea = int(os.path.getsize(str(os.getcwd()) + "/" + location))
            if sizea < 1000:
                size = str(
                    os.path.getsize(str(os.getcwd()) + "/" + location)) + " B"
            if sizea < 1000000 and sizea > 1000:
                size = str(
                    round(
                        os.path.getsize(str(os.getcwd()) + "/" + location) /
                        1000)) + " KB"
            if sizea >= 1000000 and sizea < 1000000000:
                size = str(
                    round(
                        int(os.path.getsize(str(os.getcwd()) + "/" + location)) /
                        1000000)) + " MB"
            if sizea >= 1000000000 and sizea < 1000000000000:
                size = str(
                    round(
                        int(os.path.getsize(str(os.getcwd()) + "/" + location)) /
                        1000000000)) + " GB"
            size = str(size)

            if os.path.isfile(location):
                if location not in systemdirs:
                    print(f"{'🗎' if os.path.isfile(location) else '🗀'}", end = "  ")    
                    print("- '" + colorama.Fore.LIGHTMAGENTA_EX + location +colorama.Style.RESET_ALL + "'",end=" ")
                else:
                    print(f"{'🗎' if os.path.isfile(location) else '🗀'}", end = "  ")    
                    print("- '" + colorama.Fore.LIGHTCYAN_EX + location +colorama.Style.RESET_ALL + "'",end=" ")
                print(f"({'file' if os.path.isfile(location) else 'folder'})" +
                      " - " + colorama.Fore.LIGHTGREEN_EX + size +
                      colorama.Style.RESET_ALL)

                time.sleep(0.02)
    else:
        print(f"{black}No '{ext}' files found.{reset}")





def listfolders():
    files = os.listdir(os.getcwd())
    for location in files:
        sizea = int(os.path.getsize(str(os.getcwd()) + "/" + location))
        if sizea < 1000:
            size = str(
                os.path.getsize(str(os.getcwd()) + "/" + location)) + " B"
        if sizea < 1000000 and sizea > 1000:
            size = str(
                round(
                    os.path.getsize(str(os.getcwd()) + "/" + location) /
                    1000)) + " KB"
        if sizea >= 1000000 and sizea < 1000000000:
            size = str(
                round(
                    int(os.path.getsize(str(os.getcwd()) + "/" + location)) /
                    1000000)) + " MB"
        if sizea >= 1000000000 and sizea < 1000000000000:
            size = str(
                round(
                    int(os.path.getsize(str(os.getcwd()) + "/" + location)) /
                    1000000000)) + " GB"
        size = str(size)

        if not os.path.isfile(location):
            if location not in systemdirs:
                print(f"{'🗎' if os.path.isfile(location) else '🗀'}", end = "  ")    
                print("- '" + colorama.Fore.LIGHTMAGENTA_EX + location +colorama.Style.RESET_ALL + "'",end=" ")
            else:
                print(f"{'🗎' if os.path.isfile(location) else '🗀'}", end = "  ")    
                print("- '" + colorama.Fore.LIGHTCYAN_EX + location +colorama.Style.RESET_ALL + "'",end=" ")
            print(f"({'file' if os.path.isfile(location) else 'folder'})" +
                  " - " + colorama.Fore.LIGHTGREEN_EX + size +
                  colorama.Style.RESET_ALL)

            time.sleep(0.02)


def printlogo():
    txt1 = "T  ¦░█████╗░░█████╗░██████╗░███████╗¦"
    x = txt1.center(columns)
    typerainbow(x)

    txt2 = "r  ¦██╔══██╗██╔══██╗██╔══██╗██╔════╝¦"
    x = txt2.center(columns)
    typerainbow(x)

    txt3 = "i  ¦██║░░╚═╝██║░░██║██████╔╝█████╗░░¦"
    x = txt3.center(columns)
    typerainbow(x)

    txt4 = "t  ¦██║░░██╗██║░░██║██╔══██╗██╔══╝░░¦"
    x = txt4.center(columns)
    typerainbow(x)

    txt5 = "e  ¦╚█████╔╝╚█████╔╝██║░░██║███████╗¦"
    x = txt5.center(columns)
    typerainbow(x)

    txt6 = "c  ¦░╚════╝░░╚════╝░╚═╝░░╚═╝╚══════╝¦"
    x = txt6.center(columns)
    typerainbow(x)

    txt7 = "h  ----------------------------------"
    x = txt7.center(columns)
    typerainbow(x)


def fullls():
    getdirectory()
    print("------")
    lista()
    folderscan()
    print("------")


def donotes():
    old = os.getcwd()
    os.chdir(home_directory + "Notes")

    print("------")
    try:
        if notes == 0:
            print("You don't have any notes. Let's make one!")
        else:
            if notes == 1:
                print("You currently have" + colorama.Fore.LIGHTMAGENTA_EX +
                      " 1 " + colorama.Style.RESET_ALL + "note.")
                print("------")
            else:
                print("You currently have " + colorama.Fore.LIGHTMAGENTA_EX +
                      str(notes) + colorama.Style.RESET_ALL + " notes.")
        print(
            "Would you like to do?...\n\n" + colorama.Fore.LIGHTMAGENTA_EX +
            "1)" + colorama.Style.RESET_ALL + " Create a note\n-- OR --\n" +
            colorama.Fore.LIGHTMAGENTA_EX + "2)" + colorama.Style.RESET_ALL +
            " Append (add) to a note?\n\nPlease use numbers (1 or 2) to answer."
        )
        valid = False
        while valid == False:
            choice = input(colorama.Style.RESET_ALL + termdes + " ")
            choice = str(choice)
            answers = ["1", "2"]
            if choice not in answers:
                print("Please use the" + colorama.Fore.LIGHTMAGENTA_EX +
                      " numbers 1 or 2 " + colorama.Style.RESET_ALL +
                      "to answer.")
                valid = False

            elif choice == "1" or choice == "2":
                valid = True
                break
        ###########################################################
        if choice == "1":
            print("------")
            print("What is the title of the note? ")
            valid = False
            while valid == False:
                title = input(colorama.Style.RESET_ALL + termdes + " ")
                if title.strip(" ") == "":
                    print("The name of the note cannot be blank!")
                    valid = False
                else:
                    valid = True
                    break

            filename = title + ".txt"
            f = open(filename, "w")
            print("------")
            print(
                colorama.Fore.LIGHTCYAN_EX +
                "Please write the note data below, and press Ctrl + C to save and exit."
                + colorama.Style.RESET_ALL)
            counter = 0
            while True:
                try:
                    counter = counter + 1
                    line = input(colorama.Style.RESET_ALL + colorama.Fore.LIGHTMAGENTA_EX + str(counter) +
                                 ": " + colorama.Style.RESET_ALL)
                    f.write(line + "\n")
                except KeyboardInterrupt:
                    try:
                        print("---")
                        f.close()
                        print(colorama.Fore.LIGHTGREEN_EX +
                              "File successfully saved - '" +
                              colorama.Fore.LIGHTMAGENTA_EX + filename +
                              colorama.Fore.LIGHTGREEN_EX + "'" +
                              colorama.Style.RESET_ALL +
                              "\nFind your file in the folder 'Notes'")
                        print("------")
                        os.chdir(old)
                        break
                    except:
                        print()
                        print(colorama.Fore.RED + "File failed to save..." +
                              colorama.Style.RESET_ALL)
                        print("------")
                        os.chdir(old)
                        break
        if choice != "1":
            print("------")
            print("Which note would you like to add to?")
            dir = os.getcwd()
            dlist = dir.split("/")
            print("------")
            if str(dlist[-1]) != "":
                print("Directory: '" + colorama.Fore.LIGHTMAGENTA_EX +
                      str(dlist[-1]) + colorama.Style.RESET_ALL + "'")
            else:
                print("Directory: '" + colorama.Fore.LIGHTMAGENTA_EX +
                      "replit" + colorama.Style.RESET_ALL + "'")

            print("------")
            listfiles()
            if notes == 0:
                print(colorama.Fore.LIGHTBLACK_EX +
                      "This folder is empty,\nPress Ctrl+C to cancel..." +
                      colorama.Style.RESET_ALL)
            print("------")
            valid = False
            while valid == False:
                filename = input(colorama.Style.RESET_ALL + termdes + " ")
                try:
                    with open(filename) as f:
                        None
                    valid = True
                except:
                    print(colorama.Fore.RED + "\033[1mError: file: '" +
                          filename + "' not found.")
                    valid = False
            with open(filename) as f:
                contents = f.readlines()
            f.close()
            print("------")
            print("The contents of '" + colorama.Fore.LIGHTMAGENTA_EX +
                  filename + colorama.Style.RESET_ALL + "':")
            print("------")
            for line in contents:
                print(line, end="")
                time.sleep(0.02)
            print()
            print("------")
            f = open(filename, "a")
            print(
                colorama.Fore.LIGHTCYAN_EX +
                "Please write the note data below, and press Ctrl + C to save and exit."
                + colorama.Style.RESET_ALL)
            counter = 0
            while True:
                try:
                    counter = counter + 1
                    line = input(colorama.Style.RESET_ALL + colorama.Fore.LIGHTMAGENTA_EX + str(counter) +
                                 ": " + colorama.Style.RESET_ALL)
                    f.write(line + "\n")
                except KeyboardInterrupt:
                    try:
                        print("---")
                        f.close()
                        print(colorama.Fore.LIGHTGREEN_EX +
                              "File successfully saved - '" +
                              colorama.Fore.LIGHTMAGENTA_EX + filename +
                              colorama.Fore.LIGHTGREEN_EX + "'" +
                              colorama.Style.RESET_ALL +
                              "\nFind your file in the folder 'Notes'")
                        print("------")
                        os.chdir(old)
                        break
                    except:
                        print()
                        print(colorama.Fore.RED + "File failed to save..." +
                              colorama.Style.RESET_ALL)
                        print("------")
                        os.chdir(old)
                        break

    except KeyboardInterrupt:
        print()
        print(colorama.Fore.RED + "Cancelling operation..." +
              colorama.Style.RESET_ALL)
        os.chdir(old)






####################
printlogo()
time.sleep(1)

try:
    length = len(specialMessage)-1
    msg = "\n" + colorama.Fore.LIGHTMAGENTA_EX + specialMessage + colorama.Style.RESET_ALL
    txt = msg
    msg = txt.center(columns)
except:
    if message_choice == 1:
        length = len(startms) - 1
        msg = "\n" + colorama.Fore.LIGHTCYAN_EX + "Did you know... " + startms[
            random.randint(0, length)]
        txt = msg
        msg = txt.center(columns)

    if message_choice == 2:
        length = len(messages2) - 1
        msg = "\n" + colorama.Fore.LIGHTCYAN_EX + messages2[random.randint(
            0, length)]
        txt = msg
        msg = txt.center(columns)

print(colorama.Fore.LIGHTMAGENTA_EX, end="")
for x in range(0, 2):
    txt = colorama.Style.RESET_ALL + "Loading [•----]"
    x = txt.center(columns)
    print(x)
    print(msg)
    time.sleep(0.3)
    os.system("cls" if os.name in ["nt", "dos"] else "clear")
    printlogo()

    txt = "Loading [••---]"
    x = txt.center(columns)
    print(x)
    print(msg)
    time.sleep(0.3)
    os.system("cls" if os.name in ["nt", "dos"] else "clear")
    printlogo()

    txt = "Loading [•••--]"
    x = txt.center(columns)
    print(x)
    print(msg)
    time.sleep(0.3)
    os.system("cls" if os.name in ["nt", "dos"] else "clear")
    printlogo()

    txt = "Loading [••••-]"
    x = txt.center(columns)
    print(x)
    print(msg)
    time.sleep(0.3)
    os.system("cls" if os.name in ["nt", "dos"] else "clear")
    printlogo()

    txt = "Loading [•••••]"
    x = txt.center(columns)
    print(x)
    print(msg)
    time.sleep(0.3)
    os.system("cls" if os.name in ["nt", "dos"] else "clear")
    printlogo()

print(colorama.Fore.LIGHTGREEN_EX, end="")
txt = "Complete!"
x = txt.center(columns)
print(x)

print(colorama.Style.RESET_ALL, end="")
time.sleep(2)
####################
os.system("cls" if os.name in ["nt", "dos"] else "clear")
####################
##########

####################
day = datetime.today().isoweekday()

if day == 1:
    day = "Monday"
if day == 2:
    day = "Tuesday"
if day == 3:
    day = "Wednesday"
if day == 4:
    day = "Thursday"
if day == 5:
    day = "Friday"
if day == 6:
    day = "Saturday"
if day == 7:
    day = "Sunday"

date = datetime.today().strftime("%B %d %Y")
def set_time():
    global current_time, now
    now = datetime.now()

    date_string = now.strftime("%d/%m/%Y")
    time_string = now.strftime("%H:%M:%S")

    date_checks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
    month_checks = [3, 4, 5, 6, 7, 8, 9, 10]
    date = int(date_string[0:2])
    month = int(date_string[3:5])
    valid = False
    if date in date_checks and month in month_checks:

        if month == 3:
            if date >= 26:
                valid = True
            else:
                valid = False

        elif month == 10:
            if date <= 29:
                valid = True
            else:
                valid = False


        elif month in month_checks and month != 3 and month != 10:
            valid = True


        if valid == True:

            check = time_string[0:2]

            if check[0] == "0":
                filler = "0" + str(int(time_string[0:2]) + 1)
                if len(filler) == 3:
                    filler = filler[1] + filler[2]
            else:
                filler = str(int(time_string[0:2]) + 1)

            temp = []
            for item in time_string:
                temp.append(item)

            temp[0] = filler[0]
            temp[1] = filler[1]

            current_time = ""

            for item in temp:
                current_time = current_time + item
    else:
        current_time = time_string

    if valid == False:
        current_time = time_string


set_time()
####################
def welcome():
    global USER, day, date, current_time, messages, version, balance, newsActive
    type("Welcome, " + colorama.Fore.LIGHTMAGENTA_EX + str(USER) +
         colorama.Style.RESET_ALL + "!")

    print("----------")
    print("Balance:" + colorama.Fore.YELLOW + " £" + str(balance) +
          colorama.Style.RESET_ALL)
    if newsActive == True:
        print("-----")
        print("Latest news: " + colorama.Fore.RED + str(dicti) +
          colorama.Style.RESET_ALL)
        print("-----")
    else:
        print("----------")
    print("Date and time:" + colorama.Fore.LIGHTMAGENTA_EX + " " + day + ",",
          date + ", " + str(current_time) + colorama.Style.RESET_ALL)
    print("Messages: " + colorama.Fore.LIGHTMAGENTA_EX + str(messages) +
          colorama.Style.RESET_ALL)
    print("Notes: " + colorama.Fore.LIGHTMAGENTA_EX + str(notes) +
          colorama.Style.RESET_ALL)
    print("Version: " + colorama.Fore.LIGHTMAGENTA_EX + str(version[0]) +
          colorama.Style.RESET_ALL)
    print("----------")
    print()


f = open("installcache.txt", "w+")
f.close()
os.system("python3 -m pip install howdoi > installcache.txt")
os.system("python3 -m pip install wikipedia > installcache.txt")
clear()
welcome()

####################

commands = [
    "help", "messages", "dirbk", "chdir", "ls", "clear", "cls", "date",
    "version", "location", "write", "note", "create", "document", "read",
    "execute", "run", "python", "py", "python3", "home", "homedir", "hd",
    "tree", "dtree", "dirtree", "whoami", "username", "user", "name", "design",
    "properties", "rename", "rnr", "runner", "filewd", "play", "open",
    "delete", "remove", "view", "chport", "port", "ip", "ipconfig", "find",
    "battery", "power", "findstr", "rmstr", "rmline", "command", "shop", "buy",
    "sort", "duplicate", "disk", "print", "rng", "system", "backup", "health",
    "performance"
    "diskchk", "gpu", "diskchk", "wiki", "wikipedia", "google", "search",
    "howdoi", "how", "dis", "disassemble", "cd", "pwd", "cwd", "pt", "scrape",
    "retrieve", "ws", "tutorial", "clrcache", "mv", "move", "cmdline", "tskline", "pids", "running", "tasks", "download", "curl", "wget", "makerm", "viewrm", "remind", "markrm", "imgrun", "runimg", "news", "chuser", "rmdir", "mkdir"
]
termdes = colorama.Fore.MAGENTA + "~ €" + colorama.Style.RESET_ALL
############################






os.chdir(home_directory)
while True:
    old = os.getcwd()
    try:
        os.chdir(home_directory+"/System")
        f = open("Reminders.log", "r")
        contents = f.read()
        if contents.strip() == "":
            os.remove("Reminders.log")
        f.close()
    except:
        None
    os.chdir(old)
    set_time()
    if balance == 0:
        balance = 20

    old = os.getcwd()
    if os.getcwd() != home_directory:
        os.chdir(home_directory)

        try:
            os.chdir(home_directory + "/Games_and_apps")
            exists = os.path.exists("wins.txt")

            if exists == False:
                bal = open("balancer.txt", "w")
                bal.write(str(balance))
                bal.close()
            else:
                try:
                    with open("balancer.txt", "r") as balk:
                        coler = balk.read()
                        balance = int(coler)
                    os.remove("wins.txt")
                except:
                    None
                    print("woops!")
                    os.remove("wins.txt")

            try:
                if os.path.getsize("wins.txt") != 0:
                    with open("wins.txt") as f:
                        contents = f.read()
                        moneyearned = int(contents)

                    f.close()
                    os.remove("wins.txt")
                    os.chdir(old)
                os.chdir(old)
            except:
                os.chdir(old)
            os.chdir(old)
        except:
            print("Woops! An error ocurred whilst processing your balance...")
    os.chdir(old)

    date = datetime.today().strftime("%B %d %Y")

    if os.getcwd() != home_directory:
        os.chdir(home_directory)

    set_time()

    DIR = home_directory + "/Messages"
    messages = len([
        name for name in os.listdir(DIR)
        if os.path.isfile(os.path.join(DIR, name))
    ])
    DIR2 = home_directory + "/Notes"
    notes = len([
        name for name in os.listdir(DIR2)
        if os.path.isfile(os.path.join(DIR2, name))
    ])
    DIR = home_directory + "/Documents"
    documents = len([
        name for name in os.listdir(DIR)
        if os.path.isfile(os.path.join(DIR, name))
    ])

    os.chdir(old)

    welcome = "\033[1m" + colorama.Fore.LIGHTCYAN_EX + USER + colorama.Fore.LIGHTGREEN_EX + "@Core - " + colorama.Fore.LIGHTMAGENTA_EX + colorama.Style.RESET_ALL + colorama.Fore.LIGHTMAGENTA_EX + str(
        os.getcwd())
    prompt = welcome + " " + termdes + " "
    request = input(colorama.Style.RESET_ALL + prompt + colorama.Fore.LIGHTCYAN_EX)
    print(colorama.Style.RESET_ALL, end = "")
    request = request.lower()
    request = request.strip(" ")

    try:
        eval(request)
        int(eval(request))
        print("------")
        print(colorama.Fore.LIGHTMAGENTA_EX + str(eval(request)) + colorama.Style.RESET_ALL)
        equValue = True
        print("------")
    except:
        equValue = False
        if request not in commands and request.strip(" ") != "" and equValue == False:

            print(colorama.Fore.RED + "\033[1mMono - Command '" + request +
                  "' not found.\nType 'help' for a list of commands." +
                  colorama.Style.RESET_ALL)
            if len(request) <= 10:
                for item in commands:
                    if item in request:
                        print("----------")
                        print(colorama.Fore.RED +
                              "\033[1mMonoCorrect - Did you mean: '" + item +
                              "'?" + colorama.Style.RESET_ALL)
                        print("----------")
                        break
                    check = 0
                    iteml = list(item)
                    for subject in iteml:
                        if subject in request:
                            check = check + 1
                    if check == len(iteml) or check == len(iteml) - 1:
                        if item != "ls":
                            print("----------")
                            print(colorama.Fore.RED +
                                  "\033[1mMonoCorrect - Did you mean: '" + item +
                                  "'?" + colorama.Style.RESET_ALL)
                            print("----------")
                            break

    ##################################
        if request == "help":
            printhelp()
        if request == "dirbk":
            dirback()

        if request == "chdir" or request == "cd":
            try:
                print("------")
                print("Which folder would you like to enter?")
                print("------")
                listfolders()
                valid = False

                while valid == False:
                    selection = input(colorama.Style.RESET_ALL + termdes + " ")
                    try:
                        os.chdir(selection)
                        print(colorama.Fore.LIGHTGREEN_EX +
                              "Successfully entered folder: '" +
                              colorama.Fore.LIGHTMAGENTA_EX + selection +
                              colorama.Fore.LIGHTGREEN_EX + "'" +
                              colorama.Style.RESET_ALL)
                        print("------")
                        valid = True
                    except:
                        print(colorama.Fore.RED + "\033[1mError: folder '" +
                              selection + "' not found.")
                        valid = False
            except KeyboardInterrupt:
                print()
                print(colorama.Fore.RED + "Cancelling operation..." +
                      colorama.Style.RESET_ALL)

        if request == "messages":
            if messages != 0:
                print("------")
            try:
                if messages == 0:
                    print("You currently have no messages.")
                    print("------")
                else:
                    if messages == 1:
                        print("You currently have" +
                              colorama.Fore.LIGHTMAGENTA_EX + " 1 " +
                              colorama.Style.RESET_ALL + "message.")
                        print("------")
                    else:
                        print("You currently have " +
                              colorama.Fore.LIGHTMAGENTA_EX + str(messages) +
                              colorama.Style.RESET_ALL + " messages.")

                    old = os.getcwd()
                    os.chdir(home_directory + "/Messages")

                    print("Which file would you like to read?")
                    print("------")
                    listfiles()
                    if messages == 0:
                        print(colorama.Fore.LIGHTBLACK_EX +
                              "This folder is empty,\nPress Ctrl+C to cancel..." +
                              colorama.Style.RESET_ALL)
                    print()
                    valid = False
                    while valid == False:
                        selection = input(colorama.Style.RESET_ALL + termdes + " ")
                        try:
                            with open(selection) as f:
                                contents = f.readlines()
                            f.close()
                            print()
                            print(colorama.Fore.LIGHTGREEN_EX +
                                  "Successfully obtained file contents." +
                                  colorama.Style.RESET_ALL)
                            print()
                            print(colorama.Fore.LIGHTMAGENTA_EX +
                                  "Message contents:\n" + colorama.Style.RESET_ALL)
                            print("----------------")
                            for line in contents:
                                print(line, end="")
                                time.sleep(0.02)
                            print()
                            print("----------------")
                            print()
                            valid = True
                            os.chdir(old)
                        except:
                            print(colorama.Fore.RED + "\033[1mError: file: '" +
                                  selection + "' not found.")
                            valid = False

            except KeyboardInterrupt:
                print()
                print(colorama.Fore.RED + "Cancelling operation..." +
                      colorama.Style.RESET_ALL)

        if request == "ls":
            try:
                getdirectory()
                print("------")
                lista()
                folderscan()
                print("------")
            except KeyboardInterrupt:
                print()
                print(colorama.Fore.RED + "Cancelling operation..." +
                      colorama.Style.RESET_ALL)

        if request == "clear" or request == "cls":
            os.system("cls" if os.name in ["nt", "dos"] else "clear")
            type("Welcome, " + colorama.Fore.LIGHTMAGENTA_EX + str(USER) +
                 colorama.Style.RESET_ALL + "!")

            print("----------")
            print("Balance:" + colorama.Fore.YELLOW + " £" + str(balance) +
                  colorama.Style.RESET_ALL)
            if newsActive == True:
                print("-----")
                print("Latest news: " + colorama.Fore.RED + str(dicti) +
                  colorama.Style.RESET_ALL)
                print("-----")
            else:
                print("----------")
            print(
                "Date and time:" + colorama.Fore.LIGHTMAGENTA_EX + " " + day + ",",
                date + ", " + str(current_time) + colorama.Style.RESET_ALL)
            print("Messages: " + colorama.Fore.LIGHTMAGENTA_EX + str(messages) +
                  colorama.Style.RESET_ALL)
            print("Notes: " + colorama.Fore.LIGHTMAGENTA_EX + str(notes) +
                  colorama.Style.RESET_ALL)
            print("Version: " + colorama.Fore.LIGHTMAGENTA_EX + str(version[0]) +
                  colorama.Style.RESET_ALL)
            print("----------")
            print()

        if request == "date":
            date = datetime.today().strftime("%B %d %Y")

            set_time()
            print("------")
            print(
                "Date and time:" + colorama.Fore.LIGHTMAGENTA_EX + " " + day + ",",
                date + ", " + str(current_time) + colorama.Style.RESET_ALL)
            print("------")

        if request == "version":
            print("------")
            print("Version: " + colorama.Fore.LIGHTMAGENTA_EX + str(version[0]) +
                  colorama.Style.RESET_ALL)
            print("------")
            print()

        if request == "location":
            print("------")
            print(colorama.Fore.LIGHTMAGENTA_EX + str(latlng) +
                  colorama.Style.RESET_ALL)
            print("------")

        if request == "write" or request == "note":
            old = os.getcwd()
            os.chdir(home_directory + "/Notes")

            print("------")
            try:
                if notes == 0:
                    print("You don't have any notes. Let's make one!")
                else:
                    if notes == 1:
                        print("You currently have" +
                              colorama.Fore.LIGHTMAGENTA_EX + " 1 " +
                              colorama.Style.RESET_ALL + "note.")
                        print("------")
                    else:
                        print("You currently have " +
                              colorama.Fore.LIGHTMAGENTA_EX + str(notes) +
                              colorama.Style.RESET_ALL + " notes.")
                print(
                    "Would you like to do?...\n\n" +
                    colorama.Fore.LIGHTMAGENTA_EX + "1)" +
                    colorama.Style.RESET_ALL + " Create a note\n-- OR --\n" +
                    colorama.Fore.LIGHTMAGENTA_EX + "2)" +
                    colorama.Style.RESET_ALL +
                    " Append (add) to a note?\n\nPlease use numbers (1 or 2) to answer."
                )
                valid = False
                while valid == False:
                    choice = input(colorama.Style.RESET_ALL + termdes + " ")
                    choice = str(choice)
                    answers = ["1", "2"]
                    if choice not in answers:
                        print("Please use the" + colorama.Fore.LIGHTMAGENTA_EX +
                              " numbers 1 or 2 " + colorama.Style.RESET_ALL +
                              "to answer.")
                        valid = False

                    elif choice == "1" or choice == "2":
                        valid = True
                        break
                ###########################################################
                if choice == "1":
                    print("------")
                    print("What is the title of the note? ")
                    valid = False
                    while valid == False:
                        title = input(colorama.Style.RESET_ALL + termdes + " ")
                        if title.strip(" ") == "":
                            print("The name of the note cannot be blank!")
                            valid = False
                        else:
                            valid = True
                            break

                    filename = title + ".txt"
                    f = open(filename, "w")
                    print("------")
                    print(
                        colorama.Fore.LIGHTCYAN_EX +
                        "Please write the note data below, and press Ctrl + C to save and exit."
                        + colorama.Style.RESET_ALL)
                    counter = 0
                    while True:
                        try:
                            counter = counter + 1
                            line = input(colorama.Style.RESET_ALL + colorama.Fore.LIGHTMAGENTA_EX +
                                         str(counter) + ": " +
                                         colorama.Style.RESET_ALL)
                            f.write(line + "\n")
                        except KeyboardInterrupt:
                            try:
                                print("---")
                                f.close()
                                print(colorama.Fore.LIGHTGREEN_EX +
                                      "File successfully saved - '" +
                                      colorama.Fore.LIGHTMAGENTA_EX + filename +
                                      colorama.Fore.LIGHTGREEN_EX + "'" +
                                      colorama.Style.RESET_ALL +
                                      "\nFind your file in the folder 'Notes'")
                                print("------")
                                os.chdir(old)
                                break
                            except:
                                print()
                                print(colorama.Fore.RED +
                                      "File failed to save..." +
                                      colorama.Style.RESET_ALL)
                                print("------")
                                os.chdir(old)
                                break
                if choice != "1":
                    print("------")
                    print("Which note would you like to add to?")
                    dir = os.getcwd()
                    dlist = dir.split("/")
                    print("------")
                    if str(dlist[-1]) != "":
                        print("Directory: '" + colorama.Fore.LIGHTMAGENTA_EX +
                              str(dlist[-1]) + colorama.Style.RESET_ALL + "'")
                    else:
                        print("Directory: '" + colorama.Fore.LIGHTMAGENTA_EX +
                              "replit" + colorama.Style.RESET_ALL + "'")

                    print("------")
                    listfiles()
                    if notes == 0:
                        print(colorama.Fore.LIGHTBLACK_EX +
                              "This folder is empty,\nPress Ctrl+C to cancel..." +
                              colorama.Style.RESET_ALL)
                    print("------")
                    valid = False
                    while valid == False:
                        filename = input(colorama.Style.RESET_ALL + termdes + " ")
                        try:
                            with open(filename) as f:
                                None
                            valid = True
                        except:
                            print(colorama.Fore.RED + "\033[1mError: file: '" +
                                  filename + "' not found.")
                            valid = False
                    with open(filename) as f:
                        contents = f.readlines()
                    f.close()
                    print("------")
                    print("The contents of '" + colorama.Fore.LIGHTMAGENTA_EX +
                          filename + colorama.Style.RESET_ALL + "':")
                    print("------")
                    for line in contents:
                        print(line, end="")
                        time.sleep(0.02)
                    print()
                    print("------")
                    f = open(filename, "a")
                    print(
                        colorama.Fore.LIGHTCYAN_EX +
                        "Please write the note data below, and press Ctrl + C to save and exit."
                        + colorama.Style.RESET_ALL)
                    counter = 0
                    while True:
                        try:
                            counter = counter + 1
                            line = input(colorama.Style.RESET_ALL + colorama.Fore.LIGHTMAGENTA_EX +
                                         str(counter) + ": " +
                                         colorama.Style.RESET_ALL)
                            f.write(line + "\n")
                        except KeyboardInterrupt:
                            try:
                                print("---")
                                f.close()
                                print(colorama.Fore.LIGHTGREEN_EX +
                                      "File successfully saved - '" +
                                      colorama.Fore.LIGHTMAGENTA_EX + filename +
                                      colorama.Fore.LIGHTGREEN_EX + "'" +
                                      colorama.Style.RESET_ALL +
                                      "\nFind your file in the folder 'Notes'")
                                print("------")
                                os.chdir(old)
                                break
                            except:
                                print()
                                print(colorama.Fore.RED +
                                      "File failed to save..." +
                                      colorama.Style.RESET_ALL)
                                print("------")
                                os.chdir(old)
                                break

            except KeyboardInterrupt:
                print()
                print(colorama.Fore.RED + "Cancelling operation..." +
                      colorama.Style.RESET_ALL)
                os.chdir(old)

        if request == "print" or request == "echo":
            print("------")
            print(
                f"What do you want to {colorama.Fore.LIGHTMAGENTA_EX}print{colorama.Style.RESET_ALL}?"
            )
            echo = input(colorama.Style.RESET_ALL + termdes + " ")
            print("---")
            print(echo)
            print("---")

        if request == "create" or request == "document":
            old = os.getcwd()
            os.chdir(home_directory + "/Documents")

            print("------")
            try:
                if documents == 0:
                    print("You don't have any documents. Let's make one!")
                else:
                    if documents == 1:
                        print("You currently have" +
                              colorama.Fore.LIGHTMAGENTA_EX + " 1 " +
                              colorama.Style.RESET_ALL + "document.")
                        print("------")
                    else:
                        print("You currently have " +
                              colorama.Fore.LIGHTMAGENTA_EX + str(documents) +
                              colorama.Style.RESET_ALL + " documents.")
                print(
                    "Would you like to do?...\n\n" +
                    colorama.Fore.LIGHTMAGENTA_EX + "1)" +
                    colorama.Style.RESET_ALL + " Create a file\n-- OR --\n" +
                    colorama.Fore.LIGHTMAGENTA_EX + "2)" +
                    colorama.Style.RESET_ALL +
                    " Append (add) to a file?\n\nPlease use numbers (1 or 2) to answer."
                )
                valid = False
                while valid == False:
                    choice = input(colorama.Style.RESET_ALL + termdes + " ")
                    choice = str(choice)
                    answers = ["1", "2"]
                    if choice not in answers:
                        print("Please use the" + colorama.Fore.LIGHTMAGENTA_EX +
                              " numbers 1 or 2 " + colorama.Style.RESET_ALL +
                              "to answer.")
                        valid = False

                    elif choice == "1" or choice == "2":
                        valid = True
                        break
                ###########################################################
                if choice == "1":
                    print("------")
                    print("What is the title of the file (with file extension)? ")
                    valid = False
                    while valid == False:
                        title = input(colorama.Style.RESET_ALL + termdes + " ")
                        if title.strip(" ") == "":
                            print("The name of the file cannot be blank!")
                            valid = False
                        else:
                            valid = True
                            break

                    filename = title
                    f = open(filename, "w")
                    print("------")
                    print(
                        colorama.Fore.LIGHTCYAN_EX +
                        "Please write the file data below, and press Ctrl + C to save and exit."
                        + colorama.Style.RESET_ALL)
                    counter = 0
                    while True:
                        try:
                            counter = counter + 1
                            line = input(colorama.Style.RESET_ALL + colorama.Fore.LIGHTMAGENTA_EX +
                                         str(counter) + ": " +
                                         colorama.Style.RESET_ALL)
                            f.write(line + "\n")
                        except KeyboardInterrupt:
                            try:
                                print("---")
                                f.close()
                                print(colorama.Fore.LIGHTGREEN_EX +
                                      "File successfully saved - '" +
                                      colorama.Fore.LIGHTMAGENTA_EX + filename +
                                      colorama.Fore.LIGHTGREEN_EX + "'" +
                                      colorama.Style.RESET_ALL +
                                      "\nFind your file in the folder 'Documents'")
                                print("------")
                                os.chdir(old)
                                break
                            except:
                                print()
                                print(colorama.Fore.RED +
                                      "File failed to save..." +
                                      colorama.Style.RESET_ALL)
                                print("------")
                                os.chdir(old)
                                break
                if choice != "1":
                    print("------")
                    print("Which file would you like to add to?")
                    dir = os.getcwd()
                    dlist = dir.split("/")
                    print("------")
                    if str(dlist[-1]) != "":
                        print("Directory: '" + colorama.Fore.LIGHTMAGENTA_EX +
                              str(dlist[-1]) + colorama.Style.RESET_ALL + "'")
                    else:
                        print("Directory: '" + colorama.Fore.LIGHTMAGENTA_EX +
                              "replit" + colorama.Style.RESET_ALL + "'")
                    print("------")
                    listfiles()
                    if documents == 0:
                        print(colorama.Fore.LIGHTBLACK_EX +
                              "This folder is empty,\nPress Ctrl+C to cancel..." +
                              colorama.Style.RESET_ALL)
                    print("------")
                    valid = False
                    while valid == False:
                        filename = input(colorama.Style.RESET_ALL + termdes + " ")
                        try:
                            with open(filename) as f:
                                None
                            valid = True
                        except:
                            print(colorama.Fore.RED + "\033[1mError: file: '" +
                                  filename + "' not found.")
                            valid = False

                    with open(filename) as f:
                        contents = f.readlines()
                    f.close()
                    print("------")
                    print("The contents of '" + colorama.Fore.LIGHTMAGENTA_EX +
                          filename + colorama.Style.RESET_ALL + "':")
                    print("------")
                    for line in contents:
                        print(line, end="")
                        time.sleep(0.02)
                        print()
                    print("------")
                    f = open(filename, "a")
                    print(
                        colorama.Fore.LIGHTCYAN_EX +
                        "Please write the file data below, and press Ctrl + C to save and exit."
                        + colorama.Style.RESET_ALL)
                    counter = 0
                    while True:
                        try:
                            counter = counter + 1
                            line = input(colorama.Style.RESET_ALL + colorama.Fore.LIGHTMAGENTA_EX +
                                         str(counter) + ": " +
                                         colorama.Style.RESET_ALL)
                            f.write(line + "\n")
                        except KeyboardInterrupt:
                            try:
                                print("---")
                                f.close()
                                print(colorama.Fore.LIGHTGREEN_EX +
                                      "File successfully saved - '" +
                                      colorama.Fore.LIGHTMAGENTA_EX + filename +
                                      colorama.Fore.LIGHTGREEN_EX + "'" +
                                      colorama.Style.RESET_ALL +
                                      "\nFind your file in the folder 'Documents'")
                                print("------")
                                os.chdir(old)
                                break
                            except:
                                print()
                                print(colorama.Fore.RED +
                                      "File failed to save..." +
                                      colorama.Style.RESET_ALL)
                                print("------")
                                os.chdir(old)
                                break

            except KeyboardInterrupt:
                print()
                print(colorama.Fore.RED + "Cancelling operation..." +
                      colorama.Style.RESET_ALL)
                os.chdir(old)

        if request == "read":
            try:
                print("------")
                print("Which file would you like to read?")
                dir = os.getcwd()
                dlist = dir.split("/")
                print("------")
                if str(dlist[-1]) != "":
                    print("Directory: '" + colorama.Fore.LIGHTMAGENTA_EX +
                          str(dlist[-1]) + colorama.Style.RESET_ALL + "'")
                else:
                    print("Directory: '" + colorama.Fore.LIGHTMAGENTA_EX +
                          "replit" + colorama.Style.RESET_ALL + "'")
                print("------")
                listfiles()
                DIR = os.getcwd()
                amount = len([
                    name for name in os.listdir(DIR)
                    if os.path.isfile(os.path.join(DIR, name))
                ])
                if amount == 0:
                    print(colorama.Fore.LIGHTBLACK_EX +
                          "This folder is empty,\nPress Ctrl+C to cancel..." +
                          colorama.Style.RESET_ALL)
                print("------")
                valid = False
                while valid == False:
                    filename = input(colorama.Style.RESET_ALL + termdes + " ")
                    try:
                        with open(filename) as f:
                            None
                        valid = True
                    except:
                        print(colorama.Fore.RED + "\033[1mError: file: '" +
                              filename + "' not found.")
                        valid = False
                with open(filename) as f:
                    contents = f.readlines()
                f.close()
                print("------")
                print("The contents of '" + colorama.Fore.LIGHTMAGENTA_EX +
                      filename + colorama.Style.RESET_ALL + "':")
                print("------")
                counter = 0
                index = -1
                print(contents)
                for line in contents:
                    index = index + 1
                    counter = int(counter)
                    counter = counter + 1
                    counter = str(counter)
                    line.replace(
                        "    ", colorama.Fore.LIGHTBLACK_EX + "•" +
                        colorama.Style.RESET_ALL)
                    print(counter + ":", line, end="")

                    time.sleep(0.02)
                print()
                print("------")
            except KeyboardInterrupt:
                print()
                print(colorama.Fore.RED + "Cancelling operation..." +
                      colorama.Style.RESET_ALL)

        if request == "execute" or request == "run":
            old = os.getcwd()
            try:
                print("------")
                print("Which " + colorama.Fore.LIGHTMAGENTA_EX + "python file " +
                      colorama.Style.RESET_ALL + "would you like to run?")
                print(
                    colorama.Fore.RED +
                    "Be careful when running code from sources you don't trust.\nMake sure you know what you're doing!"
                    + colorama.Style.RESET_ALL)
                getdirectory()
                print("------")
                listfiles()
                DIR = os.getcwd()
                amount = len([
                    name for name in os.listdir(DIR)
                    if os.path.isfile(os.path.join(DIR, name))
                ])
                if amount == 0:
                    print(colorama.Fore.LIGHTBLACK_EX +
                          "This folder is empty,\nPress Ctrl+C to cancel..." +
                          colorama.Style.RESET_ALL)
                print("------")
                print("Please include the file extension" +
                      colorama.Fore.LIGHTMAGENTA_EX +
                      "\n(e.g: 'file.py', or 'music.mp3'" +
                      colorama.Style.RESET_ALL + ") in your response.\n")

                valid = False
                while valid == False:
                    filename = input(colorama.Style.RESET_ALL + termdes + " ")
                    try:
                        with open(filename) as f:
                            None
                        valid = True
                    except:
                        print(colorama.Fore.RED + "\033[1mError: file: '" +
                              filename + "' not found.")
                        valid = False
                try:
                    print("------")
                    exec(open(filename).read())
                    print("------")
                    print(colorama.Fore.LIGHTMAGENTA_EX + "Session complete." +
                          colorama.Style.RESET_ALL)
                    print("------")

                except KeyboardInterrupt:
                    print("----")
                    print(colorama.Fore.LIGHTMAGENTA_EX + "Session complete." +
                          colorama.Style.RESET_ALL)
                    print("------")
                except:
                    print("------")
                    print(colorama.Fore.RED +
                          "An error occurred whilst running the file: '" +
                          filename + "'" + colorama.Style.RESET_ALL)
                    print(
                        "Make sure that the file name ends in '.py' before running anything!"
                    )
                    print("------")

            except KeyboardInterrupt:
                print()
                print(colorama.Fore.RED + "Cancelling operation..." +
                      colorama.Style.RESET_ALL)
                os.chdir(old)
            os.chdir(old)

        if request == "python" or request == "py" or request == "python3":
            try:
                print("------")
                print(
                    colorama.Fore.LIGHTMAGENTA_EX +
                    "Welcome to the Python shell for Core OS, version 1 - running Python 3.8.\nPress Ctrl+C at any time to exit!"
                    + colorama.Style.RESET_ALL)
                print("---")
                while True:
                    codea = input(colorama.Style.RESET_ALL + termdes + " ")
                    try:
                        exec(codea)
                    except:
                        print(colorama.Fore.RED + "The code contained an error." +
                              colorama.Style.RESET_ALL)
            except KeyboardInterrupt:
                print()
                print(colorama.Fore.RED + "Exiting shell..." +
                      colorama.Style.RESET_ALL)

        if request == "home" or request == "homedir" or request == "hd":
            try:
                os.chdir(home_directory)
            except:
                print("------")
                print(colorama.Fore.RED +
                      "The path for the home directory doesn't exist. (" +
                      home_directory + ")" + colorama.Style.RESET_ALL)
                print("------")

        if request == "tree" or request == "dtree" or request == "dirtree":
            try:
                old = os.getcwd()
                os.chdir(home_directory + "/System")
                f = open("tree.py", "r")
                contents = f.read()
                os.chdir(old)
                try:
                    print("------")
                    print("Scroll down!\nPress '" + colorama.Fore.LIGHTMAGENTA_EX +
                          "Ctrl + C" + colorama.Style.RESET_ALL + "' to cancel.")
                    exec(contents)
                    os.chdir(old)
                    print("------")
                except KeyboardInterrupt:
                    print("------")
                    print(colorama.Fore.RED + "Cancelling operation..." +
                          colorama.Style.RESET_ALL)
                    print("------")

            except:
                print("------")
                print(colorama.Fore.RED +
                      "An error occurred while running the tree." +
                      colorama.Style.RESET_ALL)
                print("---")
                if os.getcwd() == "/":
                    print(
                        colorama.Fore.LIGHTMAGENTA_EX +
                        "If this is running in Replit, did you try to access the Replit private folder?\nIf that's the case, that won't work.\nReplit developer permissions are required to access ths folder."
                        + colorama.Style.RESET_ALL)
                print("------")

        if request == "whoami" or request == "username" or request == "name" or request == "user":
            print("------")
            print(colorama.Fore.LIGHTMAGENTA_EX + str(USER) +
                  colorama.Style.RESET_ALL)
            print("------")

        if request == "design":
            try:
                print("------")
                print("This changes the" + colorama.Fore.LIGHTMAGENTA_EX +
                      " -> terminal design." + colorama.Style.RESET_ALL)
                print("The terminal design is currently: '" + termdes +
                      colorama.Style.RESET_ALL + "'")
                print("----")
                print("Please type a" + colorama.Fore.LIGHTMAGENTA_EX + " new " +
                      colorama.Style.RESET_ALL +
                      "terminal design below.\nPress Ctrl + C to cancel.")
                print()
                termdes = input(colorama.Style.RESET_ALL + termdes + " ")
                termdes = colorama.Fore.MAGENTA + termdes + colorama.Style.RESET_ALL
                print("------")
            except KeyboardInterrupt:
                print()
                print(colorama.Fore.RED + "Cancelling operation..." +
                      colorama.Style.RESET_ALL)
                print("------")

        if request == "properties":
            try:
                old = os.getcwd()
                print("Which" + colorama.Fore.LIGHTMAGENTA_EX + " file " +
                      colorama.Style.RESET_ALL +
                      "would you like to\nGet the properties for?")
                getdirectory()
                print("------")
                lista()
                folderscan()
                print()
                valid = False
                while valid == False:
                    selection = input(colorama.Style.RESET_ALL + termdes + " ")
                    try:
                        with open(selection) as f:
                            None
                        f.close()
                        print()
                        valid = True
                    except:
                        try:
                            os.chdir(selection)
                            os.chdir(old)
                            valid = True
                        except:
                            print(colorama.Fore.RED + "\033[1mError: location '" +
                                  selection + "' not found.")
                            valid = False
                print("------")
                print("- File/folder '" + colorama.Fore.LIGHTMAGENTA_EX +
                      selection + colorama.Style.RESET_ALL + "'")

                if os.path.isfile(old + "/" + selection):
                    print("- Location type: " + colorama.Fore.LIGHTMAGENTA_EX +
                          "file" + colorama.Style.RESET_ALL)
                else:
                    print("- Location type: " + colorama.Fore.LIGHTMAGENTA_EX +
                          "folder" + colorama.Style.RESET_ALL)
                    folderamount(old + "/" + selection)

                size = os.path.getsize(old + "/" + selection)
                if size < 1000:
                    print("- Size: " + colorama.Fore.LIGHTMAGENTA_EX + str(size) +
                          " bytes")
                elif size >= 1000 and size < 1000000:
                    size = round(size / 1000)
                    print("- Size: " + colorama.Fore.LIGHTMAGENTA_EX + str(size) +
                          " kilobytes")
                elif size >= 1000000 and size < 1000000000:
                    size = round(size / 1000000)
                    print("- Size: " + colorama.Fore.LIGHTMAGENTA_EX + str(size) +
                          " megabytes")
                elif size >= 1000000000 and size < 1000000000000:
                    size = round(size / 1000000000)
                    print("- Size: " + colorama.Fore.LIGHTMAGENTA_EX + str(size) +
                          " gigabytes")

                print(colorama.Style.RESET_ALL + "- Location: " +
                      colorama.Fore.LIGHTMAGENTA_EX + os.getcwd() +
                      colorama.Style.RESET_ALL)
                os.chdir(old)

                print("------")
            except KeyboardInterrupt:
                print()
                print(colorama.Fore.RED + "Cancelling operation..." +
                      colorama.Style.RESET_ALL)
                print("------")

        if request == "rename":
            try:
                print("------")
                old = os.getcwd()
                print("Which" + colorama.Fore.LIGHTMAGENTA_EX + " file " +
                      colorama.Style.RESET_ALL + "would you like to\nRename?")
                getdirectory()
                print("------")
                lista()
                folderscan()
                print()
                valid = False
                while valid == False:
                    selection = input(colorama.Style.RESET_ALL + termdes + " ")
                    try:
                        with open(selection) as f:
                            None
                        f.close()
                        print()
                        valid = True
                    except:
                        try:
                            os.chdir(selection)
                            os.chdir(old)
                            valid = True
                        except:
                            print(colorama.Fore.RED + "\033[1mError: location '" +
                                  selection + "' not found.")
                            valid = False
                print("------")
                filename = selection
                try:
                    print("Location name: '" + colorama.Fore.LIGHTMAGENTA_EX +
                          selection + colorama.Style.RESET_ALL + "'")
                    print("What is the new name of the file?")
                    print("Please include the file extension" +
                          colorama.Fore.LIGHTMAGENTA_EX +
                          "\n(e.g: 'file.py', or 'music.mp3'" +
                          colorama.Style.RESET_ALL + ") in your response.\n")
                    selection = input(colorama.Style.RESET_ALL + termdes + " ")
                    try:
                        os.rename(filename, selection)
                        print(colorama.Fore.LIGHTGREEN_EX +
                              "File successfully renamed to: '" + selection + "'" +
                              colorama.Style.RESET_ALL)
                        print("------")
                    except:
                        print(colorama.Fore.RED +
                              "An error ocurred whilst renaming the file." +
                              colorama.Style.RESET_ALL)
                        print("------")
                except:
                    print(colorama.Fore.RED + "An error ocurred." +
                          colorama.Style.RESET_ALL)
                    print("------")
            except KeyboardInterrupt:
                print(colorama.Fore.RED + "Cancelling operation..." +
                      colorama.Style.RESET_ALL)
                print("------")

        if request == "runner" or request == "filewd" or request == "rnr" or request == "pwd" or request == "cwd":
            file_path = os.path.realpath(__file__)
            print("------")
            print(colorama.Fore.LIGHTMAGENTA_EX + str(os.getcwd()) +
                  colorama.Style.RESET_ALL)
            print("------")

        if request == "play" or request == "open":
            old = os.getcwd()
            os.chdir("Games_and_apps")
            try:
                print("------")
                print("Which " + colorama.Fore.LIGHTMAGENTA_EX + "game/app " +
                      colorama.Style.RESET_ALL + "would you like to run?")
                print(
                    colorama.Fore.RED +
                    "Be careful when running code from sources you don't trust.\nMake sure you know what you're doing!"
                    + colorama.Style.RESET_ALL)
                getdirectory()
                print("------")
                listfiles()
                DIR = os.getcwd()
                amount = len([
                    name for name in os.listdir(DIR)
                    if os.path.isfile(os.path.join(DIR, name))
                ])
                if amount == 0:
                    print(colorama.Fore.LIGHTBLACK_EX +
                          "This folder is empty,\nPress Ctrl+C to cancel..." +
                          colorama.Style.RESET_ALL)
                print("------")
                print("Please include the file extension" +
                      colorama.Fore.LIGHTMAGENTA_EX +
                      "\n(e.g: 'file.py', or 'music.mp3'" +
                      colorama.Style.RESET_ALL + ") in your response.\n")

                valid = False
                while valid == False:
                    filename = input(colorama.Style.RESET_ALL + termdes + " ")
                    try:
                        with open(filename) as f:
                            None
                        valid = True
                    except:
                        print(colorama.Fore.RED + "\033[1mError: file: '" +
                              filename + "' not found.")
                        valid = False

                print("------")
                try:
                    exec(open(filename).read())

                except KeyboardInterrupt:
                    print()
                    print(colorama.Fore.RED + "Ending session..." +
                          colorama.Style.RESET_ALL)
                    os.chdir(old)

                except:
                    print(colorama.Fore.RED +
                          "An error ocurred whilst running the file: '" +
                          str(filename) + "'")
                os.chdir(old)

            except KeyboardInterrupt:
                print()
                print(colorama.Fore.RED + "Cancelling operation..." +
                      colorama.Style.RESET_ALL)
                os.chdir(old)
            os.chdir(old)
            print("------")
        if request == "delete" or request == "remove":
            old = os.getcwd()
            try:
                print("------")
                print("Which " + colorama.Fore.LIGHTMAGENTA_EX + "file " +
                      colorama.Style.RESET_ALL + "would you like to delete?")
                print(
                    colorama.Fore.RED +
                    "Be careful when deleting files that you don't own.\nMake sure you know what you're doing!"
                    + colorama.Style.RESET_ALL)
                getdirectory()
                print("------")
                listfiles()
                DIR = os.getcwd()
                amount = len([
                    name for name in os.listdir(DIR)
                    if os.path.isfile(os.path.join(DIR, name))
                ])
                if amount == 0:
                    print(colorama.Fore.LIGHTBLACK_EX +
                          "This folder is empty,\nPress Ctrl+C to cancel..." +
                          colorama.Style.RESET_ALL)
                valid = False
                while valid == False:
                    filename = input(colorama.Style.RESET_ALL + termdes + " ")
                    try:
                        with open(filename) as f:
                            None
                        valid = True
                    except:
                        print(colorama.Fore.RED + "\033[1mError: file: '" +
                              filename + "' not found.")
                        valid = False
                try:
                    print("------")
                    print(colorama.Fore.RED +
                          "Are you sure you want to delete this file?" +
                          colorama.Style.RESET_ALL)
                    print("Location name: '" + colorama.Fore.LIGHTMAGENTA_EX +
                          filename + colorama.Style.RESET_ALL + "'")
                    valid = False
                    while valid == False:
                        print("------")
                        print(colorama.Fore.LIGHTMAGENTA_EX +
                              "'y' - (yes)\nOR\n'n' - (no)" +
                              colorama.Style.RESET_ALL)
                        print("------")
                        choice = input(colorama.Style.RESET_ALL + termdes + " ")
                        choice = choice.strip()
                        if choice.lower() == "y" or choice.lower() == "n":
                            valid = True
                        else:
                            print(colorama.Fore.RED +
                                  "Invalid answer. Use (y/n) to respond." +
                                  colorama.Style.RESET_ALL)
                    if choice.lower() == "y":
                        if filename.strip(" ") not in systemdirs:
                            try:
                                os.remove(filename)
                                print(colorama.Fore.LIGHTGREEN_EX +
                                      "File successfully deleted: '" + filename + "'" +
                                      colorama.Style.RESET_ALL)
                            except:
                                print()
                                print(colorama.Fore.RED + "An error occurred" +
                                      colorama.Style.RESET_ALL)
                        else:
                            print(colorama.Fore.RED + "This file is a system file, and therefore cannot be removed." +
                                      colorama.Style.RESET_ALL)

                except:
                    print()
                    print(colorama.Fore.RED + "An error occurred" +
                          colorama.Style.RESET_ALL)
            except KeyboardInterrupt:
                print()
                print(colorama.Fore.RED + "Cancelling operation..." +
                      colorama.Style.RESET_ALL)

        if request == "view":
            try:
                old = os.getcwd()
                print("------")
                print("vvv Which" + colorama.Fore.LIGHTMAGENTA_EX + " file " +
                      colorama.Style.RESET_ALL +
                      "would you like to view vvv\nUsing the system path?")
                getdirectory()
                print("------")
                lista()
                folderscan()
                print()
                valid = False
                while valid == False:
                    selection = input(colorama.Style.RESET_ALL + termdes + " ")
                    try:
                        with open(selection) as f:
                            None
                        f.close()
                        valid = True
                    except:
                        try:
                            os.chdir(selection)
                            os.chdir(old)
                            valid = True
                        except:
                            print(colorama.Fore.RED + "\033[1mError: location '" +
                                  selection + "' not found.")
                            valid = False
                print("------")
                filename = selection
                try:
                    os.system(os.getcwd() + "/" + filename)
                except:
                    webbrowser.open_new(os.getcwd() + "/" + filename)

            except KeyboardInterrupt:
                print()
                print(colorama.Fore.RED + "Cancelling operation..." +
                      colorama.Style.RESET_ALL)

        if request == "chport":
            try:
                print("------")
                print("What would you like to change the port to?")
                print("This is used for local connections when using " +
                      colorama.Fore.LIGHTMAGENTA_EX + "CoreChat" +
                      colorama.Style.RESET_ALL)
                print("The current connection port is: " +
                      colorama.Fore.LIGHTMAGENTA_EX + str(dsport) +
                      colorama.Style.RESET_ALL)
                print("The current server port is: " +
                      colorama.Fore.LIGHTMAGENTA_EX + str(server_port) +
                      colorama.Style.RESET_ALL)
                valid = False
                print("---")
                print("Set the dest and source port:")

                while valid == False:
                    selection = input(colorama.Style.RESET_ALL + termdes + " ")
                    try:
                        selection = int(selection)
                        if selection >= 1 and selection <= 65535:
                            dsport = int(selection)
                            valid = True
                        else:
                            int("forced error")
                    except:
                        print(
                            colorama.Fore.RED +
                            "Error: Make sure the port is a number greater than 1 and less than 65535."
                            + colorama.Style.RESET_ALL)
                print("Set the server port:")
                valid = False
                while valid == False:
                    selection = input(colorama.Style.RESET_ALL + termdes + " ")
                    try:
                        selection = int(selection)
                        if selection >= 1 and selection <= 65535:
                            server_port = int(selection)
                            valid = True
                        else:
                            int("forced error")
                    except:
                        print(
                            colorama.Fore.RED +
                            "Error: Make sure the port is a number greater than 1 and less than 65535."
                            + colorama.Style.RESET_ALL)
                print("---")

            except KeyboardInterrupt:
                print()
                print(colorama.Fore.RED + "Cancelling operation..." +
                      colorama.Style.RESET_ALL)

        if request == "port":
            try:
                print("------")
                print("The current connection (destination and source) port is: " +
                      colorama.Fore.LIGHTMAGENTA_EX + str(dsport) +
                      colorama.Style.RESET_ALL)
                print("The current server port is: " +
                      colorama.Fore.LIGHTMAGENTA_EX + str(server_port) +
                      colorama.Style.RESET_ALL)
                print("------")
            except KeyboardInterrupt:
                print()
                print(colorama.Fore.RED + "Cancelling operation..." +
                      colorama.Style.RESET_ALL)

        if request == "ip" or request == "ipconfig":
            try:
                hostname = socket.gethostname()
                ip_address = socket.gethostbyname(hostname)
                print("------")
                print(colorama.Fore.LIGHTMAGENTA_EX + "IP address: " +
                      colorama.Style.RESET_ALL + str(ip_address))
                print("------")
            except:
                print(colorama.Fore.RED + "An error occurred." +
                      colorama.Style.RESET_ALL)

        if request == "find" or request == "findstr":
            try:
                print("------")
                print("Which file would you like to search?")
                dir = os.getcwd()
                dlist = dir.split("/")
                print("------")
                if str(dlist[-1]) != "":
                    print("Directory: '" + colorama.Fore.LIGHTMAGENTA_EX +
                          str(dlist[-1]) + colorama.Style.RESET_ALL + "'")
                else:
                    print("Directory: '" + colorama.Fore.LIGHTMAGENTA_EX +
                          "replit" + colorama.Style.RESET_ALL + "'")
                print("------")
                listfiles()
                DIR = os.getcwd()
                amount = len([
                    name for name in os.listdir(DIR)
                    if os.path.isfile(os.path.join(DIR, name))
                ])
                if amount == 0:
                    print(colorama.Fore.LIGHTBLACK_EX +
                          "This folder is empty,\nPress Ctrl+C to cancel..." +
                          colorama.Style.RESET_ALL)
                print("------")
                valid = False
                while valid == False:
                    filename = input(colorama.Style.RESET_ALL + termdes + " ")
                    try:
                        with open(filename) as f:
                            None
                        valid = True
                    except:
                        print(colorama.Fore.RED + "\033[1mError: file: '" +
                              filename + "' not found.")
                        valid = False
                with open(filename) as f:
                    contents = f.readlines()
                f.close()

                print("What would you like to search for?")
                string = input(colorama.Style.RESET_ALL + termdes + " ")
                string = string.lower()
                for line in contents:
                    linelowered = line.lower()

                    if string in linelowered:
                        index = contents.index(line)
                        linen = index + 1
                        line = line.replace("""\n""", "")
                        print("Line " + str(linen) + ": " +
                              colorama.Fore.LIGHTMAGENTA_EX +
                              str(line.strip("    ")) + colorama.Style.RESET_ALL)
                print("------")
            except KeyboardInterrupt:
                print()
                print(colorama.Fore.RED + "Cancelling operation..." +
                      colorama.Style.RESET_ALL)

        if request == "battery" or request == "power":
            print("------")
            try:
                battery = psutil.sensors_battery()
                if battery != None:
                    percent = str(battery.percent)
                    plugged = battery.power_plugged
                    plugged = "Plugged in - charging." if plugged else ""

                    print("{}, {}".format(percent, plugged))
                else:
                    print("This PC is plugged in.")
                    print("------")
            except:
                print(colorama.Fore.RED + "An error occurred." +
                      colorama.Style.RESET_ALL)

        if request == "rmstr":
            try:
                print("------")
                print("Which file would you like to edit?")
                print(
                    colorama.Fore.RED +
                    "Please note: this deletes the whole line\nin the file if it contains the specified string."
                    + colorama.Style.RESET_ALL)
                getdirectory()
                print("------")
                listfiles()
                folderscan()
                print("------")

                checkfile()
                print(filename)
                print("------")
                print("What string would you like to" +
                      colorama.Fore.LIGHTMAGENTA_EX + " remove?" +
                      colorama.Style.RESET_ALL)
                print(
                    colorama.Fore.RED +
                    "If you want to check what you want to delete,\nCancel this, and read the file ("
                    + filename + ")\nBy typing 'read', and then, '" + filename +
                    "'" + colorama.Style.RESET_ALL)
                print("------")
                string = input(colorama.Style.RESET_ALL + termdes + " ")
                print("------")
                with open(filename, "r") as f:
                    lines = f.readlines()
                    os.remove(filename)
                with open(filename, "w") as f:
                    for line in lines:
                        if string not in line:
                            f.write(line)
                f.close()

                print(colorama.Fore.LIGHTGREEN_EX +
                      "Successfully stripped file of lines containing: '" +
                      string + "'" + colorama.Style.RESET_ALL)
                print("------")
            except KeyboardInterrupt:
                print()
                print(colorama.Fore.RED + "Cancelling operation..." +
                      colorama.Style.RESET_ALL)

        if request == "rmline":
            try:
                print("------")
                print("Which file would you like to edit?")
                print(
                    colorama.Fore.RED +
                    "Please note: this deletes the whole line of the number specified."
                    + colorama.Style.RESET_ALL)
                getdirectory()
                print("------")
                listfiles()
                folderscan()
                print("------")

                checkfile()
                print(filename)
                print("------")
                print("What line would you like to" +
                      colorama.Fore.LIGHTMAGENTA_EX + " remove?" +
                      colorama.Style.RESET_ALL)
                print(
                    colorama.Fore.RED +
                    "If you want to check what you want to delete,\nCancel this, and read the file ("
                    + filename + ")\nBy typing 'read', and then, '" + filename +
                    "'" + colorama.Style.RESET_ALL)
                print("------")
                with open(filename, "r") as f:
                    contents = f.readlines()
                valid = False
                while valid == False:
                    try:
                        linen = input(colorama.Style.RESET_ALL + termdes + " ")
                        linen = int(linen)
                        if linen <= len(contents):
                            valid = True
                        else:
                            int("forced error")
                    except:
                        print(colorama.Fore.RED +
                              "The line must be a number less than " +
                              str(len(contents)))
                        valid = False

                print("------")

                os.remove(filename)
                f = open(filename, "w")

                for line in contents:
                    lineindex = linen - 1
                    if contents.index(line) != lineindex:
                        f.write(line)
                    else:
                        None

                f.close()

                print(colorama.Fore.LIGHTGREEN_EX +
                      "Successfully deleted line: '" + str(linen) + "'" +
                      colorama.Style.RESET_ALL)
                print("------")
            except KeyboardInterrupt:
                print()
                print(colorama.Fore.RED + "Cancelling operation..." +
                      colorama.Style.RESET_ALL)

        if request == "command":
            try:
                print("Which command (number) would you like help with?")
                valid = False
                while valid == False:
                    choice = input(colorama.Style.RESET_ALL + termdes + " ")
                    try:
                        int(choice)
                        if int(choice) >= 1 and int(choice) <= 32:
                            choice = int(choice)
                            valid = True
                        else:
                            int("Forced error.")
                    except:
                        print(
                            colorama.Fore.RED +
                            "Invalid choice.\n Make sure it is a number greater than 1 and less than 32!"
                            + colorama.Style.RESET_ALL)

                old = os.getcwd()
                os.chdir(home_directory + "/System")

                try:
                    with open("helpfile.txt") as f:
                        contents = f.readlines()
                    print("------")
                    print(colorama.Fore.LIGHTMAGENTA_EX + "Line " +
                          str(choice * 2) + ": " +
                          str(contents[(choice * 2) - 1]) +
                          colorama.Style.RESET_ALL)
                    print("------")
                except:
                    print(
                        colorama.Fore.RED +
                        "An error ocurred reading 'helpfile.txt'.\nMake sure that the file exists, and is located in the system folder."
                        + colorama.Style.RESET_ALL)
            except KeyboardInterrupt:
                print()
                print(colorama.Fore.RED + "Cancelling operation..." +
                      colorama.Style.RESET_ALL)

        if request == "shop" or request == "buy":
            products = ["SAIntence Deluxe"]
            prices = ["5000000"]
            try:
                print("------")
                print(colorama.Fore.LIGHTMAGENTA_EX + "Core OS - EShop" +
                      colorama.Style.RESET_ALL)
                print("------")
                type(
                    colorama.Fore.RED + "Currently under development..." +
                    colorama.Style.RESET_ALL +
                    "\nMaybe earn some money from playing BlackJack single player in the meantime?"
                )
                print("------")
                print("Balance: " + colorama.Fore.YELLOW + "£" + str(balance) +
                      colorama.Style.RESET_ALL)
                pronumber = 0

                for item in products:
                    price = prices[products.index(item)]
                    priceform = "{:,}".format(int(price))
                    pronumber = pronumber + 1
                    print(" - Product " + str(pronumber) + ": " +
                          colorama.Fore.LIGHTCYAN_EX + str(item) + "; " +
                          colorama.Fore.YELLOW + "£" + str(priceform) +
                          colorama.Style.RESET_ALL)

                print("------")
                print(
                    colorama.Fore.LIGHTMAGENTA_EX +
                    "Please use the number (1,2,3,4 etc.) of the product for purchase."
                    + colorama.Style.RESET_ALL)
                checker = False

                while checker == False:
                    purchase = input(colorama.Style.RESET_ALL + termdes + " ")
                    try:
                        purchase = int(purchase)
                        chk2 = True
                    except:
                        print(
                            colorama.Fore.RED +
                            "Please type the number corresponding to your product choice."
                            + colorama.Style.RESET_ALL)
                        chk2 = False
                    if chk2 == True:
                        if int(purchase) <= len(products):

                            if int(balance) >= int(prices[int(int(purchase) - 1)]):
                                checker = True

                            else:
                                print(colorama.Fore.RED +
                                      "Not enough money for purchase." +
                                      colorama.Style.RESET_ALL)
                                break

                        else:
                            print(colorama.Fore.RED +
                                  "Your product choice is not on the list." +
                                  colorama.Style.RESET_ALL)

                if checker == True:
                    purchasei = int(purchase)
                    products.pop(purchasei - 1)

                    old = os.getcwd()

                    if purchasei == 1:
                        writer.write_app1()
                        balance = balance - int(prices[int(purchasei) - 1])
                        prices.pop(purchasei - 1)
                        products.pop(purchasei - 1)

                    if purchasei == 1:
                        print(
                            "Purchase successful - Check it out by running the 'play' command!"
                        )
                    else:
                        print("Purchase successful!")

                    print("------")
                    os.chdir(old)

                else:
                    print("Purchase incomplete: Exiting...")
                    print("------")

            except KeyboardInterrupt:
                print()
                print(colorama.Fore.RED + "Cancelling operation..." +
                      colorama.Style.RESET_ALL)

        if request == "sort":
            try:
                path = os.getcwd()
                path = str(path)
                if str(path) != home_directory and str(
                        path) != "/home/runner" and str(path) != "/home" and str(
                            path) != home_directory + "/runner" and str(
                                path) != home_directory + "/Games_and_apps" and str(
                                    path) != home_directory + "/Games_and_apps" and str(
                                        path) != home_directory + "/Messages" and str(
                                            path) != home_directory + "/System" and str(
                                                path) != home_directory + "/System":
                    print("------")
                    print(
                        f"{colorama.Fore.RED}Are you sure you want to sort the files in this folder into folders alphabetical order?{colorama.Style.RESET_ALL}"
                    )

                    valid = input(colorama.Style.RESET_ALL + "(y/n) " + termdes + " ")
                    if valid.lower() == "y":
                        print("Sorting files...")
                        import os
                        import shutil
                        print(os.getcwd())
                        path = '/home/runner/test-for-files/folder'

                        for filename in os.listdir(path):
                            if filename.startswith('.'):
                                continue
                            first_letter = filename[0]
                            if not os.path.exists(path + '/' + first_letter):
                                os.makedirs(path + '/' + first_letter)
                            shutil.move(path + '/' + filename,
                                        path + '/' + first_letter + '/' + filename)

                        print(f"{colorama.Fore.LIGHTGREEN_EX}Complete!")
                    else:
                        print(f"{colorama.Fore.RED}Cancelled...")
                else:
                    print(f"{colorama.Fore.RED}Cannot sort runner directory.")
                print(f"{colorama.Style.RESET_ALL}----------")
            except KeyboardInterrupt:
                print()
                print(colorama.Fore.RED + "Cancelling operation..." +
                      colorama.Style.RESET_ALL)

        if request == "duplicate" or request == "dp":
            try:
                #Duplicate code
                None
                print("------")
                print("Which file would you like to " +
                      colorama.Fore.LIGHTMAGENTA_EX + "duplicate?" +
                      colorama.Style.RESET_ALL)
                getdirectory()
                print("------")
                listfiles()
                print("------")
                #duplicate code here
                valid = False
                while valid == False:
                    file = input(colorama.Style.RESET_ALL + termdes + " ")
                    if os.path.exists(file):
                        filelist = file.split(".")
                        filelist[0] = filelist[0] + str(random.randint(
                            1, 10000000))
                        filenamer = filelist[0] + "." + filelist[1]
                        shutil.copyfile(os.getcwd() + "/" + file,
                                        os.getcwd() + "/" + filenamer)

                        print(
                            f"{colorama.Fore.LIGHTGREEN_EX}File successfully copied with name: '{filenamer}'{colorama.Style.RESET_ALL} {colorama.Fore.LIGHTBLACK_EX} (there is a 1 in 10,000,000 chance that a file will get replaced with the same rng name, so it is recommended to change this!){colorama.Style.RESET_ALL}"
                        )
                        valid = True
                    else:
                        print(colorama.Fore.RED + "\033[1mError: file: '" + file +
                              "' not found.")
                        valid = False

            except KeyboardInterrupt:
                print()
                print(colorama.Fore.RED + "Cancelling operation..." +
                      colorama.Style.RESET_ALL)

        if request == "move":
            None

        if request == "rename":
            None

        if request == "rng":
            valid = False
            try:
                print("------")
                print(
                    f"What {colorama.Fore.LIGHTMAGENTA_EX}range{colorama.Style.RESET_ALL} should the number be within?\ne.g: 1,3 for between 1 and 3"
                )
                while valid == False:
                    range = input(colorama.Style.RESET_ALL + termdes + " ")
                    range = range.strip(" ")
                    if "," in range:
                        listem = range.split(",")
                        try:
                            rng1 = int(listem[0])
                            rng2 = int(listem[1])
                            valid = True
                            break
                        except:
                            valid = False
                            print(
                                f"{colorama.Fore.RED}Please type 2 numbers separated by ',' (e.g.: 1,3){colorama.Style.RESET_ALL}"
                            )

                    else:
                        valid = False
                        print(
                            f"{colorama.Fore.RED}Please type 2 numbers separated by ',' (e.g.: 1,3){colorama.Style.RESET_ALL}"
                        )
                print("------")
                print(random.randint(rng1, rng2))
                print("------")

            except KeyboardInterrupt:
                print()
                print(colorama.Fore.RED + "Cancelling operation..." +
                      colorama.Style.RESET_ALL)

        if request == "system":
            print("------")
            print(colorama.Fore.LIGHTMAGENTA_EX + "Starting shell..." +
                  colorama.Style.RESET_ALL)
            print("------")
            print("Windows/Mac Command Prompt" if os.name in
                  ["nt", "dos"] else "Unix/Linux Command Prompt")
            print("Press ctrl + c to exit")
            print("------")
            try:
                while True:
                    requesta = input(colorama.Style.RESET_ALL + termdes + " ")
                    os.system(requesta)
            except KeyboardInterrupt:
                print()
                print(colorama.Fore.RED + "Returning to Core OS" +
                      colorama.Style.RESET_ALL)

        if request == "backup":
            try:
                print("------")
                print(
                    f"{colorama.Fore.LIGHTMAGENTA_EX}This will create a backup of all files into a zip file called 'CoreBackup.zip'{colorama.Style.RESET_ALL}"
                )
                print(
                    f"Are you {colorama.Fore.RED} sure{colorama.Style.RESET_ALL} that you want to proceed?"
                )

                valid = False
                choice = None
                while valid == False:
                    choice = input(colorama.Style.RESET_ALL + termdes + " ")
                    if choice.lower() == "y":
                        valid = True
                        break
                    if choice.lower() == "n":
                        print(colorama.Fore.RED + "Cancelling operation..." +
                              colorama.Style.RESET_ALL)
                        break
                    else:
                        print(colorama.Fore.RED +
                              "Please type 'y' to confirm or 'n' to cancel." +
                              colorama.Style.RESET_ALL)
                        valid = False

                if valid == True:
                    try:
                        print("------")
                        print("{}Installing necessary packages...{}".format(
                            colorama.Fore.LIGHTMAGENTA_EX,
                            colorama.Style.RESET_ALL))
                        os.system("sudo apt install zip")
                        os.system("apt install zip")
                        os.system("install zip")
                        time.sleep(4)
                        print("Compressing...")
                        os.chdir(home_directory)
                        dirback()
                        dirs = os.getcwd()
                        dirlist = dirs.split("/")
                        length = len(dirlist) - 1
                        finaldir = dirlist[length]

                        os.system("zip CoreBackup.zip {}".format(finaldir))
                        os.chdir(home_directory)
                        time.sleep(2)
                        print("{}Compression complete.{}".format(
                            colorama.Fore.LIGHTGREEN_EX, colorama.Style.RESET_ALL))

                        print("------")
                    except:
                        print(
                            "{}An error occurred while installing packages. Please try again.{}"
                            .format(colorama.Fore.RED, colorama.Style.RESET_ALL))
            except KeyboardInterrupt:
                print()
                print(colorama.Fore.RED + "Cancelling operation..." +
                      colorama.Style.RESET_ALL)

        if request == "diskchk":
            try:
                import psutil
                print("------")
                hdd = psutil.disk_usage('/')
                print(
                    f"Total: {colorama.Fore.LIGHTMAGENTA_EX}%d GB{colorama.Style.RESET_ALL}"
                    % (hdd.total / (2**30)))
                print(
                    f"Used: {colorama.Fore.LIGHTMAGENTA_EX}%d GB{colorama.Style.RESET_ALL}"
                    % (hdd.used / (2**30)))
                print(
                    f"Free: {colorama.Fore.LIGHTMAGENTA_EX}%d GB{colorama.Style.RESET_ALL}"
                    .format(colorama.Style.RESET_ALL) % (hdd.free / (2**30)))
                print("---")
                print(
                    f"Used: {colorama.Fore.LIGHTMAGENTA_EX}{str(hdd.percent)}%{colorama.Style.RESET_ALL}"
                )
                print("------")
            except:
                try:
                    print(
                        colorama.Fore.RED +
                        "An error occurred whilst retrieving the disk statistics. Please check that you have 'psutil' installed and try again."
                        + colorama.Style.RESET_ALL)
                    os.system("python3 -m pip install psutil  > installcache.txt")
                except:
                    print("")

        if request == "health" or request == "performance":
            try:
                import psutil
                clear()
                while True:
                    print("------")
                    print(
                        "CPU:", colorama.Fore.LIGHTMAGENTA_EX +
                        str(psutil.cpu_percent(0.1)) + "%" +
                        colorama.Style.RESET_ALL)
                    print("---")
                    print('RAM: ' + colorama.Fore.LIGHTMAGENTA_EX +
                          str(psutil.virtual_memory()[2]) + "%, " +
                          str(psutil.virtual_memory()[3] / 1000000000)[0:4] +
                          " GB" + colorama.Style.RESET_ALL)
                    print("------")
                    time.sleep(1)
                    clear()
            except KeyboardInterrupt:
                print("")
            except:
                try:
                    print(
                        colorama.Fore.RED +
                        "An error occurred whilst retrieving the disk statistics. Please check that you have 'psutil' installed and try again."
                        + colorama.Style.RESET_ALL)
                    os.system("python3 -m pip install psutil  > installcache.txt")
                except:
                    print("")

        if request == "gpu":
            try:
                import nvidia_smi

                _GPU = False
                _NUMBER_OF_GPU = 0

                def _check_gpu():
                    global _GPU
                    global _NUMBER_OF_GPU
                    nvidia_smi.nvmlInit()
                    _NUMBER_OF_GPU = nvidia_smi.nvmlDeviceGetCount()
                    if _NUMBER_OF_GPU > 0:
                        _GPU = True

                def _print_gpu_usage(detailed=False):

                    if not detailed:
                        for i in range(_NUMBER_OF_GPU):
                            handle = nvidia_smi.nvmlDeviceGetHandleByIndex(i)
                            info = nvidia_smi.nvmlDeviceGetMemoryInfo(handle)
                            print(
                                f'GPU-{i}: GPU-Memory: {_bytes_to_megabytes(info.used)}/{_bytes_to_megabytes(info.total)} MB'
                            )

                def _bytes_to_megabytes(bytes):
                    return round((bytes / 1024) / 1024, 2)

                if __name__ == '__main__':
                    print("------")
                    print('Checking for Nvidia GPU...')
                    _check_gpu()
                    if _GPU:
                        _print_gpu_usage()
                    else:
                        print("No GPU found.")
            except:
                print("---")
                print(colorama.Fore.RED + "No Nvidia GPU found." +
                      colorama.Style.RESET_ALL)
                print("------")

        if request == "wikipedia" or request == "wiki":
            try:
                import wikipedia
                clear()
                print("Welcome to {}Wikipedia{} for {}Core OS{}!".format(
                    colorama.Fore.LIGHTCYAN_EX, colorama.Style.RESET_ALL,
                    colorama.Fore.LIGHTMAGENTA_EX, colorama.Style.RESET_ALL))
                print("------")
                print("Please type a search below...")
                search = input(colorama.Style.RESET_ALL + termdes + " What is... ")

                try:
                    print("------")
                    print(wikipedia.summary(search.strip(" ")))
                    print("------")
                except:
                    print(colorama.Fore.RED +
                          "There was an error searching for your topic." +
                          colorama.Style.RESET_ALL)
                    print("------")
            except KeyboardInterrupt:
                print()
                print(colorama.Fore.RED + "Cancelling operation..." +
                      colorama.Style.RESET_ALL)
            except:
                try:
                    print(
                        colorama.Fore.RED +
                        "An error occurred whilst installing wikipedia. Please check that you have 'wikipedia' installed and try again."
                        + colorama.Style.RESET_ALL)
                    os.system(
                        "python3 -m pip install wikipedia  > installcache.txt")
                except:
                    print("")

        if request == "google" or request == "search":
            from gsearch.googlesearch import search as browse
            print("------")
            print("Welcome to {}G{}o{}o{}g{}l{}e{} for {}Core{} OS!{}".format(
                colorama.Fore.BLUE, colorama.Fore.RED,
                colorama.Fore.LIGHTYELLOW_EX, colorama.Fore.BLUE,
                colorama.Fore.LIGHTGREEN_EX, colorama.Fore.RED,
                colorama.Style.RESET_ALL, colorama.Fore.LIGHTCYAN_EX,
                colorama.Fore.LIGHTMAGENTA_EX, colorama.Style.RESET_ALL))
            print("------")
            print(
                "Sorry, but the GSearch module doesn't currently function in Replit... We're working on it, though!"
            )
            print("------")

        if request == "howdoi" or request == "how":
            try:
                print("------")
                print("What do you want help with?")
                print("---")
                howto = input(colorama.Style.RESET_ALL + termdes + colorama.Fore.LIGHTGREEN_EX + " How " +
                              colorama.Style.RESET_ALL + "do I... ")
                print("------")
                os.system("howdoi " + howto)
                print("------")
                check = random.randint(1, 5)

                if check == 5:
                    valid = False
                    while valid == False:
                        checker = input(colorama.Style.RESET_ALL + "Did that answer your" +
                                        colorama.Fore.LIGHTMAGENTA_EX +
                                        " question? (y/n)\n" + termdes + " ")
                        checker = checker.strip(" ")
                        checker = checker.lower()
                        if checker == "y" or checker == "n":
                            valid = True
                            break
                        else:
                            valid = False

                    if checker == "y":
                        print(colorama.Fore.LIGHTMAGENTA_EX + "Thanks" +
                              colorama.Style.RESET_ALL + " for your feedback!")
                    else:
                        print(colorama.Fore.RED + "What could be improved?" +
                              colorama.Style.RESET_ALL)
                        improv = input(colorama.Style.RESET_ALL + termdes + " ")
                        old = os.getcwd()
                        try:
                            os.chdir(home_directory + "/System")
                            f = open("responses.txt", "a")
                            f.write(improv + "\n")
                            f.close()
                            os.chdir(old)
                        except:
                            None
                        print("------")
                        print(colorama.Fore.LIGHTMAGENTA_EX + "Thanks" +
                              colorama.Style.RESET_ALL + " for your feedback!")
                        print("------")
            except KeyboardInterrupt:
                print()
                print(colorama.Fore.RED + "Cancelling operation..." +
                      colorama.Style.RESET_ALL)
            except:
                print(
                    colorama.Fore.RED +
                    "An error ocurred whilst running howdoi...\nAre all the packages installed?"
                    + colorama.Style.RESET_ALL)

        if request == "dis" or request == "disassemble":
            try:
                print("------")
                print(
                    f"Please wait while we {colorama.Fore.LIGHTMAGENTA_EX}install{colorama.Style.RESET_ALL} the required packages..."
                )

                import dis
                time.sleep(0.5)

                print("------")
                print("This tool" + colorama.Fore.LIGHTMAGENTA_EX +
                      " disassembles " + colorama.Style.RESET_ALL +
                      "Python code into mneumonic-based bytecode.")
                print("---")

                print("What do you want to disassemble?\n-")
                print(colorama.Fore.LIGHTCYAN_EX + "(1) An input?" +
                      colorama.Style.RESET_ALL)
                print("OR")
                print(colorama.Fore.LIGHTCYAN_EX + "(2) A file?" +
                      colorama.Style.RESET_ALL)
                print("-")
                print("Please use numbers (1/2) to answer.")
                print("---")
                valid = False

                while valid == False:
                    response = input(colorama.Style.RESET_ALL + termdes + " ")

                    if response.strip(" ") == "1" or response == "2":
                        valid = True
                        break
                    else:
                        print(colorama.Fore.RED + "\033[1mPlease type '1' or '2'")
                        valid = False

                if response.strip(" ") == "1":
                    print("---")
                    print("Type the " + colorama.Fore.BLUE + "Pyt" +
                          colorama.Fore.LIGHTYELLOW_EX + "hon" +
                          colorama.Style.RESET_ALL +
                          " code that you wish to disassemble below.")
                    print("-")
                    code = input(colorama.Style.RESET_ALL + termdes + " ")

                    try:
                        print("---")
                        print(colorama.Fore.LIGHTMAGENTA_EX +
                              "disassembled code: " + colorama.Style.RESET_ALL)
                        print("------")
                        dis.dis(code)
                        print("------")
                    except:
                        print(
                            colorama.Fore.RED +
                            "There was an error disassembling your code. Please try again."
                            + colorama.Style.RESET_ALL)
                        print(colorama.Style.RESET_ALL + "------")

                elif response.strip(" ") == "2":
                    print("------")
                    print("Please name the file you wish to " +
                          colorama.Fore.LIGHTMAGENTA_EX + "disassemble." +
                          colorama.Style.RESET_ALL)
                    getdirectory()
                    print("------")
                    listfiles()
                    print("---")
                    valid = False
                    while valid == False:
                        filename = input(colorama.Style.RESET_ALL + termdes + " ")

                        if os.path.exists(filename) == True and os.path.isfile(
                                filename) == True:
                            valid = True
                        else:
                            print(
                                colorama.Fore.RED +
                                "\033[1mThe file does not exist in this directory."
                                + colorama.Style.RESET_ALL)
                    try:
                        f = open(filename, "r")
                        contents = f.read()
                        end = False
                    except:
                        print(
                            colorama.Fore.RED +
                            "There was an error reading the file. Check that it is a text-based file, and try again."
                        )
                        print("------")
                        end = True

                    if end == False:

                        try:
                            print("---")
                            print(colorama.Fore.LIGHTMAGENTA_EX +
                                  "disassembled code: " + colorama.Style.RESET_ALL)
                            print("------")
                            out = StringIO()
                            with captureStdOut(out):
                                dis.dis(contents)
                            disassembled = out.getvalue()
                            view = disassembled.split("\n")
                            view.pop(len(view) - 1)
                            for item in view:
                                print(item)
                                time.sleep(0.02)
                            print("------")
                        except:
                            print(
                                colorama.Fore.RED +
                                "There was an error disassembling your code. Please try again."
                                + colorama.Style.RESET_ALL)

                            print(colorama.Style.RESET_ALL + "------")

                    time.sleep(0.5)
                    print("Do you wish to " + colorama.Fore.LIGHTGREEN_EX +
                          "save" + colorama.Style.RESET_ALL +
                          " this to a file? (y/n)")
                    print("------")
                    valid = False
                    while valid == False:
                        checker = input(colorama.Style.RESET_ALL + termdes + " ")

                        checker = checker.lower()
                        checker = checker.strip(" ")
                        if checker == "y" or checker == "n":
                            valid = True
                            break
                        else:
                            print(colorama.Fore.RED +
                                  "\033[1mPlease answer with y/n")
                    answer = checker

                    if answer == "y":
                        try:
                            time.sleep(0.5)
                            print("---")
                            print("What name should the file have?")
                            print("---")
                            answer = input(colorama.Style.RESET_ALL + termdes + " ")
                            old = os.getcwd()
                            os.chdir(home_directory + "/Documents")
                            f = open(answer + ".pyb", "w")
                            f.write(disassembled)
                            f.close()
                            os.chdir(old)
                            time.sleep(0.5)
                            print("---")
                            print("File successfully saved... '" +
                                  colorama.Fore.LIGHTMAGENTA_EX + answer +
                                  colorama.Style.RESET_ALL +
                                  "'\nYou can find it in the '" +
                                  colorama.Fore.LIGHTMAGENTA_EX + "Documents" +
                                  colorama.Style.RESET_ALL +
                                  "' folder in the home directory.")
                            print("------")
                        except:
                            print(
                                colorama.Fore.RED +
                                "There was an error saving your code. Please try again."
                                + colorama.Style.RESET_ALL)

                            print(colorama.Style.RESET_ALL + "------")

            except KeyboardInterrupt:
                print()
                print(colorama.Fore.RED + "Cancelling operation..." +
                      colorama.Style.RESET_ALL)

        if request == "scrape" or request == "retrieve" or request == "ws":
            try:
                print("------")
                print("This tool retrieves the " + colorama.Fore.RED + "HTML" +
                      colorama.Style.RESET_ALL + " for a given " +
                      colorama.Fore.LIGHTMAGENTA_EX + "URL" +
                      colorama.Style.RESET_ALL + ".")
                print("---")
                print("Please enter a " + colorama.Fore.LIGHTMAGENTA_EX + "URL" +
                      colorama.Style.RESET_ALL + ":\n")
                url = input(colorama.Style.RESET_ALL + termdes + " ")
                print("------")
                print("Scraping page...")
                try:

                    from urllib.request import urlopen
                    page = urlopen(url)
                    print(page.read())
                except:
                    print(
                        colorama.Fore.RED +
                        "There was an unexpected error while retrieving the web page data. Please check the URL and try again."
                    )
            except KeyboardInterrupt:
                print()
                print(colorama.Fore.RED + "Cancelling operation..." +
                      colorama.Style.RESET_ALL)

        if request == "pt":
            try:
                print("Which file would you like to print?")
                getdirectory()
                print("------")
                listfiles()
                print("------")

                valid = False

                while valid == False:
                    filename = input(colorama.Style.RESET_ALL + termdes + " ")
                    if os.path.exists(filename) == True:
                        valid = True
                        break
                    else:
                        print(colorama.Fore.RED +
                              "\033[1mThe file does not exist in this directory." +
                              colorama.Style.RESET_ALL)
                        valid = False

                try:
                    os.startfile(filename, "print")
                    print("Printing file...")
                    time.sleep(1)
                    print("Request sent!")
                    print("------")
                except:
                    print(
                        colorama.Fore.RED +
                        "This feature is only available in the Windows version... sorry!"
                        + colorama.Style.RESET_ALL)
                    print("------")

            except KeyboardInterrupt:
                print()
                print(colorama.Fore.RED + "Cancelling operation..." +
                      colorama.Style.RESET_ALL)
    ####################################################################
    #BEGIN WORK ON TUTORIAL BELOW#

        def type(text):
            for item in text:
                print(item, end="", flush=True)
                time.sleep(0.03)
            time.sleep(0.3)
            print()

        def cc():
            carry = input(colorama.Style.RESET_ALL + colorama.Fore.LIGHTBLACK_EX +
                          "Press [ENTER] to continue..." +
                          colorama.Style.RESET_ALL)

        if request == "tutorial":
            try:
                old = os.getcwd()
                #begin with command one
                clear()
                type(
                    f"{colorama.Fore.LIGHTMAGENTA_EX}Welcome{colorama.Style.RESET_ALL} to the {colorama.Fore.LIGHTMAGENTA_EX}Core {colorama.Fore.LIGHTGREEN_EX}O{colorama.Fore.LIGHTCYAN_EX}S{colorama.Style.RESET_ALL} tutorial!"
                )
                type("------")
                type(
                    f"Are you {colorama.Fore.LIGHTMAGENTA_EX}ready{colorama.Style.RESET_ALL}?{colorama.Style.RESET_ALL}"
                )
                type(
                    f"(Type {colorama.Fore.LIGHTGREEN_EX}'y' for yes{colorama.Style.RESET_ALL}, or {colorama.Fore.RED}'n' for no{colorama.Style.RESET_ALL}.)"
                )
                print()
                valid = False
                while valid == False:
                    checker = input(colorama.Style.RESET_ALL + termdes + " ")
                    checker = checker.strip(" ")
                    checker = checker.lower()
                    if checker == "y" or checker == "n":
                        valid = True
                        break
                    else:
                        valid = False
                        type(
                            f"(Type {colorama.Fore.LIGHTGREEN_EX}'y' for yes{colorama.Style.RESET_ALL}, or {colorama.Fore.RED}'n' for no{colorama.Style.RESET_ALL}.)"
                        )


                if checker == "y":
                    type("------")
                    type(
                        f"Let's get {colorama.Fore.LIGHTMAGENTA_EX}started{colorama.Style.RESET_ALL}."
                    )
                    time.sleep(1)
                    clear()

                    type(
                        f"Core OS was designed to be {colorama.Fore.LIGHTMAGENTA_EX}simple and understandable{colorama.Style.RESET_ALL}, so that anyone can pick it up and know exactly what they're doing."
                    )
                    carry = input(colorama.Style.RESET_ALL + colorama.Fore.LIGHTBLACK_EX +
                                  "Press [ENTER] to continue..." +
                                  colorama.Style.RESET_ALL)
                    type(
                        f"That's why {colorama.Fore.LIGHTCYAN_EX}key words{colorama.Style.RESET_ALL} are {colorama.Fore.LIGHTMAGENTA_EX}highlighted{colorama.Style.RESET_ALL} with these {colorama.Fore.BLUE}c{colorama.Fore.RED}o{colorama.Fore.LIGHTYELLOW_EX}l{colorama.Fore.BLUE}o{colorama.Fore.LIGHTGREEN_EX}u{colorama.Fore.RED}r{colorama.Fore.BLUE}s{colorama.Style.RESET_ALL} to make things {colorama.Fore.LIGHTMAGENTA_EX}easier{colorama.Style.RESET_ALL} to read."
                    )
                    carry = input(colorama.Style.RESET_ALL + colorama.Fore.LIGHTBLACK_EX +
                                  "Press [ENTER] to continue..." +
                                  colorama.Style.RESET_ALL)
                    type("------")
                    type(
                        f"{colorama.Fore.LIGHTGREEN_EX}Anyway{colorama.Style.RESET_ALL}, on to the {colorama.Fore.LIGHTMAGENTA_EX}tutorial{colorama.Style.RESET_ALL}."
                    )
                    carry = input(colorama.Style.RESET_ALL + colorama.Fore.LIGHTBLACK_EX +
                                  "Press [ENTER] to continue..." +
                                  colorama.Style.RESET_ALL)
                    clear()
                    type(
                        f"Let's start with the {colorama.Fore.LIGHTGREEN_EX}basics{colorama.Style.RESET_ALL}."
                    )
                    cc()
                    type(
                        f"Here's the {colorama.Fore.LIGHTMAGENTA_EX}command line{colorama.Style.RESET_ALL}."
                    )
                    type(
                        f"Try typing {colorama.Fore.RED}'print' or 'echo'{colorama.Style.RESET_ALL}!{colorama.Style.RESET_ALL}"
                    )

                    request = None
                    while request != "print" or request != "echo":
                        request = input(colorama.Style.RESET_ALL + prompt)
                        request = request.lower()
                        request = request.strip(" ")

                        if request == "print" or request == "echo":
                            break
                        if request != "print" or request != "echo":
                            type(
                                f"Try typing {colorama.Fore.RED}'print' or 'echo'{colorama.Style.RESET_ALL}!{colorama.Style.RESET_ALL}"
                            )

                    if request == "print" or request == "echo":
                        print("------")
                        print(
                            f"What do you want to {colorama.Fore.LIGHTMAGENTA_EX}print{colorama.Style.RESET_ALL}?"
                        )
                        echo = input(colorama.Style.RESET_ALL + termdes + " ")
                        print("---")
                        print(echo)
                        print("---")

                    type(
                        f"{colorama.Fore.LIGHTGREEN_EX}Good{colorama.Style.RESET_ALL}! Let's move onto {colorama.Fore.LIGHTMAGENTA_EX}asking for help{colorama.Style.RESET_ALL}..."
                    )
                    cc()
                    clear()
                    type(
                        f"Remembering all of the Core {colorama.Fore.LIGHTMAGENTA_EX}commands{colorama.Style.RESET_ALL} can be {colorama.Fore.RED}difficult{colorama.Style.RESET_ALL} sometimes..."
                    )
                    cc()
                    type(
                        f"But don't worry... There is an {colorama.Fore.LIGHTCYAN_EX}extensive{colorama.Style.RESET_ALL} list of commands, accessible by simply typing {colorama.Fore.LIGHTGREEN_EX}'help'{colorama.Style.RESET_ALL}!"
                    )
                    cc()
                    type(
                        f"Here's the {colorama.Fore.LIGHTMAGENTA_EX}command line{colorama.Style.RESET_ALL} again..."
                    )
                    cc()
                    type(
                        f"Try typing {colorama.Fore.LIGHTGREEN_EX}'help'{colorama.Style.RESET_ALL}!"
                    )

                    request = None
                    while request != "help":
                        request = input(colorama.Style.RESET_ALL + prompt)
                        request = request.lower()
                        request = request.strip(" ")

                        if request == "help":
                            break
                        if request != "help":
                            type(
                                f"Try typing {colorama.Fore.LIGHTGREEN_EX}'help'{colorama.Style.RESET_ALL}!"
                            )

                    if request == "help":
                        printhelp()

                    cc()
                    type("------")
                    type(f"Woah!")
                    time.sleep(1)
                    type(
                        f"There's quite a {colorama.Fore.LIGHTGREEN_EX}lot{colorama.Style.RESET_ALL} of info there!"
                    )
                    cc()
                    clear()
                    type(
                        f"It's all {colorama.Fore.LIGHTCYAN_EX}gone{colorama.Style.RESET_ALL} now..."
                    )
                    type(
                        f"Don't {colorama.Fore.RED}fret{colorama.Style.RESET_ALL}! This {colorama.Fore.LIGHTMAGENTA_EX}tutorial{colorama.Style.RESET_ALL} should help to make this much less {colorama.Fore.RED}complex{colorama.Style.RESET_ALL}, and narrow it all down."
                    )
                    cc()
                    type(
                        f"Let's work on some more {colorama.Fore.LIGHTGREEN_EX}basic{colorama.Style.RESET_ALL} commands."
                    )
                    cc()
                    type(
                        f"{colorama.Fore.LIGHTMAGENTA_EX}Clearing the screen{colorama.Style.RESET_ALL} is something you may want to do every now and then..."
                    )
                    clutter = [
                        "a", "()", "!", "#", "~", "K", "+", "=", "^", "T", "d",
                        "¬", "`", "¦", "<", ">", "@", "?", "/", "]", "_", "%"
                    ]
                    for x in range(0, 300):
                        print(clutter[random.randint(0, (len(clutter) - 1))],
                              end="",
                              flush=True)
                    print()
                    type(
                        f"{colorama.Fore.LIGHTGREEN_EX}Clear up{colorama.Style.RESET_ALL} that {colorama.Fore.RED}clutter{colorama.Style.RESET_ALL} by typing {colorama.Fore.LIGHTMAGENTA_EX}'cls' or 'clear'{colorama.Style.RESET_ALL}!"
                    )
                    print()

                    request = None
                    while request != "clear" or request != "cls":
                        request = input(colorama.Style.RESET_ALL + prompt)
                        request = request.lower()
                        request = request.strip(" ")

                        if request == "clear" or request == "cls":
                            break
                        else:
                            type(
                                f"Try typing {colorama.Fore.LIGHTGREEN_EX}'cls' or 'clear'{colorama.Style.RESET_ALL} to clear the screen!"
                            )

                    if request == "clear" or request == "cls":
                        clear()

                    type(
                        f"Ahh... {colorama.Fore.LIGHTGREEN_EX}good{colorama.Style.RESET_ALL}."
                    )
                    type(
                        f"How about {colorama.Fore.LIGHTMAGENTA_EX}listing{colorama.Style.RESET_ALL} all of the {colorama.Fore.LIGHTMAGENTA_EX}files{colorama.Style.RESET_ALL} in a {colorama.Fore.RED}directory{colorama.Style.RESET_ALL}?"
                    )
                    cc()
                    type(
                        f"{colorama.Fore.LIGHTYELLOW_EX}Hint:{colorama.Style.RESET_ALL}{colorama.Fore.RED} 'directory'{colorama.Style.RESET_ALL} is a fancy word for {colorama.Fore.LIGHTGREEN_EX}'folder'{colorama.Style.RESET_ALL}"
                    )
                    cc()
                    type("------")
                    type(
                        f"You can do this by {colorama.Fore.LIGHTMAGENTA_EX}typing{colorama.Style.RESET_ALL} {colorama.Fore.LIGHTGREEN_EX}'ls'{colorama.Style.RESET_ALL}!"
                    )
                    type(
                        f"Why not {colorama.Fore.LIGHTMAGENTA_EX}give it a try{colorama.Style.RESET_ALL}?"
                    )

                    request = None
                    while request != "ls":
                        request = input(colorama.Style.RESET_ALL + prompt)
                        request = request.lower()
                        request = request.strip(" ")

                        if request == "ls":
                            break
                        else:
                            type(
                                f"Try typing {colorama.Fore.LIGHTGREEN_EX}'ls'{colorama.Style.RESET_ALL} to list the files!"
                            )

                    if request == "ls":
                        fullls()

                    type(
                        f"This isn't anything {colorama.Fore.LIGHTMAGENTA_EX}complicated{colorama.Style.RESET_ALL}, it's just all the files in the folder that you're in."
                    )
                    type(
                        f"It's very {colorama.Fore.LIGHTMAGENTA_EX}useful{colorama.Style.RESET_ALL} and you'll use it more and more when running {colorama.Fore.LIGHTMAGENTA_EX}Core{colorama.Style.RESET_ALL}."
                    )
                    type(f"{colorama.Fore.LIGHTYELLOW_EX}Hint: {colorama.Style.RESET_ALL}important {colorama.Fore.RED}system files{colorama.Style.RESET_ALL} and {colorama.Fore.RED}folders{colorama.Style.RESET_ALL} are highlighted in {colorama.Fore.LIGHTCYAN_EX}cyan{colorama.Style.RESET_ALL}. I recommend {colorama.Fore.RED}not{colorama.Style.RESET_ALL} deleting these files, as they could result in your system {colorama.Fore.RED}being rendered unusable{colorama.Style.RESET_ALL}.")

                    cc()
                    clear()
                    type(
                        f"You're almost a Core OS {colorama.Fore.LIGHTMAGENTA_EX}master{colorama.Style.RESET_ALL}!"
                    )
                    type(
                        f"Just a {colorama.Fore.BLUE}few{colorama.Style.RESET_ALL} more commands to go!"
                    )
                    cc()
                    type(
                        f"Hang on... did you know that you can press {colorama.Fore.LIGHTMAGENTA_EX}'ctrl' and 'c'{colorama.Style.RESET_ALL} at the same time to {colorama.Fore.RED}cancel{colorama.Style.RESET_ALL} an operation?"
                    )
                    cc()
                    type(
                        f"Let's {colorama.Fore.LIGHTGREEN_EX}give it a go{colorama.Style.RESET_ALL}!"
                    )
                    cc()
                    type("------")
                    type(
                        f"This {colorama.Fore.LIGHTMAGENTA_EX}while loop{colorama.Style.RESET_ALL} is currently {colorama.Fore.RED}running...{colorama.Style.RESET_ALL}"
                    )
                    type(
                        f"Press {colorama.Fore.LIGHTMAGENTA_EX}'ctrl' and 'c'{colorama.Style.RESET_ALL} to stop it!"
                    )

                    try:
                        while True:
                            print(clutter[random.randint(0, (len(clutter) - 1))],
                                  end="",
                                  flush=True)
                            time.sleep(0.5)
                    except KeyboardInterrupt:
                        print()

                    cc()
                    type(
                        f"{colorama.Fore.LIGHTGREEN_EX}Great!{colorama.Style.RESET_ALL}"
                    )
                    cc()
                    clear()
                    type(
                        f"Sometimes, coding {colorama.Fore.LIGHTMAGENTA_EX}ideas{colorama.Style.RESET_ALL} or {colorama.Fore.LIGHTMAGENTA_EX}concepts{colorama.Style.RESET_ALL} can be easy to {colorama.Fore.RED}forget{colorama.Style.RESET_ALL}..."
                    )
                    cc()
                    type(
                        f"No fear, {colorama.Fore.LIGHTGREEN_EX}'note'{colorama.Style.RESET_ALL} is here!"
                    )
                    type(
                        f"This works just like the {colorama.Fore.LIGHTMAGENTA_EX}'Notes'{colorama.Style.RESET_ALL} app on your phone!"
                    )
                    cc()
                    type(
                        f"Try typing {colorama.Fore.LIGHTGREEN_EX}'note'{colorama.Style.RESET_ALL} into the terminal!"
                    )
                    cc()
                    type(
                        f"{colorama.Fore.RED}IMPORTANT{colorama.Style.RESET_ALL}: If you don't press enter at the end of the last line it {colorama.Fore.RED}won't{colorama.Style.RESET_ALL} work.\nThat's just {colorama.Fore.LIGHTYELLOW_EX}Pyt{colorama.Fore.LIGHTCYAN_EX}hon{colorama.Style.RESET_ALL} for you."
                    )
                    request = None
                    while request != "note":
                        request = input(colorama.Style.RESET_ALL + prompt)
                        request = request.lower()
                        request = request.strip(" ")

                        if request == "note":
                            break
                        else:
                            type(
                                f"Try typing {colorama.Fore.LIGHTGREEN_EX}'note'{colorama.Style.RESET_ALL}!"
                            )

                    if request == "note":
                        donotes()

                        cc()

                    type(
                        f"{colorama.Fore.LIGHTGREEN_EX}Great{colorama.Style.RESET_ALL}!"
                    )

                    type(
                        f"Ever have a {colorama.Fore.LIGHTMAGENTA_EX}blank mind{colorama.Style.RESET_ALL} while coding, or {colorama.Fore.LIGHTMAGENTA_EX}really{colorama.Style.RESET_ALL} need to know how to do something?"
                    )
                    type(
                        f"A neat little {colorama.Fore.RED}module{colorama.Style.RESET_ALL} called {colorama.Fore.LIGHTMAGENTA_EX}'howdoi'{colorama.Style.RESET_ALL} can give you quick reminders."
                    )
                    cc()
                    type(
                        f"Try typing {colorama.Fore.LIGHTMAGENTA_EX}'howdoi'{colorama.Style.RESET_ALL}, then..."
                    )
                    type(
                        f"{colorama.Fore.LIGHTGREEN_EX}anything you might need to know.{colorama.Style.RESET_ALL}!"
                    )
                    cc()
                    request = None
                    while request != "howdoi":
                        request = input(colorama.Style.RESET_ALL + prompt)
                        request = request.lower()
                        request = request.strip(" ")

                        if request == "howdoi":
                            break
                        else:
                            type(
                                f"Try typing {colorama.Fore.LIGHTGREEN_EX}'howdoi'{colorama.Style.RESET_ALL}!"
                            )

                    if request == "howdoi":
                        try:
                            print("------")
                            print("What do you want help with?")
                            print("---")
                            howto = input(colorama.Style.RESET_ALL + termdes + colorama.Fore.LIGHTGREEN_EX +
                                          " How " + colorama.Style.RESET_ALL +
                                          "do I... ")
                            print("------")
                            os.system("howdoi " + howto)
                            print("------")
                            check = random.randint(1, 5)

                            if check == 5:
                                valid = False
                                while valid == False:
                                    checker = input(colorama.Style.RESET_ALL + "Did that answer your" +
                                                    colorama.Fore.LIGHTMAGENTA_EX +
                                                    " question? (y/n)\n" +
                                                    termdes + " ")
                                    checker = checker.strip(" ")
                                    checker = checker.lower()
                                    if checker == "y" or checker == "n":
                                        valid = True
                                        break
                                    else:
                                        valid = False

                                if checker == "y":
                                    print(colorama.Fore.LIGHTMAGENTA_EX +
                                          "Thanks" + colorama.Style.RESET_ALL +
                                          " for your feedback!")
                                else:
                                    print(colorama.Fore.RED +
                                          "What could be improved?" +
                                          colorama.Style.RESET_ALL)
                                    improv = input(colorama.Style.RESET_ALL + termdes + " ")
                                    old = os.getcwd()
                                    try:
                                        os.chdir(home_directory + "/System")
                                        f = open("responses.txt", "a")
                                        f.write(improv + "\n")
                                        f.close()
                                        os.chdir(old)
                                    except:
                                        None
                                    print("------")
                                    print(colorama.Fore.LIGHTMAGENTA_EX +
                                          "Thanks" + colorama.Style.RESET_ALL +
                                          " for your feedback!")
                                    print("------")
                        except KeyboardInterrupt:
                            print()
                            print(colorama.Fore.RED + "Cancelling operation..." +
                                  colorama.Style.RESET_ALL)
                        except:
                            print(
                                colorama.Fore.RED +
                                "An error ocurred whilst running howdoi...\nAre all the packages installed?"
                                + colorama.Style.RESET_ALL)

                    cc()
                    type("------")
                    type(
                        f"Sometimes, it may ask for {colorama.Fore.LIGHTMAGENTA_EX}feedback{colorama.Style.RESET_ALL}. Don't worry about that {colorama.Fore.RED}too much{colorama.Style.RESET_ALL}... it's just for {colorama.Fore.LIGHTMAGENTA_EX}future improvements{colorama.Style.RESET_ALL} :D"
                    )
                    cc()

                    type(
                        f"Almost {colorama.Fore.LIGHTGREEN_EX}done{colorama.Style.RESET_ALL}!"
                    )
                    cc()
                    clear()
                    type(
                        f"To {colorama.Fore.LIGHTMAGENTA_EX}enter{colorama.Style.RESET_ALL} a directory (or folder), simply type {colorama.Fore.LIGHTMAGENTA_EX}'chdir'{colorama.Style.RESET_ALL}!"
                    )

                    request = None
                    while request != "chdir":
                        request = input(colorama.Style.RESET_ALL + prompt)
                        request = request.lower()
                        request = request.strip(" ")

                        if request == "chdir":
                            break
                        else:
                            type(
                                f"Try typing {colorama.Fore.LIGHTGREEN_EX}'chdir'{colorama.Style.RESET_ALL}!"
                            )

                    if request == "chdir":
                        try:
                            print("------")
                            print("Which folder would you like to enter?")
                            print("------")
                            listfolders()
                            valid = False

                            while valid == False:
                                selection = input(colorama.Style.RESET_ALL + termdes + " ")
                                try:
                                    os.chdir(selection)
                                    print(colorama.Fore.LIGHTGREEN_EX +
                                          "Successfully entered folder: '" +
                                          colorama.Fore.LIGHTMAGENTA_EX +
                                          selection + colorama.Fore.LIGHTGREEN_EX +
                                          "'" + colorama.Style.RESET_ALL)
                                    print("------")
                                    valid = True
                                except:
                                    print(colorama.Fore.RED +
                                          "\033[1mError: folder '" + selection +
                                          "' not found.")
                                    valid = False
                        except KeyboardInterrupt:
                            print()
                            print(colorama.Fore.RED + "Cancelling operation..." +
                                  colorama.Style.RESET_ALL)

                    cc()
                    type(
                        f"{colorama.Fore.LIGHTGREEN_EX}Perfect{colorama.Style.RESET_ALL}! Last command..."
                    )
                    cc()
                    clear()
                    type(
                        f"Once you're in a {colorama.Fore.LIGHTMAGENTA_EX}folder{colorama.Style.RESET_ALL}, you might realise that you {colorama.Fore.RED}can't{colorama.Style.RESET_ALL} use {colorama.Fore.LIGHTMAGENTA_EX}'chdir'{colorama.Style.RESET_ALL} to go back to the folder that {colorama.Fore.LIGHTMAGENTA_EX}you just came from{colorama.Style.RESET_ALL}."
                    )
                    cc()
                    type(
                        f"You can use {colorama.Fore.LIGHTMAGENTA}dirbk{colorama.Style.RESET_ALL} to {colorama.Fore.RED}return{colorama.Style.RESET_ALL} to where you just were."
                    )
                    type(f"Let's give it a go!")
                    cc()
                    type("------")
                    request = None
                    while request != "dirbk":
                        request = input(colorama.Style.RESET_ALL + prompt)
                        request = request.lower()
                        request = request.strip(" ")

                        if request == "dirbk":
                            break
                        else:
                            type(
                                f"Try typing {colorama.Fore.LIGHTGREEN_EX}'dirbk'{colorama.Style.RESET_ALL}!"
                            )
                        dirback()
                        print(prompt)
                        type("------")
                        cc()
                        type(
                            f"I think you're {colorama.Fore.LIGHTGREEN_EX}ready{colorama.Style.RESET_ALL} to explore the {colorama.Fore.LIGHTCYAN}wild world{colorama.Style.RESET_ALL} of the {colorama.Fore.RED}help section{colorama.Style.RESET_ALL} now..."
                        )
                        cc()
                        type(
                            f"I would recommend using {colorama.Fore.LIGHTMAGENTA_EX}'read'{colorama.Style.RESET_ALL} to have a look at the note that you made as a first step!"
                        )
                        cc()
                        type(
                            f"Remember {colorama.Fore.LIGHTMAGENTA_EX}'ctrl' + 'c'{colorama.Style.RESET_ALL}? Use it now to {colorama.Fore.RED}end{colorama.Style.RESET_ALL} the tutorial!"
                        )
                        try:
                            while True:
                                None

                        except KeyboardInterrupt:
                            type(
                                f"Enjoy using {colorama.Fore.LIGHTMAGENTA_EX}Core{colorama.Fore.LIGHTCYAN_EX}OS{colorama.Style.RESET_ALL}!"
                            )
                            type("------")
                            cc()

            except KeyboardInterrupt:
                print()
                print(colorama.Fore.RED + "Cancelling operation..." +
                      colorama.Style.RESET_ALL)
                os.chdir(old)
            except:
                print()
                type(colorama.Fore.RED + "An unexpected error ocurred... sorry!" +
                     colorama.Style.RESET_ALL)
                os.chdir(old)

        if request == "clrcache":
            old = os.getcwd()
            
            os.chdir(home_directory)

            os.remove("installcache.txt")

            f = open("installcache.txt", "w+")

            f.close()

            print("------")
            print(
                f"Cache {colorama.Fore.LIGHTGREEN_EX}cleared{colorama.Style.RESET_ALL}."
            )
            print("------")

            os.chdir(old)

        if request == "text":
            colorList = ["red", "yellow", "green", "blue", "purple"]

            def typeUser(text, delay, color):
                if color == "red":
                    color = colorama.Fore.RED
                elif color == "yellow":
                    color = colorama.Fore.LIGHTYELLOW_EX
                elif color == "green":
                    color = colorama.Fore.LIGHTGREEN_EX
                elif color == "blue":
                    color = colorama.Fore.LIGHTCYAN_EX
                elif color == "purple":
                    color = colorama.Fore.LIGHTMAGENTA_EX
                elif color == "None" or color == None:
                    color = None
                for char in text:
                    if color != None:
                        print(color + char, end="", flush=True)
                    else:
                        print(char, end="", flush=True)
                    time.sleep(float(int(delay) / 100))
                print(colorama.Style.RESET_ALL)
                return 0

            userText = None
            userDelay = None
            userColor = "null"

            typeUser("Type a string, delay, and colour, separated with commas.", 7,
                     "purple")
            typeUser("E.g.: Hello, 7, green", 7, "None")
            typeUser(
                f"The delay is in {colorama.Fore.LIGHTMAGENTA_EX}hundredths of seconds{colorama.Style.RESET_ALL}.",
                7, None)
            print("------")
            while not isinstance(userDelay,
                                 int) and not userColor.lower() in colorList:
                userText, userDelay, userColor = input(colorama.Style.RESET_ALL + 
                    f"Text, delay, colour {termdes} ").strip(" ").split(",")
                print("------")
                userText = userText.strip(" ")
                userDelay = userDelay.strip(" ")
                userColor = userColor.strip(" ")
                userDelaytemp = None
                try:
                    userDelaytemp = int(userDelay)
                except:
                    userDelaytemp = None

                if not isinstance(userDelaytemp,
                                  int) or not userColor.lower() in colorList:

                    if not isinstance(userDelaytemp, int):
                        print(
                            f"The delay should be a {colorama.Fore.LIGHTMAGENTA_EX}number{colorama.Style.RESET_ALL}. This is in {colorama.Fore.LIGHTMAGENTA_EX}hundredths{colorama.Style.RESET_ALL} of seconds."
                        )

                    if not userColor.lower() in colorList:
                        print("Please choose a colour in the colour list.")
                        print(colorama.Style.RESET_ALL + "-" +
                              colorama.Fore.LIGHTMAGENTA_EX,
                              end=" ")
                        print(*colorList,
                              sep=colorama.Style.RESET_ALL + "\n- " +
                              colorama.Fore.LIGHTMAGENTA_EX)
                        print(colorama.Style.RESET_ALL + "------")

            typeUser(userText, userDelay, userColor)
            print("------")



        if request == "move" or request == "mv":
            old = os.getcwd()
            try:
                print(f"Which {colorama.Fore.LIGHTMAGENTA_EX}file{colorama.Style.RESET_ALL} would you like to {colorama.Fore.LIGHTMAGENTA_EX}move{colorama.Style.RESET_ALL}?")

                getdirectory()
                print("------")
                listfiles()
                folderscan()
                print("------")
                valid = False
                while valid == False:
                    filename = input(colorama.Style.RESET_ALL + termdes + " ")
                    try:
                        with open(filename) as f:
                            None
                        valid = True
                    except:
                        print(colorama.Fore.RED + "\033[1mError: file: '" + filename +
                              "' not found.")
                        valid = False

                filename = filename
                if filename not in systemdirs:
                    print(f"Where would you like to {colorama.Fore.LIGHTMAGENTA_EX}move{colorama.Style.RESET_ALL} it to?")
                    getdirectory()
                    print("------")
                    listfolders()
                    folderscan()
                    print("------")

                    valid = False
                    while valid == False:
                        foldername = input(colorama.Style.RESET_ALL + termdes + " ")
                        if os.path.isdir(foldername) == True and filename not in systemdirs:
                            valid = True
                            try:
                                shutil.move(filename, foldername)
                                print(f"{colorama.Fore.LIGHTGREEN_EX}Move complete!{colorama.Style.RESET_ALL}")
                                print("------")
                            except:
                                print(colorama.Fore.RED + "That didn't quite work. Please make sure that your paths are valid." + colorama.Style.RESET_ALL)
                                break

                        elif os.path.isdir(foldername) == False:
                            print(colorama.Fore.RED + "\033[1mError: file: '" + foldername +
                                  "' not found." + colorama.Style.RESET_ALL)
                            valid = False
                        elif filename in systemdirs:
                            print(colorama.Fore.RED + "System files may not be moved." + colorama.Style.RESET_ALL)
                            break
                else:
                    print(colorama.Fore.RED + "System files may not be moved." + colorama.Style.RESET_ALL)

            except KeyboardInterrupt:
                print()
                print(colorama.Fore.RED + "Cancelling operation..." +
                      colorama.Style.RESET_ALL)
                os.chdir(old)


        if request == "pids" or request == "running" or request == "tasks":
            try:
                print("----------")
                print(f"Here is a {colorama.Fore.LIGHTMAGENTA_EX}list{colorama.Style.RESET_ALL} of all of the currently running {colorama.Fore.LIGHTMAGENTA_EX}tasks{colorama.Style.RESET_ALL}.")
                gettasks()
            except KeyboardInterrupt:
                print()
                print(colorama.Fore.RED + "Cancelling operation..." +
                      colorama.Style.RESET_ALL)
                os.chdir(old)

        if request == "cmdline" or request == "tskline":
            try:
                print("----------")
                print(f"Which {colorama.Fore.LIGHTMAGENTA_EX}task{colorama.Style.RESET_ALL} would you like to get the {colorama.Fore.LIGHTMAGENTA_EX}command line{colorama.Style.RESET_ALL} for?")
                gettasks()
                valid = False

                while valid == False:
                    taskid = input(colorama.Style.RESET_ALL + termdes + " ")
                    try:
                        taskid = int(taskid)
                        if int(taskid) in runningProcesses:
                            valid = True
                            break
                        else:
                            valid = False
                            print(colorama.Fore.RED + "Please enter a valid task number" + colorama.Style.RESET_ALL)
                    except:
                        valid = False
                        print(colorama.Fore.RED + "Please enter a valid task number" + colorama.Style.RESET_ALL)



                temp = psutil.Process(taskid)
                listwe = temp.cmdline()
                print("------")
                for item in listwe:
                    print(" - " + colorama.Fore.LIGHTMAGENTA_EX + item + colorama.Style.RESET_ALL)
                    time.sleep(0.02)
                print("------")


            except KeyboardInterrupt:
                print()
                print(colorama.Fore.RED + "Cancelling operation..." +
                      colorama.Style.RESET_ALL)
                os.chdir(old)    

        if request == "curl" or request == "wget" or request == "download":
            try:
                red = colorama.Fore.RED
                purple = colorama.Fore.LIGHTMAGENTA_EX
                green = colorama.Fore.LIGHTGREEN_EX
                blue = colorama.Fore.LIGHTCYAN_EX
                black = colorama.Fore.LIGHTBLACK_EX
                reset = colorama.Style.RESET_ALL
                old = os.getcwd()

                def exclusiveType(text):
                    for x in text:
                        print(x, end = "", flush = True)
                        time.sleep(0.02)
                    print()

                def dirback():
                    global parent
                    parent = os.path.dirname(os.getcwd())
                    os.chdir(parent)


                valid = False
                print("------")
                exclusiveType(f"Please enter the {purple}URL{reset} of the {blue}file{reset} you want to {green}download{reset}.")

                while valid == False:
                    url = input(colorama.Style.RESET_ALL + f"{termdes} {blue}")
                    print(reset, end = "")
                    valid = True

                exclusiveType(f"Type a {blue}file name{reset} to {green}save{reset} the file as.")
                exclusiveType(f"If you wish to {purple}enter a directory{reset}, simply type its {blue}name{reset}.")
                exclusiveType(f"If you wish {red}to go back{reset}, type '{blue}dirbk{reset}'")


                fullls()


                valid = False
                while valid == False:
                    userI = input(colorama.Style.RESET_ALL + f"{termdes} {blue}")
                    print(reset, end = "")
                    if userI in os.listdir(os.getcwd()):
                        try:
                            os.chdir(userI)
                            getdirectory()
                            print("------")

                        except:
                            exclusiveType("This file name is taken.")

                    elif userI.lower().strip() == "dirbk":
                        dirback()
                        getdirectory()
                        print("------")
                    else:
                        try:

                            os.system(f"curl {url} -o {userI} > installcache.txt")
                            print(reset, end = "")
                            print(f"{green}Operation complete.{reset}\n------")
                            valid = True
                        except:
                            print(red + "A fatal error occurred whilst trying to download the file. Please try again." + reset)

            except KeyboardInterrupt:
                print()
                print(colorama.Fore.RED + "Cancelling operation..." +
                      colorama.Style.RESET_ALL)
                os.chdir(old)
            except:
                print()
                print(colorama.Fore.RED + "A fatal error occurred. Please try again." +
                      colorama.Style.RESET_ALL)
                os.chdir(old)



        if request == "makerm":
            try:
                red = colorama.Fore.RED
                purple = colorama.Fore.LIGHTMAGENTA_EX
                green = colorama.Fore.LIGHTGREEN_EX
                blue = colorama.Fore.LIGHTCYAN_EX
                black = colorama.Fore.LIGHTBLACK_EX
                reset = colorama.Style.RESET_ALL
                old = os.getcwd()

                print("------")
                def exclusiveType(text):
                    for x in text:
                        print(x, end = "", flush = True)
                        time.sleep(0.02)
                    print()

                valid = False
                exclusiveType(f"Please type a reminder {purple}title{reset}:")
                while valid == False: 
                    title = input(reset + termdes + " " + blue)
                    if title.strip() != "":
                        valid = True
                    else:
                        valid = False
                        print(red + "Reminder title cannot be empty." + reset)
                print(reset, end = "")
                exclusiveType(f"Please type a short reminder {green}description{reset}:")
                exclusiveType(black + "Type nothing and click [ENTER] for no description.")
                description = input(reset + f"{termdes} " + blue)

                print(reset, end = "")
                exclusiveType(f"Please type a reminder {blue}time{reset}:")
                exclusiveType(black + "Type nothing and click [ENTER] for no time.")
                valid = False
                while valid == False:
                    timeA = input(reset + black + "(HH:MM)"+reset+f" {termdes} " + blue)
                    print(reset, end = "")
                    if str(timeA).strip() != "":
                        try:
                            timeA = datetime.strptime(timeA, "%H:%M")
                            valid = True
                        except ValueError:
                            print(red + "Invalid time format. Please try again." + reset)
                    else:
                        valid = True



                if str(timeA).strip() != "":
                    timeR = str(timeA)[11:len(str(timeA))-3]
                else:
                    timeR = "No time."

                if description.strip() != "":
                    description = description
                else:
                    description = "No description."
                os.chdir(home_directory)
                os.chdir("System")

                if os.path.exists("Reminders.log") and os.path.getsize("Reminders.log") > 0:
                    f = open("Reminders.log", "a")
                    f.write(title + "/"+description+"/"+ timeR + "\n")
                else:
                    f = open("Reminders.log", "w")
                    f.write(title + "/"+description+"/"+ timeR + "\n")

                f.close()
                print(green + "Reminder successfully added!" + reset +f" Type '{purple}viewrm{reset}' at {blue}any time{reset} to view {green}reminders{reset}." + reset)
                print("------")
                os.chdir(old)
            except KeyboardInterrupt:
                print()
                print(colorama.Fore.RED + "Cancelling operation..." +
                      colorama.Style.RESET_ALL)
                os.chdir(old)
            except:
                print()
                print(colorama.Fore.RED + "A fatal error occurred. Please try again." +
                      colorama.Style.RESET_ALL)
                os.chdir(old)

        if request == "viewrm" or request == "remind":
            try:
                red = colorama.Fore.RED
                purple = colorama.Fore.LIGHTMAGENTA_EX
                green = colorama.Fore.LIGHTGREEN_EX
                blue = colorama.Fore.LIGHTCYAN_EX
                black = colorama.Fore.LIGHTBLACK_EX
                reset = colorama.Style.RESET_ALL
                old = os.getcwd()

                os.chdir(home_directory)
                os.chdir("System")

                if os.path.exists("Reminders.log") and os.path.getsize("Reminders.log") > 0:
                    f = open("Reminders.log")

                    contents = f.read().splitlines()

                    reminders = []
                    for item in contents:
                        reminders.append(item.split("/"))

                    colour1 = blue
                    colour2 = purple
                    colour3 = green

                    colournum = 0
                    idx = 0
                    print(black + "------" + reset)  
                    for item in reminders:

                        idx = idx +1

                        title = item[0]
                        description = item[1]
                        time = item[2]

                        colournum = colournum + 1
                        if colournum == 1:
                            colour = colour1
                        elif colournum == 2:
                            colour = colour2
                        elif colournum == 3:
                            colour = colour3
                        elif colournum == 4:
                            colournum = 1
                            colour = colour1



                        print(f"{colour}Reminder {idx}:{reset} {item[0]}")
                        print(black + "------" + reset)  
                        if description != "No description.":
                            print(f"Description: \033[3m{black}{description}{reset}")
                        else:
                            print(black + "No description." + reset)
                        print(black + "------" + reset)  
                        print(f"Time: {blue}{time}{reset}")
                        print(black + "---------\n" + reset) 
                        if reminders.index(item) != len(reminders)-1:
                            print(black + "---------" + reset) 
                else:
                    print(black + "---------" + reset) 
                    print(red + "No reminders found." + reset + f" Type '{purple}makerm{reset}' to {blue}make one{reset}!")
                    print(black + "---------" + reset) 
            except KeyboardInterrupt:
                print()
                print(colorama.Fore.RED + "Cancelling operation..." +
                      colorama.Style.RESET_ALL)
                os.chdir(old)

            except:
                print()
                print(colorama.Fore.RED + "A fatal error occurred. Please try again." +
                      colorama.Style.RESET_ALL)
                os.chdir(old)

        if request == "markrm":
            try:

                blue = colorama.Fore.LIGHTCYAN_EX
                green = colorama.Fore.LIGHTGREEN_EX
                purple  = colorama.Fore.LIGHTMAGENTA_EX
                red = colorama.Fore.RED
                black = colorama.Fore.LIGHTBLACK_EX
                reset = colorama.Style.RESET_ALL
                old = os.getcwd()
                os.chdir(home_directory)
                os.chdir("System")
                if os.path.exists("Reminders.log") and os.path.getsize("Reminders.log") > 0:
                    f = open("Reminders.log","r")
                    contents = f.read().splitlines()

                    reminders = []
                    for item in contents:
                        reminders.append(item.split("/"))

                    colour1 = blue
                    colour2 = purple
                    colour3 = green

                    colournum = 0
                    idx = 0
                    print(black + "------" + reset)  
                    for item in reminders:

                        idx = idx +1

                        title = item[0]
                        description = item[1]
                        time = item[2]

                        colournum = colournum + 1
                        if colournum == 1:
                            colour = colour1
                        elif colournum == 2:
                            colour = colour2
                        elif colournum == 3:
                            colour = colour3
                        elif colournum == 4:
                            colournum = 1
                            colour = colour1



                        print(f"{colour}Reminder {idx}:{reset} {item[0]}")
                        print(black + "------" + reset)  
                        if description != "No description.":
                            print(f"Description: \033[3m{black}{description}{reset}")
                        else:
                            print(black + "No description." + reset)
                        print(black + "------" + reset)  
                        print(f"Time: {blue}{time}{reset}")
                        print(black + "---------\n" + reset) 


                        if reminders.index(item) != len(reminders)-1:
                            print(black + "---------" + reset) 
                        f.close()


                    valid = False
                    while valid == False:

                        print(f"Enter the {purple}number{reset} of the {blue}reminder{reset} you want to {green}tick off{reset}.")

                        delete = input(f"{reset}{termdes}{blue} ")
                        print(reset, end = "")

                        try:
                            delete = int(delete)
                            if delete > 0 and delete <= len(reminders):
                                valid = True
                            else:
                                print(f"{red}Invalid input.{reset}")
                        except:
                            print(f"{red}Invalid input.{reset}")
                    f = open("Reminders.log", "r")
                    reminderstr = f.read().splitlines() 
                    f.close()
                    deleted = reminderstr[delete-1]
                    reminderstr.pop(delete-1)
                    f = open("Reminders.log", "w")
                    for item in reminderstr:
                        f.write(item + "\n")
                    f.close()
                    deleted = deleted.split("/")
                    deleted = deleted[0]
                    print(black + "---------" + reset) 
                    print(f"Reminder: '{purple}{deleted}{reset}' marked as {green}done{reset}.")
                    print(black + "---------" + reset) 
                    os.chdir(old)

                else:
                    print(black + "---------" + reset) 
                    print(f"You currently have {red}no reminders{reset}. Type '{purple}makerm{reset}' to {blue}make some{reset}.")
                    print(black + "---------" + reset) 
                    os.chdir(old)
            except KeyboardInterrupt:
                print()
                print(colorama.Fore.RED + "Cancelling operation..." +
                      colorama.Style.RESET_ALL)
                os.chdir(old)
            except:
                print()
                print(colorama.Fore.RED + "A fatal error occurred. Please try again." +
                      colorama.Style.RESET_ALL)
                os.chdir(old)




        if request == "imgrun" or request == "runimg": 
            try:
                old = os.getcwd()
                getdirectory()
                print("------")
                listfilesExt(".AppImage")
                print("------")
                print(f"Which {blue}AppImage{reset} do you wish to {green}run{reset}? ({red}Be careful when running images from unknown sources{reset}...)")


                valid = False
                while valid == False:
                    temp = input(termdes + " ")
                    if temp.strip() in os.listdir(os.getcwd()) and temp.endswith(".AppImage"):
                        valid = True
                    else:
                        print(f"{red}Please give a valid .AppImage name.{reset}")
                        valid = False


                filename = temp.strip()
                print(f"{blue}Preparing{reset} to run {purple}AppImage{reset}...")
                print(f"{red}Please be aware{reset} that you may have to install the {blue}AppImage's dependencies{reset} through the {blue}terminal{reset}.")
                time.sleep(2)
                print(f"Use the '{blue}System{reset}' command to do this.")
                time.sleep(1)
                os.system(f"chmod +x ./{filename}")
                os.system(f"./{filename} --appimage-extract")
                os.system(f"./squashfs-root/AppRun --no-sandbox")
                print(f"{green}Done!{reset}")

            except KeyboardInterrupt:
                print()
                print(colorama.Fore.RED + "Cancelling operation..." +
                      colorama.Style.RESET_ALL)
                os.chdir(old)
            except:
                print()
                print(colorama.Fore.RED + "A fatal error occurred. Please try again." + reset)
                os.chdir(old)



        if request == "news":

            try:
                old = os.getcwd()
                print(f"Would you like to {red}deactivate the news{reset} on the {purple}terminal{reset}? {black}(y/n){reset}")
                valid = False
                while valid == False:
                    temp = input(termdes + " ")

                    if temp.lower().strip() in ["y", "n"]:
                        valid = True
                    else:
                        valid = False
                        print(f"{blue}Please type{reset} '{green}y{reset}' or '{red}n{reset}'.")

                if temp.lower().strip() == "y":
                    newsActive = False
                    print(f"{red}News{reset} {blue}disabled{reset}.")
                else:
                    newsActive = True
                    print(f"{red}News{reset} {blue}enabled{reset}.")
            except KeyboardInterrupt:
                print()
                print(colorama.Fore.RED + "Cancelling operation..." +
                      colorama.Style.RESET_ALL)
                os.chdir(old)




        if request == "chuser":
            try:
                changed = False
                wrong = False
                print(f"What should the {purple}username{reset} be {blue}changed to{reset}?")
                newUser = input(termdes + " ")
                for item in newUser:
                    if item.lower() not in alpha:
                        wrong = True
                        break
                    else:
                        wrong = False
    
                    
                users = []
                for item in os.listdir(ogdir):
                    users.append(item.lower())
    
                if len(newUser) < 17 and len(newUser) > 0 and newUser.lower() not in users and wrong == False:
                    old = os.getcwd()
                    os.chdir(ogdir)
                    os.rename(USER, newUser)
                    os.chdir(ogdir)
                    f = open("UWP.lock", "r")
                    contents = f.read().splitlines()
                    for item in contents:
                        if USER in item:
                            itemIdx = contents.index(item)
                            splitOne = item.split(",")
                            splitOne[0] = newUser
                            contents[itemIdx] = ",".join(splitOne)
                    f.close()
                    os.remove("UWP.lock")
                    f = open("UWP.lock", "w")
                    for item in contents:
                        if item.strip() != "":
                            f.write("\n" + item + "\n")
                            
                    f.close()
                    home_directory = ogdir + "/" + newUser
                    os.chdir(home_directory)
                    USER = newUser
                    username = newUser
                    changed = True
                else:
                    changed = False
                    print("Invalid username.")
                    if len(newUser)>=17:
                        print(f"{red}Username must have less than 17 characters.{reset}")
                    if len(newUser)<=0:
                        print(f"{red}Username must have at least one character.{reset}")
                    if newUser.lower() in users:
                        print(f"{red}Username already exists.{reset}")
    
                    if wrong == False:
                        print(f"{red}Username may only contain letters and underscores.{reset}")
                if changed == True:
                    print(f"{green}Username changed successfully.{reset}")
                print("------")
            
            except KeyboardInterrupt:
                print()
                print(colorama.Fore.RED + "Cancelling operation..." +reset)
                os.chdir(home_directory)
                old = os.getcwd()

        if request == "rmdir":
            old = os.getcwd()
            try:
                print("------")
                print("Which " + colorama.Fore.LIGHTMAGENTA_EX + "directory " +
                      colorama.Style.RESET_ALL + "would you like to delete?")
                print(
                    colorama.Fore.RED +
                    "Be careful when deleting directories that you don't own.\nMake sure you know what you're doing!"
                    + colorama.Style.RESET_ALL)
                getdirectory()
                print("------")
                listfolders()
                DIR = os.getcwd()
                amount = len([
                    name for name in os.listdir(DIR)
                    if os.path.isfile(os.path.join(DIR, name))
                ])
                if amount == 0:
                    print(colorama.Fore.LIGHTBLACK_EX +
                          "This folder is empty,\nPress Ctrl+C to cancel..." +
                          colorama.Style.RESET_ALL)
                valid = False
                while valid == False:
                    filename = input(colorama.Style.RESET_ALL + termdes + " ")
                    if os.path.isfile(filename):
                        print(colorama.Fore.RED + "\033[1mError: directory: '" +
                              filename + "' not found.")
                        valid = False
                    else:
                        valid = True
                try:
                    print("------")
                    print(colorama.Fore.RED +
                          "Are you sure you want to delete this directory?" +
                          colorama.Style.RESET_ALL)
                    print("Location name: '" + colorama.Fore.LIGHTMAGENTA_EX +
                          filename + colorama.Style.RESET_ALL + "'")
                    valid = False
                    while valid == False:
                        print("------")
                        print(colorama.Fore.LIGHTMAGENTA_EX +
                              "'y' - (yes)\nOR\n'n' - (no)" +
                              colorama.Style.RESET_ALL)
                        print("------")
                        choice = input(colorama.Style.RESET_ALL + termdes + " ")
                        choice = choice.strip()
                        if choice.lower() == "y" or choice.lower() == "n":
                            valid = True
                        else:
                            print(colorama.Fore.RED +
                                  "Invalid answer. Use (y/n) to respond." +
                                  colorama.Style.RESET_ALL)
                    if choice.lower() == "y":
                        if filename.strip(" ") not in systemdirs:
                            try:
                                shutil.rmtree(filename)
                                print(colorama.Fore.LIGHTGREEN_EX +
                                      "Directory successfully deleted: '" + filename + "'" +
                                      colorama.Style.RESET_ALL)
                            except:
                                print()
                                print(colorama.Fore.RED + "An error occurred" +
                                      colorama.Style.RESET_ALL)
                        else:
                            print(colorama.Fore.RED + "This directory is a system directory, and therefore cannot be removed." +
                                      colorama.Style.RESET_ALL)
                    print("------")
                except:
                    print()
                    print(colorama.Fore.RED + "An error occurred" +
                          colorama.Style.RESET_ALL)
            except KeyboardInterrupt:
                print()
                print(colorama.Fore.RED + "Cancelling operation..." +
                      colorama.Style.RESET_ALL)
    
        if request == "mkdir":
            old = os.getcwd()
            try:
                print("------")
                print(f"{green}What{reset} would you like to {blue}name{reset} the {red}directory{reset}?")
                print("------")
                valid = False
                while valid == False:
                    foldername = input(termdes + " ")
                    if foldername.strip(" ") not in systemdirs and foldername.strip(" ") not in os.listdir(os.getcwd()):
                        os.mkdir(foldername)
                        valid = True
                        break
                    else:
                        print(f"{red}This folder already exists.{reset}")
                        valid = False
                print(f"{green}Directory successfully created: '{foldername}'{reset}")
                print("------")
            except KeyboardInterrupt:
                print()
                print(colorama.Fore.RED + "Cancelling operation..." +reset)
                os.chdir(old)

    #####################################
