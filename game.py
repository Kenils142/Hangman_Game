from random import choice

class Game:
    words = ['cat', 'dog', 'bear', 'elephant', 'eagle', 'owl', 'parrot', 'penguin', 'snake', 'lizard', 'crocodile', 'turtle', 'frog', 'toad', 'salamander', 'newt', 'shark', 'dolphin', 'salmon', 'goldfish', 'ant', 'bee', 'butterfly', 'spider', 'koala', 'kiwi', 'ostrich', 'anaconda', 'komodo dragon', 'chameleon', 'gecko', 'axolotls', 'uakaris', 'caecilian', 'anglerfish', 'seahorse', 'lungfish', 'seahorse']
    word = user_guessed = []
    lives = 10
    score = 0
    isGameOver = False

    def __init__(self):
        self.setNew()
        self.game()

    def setNew(self):
        self.word = list(choice(self.words))
        self.user_guessed = []

        for c in self.word:
            if c != " ":
                self.user_guessed.append("_")
            else:
                self.user_guessed.append(" ")
        
        for i in range(len(self.user_guessed)):
            print(self.user_guessed[i], end="")

        print()
            

    def game(self):
        while not self.isGameOver:
            guess = input()
            if guess in self.word:
                for i in range(len(self.word)):
                    if(self.word[i] == guess and self.word[i] != self.user_guessed[i]):
                        self.user_guessed[i] = guess
                        self.score += 10
                
                for i in range(len(self.user_guessed)):
                    print(self.user_guessed[i], end="")
            
                print()

            else: 
                self.score -= 20
                self.lives -= 1
            
            if self.word == self.user_guessed:
                self.score += 100
                self.setNew()

            if(self.lives == 0):
                self.isGameOver = True
                print(self.score)
                

if __name__ == "__main__":
    game_instance = Game()
