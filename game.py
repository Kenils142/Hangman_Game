from random import choice

#Function for selecting random word
def selector():
    words = ['cat', 'dog', 'bear', 'elephant', 'eagle', 'owl', 'parrot', 'penguin', 'snake', 'lizard', 'crocodile', 'turtle', 'frog', 'toad', 'salamander', 'newt', 'shark', 'dolphin', 'salmon', 'goldfish', 'ant', 'bee', 'butterfly', 'spider', 'koala', 'kiwi', 'ostrich', 'anaconda', 'komodo dragon', 'chameleon', 'gecko', 'axolotl', 'uakari', 'caecilian', 'anglerfish', 'lungfish', 'seahorse']
    
    return choice(words)

def display(word, guessed, score, life):
    #displaying what letters in words left to be guessed
    for i in word:
        if i in guessed :
            print(i, end="")
        else:
            print("_", end="")
    print(f'   score:{score} lives:{life}')

def game():
    word = selector()
    guessed = set()
    guessed.add(" ")
    score = 0
    life = 10
    isGameOver = False

    while not isGameOver:

        display(word, guessed, score, life)

        inp = set(input("Enter Letter of word:"))

        #check for all unique characters entered dy user
        for i in inp:

            #If letter is already guessed ignore checking again
            if i not in guessed:

                #checking if guessed letter is in word
                if i in word:
                    guessed.add(i)
                    score += 10

                    #If word gussed, create new word to guess
                    if set(word) <= guessed:
                        print("Sucess")
                        score += 100
                        display(word, guessed, score, life)
                        word = selector()
                        guessed = set()
                        del inp

                #If guess was incorrect
                else:
                    score -= 20
                    life -= 1

                    #if out of lives
                    if life == 0:
                        print(f'Game Over, Your score is {score}')
                        isGameOver = True
                        break                       

if __name__ == "__main__":
    game()