from phrasehunter.phrase import Phrase

import random

class Game:
    
    phrases = [
        ("Will Smith slaps Chris Rock"),
        ("Chinese Food"),
        ("Fried Chicken"),
        ("Popeyes Biscuit"),
        ("Fried Noodle"),
    ]
    
    def __init__(self):
        self.phrases = Game.phrases
        self.win = None
        self.lives = 10
        self.missed = 0
        self.active_phrase = None
        self.guesses = []
        
    def start(self):
        self.active_phrase = self.get_random_phrase() 
        self.welcome()
    
    def get_random_phrase(self):
        chosen_phrase = random.choice(self.phrases) 
        return chosen_phrase

    def welcome(self): 
        ready = 0
        while ready == 0:
            ready = input("Welcome to PhraseHunters, Want to play (y/n)> ")
            if ready == "y":
                self.get_guess()
            if ready == "n":
                print("Goodbye")
                exit() 
            else:
                print("Please choose a valid option")

    def get_guess(self): 
        guessing = True
        while guessing == True:
            phrase = Phrase(self.active_phrase)
            self.display_phrase = phrase.display(self.guesses)
            check = phrase.check_complete(self.lives, self.display_phrase, self.active_phrase) 
            if check == "You won":
                self.game_over(check) 
            if check == "You lose":
                self.game_over(check) 
            if check == "incomplete":
                print("")
            current_guess = input("Guess a letter: ").lower()            
            if current_guess not in self.active_phrase: 
                self.lives -= 1
                self.missed += 1
            print("You have {} out of 10 lives remaining".format(self.lives)) 
            if len(current_guess) > 1:
                print("Guess one letter at a time") 
            else:
                self.guesses.append(current_guess)
                
    def game_over(self, status): 
        if status == "You lose":
            print("You lose")
            exit()
        if status == "You won":
            print("You won")
            exit()
            
