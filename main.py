import random

#Global variables to avoid errors
global num_wrong_guesses
global secret_word
global previous_guesses
global correct_guesses
global you_win
previous_guesses = [] #List of previous guesses
correct_guesses = [] #List of correct guesses
word_bank = ["ALONG","UNTIL","GRANT","SPEAK","ENJOY", "BELLS", "ELVES", "MERRY", "GRACE", "FEAST", "AROMA", "MUSIC", "SHARE", "PEACE", "JOLLY", "SANTA", "SERVE", "UNITY"] #Word list for game, must be ALL CAPS
num_wrong_guesses = 0 #Number of wrong guesses

the_guess = "" #The guess inputted by the player
you_win = 0 #Did you win? 1 if yes, 0 if no or not yet

#List with all the snowman print outs. Keeps the code readable.
snowman_list = [
'''
     __
   _|==|_  
    ('')___/
>--(`^^')
  (`^'^'`)
  `======' 
''',
'''
     __  
    ('')___/
>--(`^^')
  (`^'^'`)
  `======' 
''',
'''
     __  
    ('')
>--(`^^')
  (`^'^'`)
  `======' 
''',
'''
     __  
    ('')
   (`^^')
  (`^'^'`)
  `======' 
''',
'''
     __  
    ('')
   (`^^')
   `====' 
''',
'''
     __  
    ('')
    `=='
''',
r'''
Your snowman melted!
''']


def guess(category): #Takes care of user input for guessing.
    if category == 1: #First guess
        print("\nWhat is your first guess?")
        user_guess = input()
        if len(user_guess) == 1 and user_guess.isalpha() == True: #Check for bad input
            if user_guess.upper() in previous_guesses:
                user_guess = guess(3)
                previous_guesses.append(user_guess.upper()) #add the guess to the previous guess list
                return(user_guess)

            previous_guesses.append(user_guess.upper()) #add the guess to the previous guess list
            return(user_guess)
            
        else:
            user_guess = guess(2)
            previous_guesses.append(user_guess.upper()) #add the guess to the previous guess list
            return(user_guess) 
    
    if category == 2: #Input not valid
        print("Your input wasn't valid. Please use characters only. \nWhat is your next guess?")
        user_guess = input()
        if len(user_guess) == 1 and user_guess.isalpha() == True: #Check for bad input
            if user_guess.upper() in previous_guesses:
                user_guess = guess(3)
                previous_guesses.append(user_guess.upper()) #add the guess to the previous guess list
                return(user_guess)
                
          
            previous_guesses.append(user_guess.upper()) #add the guess to the previous guess list
            return(user_guess)
        else:
            user_guess = guess(2)
            previous_guesses.append(user_guess.upper()) #add the guess to the previous guess list
            return(user_guess)  

    if category == 3: #Input already guessed
        print("You already guessed that letter!\nWhat is your next guess?")
        user_guess = input()
        if len(user_guess) == 1 and user_guess.isalpha() == True: #Check for bad input
            if user_guess.upper() in previous_guesses:
                user_guess = guess(3)
                previous_guesses.append(user_guess.upper()) #add the guess to the previous guess list
                return(user_guess)
        
            previous_guesses.append(user_guess.upper()) #add the guess to the previous guess list
            return(user_guess)
        else:
            user_guess = guess(2)
            previous_guesses.append(user_guess.upper()) #add the guess to the previous guess list
            return(user_guess)  
            
    else: #Normal guess after first guess
        print("What is your next guess?")
        user_guess = input()
        if len(user_guess) == 1 and user_guess.isalpha() == True: #Check for bad input
            if user_guess.upper() in previous_guesses:
                user_guess = guess(3)
                previous_guesses.append(user_guess.upper()) #add the guess to the previous guess list
                return(user_guess)
    
            previous_guesses.append(user_guess.upper()) #add the guess to the previous guess list
            return(user_guess)
        else:
            user_guess = guess(2)
            previous_guesses.append(user_guess.upper()) #add the guess to the previous guess list
            return(user_guess) 

def choose_word(): #Choose the secret word
    return(random.choice(word_bank))

def snowman_print(guesses): #Print our poor friend :(
    print(snowman_list[guesses])

def check_guess(letter): #Check if letter is in secret_word
    global num_wrong_guesses
    if letter.upper() in secret_word:
        print("Nice job! Your guess is correct.")
        return(reveal_word())
    else:
        print("Whoops, you didn't guess correctly.")
        num_wrong_guesses += 1
        snowman_print(num_wrong_guesses)
        reveal_word()

def repeat_game(): #Handles repeating the game
    play_again = input("Would you like to play again? (Y/N) ")
    if play_again == "Y":
        return(1)
    elif play_again == "N":
        print("Thanks for playing! Exiting now.")
        exit(0)
    else:
        print("Sorry, your input is invalid. Try again.")
        repeat_game()
    
def reveal_word(): #Reveal the correct letters in the word
    global you_win
    word_reveal = ""
    for character in secret_word:
        if character in previous_guesses:
            word_reveal += character + " "
        else:
            word_reveal += "__ "
    print(word_reveal + "\n")

    #remove the spaces in between the letters, if it matches with the secret word, then the player won
    if word_reveal.replace(" ", "") == secret_word: 
        you_win = 1
        
        
def play_snowman(): #Main game, ties all of the previous functions together.
    global you_win
    print("Welcome to Snowdle!")
    print("Snowman ASCII art from asciiart.eu/holiday-and-events/christmas/snowmen by artist \"ldb.\"")
    the_guess = guess(1)
    check_guess(the_guess)
    while num_wrong_guesses < 6: #There are 7 levels of snowman printouts, 0 is where we start counting
        the_guess = guess(10)
        check_guess(the_guess)
        
        if you_win == 1:
            print("WOW! You guessed the word correctly!")
            return ""
    print("Well...looks like you couldn't guess the right word.")
    print("The correct word was..." + secret_word)
 
while True: #Main game loop, runs forever until the player quits.
    #choose the secret word
    secret_word = choose_word()
    
    #reset a bunch of variables if the player wants to play the game again
    num_wrong_guesses = 0
    previous_guesses = []
    correct_guesses = []
    you_win = 0
    
    #start the game
    play_snowman()
    
    #does the player want to play again?
    repeat_game()    