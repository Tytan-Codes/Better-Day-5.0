import subprocess
import os
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
import platform
import sys
import time
import click
from better_day.main import main

@click.command()
def better_day():
    main()

if __name__ == '__main__':
    better_day()


# Check if the user has already accepted the liability disclaimer
def printt(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    print('')

def main():
    os.system('cls')
    print(f'{Style.BRIGHT + Fore.YELLOW}[{Fore.RED}#{Fore.YELLOW}] ')
    print(f'{Style.BRIGHT + Fore.RED}[{Fore.WHITE}1{Fore.RED}]')

def newhere():
    os.system('cls')    
    printt('Hello, welcome to Better Day 5.0')
    time.sleep(2)
    printt('You seem to be new here, I think that you should go around with my tutorial first, don\'t worry, you won\'t regret it.\nYou don\'t even need to leave the terminal window.')
    time.sleep(1)
    printt('Type \'go\' to continue')
    newGo = str(input(''))
    if newGo == 'go':
        print('py main.py')
        time.sleep(0.05)
        os.system('cls')
        print(Style.BRIGHT + """  ____       _   _                  _____              
 |  _ \     | | | |                |  __ \             
 | |_) | ___| |_| |_ ___ _ __      | |  | | __ _ _   _ 
 |  _ < / _ \ __| __/ _ \ '__|     | |  | |/ _` | | | |
 | |_) |  __/ |_| ||  __/ |     _  | |__| | (_| | |_| |
 |____/ \___|\__|\__\___|_|    (_) |_____/ \__,_|\__, |
                                                  __/ |
                                                 |___/ """)
    print(Style.BRIGHT + 'Author        :   ', Fore.RED + Style.BRIGHT + 'Tytan-Codes')
    print(Style.BRIGHT + 'Code Type     :   ', Fore.RED + Style.BRIGHT + 'Python 3')
    print(Style.BRIGHT + 'Description   :   ', Fore.RED + Style.BRIGHT + 'Cool python things')
    print(Style.BRIGHT + 'Goal          :   ', Fore.RED + Style.BRIGHT + 'Make something COOL')
    print(Style.BRIGHT + 'Github        : ', Fore.RED + Style.BRIGHT +'  github.com/Tytan-Codes')
    print(Style.BRIGHT + 'Version       : ', Fore.RED + Style.BRIGHT + '  Stable, v5.0.0 -- Better Day Project')
    print(Style.BRIGHT + '(c) 2022-2033, Tytan-Codes All rights reserved')
    print(Style.BRIGHT + Fore.YELLOW + '* ' + Style.BRIGHT + 'Trust Me It\'s good' + Style.BRIGHT + Fore.RED + ' -- ' + Style.BRIGHT + 'I\'m a CODER' + Style.BRIGHT + Fore.YELLOW + ' *')
    time.sleep(1)
    printt('This is where you tap enter')
    printt('This will now pop up.')
    time.sleep(1)
    os.system('cls')
    print(Style.BRIGHT + Fore.YELLOW + '[' + Style.BRIGHT + Fore.RED + '#' + Style.BRIGHT + Fore.YELLOW + '] Options:')
    print(Style.BRIGHT + Fore.RED + '   {' + Style.BRIGHT + Fore.WHITE +'1' + Style.BRIGHT + Fore.RED + '}' + Style.BRIGHT + Fore.YELLOW + ' ~> ' +  Style.BRIGHT + Fore.WHITE +' Search')
    print(Style.BRIGHT + Fore.RED + '   {' + Style.BRIGHT + Fore.WHITE +'2' + Style.BRIGHT + Fore.RED + '}' + Style.BRIGHT + Fore.YELLOW + ' ~> ' +  Style.BRIGHT + Fore.WHITE +' System')
    print(Style.BRIGHT + Fore.RED + '   {' + Style.BRIGHT + Fore.WHITE +'3' + Style.BRIGHT + Fore.RED + '}' + Style.BRIGHT + Fore.YELLOW + ' ~> ' +  Style.BRIGHT + Fore.WHITE + ' For beta users')
    print(Style.BRIGHT + Fore.RED + '   {' + Style.BRIGHT + Fore.WHITE +'4' + Style.BRIGHT + Fore.RED + '}' + Style.BRIGHT + Fore.YELLOW + ' ~> ' +  Style.BRIGHT + Fore.WHITE + ' For beta users')
    print(Style.BRIGHT + Fore.RED + '   {' + Style.BRIGHT + Fore.WHITE +'5' + Style.BRIGHT + Fore.RED + '}' + Style.BRIGHT + Fore.YELLOW + ' ~> ' +  Style.BRIGHT + Fore.WHITE + ' For beta users')
    print(Style.BRIGHT + Fore.RED + '   {' + Style.BRIGHT + Fore.WHITE +'0' + Style.BRIGHT + Fore.RED + '}' + Style.BRIGHT + Fore.YELLOW + ' ~> ' +  Style.BRIGHT + Fore.WHITE +' Back')
    
    print(Style.BRIGHT + Fore.RED + 'Better Day ' + Style.BRIGHT + Fore.YELLOW + '> ' + Style.BRIGHT + Fore.RED + 'Choose ')
    time.sleep(1)
    printt('This is where you pick one.')
    break
    main()
    
######################################################





            
            

def starter():
    os.system('cls')        
    print(Style.BRIGHT + """  ____       _   _                  _____              
 |  _ \     | | | |                |  __ \             
 | |_) | ___| |_| |_ ___ _ __      | |  | | __ _ _   _ 
 |  _ < / _ \ __| __/ _ \ '__|     | |  | |/ _` | | | |
 | |_) |  __/ |_| ||  __/ |     _  | |__| | (_| | |_| |
 |____/ \___|\__|\__\___|_|    (_) |_____/ \__,_|\__, |
                                                  __/ |
                                                 |___/ """)
    print(Style.BRIGHT + 'Author        :   ', Fore.RED + Style.BRIGHT + 'Tytan-Codes')
    print(Style.BRIGHT + 'Code Type     :   ', Fore.RED + Style.BRIGHT + 'Python 3')
    print(Style.BRIGHT + 'Description   :   ', Fore.RED + Style.BRIGHT + 'Cool python things')
    print(Style.BRIGHT + 'Goal          :   ', Fore.RED + Style.BRIGHT + 'Make something COOL')
    print(Style.BRIGHT + 'Github        : ', Fore.RED + Style.BRIGHT +'  github.com/Tytan-Codes')
    print(Style.BRIGHT + 'Version       : ', Fore.RED + Style.BRIGHT + '  Stable, v5.0.0 -- Better Day Project')
    print(Style.BRIGHT + '(c) 2022-2033, Tytan-Codes All rights reserved')
    print(Style.BRIGHT + Fore.YELLOW + '* ' + Style.BRIGHT + 'Trust Me It\'s good' + Style.BRIGHT + Fore.RED + ' -- ' + Style.BRIGHT + 'I\'m a CODER' + Style.BRIGHT + Fore.YELLOW + ' *')
    print('')
    enter = input(Style.BRIGHT + Fore.YELLOW + '[' + Style.BRIGHT + Fore.RED + '~' + Style.BRIGHT + Fore.YELLOW + '] ' + Style.BRIGHT + Fore.RED + 'Press Enter to Continue...' )

    if enter == "":
        main()

    else:
        print(Style.BRIGHT + Fore.RED +"THATS NOT ENTER, THAT\'s ", enter)
        
############################################
if os.path.exists('accepted.txt'):
    print('Welcome back!')
    main()
else:
    # Display the liability disclaimer
    print('Welcome to the program!')
    print('Before you continue, you must accept the liability disclaimer.')
    print('Liability Disclaimer: [insert liability disclaimer here]')

    # Ask the user if they accept the liability disclaimer
    while True:
        response = input('Do you accept the liability disclaimer? (Y/N)').lower()
        if response == 'y':
            # Create a file indicating that the user has accepted the liability disclaimer
            with open('accepted.txt', 'w') as f:
                f.write('Accepted')
            print('Thank you for accepting the liability disclaimer. You may proceed with the program.')
            newhere()
        elif response == 'n':
            # End the program if the user does not accept the liability disclaimer
            print('You must accept the liability disclaimer to use the program. Exiting...')
            exit()
        else:
            print('Invalid response. Please enter Y or N.')
        
        
starter()
