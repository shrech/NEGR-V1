import requests

def delete_webhook(webhook_url):
    response = requests.delete(webhook_url)
    if response.status_code == 204:
        print("[+] Webhook supprimé avec succès.")
    else:
        print(f"[-] Erreur : {response.status_code}")

webhook_url = input("Entrez l'URL du webhook à supprimer : ")
delete_webhook(webhook_url)