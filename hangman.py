import random
 
 def read_words_from_file(file_path):
     with open(file_path, 'r') as file:
         words = [line.strip() for line in file.readlines()]
     return words
 
 def choose_word(word_list):
     return random.choice(word_list)
 
 def play_hangman(word):
     print("\nWelcome to Hangman!")
     guessed_letters = []
     wrong_guesses = 0
     max_guesses = 6
     word_display = ['_'] * len(word)
 
 
     while wrong_guesses < max_guesses:
         print(" ".join(word_display))
         guess = input("Guess your letter: ").upper()
 
         if len(guess) != 1 or not guess.isalpha():
             print("Please enter a valid letter.")
             continue
 
         if guess in guessed_letters:
             print(f"You already guessed the letter {guess}. Try again.")
             continue
 
         guessed_letters.append(guess)
 
         if guess in word:
             print(f"Good job! The letter {guess} is in the word.")
             for i in range(len(word)):
                 if word[i] == guess:
                     word_display[i] = guess
         else:
             wrong_guesses += 1
             print(f"Incorrect! You have {max_guesses - wrong_guesses} guesses left.")
 
         if '_' not in word_display:
             print(" ".join(word_display))
             print("Congratulations! You've guessed the word correctly.")
             return True
 
     print("Game Over! The correct word was:", word)
     return False
 
 def main():
     word_list = read_words_from_file('words.txt')  
     while True:
         word = choose_word(word_list).upper()
         play_hangman(word)
 
         play_again = input("Do you want to play again? (y/n): ").lower()
         if play_again != 'y':
             print("Thank you for playing Hangman!")
             break
 
 if __name__ == "__main__":
     main()