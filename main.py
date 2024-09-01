import curses
from curses import wrapper # takes over terminal for duration of program
import time
import random

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to the Speed Typing Test!\n") 
    stdscr.addstr("Press any key to begin!\n") 
    stdscr.refresh()
    stdscr.getkey() # place user key pressed input onto output screen

def display_text(stdscr, target, current, wpm = 0):
    stdscr.addstr(target)
    stdscr.addstr(1, 0, f"WPM: {wpm}")
    

    for i, char in enumerate(current): # iterate through letters already pressed
        correct_char = target[i]
        color = curses.color_pair(1) # default green text
        if char != correct_char:
            color =  curses.color_pair(2) # change text color to red
        stdscr.addstr(0,i,char, color) # place current char in target_text string as different color

def load_text():
    with open("text.txt", "r") as file:
        line_list = file.readlines() # lines stored in a list of strings
        return random.choice(line_list).strip() # return pseudorandom line without extra delimiters

def wpm_test(stdscr):
    
    target_text = load_text() # text user has to enter
    current_text = [] #txt user has entered
    wpm = 0
    start_time = time.time() 
    stdscr.nodelay(True)

    # continually prompts user for character, overlaps target_text with inputa
    while True:
        time_elapsed = max(time.time() - start_time, 1)
        wpm = len(current_text) / (time_elapsed / 60) #c alculate current characters per minute
        wpm = round(wpm/5) # characters per minute / 5 (assuming the average word has 5 characters) gives us words per minute 

        stdscr.clear()
        display_text(stdscr, target_text, current_text, wpm)
        stdscr.refresh()

        if "".join(current_text) == target_text: #convert typed list to str and compare to target
            stdscr.nodelay(False)
            break

        try:
            key = stdscr.getkey() # user input key      
        except:
            continue #if no key entered, skip any exceptions thrown

        if ord(key) == 27:
            break

        if key in ("KEY_BACKSPACE", '\b', "\x7f"):
            if len(current_text) > 0:
                current_text.pop()
        elif len(current_text) < len(target_text):
            current_text.append(key)


# standard output takeover screen
def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)

    start_screen(stdscr)
    while True:
        wpm_test(stdscr)
        stdscr.addstr(2, 0, "You completed the text! Press any key to continue... \nPress ESC to end.")
        key = stdscr.getkey()
        if ord(key) == 27:
            break

wrapper(main) #call wrapper func with main arg to evoke takeover