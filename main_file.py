import random
import time
from enum import Enum
from tkinter import messagebox
import graphics
import game_mechanics

################### GAME LOOP #########################
def Game_Loop():
    wnd = graphics.Window(True)
    is_running = True
    while is_running:
        user_input = ''

        # Initialize the game
        mechanics = game_mechanics.Game_Mechanics()
        tries = 0
        user_input = -1
        # Set the 
        user_selection = wnd.Render_Menu()

        # variable to keep track of game state in gameloop
        game_state = game_mechanics.Game_State.NONE

        if user_selection == 2:
            wnd.on_window_closed()
        # If player is human, loop the game until player guesses the number
        elif user_selection == 0:
            while game_state != game_mechanics.Game_State.GAME_OVER:
                tries +=1
                wnd.Render('')

                game_state = wnd.poll_events()
                if game_state == graphics.Input_State.READY:
                    game_state = mechanics.Validate_Guess(wnd.Get_Guess())

                    if game_state == game_mechanics.Game_State.TOO_LOW:
                        wnd.Render("Too low")
                    elif game_state == game_mechanics.Game_State.TOO_HIGH:
                        wnd.Render("Too high")
                    elif game_state == game_mechanics.Game_State.GAME_OVER:
                        wnd.Render(f"YOU WIN! num of guesses: {tries}")
                        time.sleep(1)

        # If player is not human, create an ai object and ask it to guess the number until guess is correct
        elif user_selection == 1:
            ai_user = game_mechanics.AI()
            while game_state != game_mechanics.Game_State.GAME_OVER:
                tries +=1
                if tries > 0:
                    time.sleep(0.7)
                user_input = ai_user.Make_Guess()
                wnd.Render(str(user_input))
                game_state = mechanics.Validate_Guess(user_input)

                wnd.Check_Quit() # Check if user want's to quit
                time.sleep(0.7)
                if game_state == game_mechanics.Game_State.TOO_LOW:
                    ai_user.Set_Bounds(False)
                    wnd.Render("Too low")
                elif game_state == game_mechanics.Game_State.TOO_HIGH:
                    ai_user.Set_Bounds(True)
                    wnd.Render("Too high")
                elif game_state == game_mechanics.Game_State.GAME_OVER:
                    wnd.Render(f"YOU WIN! num of guesses: {tries}")
                    time.sleep(1)
        else:
            messagebox.showerror("ERROR", "error has occured selecting player")
            wnd.on_window_closed()
        
#######################################################

def main():
    Game_Loop()
    

if __name__ == "__main__":
    main()