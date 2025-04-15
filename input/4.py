import requests
import time

def spam_webhook(webhook_url, message):
    while True:
        response = requests.post(webhook_url, json={"content": message})
        if response.status_code == 204:
            print("[+] Message envoyé au webhook.")
        else:
            print(f"[-] Erreur : {response.status_code}")
        time.sleep(1)

webhook_url = input("Entrez l'URL du webhook : ")
message = input("Entrez le message à envoyer : ")
spam_webhook(webhook_url, message)