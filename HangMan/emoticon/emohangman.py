#! /usr/local/bin/python3
import os 
import time

## list to be used
SecureWord=[]


## Ready Player 1 
word= input ("Player 1: Please enter the word!").lower()
SecureWord=list(word)
SecureList=["_"]*len(word)
os.system('clear')

#Helps provide transition time between players 
print ("You can now pass keyboard to player 2.")
for i in range(3,0,-1):
    time.sleep(1)
    print (i)
os.system('clear')

##Ready Player 2 
print (""" Welcome to Hangman!  
             +---+
             |
             |
             |
             |
             ======= 
             
              """)
print("The word has " + str(len(word)) + " letters.")
print ("_"*len(word))


### Decouple this section for guess function/class 
## Handles player 2 guesses 
turn =0
while turn < 6:
    guess = input ("Player 2: You can now guess the word or guess a Letter. \n What is your guess?").lower()
    if guess == word:
     print ("YAYA! You win!")
     exit()
    elif guess in SecureWord:
            for (location, character) in enumerate(SecureWord):
                if character==guess:
                    print (guess +" is located in position: " + str(location))
                    SecureList[location]=guess 
            print (str(SecureList))
            if SecureList == SecureWord:
                print ("YAYA! You Win! The word was " +str(word) +".")
                exit()
    else:
        print (guess + " is not in the word!")
        turn+=1
        if turn==1:
            from emoboard import head
            head()
        elif turn ==2:
            from emoboard import body
            body()
        elif turn ==3:
            from emoboard import rarm
            rarm() 
        elif turn ==4: 
            from emoboard import larm
            larm()
        elif turn ==5: 
            from emoboard import lleg
            lleg()
        elif turn ==6:
            from emoboard import rleg
            rleg()
            
 