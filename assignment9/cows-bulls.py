import random
 
 class CowsAndBullsGame:
     def __init__(self):
         self.secret_number = self.generate_secret_number()
         self.guesses = 0
 
     def generate_secret_number(self):
         digits = random.sample(range(10), 4) 
         return ''.join(map(str, digits))
 
     def get_cows_and_bulls(self, guess):
         cows = bulls = 0
         for i in range(4):
             if guess[i] == self.secret_number[i]:
                 cows += 1
             elif guess[i] in self.secret_number:
                 bulls += 1
         return cows, bulls
 
     def play(self):
         print("Welcome to Cows and Bulls Game!")
         print("I have generated a 4-digit number with no repeating digits.")
         print("Try to guess the number. After each guess, I will tell you how many Cows and Bulls you have.")
         
         while True:
             guess = input("Enter your 4-digit guess (no repeating digits): ")
 
             if len(guess) != 4 or not guess.isdigit() or len(set(guess)) != 4:
                 print("Invalid input. Please enter a 4-digit number with no repeating digits.")
                 continue
             
             self.guesses += 1
             cows, bulls = self.get_cows_and_bulls(guess)
 
             if cows == 4:
                 print(f"Congratulations! You've guessed the correct number {self.secret_number} in {self.guesses} guesses.")
                 break
             else:
                 print(f"{cows} Cow(s), {bulls} Bull(s)")
 
 game = CowsAndBullsGame()
 game.play()