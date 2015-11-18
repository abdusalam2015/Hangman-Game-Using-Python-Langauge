#authot : Abdussalam 
#Email : abdussalm93@stud.fci-cu.edu.eg

import string
import copy
import random
remainingChance=0
missedLitters=[]
storeWords =[]
word = [];newWord=[];copyword=[]
def printList(list1):
	if(len(list1)):
		for x in range  (0,len(list1)) : 
			print list1[x],
	else :return None
	return ""
def isGood ():
	print "Chances Remaining    :  ",remainingChance
	print "Missed Letters/Digits  :  ",printList(missedLitters)
	printList( newWord)

def initialNewWord():
	for x in word :
		newWord.append('_'+"") 
 	printList(newWord)
 
def loadAllWords(fileName):
	with open("HangMan.txt","r") as f:
		for line in f:
    			storeWords.append(line.rstrip('\n'))

def getRandomWord():
	return random.choice(storeWords)
 

def gameDescription():
	print "welcome in Hangman Game \nGame Rules :\n1- Every just one character by one character \n2- You have only 6 chances to lose \n3- You have to fill all dashes to Win\n   -- Go -- "


loadAllWords("HangMan.txt");
gameDescription()
while True:
	word = list(getRandomWord())
	initialNewWord()
	copyword = list(word)  
	while True:
		char =  raw_input("\nyour guess (letters only) : ")
		isAlpha = char.isalpha()
		if   isAlpha:
			if char  in word:
				isFound = 1
			else: isFound = -1
			if char in newWord and isFound ==-1:
				print "You have already tried this letter or digit . Guess again!"
			elif isFound != -1 :
				while char  in word:
					index = word.index(char)
					word[index]=''
					newWord[index]=char
				isGood()
			else :
				print "This Character is not present in the name."
				missedLitters.append(char)
				remainingChance +=1
				isGood()
			if remainingChance == 6:
				if newWord != copyword : 
					print "\n		GAME OVER \n		Result : Lose\n		Correct Word is : ",printList(copyword);
					choice =  input("\n1- play again\n2- Quit\n")
					break
			elif newWord == copyword :
				print "\n		Win \n		Result : Win\n		Correct Word : ",printList(copyword);
				choice =  input("\n1- play again\n2- Quit\n")
				break		
		else : 
			print "Not a valid character. please enter a letter ."
	if choice != 1 : break
 	missedLitters[:]=[] 
	newWord[:]=[]
	word[:]=[]
	copyword[:]=[]
	remainingChance=0
