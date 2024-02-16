import os

def write_message():
    home_directory = os.getcwd()
    old = home_directory
    os.chdir(home_directory + "/Messages")
    f = open("welcome.txt", "w+")
    contents = """Hello Core user! The team at TriTech is proud to announce that we have begun working on another OS!

This shell aims to be understandable and simple to use, 
so that just about anyone can pick it up and learn it in a matter of seconds.

The commands will all be single word, and all be prompt-based after the return key is pressed.
It would be much appreciated if you reported any bugs in the comment section below.
Hope you enjoy using Core!"""
    f.write(contents)
    f.close()
    os.chdir(old)


def write_version():
    home_directory = os.getcwd()
    old = home_directory
    os.chdir(home_directory + "/System")
    f = open(".version", "w+")
    contents = """Core OS, Version 1.2.3, Beta Replit QoL Release, Unix-based"""
    f.write(contents)
    f.close()
    os.chdir(old)


def write_app1():
    home_directory = os.getcwd()
    old = home_directory
    os.chdir(home_directory + "/Games_and_apps")
    f = open("SAIntence_Deluxe.py", "w+")
    contents = str("""import os
import time
import random

att = []
overload = 0
truer = False

def size_exception():
	global nlines
	if int(os.path.getsize("attempts.txt")) < 2:
		fff = open("attempts.txt", "a")
		nlines = sum(1 for line in open('attempts.txt'))
		fff.write("\n")
		fff.close()


def check():
	global att, truer
	file = open("attempts.txt", "r")
	contents = file.read()
	if str(att) in str(contents):
		truer = True
	elif str(att) not in str(contents):
		truer = False

def setvar():
	global echelon, correct, i, f, fileread, contents
	echelon = 0
	correct = "null"
	i = 0
	f = open("attempts.txt", "a")
	fileread = open('attempts.txt','r')
	contents = fileread.read()


setvar()
while True:
	os.system("clear")
	mode = input("What mode should be run?\n(1) Learn\nOR\n(2) Test\n>>> ")
	print(mode)
	if mode.lower() == "1":
		print("You chose - learn")
	
		i = 0
		print("-----------------------------------")
		echelon = echelon + 1
		print("\u001b[32;1mEchelon", str(echelon))
		print("\u001b[0mSentence error network")
		print("attempts.txt size: " + str(os.path.getsize("attempts.txt")) + " byte(s).")
		print()
		
		sentence = input("\u001b[36;1mType a sentence for echelon " + str(echelon) + "\n>>> \u001b[0m")
		sent = sentence.lower()
		sentl = sent.split()
		att = sent.split()
		correct = "null"
	
	#def runner():
		while correct.lower() != "y":
			for word in att:
				word.lower()
			random.shuffle(att)
			random.shuffle(att)
			check()
			
			if truer == False:
				if str(att) != str(sentl):
					overload = 0
				
				if str(att) != str(sentl):
					print()
					print("---------")
					i = i + 1
					print("\u001b[4m\u001b[32;1mGuess " + str(i) + ":\u001b[0m ", end = "", flush = True)
					print(*att, sep = " ", end = "", flush = True)
					print()
				
				if str(att) != str(sentl):
					f = open("attempts.txt", "a")
					print("Incorrect guess...")
					pos = f.tell()
					f.write(str(att) + "\n")
					f.close()
				else:
					random.shuffle(att)
					truer = True
					overload = overload + 1
					if overload > 10000:
						print()
						print("Processing complete - file write complete.")
						n = input("Press enter >>> ")
						break
			else:
				overload = overload + 1
				if overload > 10000:
					print()
					print("Processing complete - file write complete.")
					n = input("Press enter >>> ")
					break
	
	elif mode.lower() == "2":
		print("You chose - Test")
		i = 0
		print("-----------------------------------")
		echelon = echelon + 1
		print("\u001b[32;1mEchelon", str(echelon))
		print("\u001b[0mSentence error network")
		print("attempts.txt size: " + str(os.path.getsize("attempts.txt")) + " byte(s).")
		print("----")
		print("NOTE: The AI will not learn in this mode.")
		print("----")
		
		sentence = input("\u001b[36;1mType a scrambled sentence for echelon " + str(echelon) + "\n>>> \u001b[0m")
		sent = sentence.lower()
		sentl = sent.split()
		att = sent.split()
		correct = "null"
		random.shuffle(att)
		random.shuffle(att)
		
		correct = "null"
		
		while correct.lower() != "y":
			random.shuffle(att)
			check()
			if correct.lower() != "y":
				if truer == False:
					overload = 0
					print()
					print("---------")
					i = i + 1
					print("\u001b[4m\u001b[32;1mGuess " + str(i) + ":\u001b[0m ", end = "", flush = True)
					print(*att, sep = " ", end = "", flush = True)
					print()
					correct = input("(y/n) >>> ")
				else:
					random.shuffle(att)
			else:
			
				print("")
				print("If you recieved any incorrect sentences, make sure that you have stored them in learn mode!")
				break
		n = input("Press enter >>> ")
		
		
		
		
				
				
				""")
    f.write(contents)
    f.close()
    os.chdir(old)


