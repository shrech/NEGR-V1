import requests

def ip_lookup(ip_address, webhook_url):
    try:
        # Utilisation de l'API ipinfo.io pour obtenir des détails sur l'adresse IP
        url = f"https://ipinfo.io/{ip_address}/json"
        response = requests.get(url)
        data = response.json()

        # Vérification si la réponse contient des informations valides
        if response.status_code == 200:
            # Extraction des informations
            ip_info = {
                "IP": data.get('ip'),
                "Ville": data.get('city', 'Inconnue'),
                "Région": data.get('region', 'Inconnue'),
                "Pays": data.get('country', 'Inconnu'),
                "Organisation": data.get('org', 'Inconnu'),
            }
            
            # Extraction des coordonnées géographiques (latitude, longitude)
            loc = data.get('loc', 'Inconnue')
            if loc != 'Inconnue':
                latitude, longitude = loc.split(',')
                ip_info["Latitude"] = latitude
                ip_info["Longitude"] = longitude
                # Ajouter un lien vers Google Maps
                ip_info["Google Maps"] = f"https://www.google.com/maps?q={latitude},{longitude}"
            else:
                ip_info["Coordonnées géographiques"] = "Inconnues"

            # Préparation du message à envoyer au webhook Discord
            message = "\n".join([f"{key}: {value}" for key, value in ip_info.items()])
            
            # Changer le nom du webhook sur Discord et envoyer le message
            webhook_data = {
                "content": message,
                "username": "IP Info"
            }
            
            # Envoi du message via le webhook
            response = requests.post(webhook_url, json=webhook_data)
            
            if response.status_code == 204:
                print("Informations envoyées avec succès au webhook Discord.")
            else:
                print(f"Erreur lors de l'envoi des données au webhook. Status code: {response.status_code}")
        else:
            print("Erreur : Impossible de récupérer les données pour cette IP.")
    except Exception as e:
        print(f"Erreur lors de l'exécution de la recherche IP : {str(e)}")

def main():
    print("[14] > IP Lookup")
    ip_address = input("Entrez l'adresse IP à rechercher : ")
    webhook_url = input("Entrez l'URL du Webhook Discord : ")
    ip_lookup(ip_address, webhook_url)
    message = "IP Lookup exécuté avec succès !"
    print(message)

if __name__ == "__main__":
    main()