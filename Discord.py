from colorama import Fore, init, Style
import threading
import requests
import random
import ctypes
import time
import os

ctypes.windll.kernel32.SetConsoleTitleW('Discord Nickname Changer | Developed by jokers')
init(convert=True, autoreset=True)
SuccessCounter = 0
ErrorCounter = 0
os.system('cls')

print(Fore.WHITE + Style.BRIGHT + 'Server ID:')
try:
    ServerID = int(input(Fore.GREEN + '> ' + Fore.WHITE + Style.BRIGHT))
except ValueError as e:
    print(' ')
    print(Fore.RED + '[ERROR] ' + Fore.WHITE + Style.BRIGHT + str(e))
    input()
    quit()
print(Fore.WHITE + Style.BRIGHT + '\nToken:')
token = str(input(Fore.GREEN + '> ' + Fore.WHITE + Style.BRIGHT))
print(' ')

def ChangeNickname():
    global SuccessCounter
    global ErrorCounter
    try:
        session = requests.Session()
        headers = {
            'authorization': token,
            'content-type': 'application/json',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
        }
        nicknames = ['jokers', 'https://github.com/jokersxd', 'Hello world!', 'abc', '123']
        data = '{"nick":"' + random.choice(nicknames) + '"}'
        r = session.patch('https://discord.com/api/v6/guilds/' + str(ServerID) + '/members/%40me/nick', headers=headers, data=data)
        if 'nick' in r.text:
            try:
                print(Fore.GREEN + '[SUCCESS] ' + Fore.WHITE + Style.BRIGHT + 'Nickname: ' + r.text.split('{"nick": "')[1].split('"}')[0])
                SuccessCounter += 1
                ctypes.windll.kernel32.SetConsoleTitleW('Discord Nickname Changer | Success: ' + str(SuccessCounter) + ' | Errors: ' + str(ErrorCounter))
            except IndexError:
                print(Fore.RED + '[ERROR] ' + Fore.WHITE + Style.BRIGHT + 'list index out of range')
                ErrorCounter += 1
                ctypes.windll.kernel32.SetConsoleTitleW('Discord Nickname Changer | Success: ' + str(SuccessCounter) + ' | Errors: ' + str(ErrorCounter))
        elif 'You are being rate limited.' in r.text:
            print(Fore.RED + '[ERROR] ' + Fore.WHITE + Style.BRIGHT + 'Ratelimited')
            ErrorCounter += 1
            ctypes.windll.kernel32.SetConsoleTitleW('Discord Nickname Changer | Success: ' + str(SuccessCounter) + ' | Errors: ' + str(ErrorCounter))
        elif 'Unauthorized' in r.text:
            print(Fore.RED + '[ERROR] ' + Fore.WHITE + Style.BRIGHT + 'Improper token has been passed.')
            ErrorCounter += 1
            ctypes.windll.kernel32.SetConsoleTitleW('Discord Nickname Changer | Success: ' + str(SuccessCounter) + ' | Errors: ' + str(ErrorCounter))
        elif 'Unknown Guild' in r.text:
            print(Fore.RED + '[ERROR] ' + Fore.WHITE + Style.BRIGHT + 'Invalid Server ID')
            ErrorCounter += 1
            ctypes.windll.kernel32.SetConsoleTitleW('Discord Nickname Changer | Success: ' + str(SuccessCounter) + ' | Errors: ' + str(ErrorCounter))
        elif 'Unknown Member' in r.text:
            print(Fore.RED + '[ERROR] ' + Fore.WHITE + Style.BRIGHT + 'Member not inside of guild')
            ErrorCounter += 1
            ctypes.windll.kernel32.SetConsoleTitleW('Discord Nickname Changer | Success: ' + str(SuccessCounter) + ' | Errors: ' + str(ErrorCounter))
        elif 'Missing Permissions' in r.text:
            print(Fore.RED + '[ERROR] ' + Fore.WHITE + Style.BRIGHT + "Member doesn't have permissions to change nickname")
            ErrorCounter += 1
            ctypes.windll.kernel32.SetConsoleTitleW('Discord Nickname Changer | Success: ' + str(SuccessCounter) + ' | Errors: ' + str(ErrorCounter))
        else:
            print(r.text)
    except:
        pass
    time.sleep(1)

while True:
    ChangeNickname()
