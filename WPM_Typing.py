import curses
from curses import wrapper
import time

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Hello this is the wpm typing tester!")
    stdscr.addstr("\n press any key to start !")
    stdscr.refresh()
    stdscr.getkey()

def display_text(stdscr , text , user_text , wpm= 0):
    stdscr.addstr(text)
    stdscr.addstr(1 , 0 ,f"WPM : {wpm}")
    for i , char in enumerate(user_text):
        rightColor = curses.color_pair(1)
        wrongColor = curses.color_pair(2)
        if text[i] == user_text[i]:
            stdscr.addstr(0 ,i ,char,rightColor)
        else:
            stdscr.addstr(0 ,i ,char,wrongColor)


def wpm_test(stdscr):
    test_text = "This is a test text to test the speed of write in wpm!"
    user_input_text = []
    wpm = 0
    stat_time = time.time()
    stdscr.nodelay(True)
    while True:
        elapsedTime = max(time.time() - stat_time , 1)
        wpm =  round((len(user_input_text) / (elapsedTime / 60)) / 5)
        stdscr.clear()
        display_text(stdscr ,test_text, user_input_text , wpm)
        stdscr.refresh()

        if "".join(user_input_text) == test_text:
            stdscr.nodelay(False)
            break
        try:
            key =  stdscr.getkey()
        except:
            continue
        if ord(key) == 27:
            break
        if ord(key) == 8:
            if len(user_input_text) > 0:
                user_input_text.pop()
        elif len(user_input_text) < len(test_text):
            user_input_text.append(key)

def main(stdscr):
    # Create Font , Background colors pairs (id , font_color , background_color)
    curses.init_pair(1, curses.COLOR_GREEN , curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED   , curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE , curses.COLOR_BLACK)

    start_screen(stdscr)
    while True:
        wpm_test(stdscr) 
        stdscr.addstr(2,0,"You compelete the text ! Press any key to start again or ESC to exit!")
        stdscr.refresh()
        key = stdscr.getkey()
        if ord(key) == 27:
            break



wrapper(main)