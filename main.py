# Import required libraries
from tkinter import *
from text_generator import TextGenerator
import time

what_is_highscore = 0
time_elapsed = ''
article = ''
starttime = ''
FONT_COLOR = '#000000'
BG_COLOR = '#D9DCFC'

text = TextGenerator()

#------------------------------------UI-------------------------------------#

window = Tk()
window.title('Typing Speed Test')
window.config(padx=200, pady=200, bg=BG_COLOR)

# Lastscore label
lastscore = Label(text=f'Last score: 0 WPM', bg=BG_COLOR, fg=FONT_COLOR, font=('Courier',10,'bold'))
lastscore.grid(column=2, row=0)

# Highscore label
highscore = Label(text=f'High score: {what_is_highscore} WPM', bg=BG_COLOR, fg=FONT_COLOR, font=('Courier',10,'bold'))
highscore.grid(column=1, row=0)

# Article Label
article_on_screen = Label(text='Typing Speed Test', fg=FONT_COLOR, bg=BG_COLOR, font=('Courier',20,'bold'), wraplength=300, justify="center")
# article_on_screen.bind('<Configure>', lambda e: article_on_screen.config(wraplength=article_on_screen.winfo_width()))
article_on_screen.grid(column=0, row=1, columnspan=3)

# TextBox Creation
#Text
inputtxt = Text(height=5, width=50)
inputtxt.grid(column=0, row=2, columnspan=3)

#------------------------------------TIMER-------------------------------------#
def start_timer():
    global article
    article = text.random_article()
    window.update()
    #Puts cursor in textbox.
    inputtxt.focus()

    # Replaces text on screen with random text
    article_on_screen.config(text=article)
    global starttime
    starttime = time.time()
    return starttime


def stop_timer(event): # "Press Ctrl + x to Stop Timer"
    #Get's current value in textbox at line 1, character 0
    if article == inputtxt.get("1.0", 'end-1c'):
        # Calculates how many words are in the article
        no_of_words = len(article.split(' '))
        endtime = time.time()
        global time_elapsed
        time_elapsed = round((float(endtime - starttime) / 60),1) # Conversion to minutes
        article_on_screen.config(text=f'Rate: {no_of_words/time_elapsed} WPM')
        update_score()
    else:
        pass

#------------------------------------------------------------------------------#

#--------------------------------UPDATE SCORE----------------------------------#
def update_score():
    no_of_words = len(article.split(' '))
    lastscore.config(text=f'Last score: {no_of_words/time_elapsed} WPM')
    # Updates the highscore if achieved
    global what_is_highscore
    if (no_of_words/time_elapsed) > what_is_highscore:
        what_is_highscore = no_of_words/time_elapsed
        highscore.config(text=f'High score: {what_is_highscore} WPM')

#------------------------------------------------------------------------------#

# Buttons UI
starttimer_button = Button(text='Start Timer', font=('Courier',8,'bold'), command=start_timer)
starttimer_button.grid(column=0, row=3, columnspan=3)

# Define an event to close the window
def close_win(e):
   window.destroy()

# Bind the ESC key with the callback function
window.bind('<Escape>', lambda e: close_win(e))

#Bind the Keyboard shortcut Key
window.bind('<Control-x>', stop_timer)

window.mainloop()
