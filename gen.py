import time, os
start = time.perf_counter()
os.system('cls')
from colorama import Fore
import threading,requests,random,ctypes
from dhooks import Webhook

class GenNitroCode():
    def __init__(self):
        self.nitroCode = ''
        char = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        for i in range(16):
            self.nitroCode = self.nitroCode + random.choice(char)

def getWebhook():
    with open("webhook-link.txt", "r") as webhook:
        result = webhook.read()
        webhook.close()
    return result

def getProxies():
    r = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=5000&ssl=yes')
    proxies = []
    for proxy in r.text.split('\n'):
        proxy = proxy.replace('\r', '')
        if proxy:
            proxies.append(proxy)
    return proxies

def testNitroCodes():
    webhook = getWebhook()
    if webhook == "None":
        usingWebhook = False
    else:
        usingWebhook = True
    testedCodes = 0
    for i in range(3):
        ProxyList = getProxies()
        for proxy in ProxyList:
            ProxyParameters ={'http://': proxy,'https://': proxy}
            for i in range(3):
                nitrocode = GenNitroCode()
                url = requests.get(f"https://discordapp.com/api/v6/entitlements/gift-codes/{nitrocode.nitroCode}", proxies=ProxyParameters, timeout=5)
                if url.status_code == 200:
                    if usingWebhook == True:
                        hook = Webhook(webhook)
                        hook.send(content=f"@everyone nitro is ready https://discord.gift/{nitrocode.nitroCode}")
                    with open('nitroCodes.txt', 'w') as nitros:
                        nitros.write(nitrocode.nitroCode)
                        nitros.close()
                    print(f"{Fore.WHITE}[{Fore.GREEN}!{Fore.WHITE}] {Fore.GREEN}VALID CODE{Fore.WHITE} : https://discord.gift/{nitrocode.nitroCode}")
                print(f"{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}] {Fore.RED}INVALID CODE{Fore.WHITE} : https://discord.gift/{nitrocode.nitroCode}")
                testedCodes += 1
    with open('testedCodes.txt', 'r+', encoding="utf8") as file:
        count = file.read()
        newCount = int(count) + testedCodes
        file.close()

    with open('testedCodes.txt', 'w', encoding="utf8") as file:
        file.write(str(newCount))
        file.close()
    testNitroCodes()

def main(start):
    ctypes.windll.kernel32.SetConsoleTitleA("Nitro generator")
    print(f"""{Fore.MAGENTA}
    _   ________________  ____     _____________   __
   / | / /  _/_  __/ __ \/ __ \   / ____/ ____/ | / /
  /  |/ // /  / / / /_/ / / / /  / / __/ __/ /  |/ / 
 / /|  // /  / / / _, _/ /_/ /  / /_/ / /___/ /|  /  
/_/ |_/___/ /_/ /_/ |_|\____/   \____/_____/_/ |_/   
                                                     
    """)
    finished = time.perf_counter()
    timeToLoad = finished-start
    print(f"PROGRAM CHARGÉ EN {timeToLoad}s...\n")
    print("[ Threads : 1 - 200 | à partir de 25 attention cpu ]\n")
    print("[ Veux tu recevoir le code avec un webhook (Y/N) ? ]\n")
    webhook = str(input('-> '))
    if webhook == "Y":
        webhooklink = str(input('Webhook link => '))
        webhookExample = 'https://discord.com/api/webhooks/'
        if webhookExample in webhooklink:
            with open('webhook-link.txt', 'w') as webhookFile:
                webhookFile.write(webhooklink)
                webhookFile.close()
        else:
            print('Il y a un problème avec ton webhook.')
            time.sleep(1)
            os.system('cls')
            main(start)
    elif webhook == "N":
        with open('webhook-link.txt', 'w') as webhookFile:
            webhookFile.write("None")
            webhookFile.close()
    else:
        print(f'{Fore.RED}[!] Ta demande est invalide !')
        time.sleep(1)
        os.system('cls')
        main(start)

    try:
        threads = int(input('Threads => '))
        if threads <= 200:
            for i in range(threads):
                thread = threading.Thread(target=testNitroCodes)
                thread.start()
        else:
            print(f'{Fore.RED}[!] Ta demande est invalide !')
            time.sleep(1)
            os.system('cls')
            main(start)
    except ValueError:
        os.system('cls')
        main(start)

main(start)