#!/usr/bin/env python

import random

def main():
    """ Learning Alphabet with Game !."""
    print("Guess that fruit!")

    print("\nEASY: You will be given an alphabet and you have to guess the fruit that start with that alphabet ")

    print( "\nPlease Start writing your answer with a CAPITAL letter" )

    fruit = [
        "cranberry",
        "cherry",
        "coconut",
        "Coconut",
        "Cranberry",
        "Coconut"
       ]

    x = random.choice(fruit)
    
    guess = None

    while x != guess:

        guess = str(input("\nState a fruit that start with alphabet C ? "))
        
        if x == guess:
            print("\nYou guessed {}. Cheers !! Correct!\U0001F601".format(guess))
            break
        else:
            print("\nYou guessed {}. Oh No!. Try Again!\U0001F605".format(guess))


    fruit = [
        "Apple",
        "Avocado",
        "Apricot",
        ]

    x = random.choice(fruit)
    
    guess = None

    while x != guess:

        guess = str(input("State a fruit that start with alphabet A ? "))
        
        if x == guess:
            print("\nYou guessed {}. Hurray! Correct!\U0001F602".format(guess))
            break
        else:
            print("\nYou guessed {}. Haiyaa~!. Try Again!\U0001F600".format(guess))

    fruit = [
        "Banana",
        "Blueberry",
        "Blackcurrent",
        ]

    x = random.choice(fruit)
    
    guess = None

    while x != guess:

        guess = str(input("State a fruit that start with alphabet B ? "))
        
        if x == guess:
            print("\nYou guessed {}. Hurray! Correct!\U0001F607".format(guess))
            break
        else:
            print("\nYou guessed {}. We Can Do This! Another One \U0001F923".format(guess))

    fruit = [
        "Dragonfruit",
        "Durian",
        "Date"]

    x = random.choice(fruit)
    
    guess = None

    while x != guess:

        guess = str(input("State a fruit that start with alphabet D ? "))
        
        if x == guess:
            print("\nYou guessed {}. Hurray! Correct!\U0001F60D".format(guess))
            break
        else:
            print("\nYou guessed {}. Never Give Up!. Try Again!".format(guess))

    fruit = [
        "Mango",
        "Mangosteen",
        "Melon"
        ]

    x = random.choice(fruit)
    
    guess = None

    while x != guess:

        guess = str(input("State a fruit that start with alphabet M ? "))
        
        if x == guess:
            print("\nYou guessed {}. Hurray! Correct! \U0001F601".format(guess))
            break
        else:
            print("\nYou guessed {}. Come On! !\U0001F612".format(guess))
    
    print("\nNEXT LEVEL ! \U0001F601")

    fruit = [
        "Grape",
        "Blackcurrent",
        "Dragonfruit"
        ]

    x = random.choice(fruit)
    
    guess = None

    while x != guess:

        guess = str(input("MEDIUM: Guess a fruit that colored purple? \0001F619"))
        
        if x == guess:
            print("\nYou guessed {}. Hurray! Correct! \U0001F601".format(guess))
            break
        else:
            print("\nYou guessed {}. Come On! !\U0001F612".format(guess))

    fruit = [ 
        "Banana", 
        "Lemon", 
        "Pineapple" 
        ] 
 
    x = random.choice(fruit) 
     
    guess = None 
 
    while x != guess: 
 
        guess = str(input("MEDIUM: Guess a fruit that colored yellow? \0001F619")) 
         
        if x == guess: 
            print("\nYou guessed {}. Hurray! Correct! \U0001F601".format(guess)) 
            break 
        else: 
            print("\nYou guessed {}. Come On! !\U0001F612".format(guess)) 

    fruit = [ 
        "Strawberry", 
        "Watermelon", 
        "Cherry" 
        ] 
 
    x = random.choice(fruit) 
     
    guess = None 
 
    while x != guess: 
 
        guess = str(input("MEDIUM: Guess a fruit that colored red? \0001F619")) 
         
        if x == guess: 
            print("\nYou guessed {}. Hurray! Correct! \U0001F601".format(guess)) 
            break 
        else: 
            print("\nYou guessed {}. Come On! !\U0001F612".format(guess)) 

    fruit = [ 
        "Grape", 
        "Avocado", 
        "Guava" 
        ] 
 
    x = random.choice(fruit) 
     
    guess = None 
 
    while x != guess: 
 
        guess = str(input("MEDIUM: Guess a fruit that colored green? \0001F619")) 
         
        if x == guess: 
            print("\nYou guessed {}. Hurray! Correct! \U0001F601".format(guess)) 
            break 
        else: 
            print("\nYou guessed {}. Come On! !\U0001F612".format(guess)) 

    fruit = [ 
        "Papaya", 
        "Apricot", 
        "Mango" 
        ] 
 
    x = random.choice(fruit) 
     
    guess = None 
 
    while x != guess: 
 
        guess = str(input("MEDIUM: Guess a fruit that colored orange? \0001F619")) 
         
        if x == guess: 
            print("\nYou guessed {}. Hurray! Correct! \U0001F601".format(guess)) 
            break 
        else: 
            print("\nYou guessed {}. Come On! !\U0001F612".format(guess))

    print("\n Next level ! \U0001F601")

    fruit = [
                "Contain pottasium",]

    x = random.choice(fruit)
    print("LET'S MOVE TO THE HARD PART")
    answer=input('\nAre you ready to play the Quiz ? (yes/no) : ')
    print("\nChoose the correct answer below")
    print("\nANSWERS OPTIONS: Contain Pottasium, Contain Zinc, Good For Digestion")
    print("\nPlease write the answer exactly like the answers options")

    guess = None

    while x != guess:

                    guess = str(input("HARD: State the benefit for eating banana? \0001F619"))

                    if x == guess:
                        print("\nYou guessed {}. Hurray! Correct! \U0001F601".format(guess))
                        break
                    else:
                        print("\nYou guessed {}. Come On! !\U0001F612".format(guess))

    fruit = [
            "Brigthens the skin",]

    x = random.choice(fruit)
    print("Choose the correct answer below")
    print("\nANSWERS OPTIONS: Brigthens the skin, Prevents insomnia, Creating haemoglobin")
    print("\nPlease write the answer exactly like the answers options")

    guess = None

    while x != guess:

                    guess = str(input("HARD: State the benefit for eating apple? \0001F619"))

                    if x == guess:
                        print("\nYou guessed {}. Hurray! Correct! \U0001F601".format(guess))
                        break
                    else:
                        print("\nYou guessed {}. Come On! !\U0001F612".format(guess))

    fruit = [
            "Protects heart",]

    x = random.choice(fruit)
    print("Choose the correct answer below")
    print("\nANSWERS OPTIONS: Prevents arthritis, Protects heart, Remove toxins")
    print("\nPlease write the answer exactly like the answers options")

    guess = None

    while x != guess:

                    guess = str(input("HARD: State the benefit for eating dragonfruit? \0001F619"))

                    if x == guess:
                        print("\nYou guessed {}. Hurray! Correct! \U0001F601".format(guess))
                        break
                    else:
                        print("\nYou guessed {}. Come On! !\U0001F612".format(guess))
            
    fruit = [
            "Boosts immunity",]

    x = random.choice(fruit)
    print("Choose the correct answer below")
    print("\nANSWERS OPTIONS: Improve vision, Prevent scurvy, Boosts immunity")
    print("\nPlease write the answer exactly like the answers options")

    guess = None

    while x != guess:

                    guess = str(input("HARD: State the benefit for eating dragonfruit? \0001F619"))

                    if x == guess:
                        print("\nYou guessed {}. Hurray! Correct! \U0001F601".format(guess))
                        break
                    else:
                        print("\nYou guessed {}. Come On! !\U0001F612".format(guess))
                        print("\nCONGRATULATION ! YOU DID IT \U0001F601 !")
main()


    


        


       

