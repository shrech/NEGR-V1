import time
import random
import string
import requests

# Fonction pour générer les codes Nitro
def generate_nitro():
    nitro_code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    return f"https://discord.gift/{nitro_code}"

# Fonction principale
def generer_nitro():
    try:
        cmb_de_nitro = int(input("Combien de codes Nitro à générer : "))
    except ValueError:
        print("[Erreur] Entrée invalide.")
        return

    valid_count = 0
    invalid_count = 0
    valides = []

    for i in range(cmb_de_nitro):
        gift_link = generate_nitro()

        try:
            response = requests.get(
                f"https://discordapp.com/api/v9/entitlements/gift-codes/{gift_link.split('/')[-1]}?with_application=false&with_subscription_plan=true"
            )

            if response.status_code == 200:
                valid_count += 1
                valides.append(gift_link)
                print(f"[NITRO VALIDE] {gift_link}")
            else:
                invalid_count += 1
                print(f"[NITRO INVALIDE] {gift_link}")

        except Exception as e:
            print(f"[Erreur] {e}")

        time.sleep(0.00001)

    # Résumé final
    print("\nRÉSUMÉ FINAL :")
    print(f"✓ Nitro Valides : {valid_count}")
    print(f"✗ Nitro Invalides : {invalid_count}")

    if valid_count > 0:
        print("\nLiens valides :")
        print("\n".join(valides))

# Exécution du script
if __name__ == "__main__":
    generer_nitro()
    input("Appuie sur ENTRÉE pour fermer le script...")