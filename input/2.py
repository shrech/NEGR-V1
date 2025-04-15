import requests
import time

def spam_dm(token, user_id, message):
    url = f"https://discordapp.com/api/v9/users/{user_id}/messages"
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
user_id = input("Entrez l'ID de l'utilisateur cible : ")
message = input("Entrez le message à envoyer : ")
spam_dm(token, user_id, message)