def write_tree():
    home_directory = os.getcwd()
    old = home_directory
    os.chdir(home_directory + "/System")
    f = open("tree.py", "w+")
    contents = """from pathlib import Path
import os

class DisplayablePath(object):
  display_filename_prefix_middle = '├──'
  display_filename_prefix_last = '└──'
  display_parent_prefix_middle = '	'
  display_parent_prefix_last = '│   '

  def __init__(self, path, parent_path, is_last):
	  self.path = Path(str(path))
	  self.parent = parent_path
	  self.is_last = is_last
	  if self.parent:
		  self.depth = self.parent.depth + 1
	  else:
		  self.depth = 0

  @property
  def displayname(self):
	  if self.path.is_dir():
		  return self.path.name + '/'
	  return self.path.name

  @classmethod
  def make_tree(cls, root, parent=None, is_last=False, criteria=None):
	  root = Path(str(root))
	  criteria = criteria or cls._default_criteria

	  displayable_root = cls(root, parent, is_last)
	  yield displayable_root

	  children = sorted(list(path
							 for path in root.iterdir()
							 if criteria(path)),
						key=lambda s: str(s).lower())
	  count = 1
	  for path in children:
		  is_last = count == len(children)
		  if path.is_dir():
			  yield from cls.make_tree(path,
									   parent=displayable_root,
									   is_last=is_last,
									   criteria=criteria)
		  else:
			  yield cls(path, displayable_root, is_last)
		  count += 1

  @classmethod
  def _default_criteria(cls, path):
	  return True

  @property
  def displayname(self):
	  if self.path.is_dir():
		  return self.path.name + '/'
	  return self.path.name

  def displayable(self):
	  if self.parent is None:
		  return self.displayname

	  _filename_prefix = (self.display_filename_prefix_last
						  if self.is_last
						  else self.display_filename_prefix_middle)

	  parts = ['{!s} {!s}'.format(_filename_prefix,
								  self.displayname)]

	  parent = self.parent
	  while parent and parent.parent is not None:
		  parts.append(self.display_parent_prefix_middle
					   if parent.is_last
					   else self.display_parent_prefix_last)
		  parent = parent.parent

	  return ''.join(reversed(parts))
Folder = os.getcwd()
paths = DisplayablePath.make_tree(Path(Folder))
for path in paths:
  print(path.displayable())"""
    f.write(contents)
    f.close()
    os.chdir(old)


def write_english():
    home_directory = os.getcwd()
    old = home_directory
    os.chdir(home_directory + "/Games_and_apps")
    f = open("English_words.py", "w+")
    contents = """import os
f = open("wiki-100k.txt", "r")
context = f.readlines()
change = -1
for line in context:
	change = change + 1
	if "#" in line:
		context.pop(change)

contexta = context
new = []
for item in contexta:
	iteml = item.lower()
	new.append(iteml)

f = open("new-list.txt", "w")

for item in new:
	f.write(item)

sentence = []

f.close()
f = open("new-list.txt","r")

words = f.read().splitlines()

import random

for x in range (0, 20):
	sentence.append(words[random.randint(0, len(words)-1)])

for item in sentence:
	if sentence.index(item) == 0:
		None
	
	print(f"- {item}",  f"{words.index(item)}", end = "\n")

print("--------")

while True:
	print("Please type a word: ", end = "")
	word = input("")
	index = -1
	indexfalse = 0
	for item in words:
		index = index+1
		if word.lower() == item:
			break
		else:
			None
			indexfalse = index + 1
			
	if indexfalse != len(words):
		print(f"{word} - {index + 1}")
		print("--------")
	else:
		print("Error: Word not in list...")
		print("--------")
"""
    f.write(contents)
    f.close()
    os.chdir(old)
