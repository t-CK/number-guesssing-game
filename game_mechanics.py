from random import randint
import time
from enum import Enum
from pygame import QUIT
from pygame import event

class Game_State(Enum):
    NONE      = 0
    TOO_HIGH  = 1
    TOO_LOW   = 2
    GAME_OVER = 3

class Game_Mechanics:
    _secret_number  :int

    def __init__(self):
        self._secret_number = randint(0, 1000)
    
    def Validate_Guess(self, guess :int) -> Game_State:
        if guess == self._secret_number:
            return Game_State.GAME_OVER
        elif guess < self._secret_number:
            return Game_State.TOO_LOW
        elif guess > self._secret_number:
            return Game_State.TOO_HIGH
        

    
##################### AI LOGIC ##########################

class AI:
    
    # Store highest and lowest guesses into class variables to decrease the bunds of guess
    _max_guess :int
    _min_guess :int
    _prev_guess :int

    # Initialize values for _max_guess and _min_guess
    # Values are one off bounds because number may be 1000 of 0
    def __init__(self) -> None:
        self._max_guess = 1001
        self._min_guess = -1

    # update the values of _min_guess and _max_guess
    def Set_Bounds(self, was_high :bool) -> None:
        if was_high:
            self._max_guess = self._prev_guess
        else:
            self._min_guess = self._prev_guess

    def Make_Guess(self) -> int:
        # Get random number, within the bonds of _min_guess and _max_guess as ai input
        guess = randint(self._min_guess +1, self._max_guess -1)

        # Get new random number while the guess is out of bounds
        while guess <= self._min_guess and guess >= self._max_guess:
            guess = randint((self._min_guess +1), (self._max_guess -1))
        self._prev_guess = guess
        time.sleep(0.5)
        return guess

########################################################