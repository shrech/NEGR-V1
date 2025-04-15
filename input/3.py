import requests
import time

def spam_message(token, channel_id, message):
    url = f"https://discordapp.com/api/v9/channels/{channel_id}/messages"
    headers = {
        "Authorization": token
    }
    payload = {
        "content": message
    }
    while True:
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 200:
            print("[+] Message envoyé avec succès.")
        else:
            print(f"[-] Erreur : {response.status_code}")
        time.sleep(1)

token = input("Entrez votre token Discord : ")
channel_id = input("Entrez l'ID du canal cible : ")
message = input("Entrez le message à envoyer : ")
spam_message(token, channel_id, message)