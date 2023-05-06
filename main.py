import subprocess

# Set the GitHub repository URL and the branch name
github_url = "https://github.com/tytan-codes/better-day.git"
branch_name = "Unstable"
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

def picker(nehow):
    nehoww = platform.system()
    if nehoww == 'Windows':
        os.system(f'{nehow}')
    if nehoww == 'Windows':
        os.system(f'{nehow}')
        
def os():
    current_os = platform.system()
    
    if current_os == 'Windows':
        thing()
    elif current_os == 'Linux':
        Linux()
    else:
        print('You operating system is not supported yet.')
        print(f"Unknown operating system: {current_os}")
        exit()