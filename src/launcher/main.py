import os, requests
from colorama import Fore, Back, Style

DIR = os.path.dirname(__file__)
REPO = 'mov-ebx/discord-scripts'

VERS = requests.get('https://raw.githubusercontent.com/'+REPO+'/main/VERSION').text
SCRIPTS = requests.get('https://raw.githubusercontent.com/'+REPO+'/main/data/scripts.json').json()

# Title
print('Launcher version 0.1b'+Fore.RED+'''
  ____  _                       _   ____            _       _       
 |  _ \(_)___  ___ ___  _ __ __| | / ___|  ___ _ __(_)_ __ | |_ ___ 
 | | | | / __|/ __/ _ \| '__/ _` | \___ \ / __| '__| | '_ \| __/ __|
 | |_| | \__ \ (_| (_) | | | (_| |  ___) | (__| |  | | |_) | |_\__ \\
 |____/|_|___/\___\___/|_|  \__,_| |____/ \___|_|  |_| .__/ \__|___/
         ''' + Fore.RESET + 'created by ' + REPO.split('/')[0] + (' ' * (33 - len(REPO.split('/')[0]))) + Fore.RED + '|_|\n' + Fore.RESET)
token = input("\nPlease enter your Discord token (this wont be shared or saved anywhere): ")

# Auto updater
def download_scripts():
    VER = open(DIR+'/version', 'r').readlines()[0]
    print('Downloading scripts!\n')
    for script in SCRIPTS:
        url = 'https://raw.githubusercontent.com/'+REPO+'/main/src/scripts/'+script
        if os.path.exists(DIR+'/scripts/'+script) == False:
            print(' + Downloading '+script+'...')
            open(DIR+'/scripts/'+script, 'x').writelines(requests.get(url).text)
        elif float(SCRIPTS[script]) > float(VER):
            print(' + Updating '+script+'...')
            open(DIR+'/scripts/'+script, 'w').writelines(requests.get(url).text)
        else:
            print(' + '+script+' is up to date!')
    open(DIR+'/version', 'w').writelines(VERS)
    print('')
if os.path.exists(DIR+'/version') == False:
    open(DIR+'/version', 'w').writelines('0')
try:
    if os.path.exists(DIR+'/scripts') == False:
        os.mkdir(DIR+'/scripts')
        download_scripts()
    elif open(DIR+'/version', 'r+').readlines()[0] != VERS:
        download_scripts()
except IndexError:
    download_scripts()

# Command line
scripts = os.listdir(DIR+'/scripts/')
print("Commands:\n - scripts\n - run [id]\n")
while True:
    command = input('> ')
    if command.split(' ')[0] == 'scripts':
        print('\nScripts:')
        i = 1
        for script in scripts:
            if script.endswith('.py'):
                desc = __import__('scripts.'+script[:-3], fromlist=[None]).desc
                print(f' {i}) {script[:-3]} - {desc}')
                i += 1
        print("")
    elif command.split(' ')[0] == 'run':
        try:
            command = command.split(' ')[1]
            script = scripts[len(scripts)-i+int(command)]
            print(f'\nSelected {script}\n')
            params = {"token":token}
            iparams = __import__('scripts.'+script[:-3], fromlist=[None]).params
            for param in iparams:
                if param != "token":
                    params[param] = input("Enter "+iparams[param]+": ")
            print("\nRunning "+script[:-3]+"...")
            __import__('scripts.'+script[:-3], fromlist=[None]).run(**params)
            print("\nDone!\n")
        except:
            print("\nUnable to run. Try again?\n")