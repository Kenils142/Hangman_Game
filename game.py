from random import choice
from pynput import keyboard

key_pressed = None

#Function for selecting random word
def selector():
    words = ['cat', 'dog', 'bear', 'elephant', 'eagle', 'owl', 'parrot', 'penguin', 'snake', 'lizard', 'crocodile', 'turtle', 'frog', 'toad', 'salamander', 'newt', 'shark', 'dolphin', 'salmon', 'goldfish', 'ant', 'bee', 'butterfly', 'spider', 'koala', 'kiwi', 'ostrich', 'anaconda', 'komodo dragon', 'chameleon', 'gecko', 'axolotl', 'uakari', 'caecilian', 'anglerfish', 'lungfish', 'seahorse']
    
    return choice(words)

#Event Handler for key presses
def on_key_press(key):
    if hasattr(key, 'char'):
        if key.char.isalpha():
            global key_pressed
            key_pressed = key.char
            return False

def game():
    word = selector()
    guessed = set()
    guessed.add(" ")
    score = 0
    life = 10

    while(True):
        #For testing purposes / comment out when gui developed 
        for i in word:
            if i in guessed :
                print(i, end="")
            else:
                print("_", end="")
        print(f'   score:{score} lives:{life}')

        with keyboard.Listener(on_press=on_key_press) as Listener:
            Listener.join()
    
        #If letter is already guessed ignore checking again
        if key_pressed not in guessed:
            #checking if gussed letter is in word
            if key_pressed in word:
                guessed.add(key_pressed)
                score += 10

                #If word gussed, create new word to guess
                if set(word) <= guessed:
                    print("Sucess")
                    score += 100
                    for i in word:
                        if i in guessed :
                            print(i, end="")
                        else:
                            print("_", end="")
                    print(f'   score:{score} lives:{life}')
                    word = selector()
                    guessed = set()

            #If guess was incorrect
            else:
                score -= 20
                life -= 1

                #if out of lives
                if life == 0:
                    print(f'Game Over, Your score is {score}')
                    break

if __name__ == "__main__":
    game()