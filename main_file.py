import random
import time
from enum import Enum
import graphics
import game_mechanics
from pygame import event
from pygame import display

################### GAME LOOP #########################
def Game_Loop():
    play_game = True
    user_input = ''
            
    wnd = graphics.Window(True)

    # Initialize the game
    mechanics = game_mechanics.Game_Mechanics()
    tries = 0
    user_input = -1
    user = wnd.set_player()

    # If player is human, loop the game until player guesses the number
    if user:
        while mechanics.validate_guess(user_input) != "done":
            tries +=1
            wnd.render('')
            
            res = wnd.poll_events()
            if res == graphics.Input_State.READY:
                res = mechanics.validate_guess(wnd.Get_guess())

                if res == game_mechanics.Game_State(2):
                    wnd.render("Too low")
                elif res == game_mechanics.Game_State(1):
                    wnd.render("Too high")
                elif res == game_mechanics.Game_State(0):
                    wnd.render(f"YOU WIN! num of guesses: {tries}")
                    
    # If player is not human, create an ai object and ask it to guess the number until guess is correct
    else:
        ai_user = game_mechanics.AI()
        while mechanics.validate_guess(user_input) != game_mechanics.Game_State.GAME_OVER:
            wnd.Check_Quit()
            tries +=1
            if tries > 0:
                time.sleep(0.7)
            user_input = ai_user.Make_Guess()
            wnd.render(str(user_input))
            res = mechanics.validate_guess(user_input)

            time.sleep(0.7)
            if res == game_mechanics.Game_State(2):
                ai_user.Set_Bounds(False)
                wnd.render("Too low")
            elif res == game_mechanics.Game_State(1):
                ai_user.Set_Bounds(True)
                wnd.render("Too high")
            elif res == game_mechanics.Game_State(0):
                wnd.render(f"YOU WIN! num of guesses: {tries}")
#######################################################

def main():
    Game_Loop()
    

if __name__ == "__main__":
    main()