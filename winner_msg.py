from tkinter import *
from tkinter import ttk

color_winner = ""

def Winn():
    winn = Tk()  
    winn.title("Turtle Race")

    winner_mgs = ttk.Frame(winn, padding=10)
    winner_mgs.grid()
    winner_mgs.pack(pady=50)

    window_width = 400
    window_height = 200

    # Get the screen width and height
    screen_width = winn.winfo_screenwidth()
    screen_height = winn.winfo_screenheight()

    # Calculate the x and y coordinates to center the window
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2


    # Set the window geometry to center it
    winn.geometry(f"{window_width}x{window_height}+{x}+{y}")
    print_msg = f"**Congratulations**\n\nYour turtle {color_winner.capitalize()} is the winner."
    ttk.Label(winner_mgs, text=print_msg, font=("Helvetica", 16), foreground="black").grid(column=0, row=0)
    winn.mainloop()


if __name__ == "__main__": 
    Winn()




