import random
import json
import os
import sys
from kolo import slomate, midmate, fastmate, ultramate, Format, Symbols, RESET, wiper

# BALANCE ----------------------------------------------

BALANCE_FILE = "balance.json"
STARTING_BALANCE = 100000000    # ¥100 million

def load_balance():
    if os.path.exists(BALANCE_FILE):
        with open(BALANCE_FILE, "r") as file:
            data = json.load(file)
            return data.get("balance", STARTING_BALANCE)
    else:
        return STARTING_BALANCE

def format_balance(balance):
    if balance >= 1_000_000_000:  # B
        return f"{balance / 1_000_000_000:.2f}B"
    elif balance >= 1_000_000:  # Mil
        return f"{balance / 1_000_000:.2f}M"
    elif balance >= 1_000:  # Thou
        return f"{balance / 1_000:.2f}k"
    else:
        return f"{balance}"

def save_balance(balance):
    with open(BALANCE_FILE, "w") as file:
        json.dump({"balance": balance}, file)

# BET --------------------------------------------------

def parse_bet(bet_str):
    bet_str = bet_str.replace(",", ".").strip().lower()
    if bet_str.endswith("k"):  # Thou
        return int(float(bet_str[:-1]) * 1_000)
    elif bet_str.endswith("m"):  # Mil
        return int(float(bet_str[:-1]) * 1_000_000)
    elif bet_str.endswith("b"):  # B
        return int(float(bet_str[:-1]) * 1_000_000_000)
    else:
        return int(bet_str)  
        
# LOOKS ------------------------------------------------

def loading_screen():
    wiper()
    
    midmate(f"{Format.BOLD}WELCOME TO... {RESET}", style=Format.WHITE)
    ultramate(rf"""
{Format.BOLD}{Format.BLACK}                                          _..._                           {RESET}      
{Format.BOLD}{Format.WHITE}                  _______              .-'_..._''.                        {RESET}      
{Format.BOLD}{Format.WHITE}   __  __   ___   \  ___ `'.   .--.  .' .'      '.\     __.....__         {RESET}      
{Format.BOLD}{Format.BLACK}  |  |/  `.'   `.  ' |--.\  \  |__| / .'            .-''         '.       {RESET}      
{Format.BOLD}{Format.BLACK}  |   .-.  .-.   ' | |    \  ' .--.. '             /     .-''"'-.  `.     {RESET}      
{Format.BOLD}{Format.WHITE}  |  |  |  |  |  | | |     |  '|  || |            /     /________\   \    {RESET}      
{Format.BOLD}{Format.WHITE}  |  |  |  |  |  | | |     |  ||  || |            |                  |    {RESET}      
{Format.BOLD}{Format.BLACK}  |  |  |  |  |  | | |     ' .'|  |. '            \    .-------------'    {RESET}      
{Format.BOLD}{Format.BLACK}  |  |  |  |  |  | | |___.' /' |  | \ '.          .\    '-.____...---.    {RESET}      
{Format.BOLD}{Format.WHITE}  |__|  |__|  |__|/_______.'/  |__|  '. `._____.-'/ `.             .'     {RESET}      
{Format.BOLD}{Format.WHITE}                  \_______|/           `-.______ /    `''-...... -'       {RESET}      
{Format.BOLD}{Format.BLACK}                                                `                         {RESET}                                                                                  
    """)
    
    midmate(f"{Format.BOLD}{Format.WHITE}HOW IT WORKS:{RESET}")
    fastmate(f"""
    {Format.BLUE}󰎤 {RESET}{Format.ITALIC} Place your bet {Format.GREEN}(in {Symbols.YEN}){RESET}
    {Format.BLUE}󰎧 {RESET}{Format.ITALIC} Select a dice: {Format.BLACK}Black{RESET}{Format.ITALIC} 󱋱  {Format.WHITE}White{RESET}{Format.ITALIC} 󱋱  {Format.RED}Red{RESET}
    {Format.BLUE}󰎪 {RESET}{Format.ITALIC} The dealer picks its dice; you both roll!{RESET}
    {Format.BLUE}󰎭 {RESET}{Format.ITALIC} If your number is higher, you double your bet {RESET}{Symbols.TROPHY}
    {Format.BLUE}󰎱 {RESET}{Format.ITALIC} If your number is lower, the dealer keeps the pot {Format.RED}{Symbols.ERROR}{RESET}
    """)
    
    # dice details
    midmate(f"{Format.BOLD}{Format.WHITE}DICE DETAILS:{RESET}")
    fastmate(f"""
    {Format.BLACK}Black 󰝮 :{RESET} 3, 3, 4, 4, 8, 8
    {Format.RED}Red 󰝮 :  {RESET} 2, 2, 6, 6, 7, 7
    {Format.WHITE}White 󰝮 :{RESET} 1, 1, 5, 5, 9, 9
    """)
    
    # probabilities
    midmate(f"{Format.BOLD}{Format.WHITE}DYNAMICS:{RESET}")
    fastmate(f"""
    {Format.GREEN}Black > White:{RESET} 66.7%
    {Format.GREEN}White > Red:{RESET} 66.7%
    {Format.GREEN}Red > Black:{RESET} 66.7%
    """)
    
    input(f"\n\n{Format.BOLD}ENTER to begin...{RESET}")
    wiper()

