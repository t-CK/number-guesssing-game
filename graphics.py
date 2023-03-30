import pygame
import sys
from enum import Enum
from sys import *
import pygame
from pygame.display import *
from pygame.color import *
from pygame.draw import *
from pygame.locals import *
from pygame.sysfont import *
from pygame.font import *
from pygame.event import *
from pygame.color import *

class Input_State(Enum):
    READY = 0
    WAIT_FOR_INPUT = 1
    QUIT = 2

class Window:
    """Class to handle graphical output to window"""
    _name :str
    _width :int
    _height :int
    _native_window :pygame.Surface
    _player_human :bool
    _background_color = (0, 0, 0)
    _font :pygame.font.Font
    _guess :int

    def __init__(self, is_human :bool) -> None:
        self._player_human = is_human

        # Set window values
        self._width = 1000
        self._height = 800
        self._name = "Number guessing game"

        # Setup the display
        pygame.display.init()
        self._native_window = pygame.display.set_mode((self._width, self._height), pygame.SCALED, 0, False)
        pygame.display.set_caption(self._name)
        pygame.display.is_fullscreen = False

        pygame.font.init()
        self._font = pygame.font.SysFont(None, 150, True)

    def set_player(self) -> bool:
        is_valid = False
        setup_text = self._font.render("Choose player:", False, (100, 250, 200))
        opt_1_chosen = True # To keep track of user selection
        while not is_valid:
            self._native_window.fill(self._background_color)
            self._native_window.blit(setup_text, (20, 20))

            # Set option message colors to mach selection
            if opt_1_chosen:
                opt_1 = self._font.render("Human", False, (0, 200, 0))
                self._native_window.blit(opt_1, (50, 200))
                opt_2 = self._font.render("AI", False, (200, 0, 0))
                self._native_window.blit(opt_2, (50, 300))
            elif not opt_1_chosen:
                opt_1 = self._font.render("Human", False, (200, 0, 0))
                self._native_window.blit(opt_1, (50, 200))
                opt_2 = self._font.render("AI", False, (0, 200, 0))
                self._native_window.blit(opt_2, (50, 300))

            # Poll events on selection loop
            if pygame.event.peek():
                keys = pygame.key.get_pressed()
                e = pygame.event.poll()
                if e.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                    self.on_window_closed()
                    break
                if keys[pygame.K_UP] or keys[pygame.K_DOWN]:
                    if opt_1_chosen:    # Flip opt_1_chosen to render selection to window
                        opt_1_chosen = False
                    else:
                        opt_1_chosen = True
                if keys[pygame.K_RETURN] or keys[pygame.K_KP_ENTER]:
                    self._native_window.fill(self._background_color)
                    is_valid = True
                    
            pygame.display.flip()
        self._native_window.fill(self._background_color)
        img = self._font.render("Guess a number:", False, (100, 250, 250))
        self._native_window.blit(img, (0, 0))
        pygame.display.flip()
        return opt_1_chosen    # Return the selection

    def render(self, msg :str):
        if msg != '':
            self._native_window.fill(self._background_color)
            if msg.find("YOU WIN!") != -1:
                img = self._font.render(msg[:8], False, (0, 250, 0))
                self._native_window.blit(img, (0, 0))
                self._font = pygame.font.SysFont(None, 100, True)
                img = self._font.render(msg[8:], False, (100, 250, 200))
                self._native_window.blit(img, (50, 150))
            else:
                if msg == "Too low":
                    img = self._font.render(msg, False, (250, 0, 0))
                else:
                    img = self._font.render(msg, False, (0, 250, 0))
                self._native_window.blit(img, (0, 0))
            pygame.display.flip()
    
    def update(self, string :str) ->None:
        """Updates window afrer key press has been detected"""
        self._native_window.fill(self._background_color)
        img = self._font.render("Guess a number:", False, (100, 250, 250))
        
        self._native_window.blit(img, (0, 0))
        img = self._font.render(string, False, (100, 250, 200))
        self._native_window.blit(img, (100, 250))
        pygame.display.flip()

    # Check if user has exited the game
    def Check_Quit(self):
        e = pygame.event.poll()
        if e.type == pygame.QUIT:
            self.on_window_closed()
            return Input_State.QUIT
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                self.on_window_closed()

    def poll_events(self) -> Input_State:
        if self._player_human:
            print_string = ''

            # Poll events
            while True:
                e = pygame.event.poll()
                if e.type == pygame.QUIT:
                    self.on_window_closed()
                    return Input_State.QUIT
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        self.on_window_closed()
                        break
                    if len(print_string) < 4:
                        if e.key == pygame.K_0 or e.key == pygame.K_KP0:
                            print_string += '0'
                            self.update(print_string)
                        elif e.key == pygame.K_1 or e.key == pygame.K_KP1:
                            print_string += '1'
                            self.update(print_string)
                        elif e.key == pygame.K_2 or e.key == pygame.K_KP2:
                            print_string += '2'
                            self.update(print_string)
                        elif e.key == pygame.K_3 or e.key == pygame.K_KP3:
                            print_string += '3'
                            self.update(print_string)
                        elif e.key == pygame.K_4 or e.key == pygame.K_KP4:
                            print_string += '4'
                            self.update(print_string)
                        elif e.key == pygame.K_5 or e.key == pygame.K_KP5:
                            print_string += '5'
                            self.update(print_string)
                        elif e.key == pygame.K_6 or e.key == pygame.K_KP6:
                            print_string += '6'
                            self.update(print_string)
                        elif e.key == pygame.K_7 or e.key == pygame.K_KP7:
                            print_string += '7'
                            self.update(print_string)
                        elif e.key == pygame.K_8 or e.key == pygame.K_KP8:
                            print_string += '8'
                            self.update(print_string)
                        elif e.key == pygame.K_9 or e.key == pygame.K_KP9:
                            print_string += '9'
                            self.update(print_string)
                    if e.key == pygame.K_BACKSPACE:
                        print_string = print_string[:-1]
                        self.update(print_string)
                    if e.key == pygame.K_RETURN or e.key == pygame.K_KP_ENTER:
                        if len(print_string) > 0:
                            break
        self._guess = int(print_string)
        return Input_State(0)
    
    def Get_guess(self) -> int:
        return self._guess

    # Handle window closing and player quitting the game
    def on_window_closed(self):
        """Called on window being closed.
        Shuts down graphical subsystems"""
        pygame.display.quit()
        pygame.font.quit()
        sys.exit()