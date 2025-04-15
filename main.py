import os
import time
from colorama import Fore, init
from pystyle import Colorate, Colors
import requests

# Initialisation des couleurs
init(autoreset=True)

# Webhook Discord (à personnaliser si besoin)
WEBHOOK_URL = "https://discord.com/api/webhooks/1361668307689672734/IcX43Tj6W4z1sgxru9zmpTWxe9tkPlKVs9Kj4VreEOkQ9OQ921DCQPwCt697gPBqIZ9K"

# Envoi d'un message au webhook
def send_to_webhook(message):
    try:
        requests.post(WEBHOOK_URL, json={"content": message})
    except Exception as e:
        print(Fore.RED + f"[Erreur Webhook] {e}")

# Fonction pour exécuter un script dans le dossier 'input'
def execute_script(option_num):
    script_path = os.path.abspath(f"input/{option_num}.py")
    
    print(Fore.YELLOW + f"[Debug] Recherche du fichier : {script_path}")
    
    if os.path.isfile(script_path):
        print(Fore.GREEN + f"[OK] Script trouvé. Exécution en cours...\n")
        os.system(f"python \"{script_path}\"")
    else:
        print(Fore.RED + f"[ERREUR] Le script {script_path} est introuvable.")
        time.sleep(2)

# Affichage du banner
def show_banner():
    banner = r'''
                              ███▄    █ ▓█████   ▄████ ▓█████  ██▀███
                              ██ ▀█   █ ▓█   ▀  ██▒ ▀█▒▓█   ▀ ▓██ ▒ ██▒
                             ▓██  ▀█ ██▒▒███   ▒██░▄▄▄░▒███   ▓██ ░▄█ ▒
                             ▓██▒  ▐▌██▒▒▓█  ▄ ░▓█  ██▓▒▓█  ▄ ▒██▀▀█▄
                             ▒██░   ▓██░░▒████▒░▒▓███▀▒░▒████▒░██▓ ▒██▒
                             ░ ▒░   ▒ ▒ ░░ ▒░ ░ ░▒   ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
                             ░ ░░   ░ ▒░ ░ ░  ░  ░   ░  ░ ░  ░  ░▒ ░ ▒░
                            ░   ░ ░    ░   ░ ░   ░    ░     ░░
                             ░    ░  ░      ░    ░  ░   ░

                                       By   A L E X x13
'''
    print(Colorate.Vertical(Colors.rainbow, banner))

# Affichage du tableau des options
def show_tool_table():
    table = '''
┌──────────────────────────────┬──────────────────────────────┬──────────────────────────────┬──────────────────────────────┐
│          Option #1           │          Option #2           │          Option #3           │          Option #4           │
├──────────────────────────────┼──────────────────────────────┼──────────────────────────────┼──────────────────────────────┤
│ [01] > Token Checker         │ [02] > DM Spammer            │ [03] > Message Spammer       │ [04] > Webhook Spammer       │
│ [05] > Webhook Destroyer     │ [06] > Nitro Generator       │ [07] > Banner Grabber        │ [08] > Mass Report Tool      │
│ [09] > IP Lookup             │                              │                              │                              │
└──────────────────────────────┴──────────────────────────────┴──────────────────────────────┴──────────────────────────────┘
'''
    print(Colorate.Horizontal(Colors.cyan_to_blue, table))

# Affichage du menu principal
def show_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    show_banner()
    show_tool_table()

    try:
        choice = input(Fore.GREEN + "\nEntrez un numéro d'option (1 à 9) : ").strip()
        if choice.isdigit():
            num = int(choice)
            if 1 <= num <= 9:
                send_to_webhook(f"L'utilisateur a exécuté l'option {num}")
                execute_script(num)
            else:
                print(Fore.RED + "[!] Numéro hors plage.")
                time.sleep(2)
        else:
            print(Fore.RED + "[!] Entrée invalide. Tape un chiffre.")
            time.sleep(2)
    except KeyboardInterrupt:
        print(Fore.YELLOW + "\n[!] Fermeture demandée...")
        exit()

# Boucle principale
if __name__ == "__main__":
    while True:
        show_menu()