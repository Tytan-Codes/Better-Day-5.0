import subprocess
import os
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
import platform
import sys
import time
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
######################################################

# Set the GitHub repository URL and the branch name
github_url = "https://github.com/tytan-codes/better-day-5.0.git"
branch_name = "Stable"
script_name = "main.py"
# Get the latest commit hash from the GitHub repository for the specified branch
cmd = f"git ls-remote {github_url} {branch_name}"
result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
if result.returncode != 0:
    print("Error getting latest commit hash from GitHub.")
    exit()
latest_commit = result.stdout.decode().split()[0]

# Check if the latest commit is already downloaded
cmd = "git rev-parse HEAD"
result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
if result.returncode != 0:
    print("Error getting current commit hash.")
    exit()
current_commit = result.stdout.decode().strip()

if current_commit == latest_commit:
    print("You are running the latest version of the script.")
else:
    print("A new version of the script is available on GitHub.")
    print(f"Latest commit on {branch_name}: {latest_commit}")

    
    print(f"{Style.BRIGHT + Fore.RED}You are running an outdated version of the script.")
    print(f"{Style.BRIGHT}A new version of the script is available on GitHub.")
    print(f"{Style.BRIGHT + Fore.RED}Please update by running update.py")
    print(f'{Style.BRIGHT + Fore.RED}You updating will make your experience better')
    exit()


current_os = platform.system()
        

print('You operating system is not supported yet.')
print(f"Unknown operating system: {current_os}")
exit()


            
            
############################################
if os.path.exists('accepted.txt'):
    print('Welcome back!')
    starter()
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
        newhere()

    else:
        print(Style.BRIGHT + Fore.RED +"THATS NOT ENTER, THAT\'s ", enter)
        
        
        
starter()
