import random
from typing_extensions import Literal

class GuessingGame:
    '''
    A class used to represent a Guessing Game

    ...

    Attributes
    ----------
    min : int
        the minimum value that the number can be
    max : int
        the maximum value that the number can be

    Methods
    -------
    play()
        Plays the game. The game involves requesting the user guess the
        number until they correctly guess or quit. If they finish a
        round it will ask if they want to play again. Keeps track of the
        player's score for the game and highscore across games.
    '''
    
    def __init__(self, min: int = 1, max: int = 100) -> None:
        self.min = min
        self.max = max

    def play(self) -> None:
        print('Enter Q at any time to quit.')
        first_round = True
        highscore = None
        while True:
            play = self._options(first_round)
            if not play:
                print('Thank you for playing!')
                break
            result = self._guess(highscore)
            if result == 'quit':
                print('Thank you for playing!')
                break
            highscore = result
            first_round = False

    def _guess(self, highscore: int | None) -> int | Literal['quit']:
        print(f'Generating a number from {self.min} to {self.max}...')
        number = random.randint(self.min, self.max)
        score = 1
        while True:
            guess = input('What is the number? ')
            if guess.lower() == 'q':
                return 'quit'
            try:   
                guess = int(guess)
            except ValueError:
                print('Please enter an integer.')
                continue
            if guess < number:
                print('You guessed too low.')
                score += 1
            elif guess > number:
                print('You guessed too high.')
                score += 1
            else:
                print('You did it! You Win!')
                print(f'You guessed in {score} attempts.')
                highscore = self._update_highscore(score, highscore)
                return highscore

    def _update_highscore(self, score: int, highscore: int | None):
        if highscore is None or highscore > score:
            print('You got a new highscore!')
            return score
        return highscore

    def _options(self, first_round: bool) -> bool:
        while True:
            confirm = ['yes', 'y']
            deny = ['no', 'n', 'q']
            if first_round:
                again = ''
            else:
                again = 'again '
            user_input = input(f'Would you like to play {again}({confirm[0]}/{deny[0]})? ')
            decision = user_input.lower()
            if decision in confirm:
                return True
            if decision in deny:
                return False
            print(f'Please enter {confirm[0]}/{deny[0]}.')

if __name__ == "__main__":
    game = GuessingGame()
    game.play()