# GAME -------------------------------------------------

def roll_die(die_faces):
    return random.choice(die_faces)

def magic(with_loading_screen=True):
    if with_loading_screen:
        loading_screen()
    wiper()
    balance = load_balance()

    dice = {
        "Black": [3, 3, 4, 4, 8, 8],
        "White": [1, 1, 5, 5, 9, 9],
        "Red": [2, 2, 6, 6, 7, 7]
    }
    dealer_strategy = {"Black": "White", "White": "Red", "Red": "Black"}

    while balance > 0:
        fastmate(f"{Format.ITALIC}Your balance: {Format.GREEN}{Symbols.YEN} {format_balance(balance)}")
        
        try:
            midmate(f"\n\n{Format.WHITE}How much would you like to bet?", style=Format.BOLD)
            bet_str = input()
            bet = parse_bet(bet_str)
            if bet <= 0 or bet > balance:
                fastmate("Invalid bet amount. Try again.", style=Format.RED)
                continue
        except ValueError:
            fastmate("Please enter a valid number.", style=Format.RED)
            continue

        fastmate(f"\n{Format.BOLD}{Format.WHITE}Choose your dice (Black, White, Red):{RESET}")
        player_choice = input().capitalize()
        if player_choice not in dice:
            fastmate(f"{Format.RED}Invalid choice. Try again.{RESET}")
            continue

        dealer_choice = dealer_strategy[player_choice]
        slomate(f"\n{Format.ITALIC}The dealer picks the {Format.BLUE}{Format.BOLD}{dealer_choice}{RESET} dice!")
        wiper()

        player_roll = roll_die(dice[player_choice])
        dealer_roll = roll_die(dice[dealer_choice])

        midmate(f"{Format.WHITE}{Symbols.DICE} {Format.ITALIC}{Format.BOLD}Rolling the dices...{RESET}")
        slomate(f"\n\n{Format.BLUE}{Format.BOLD}You rolled:{RESET} {Format.BOLD}{player_roll}{RESET}")
        slomate(f"{Format.ITALIC}{Format.RED}Dealer rolled:{RESET}{Format.ITALIC} {Format.BOLD}{dealer_roll}{RESET}")

        balance -= bet
        
        if player_roll > dealer_roll:
            winnings = bet * 2
            slomate(f"\n\n{Symbols.TROPHY} You won {Format.GREEN}{Symbols.YEN} {format_balance(winnings)}!{RESET}")
            balance += winnings
        else:
            slomate(f"\n\n{Format.UNDERLINE}{Format.RED}YOU LOST {Symbols.YEN} {format_balance(bet)}...{RESET}")

        save_balance(balance)

        if balance > 0:
            midmate(f"\n\n{Format.BOLD}Go again (y/n)?{RESET}")
            play_again = input().lower()
            if play_again != "y":
                wiper()
                break
        wiper()

    fastmate(f"{Format.MAGENTA}Game over! Come back soon!{RESET}")
    save_balance(balance)

if __name__ == "__main__":
    try:
        with_loading = "-nl" not in sys.argv
        magic(with_loading_screen=with_loading)
    except KeyboardInterrupt:
        wiper()
        print(f"{Format.MAGENTA}SEE YA LATER!{RESET}")
        sys.exit(0)
