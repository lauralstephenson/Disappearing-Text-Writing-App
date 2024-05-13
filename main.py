#This is an app where the text disappears after 5 seconds of typing.
#Work can be saved, but the save must happen within 5 seconds.
#It is used to train typists to type fast AND to continually save their work.
from tkinter import *

user_text = ""
timer = None

def start_calculating(event):
    global timer, user_text
 
    if timer is not None:
        window.after_cancel(timer)
 
    if event.keysym == "BackSpace":
        user_text = user_text[0: len(user_text) - 1]
 
    elif event.char:
        user_text += event.char
        timer = window.after(5000, reset_app)
 
    return
 
#Resets the app and deletes all the text. 
def reset_app():
    global timer, user_text
    typing_area.delete("1.0", "end")
    user_text = ""
    timer = None
    return
 
 
 #Save the user's texts
def save_text():
    global user_text
    if user_text == "":
        return
    try:
        f = open("writeups.txt", "r")
    except FileNotFoundError:
        f = open("writeups.txt", "w")
        f.write(user_text)
        user_text = ""
        return
    else:
        cont = f.read()
        if cont == "":
            text_to_write = user_text
        else:
            text_to_write = f'\n{user_text}'
 
        with open("writeups.txt", "a") as f:
            f.write(text_to_write)
            user_text = ""
    finally:
        return

#The UI is TKinter with constants for colors, fonts, etc.
#Colors
BORDER = "#3C2C3E"
FG = "light blue"
BG = "#4B5D67"

#Font Families
FONT_FAMILY_1 = "Calibri"
FONT_FAMILY_2 = "Arial"

#FONT SIZES
FONT_SIZE_1 = 14
FONT_SIZE_2 = 18
FONT_SIZE_3 = 24
 
#FONT STYLES
FONT_STYLE_1 = "normal"
FONT_STYLE_2 = "italic"
FONT_STYLE_3 = "bold"

#UI Font, Family, Style, and Size
PARA_FONT = (FONT_FAMILY_1, FONT_SIZE_1, FONT_STYLE_3)
PARA_FONT_2 = (FONT_FAMILY_1, 12, FONT_STYLE_2)
HEAD_FONT = (FONT_FAMILY_2, FONT_SIZE_3, FONT_STYLE_1)

#UI Welcome Message
heading = "WRITE WITH MAGICAL INK"
#App instructions
instruction = "If you don't press any key within 5 seconds, your text will disappear!"

#CREATING OUR TKINTER WINDOW

"""
1. Create a TKinter window object.
2. Create a title.
3. Set window properties, like background colors and padding.
"""

window = Tk()
window.title("Disappearing Text Desktop App")
window.config(bg=BG, padx=20, pady=10)

#Create the widgets

#Heading
heading = Label(text=heading, font=HEAD_FONT, bg=BG,
                fg=FG, padx=10, pady=10)

#Instructions
instruction = Label(text=instruction, font=PARA_FONT_2, fg=FG,
                    bg=BG, pady=10)

#Text typing area
typing_area = Text(font=PARA_FONT, bg=BG, fg=FG,
                   width=100, height=15, wrap="w",
                   highlightcolor=BORDER,
                   highlightthickness=4,
                   highlightbackground=BORDER,
                   padx=5, pady=5)

#Text area calculations
typing_area.bind("<KeyPress>", start_calculating)

#A reset button so user can reset the application
reset_btn = Button(text="Reset", fg=FG, bg=BG, font=PARA_FONT,
                   highlightbackground=FG,
                   highlightcolor=FG,
                   highlightthickness=0, border=3,
                   command=reset_app, width=50)

#Save button for user to save the text in a text file
save_btn = Button(text="Save", fg=FG, bg=BG,
                  font=PARA_FONT,
                  highlightbackground=FG,
                  highlightcolor=FG, highlightthickness=0,
                  border=3,
                  command=save_text, width=50)

#Widgets placed in window
heading.grid(row=0, column=0, columnspan=3)
instruction.grid(row=2, column=0, columnspan=3)
typing_area.grid(row=3, column=0, columnspan=3)
reset_btn.grid(row=4, column=0)
save_btn.grid(row=4, column=2)

#Keep the window open unless explicitly closed
window.mainloop()