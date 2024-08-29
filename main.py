import curses
from curses import wrapper # takes over terminal for duration of program

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to the Speed Typing Test!\n") 
    stdscr.addstr("Press any key to begin!\n") 
    stdscr.refresh()
    stdscr.getkey() # place user key pressed input onto output screen


def wpm_test(stdscr):
    target_text = "Hello world this is some test text for this app!"
    current_text = [] #txt user has entered
    
    stdscr.clear()
    stdscr.addstr(target_text) 
    stdscr.refresh()
    stdscr.getkey()


# standard output takeover screen
def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)

    start_screen(stdscr)
    wpm_test(stdscr)

wrapper(main) #call wrapper func with main arg to evoke takeover