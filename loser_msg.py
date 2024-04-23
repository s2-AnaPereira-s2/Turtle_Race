from tkinter import *
from tkinter import ttk

color_winner = ""

def Losee():
    losee = Tk()
    losee.title("Turtle Race")

    loser_mgs = ttk.Frame(losee, padding=10)
    loser_mgs.grid()
    loser_mgs.pack(pady=50)

    window_width = 400
    window_height = 200

    # Get the screen width and height
    screen_width = losee.winfo_screenwidth()
    screen_height = losee.winfo_screenheight()

    # Calculate the x and y coordinates to center the window
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2


    # Set the window geometry to center it
    losee.geometry(f"{window_width}x{window_height}+{x}+{y}")
    print_msg = f"Pouts...not this time!!!\n\nThe turtle {color_winner.capitalize()} is the winner."
    ttk.Label(loser_mgs, text=print_msg, font=("Helvetica", 16), foreground="black").grid(column=0, row=0)
    losee.mainloop()

if __name__ == "__main__":
    Losee()

