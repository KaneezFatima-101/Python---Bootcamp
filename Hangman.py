from words import words_list
import random


def important():
    word = getrandom()
    play(word)

    while input("Do you want to play again (Y/N): ").upper() == 'Y':
        word = getrandom()
        play(word)


def getrandom():
    word = random.choice(words_list)    # pick a single word from words_list
    return word.upper()


def play(word):
    word_completion = '_' * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6

    print("Let's play Hangman!!!")
    print(displayhangman(tries))
    print(word_completion)
    print()

    while not guessed and tries > 0:
        guess = input("Enter your guess: ").upper()
        if len(guess) == 1 and guess.isalpha():  # checks if it is a alphabet
            if guess in guessed_letters:
                print("You have already guessed the letter ", guess)
            elif guess not in word:
                print(guess, " is not in word")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good Job, ", guess, "is in the word.")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                # convert TEST (word) to ['T','E','S','T'] in order to exchange it with _

                indices = [i for i, letter in enumerate(word) if letter == guess]
                # meaning
                # for i, letter in enumerate(word)
                #     if letter == guess:
                #        indices.append(i)
                # Enumerate use to give index along with the value at the index
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True

            print(word_completion)

        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word

        else:
            print("Not a valid guess.")

        print(displayhangman(tries))
        print(word_completion)
        print()
    if guessed:
        print("Congrats, you guessed the word! You win!!")
    elif tries ==0:
        print("Sorry, you ran out of tries. The word was "+word + ". Better luck next time.")


def displayhangman(tries):

    stages = [  # 6 final state: head, torso, both arms and both legs
        """ 
              --------
              |    |
              |    O
              |   \\|/
              |    |
              |   / \\
        """,
        # 5 head, torso, both arms, one leg
        """   
              --------
              |    |
              |    O
              |   \\|/
              |    |
              |   / 
        """,
        # 4 head, torso, two arms
        """   
              --------
              |    |
              |    O
              |   \\|/
              |    |
              |   
        """,
        # 3 head, torso, one arm
        """   
              --------
              |    |
              |    O
              |   \\|
              |    |
              |   
        """,
        # 2 head and torso
        """   
              --------
              |    |
              |    O
              |    |
              |    |
              |  
        """,
        # 1 head
        """   
              --------
              |    |
              |    O
              |    
              |    
              |  
        """,
        # initial state
        """   
              --------
              |    |
              |    
              |    
              |    
              |  
        """
    ]
    return stages[tries]


if __name__ == "__main__":
    important()
