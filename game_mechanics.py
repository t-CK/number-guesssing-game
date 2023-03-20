from random import randint
import time
from enum import Enum
from pygame import QUIT
from pygame import event

class Game_State(Enum):
    GAME_OVER = 0
    TOO_HIGH = 1
    TOO_LOW = 2

class Game_Mechanics:
    _secret_number  :int

    def __init__(self):
        self._secret_number = randint(0, 1000)
    
    def validate_guess(self, guess :int) -> Game_State:
        if guess == self._secret_number:
            return Game_State(0)
        elif guess < self._secret_number:
            return Game_State(2)
        elif guess > self._secret_number:
            return Game_State(1)
        

    
##################### AI LOGIC ##########################

class AI:
    
    # Store max and low guesses into class variables to decrease the bunds of guess
    _max_guess :int
    _min_guess :int
    _prev_guess :int

    # Initialize values for max_guess and min_guess
    def __init__(self) -> None:
        self._max_guess = 1001
        self._min_guess = -1

    # set the values of minGuess and maxGuess
    def Set_Bounds(self, was_high :bool) -> None:
        if was_high:
            self._max_guess = self._prev_guess
        else:
            self._min_guess = self._prev_guess

    def Make_Guess(self) -> int:
        # Get random number as ai input
        guess = randint(self._min_guess +1, self._max_guess -1)

        # Get new random number while the guess is out of bounds
        while guess <= self._min_guess and guess >= self._max_guess:
            guess = randint((self._min_guess +1), (self._max_guess -1))
        self._prev_guess = guess
        time.sleep(0.5)
        return guess

########################################################