import os, requests

DIR = os.path.dirname(__file__)
REPO = "mov-ebx/discord-scripts"

VERS = requests.get("https://raw.githubusercontent.com/"+REPO+"/Beta/VERSION").text
SCRIPTS = requests.get("https://raw.githubusercontent.com/"+REPO+"/Beta/data/scripts.json").text
print(SCRIPTS)

def download_scripts():
    open(DIR+'/version', 'w').writelines(VERS)
    print('XD')

if os.path.exists(DIR+'/version') == False:
    open(DIR+'/version', 'w').writelines("0")
try:
    if os.path.exists(DIR+'/../scripts') == False:
        os.mkdir(DIR+'/../scripts')
        download_scripts()
    elif open(DIR+'/version', 'r+').readlines()[0] != VERS:
        download_scripts()
except IndexError:
    download_scripts()