import time
import sys
import os

class Format:
    BOLD = "\033[1m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"
    BLACK = "\033[30m"
    BG_RED = "\033[101m"
    BG_GREEN = "\033[102m"
    BG_YELLOW = "\033[103m"
    BG_BLUE = "\033[44m"
    BG_MAGENTA = "\033[105m"
    BG_CYAN = "\033[106m"
    BG_WHITE = "\033[107m"
    BG_BLACK = "\033[40m"
    
RESET = "\033[0m"

class Symbols:
    HEART = "♥"
    DIAMOND = "♦"
    CLUB = "♣"
    SPADE = "♠"
    YEN = "¥"
    DOLLAR = "$"
    CHIP = "⬤"
    DICE = "󰝮 "
    STAR = "★"
    TROPHY = "🏆"
    ERROR = " "

def slomate(text, delay=0.125, style=RESET):
    """8 chars per second"""
    styled_text = f"{style}{text}{RESET}"
    for char in styled_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)  
    sys.stdout.write("\n")

def midmate(text, delay=0.01, style=RESET):
    """100 chars per second"""
    styled_text = f"{style}{text}{RESET}"
    for char in styled_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)  
    sys.stdout.write("\n")
    
def fastmate(text, delay=0.0025, style=RESET):
    """500 chars per second"""
    styled_text = f"{style}{text}{RESET}"
    for char in styled_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)  
    sys.stdout.write("\n")

def ultramate(text, delay=0.0015, style=RESET):
    """1000 chars per second"""
    styled_text = f"{style}{text}{RESET}"
    for char in styled_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)  
    sys.stdout.write("\n")

def wiper():
    os.system('cls' if os.name == 'nt' else 'clear')
