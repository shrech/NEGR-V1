import requests
import json

WEBHOOK_URL = "https://discord.com/api/webhooks/TON_WEBHOOK_ICI"

def send_to_webhook(message):
    try:
        requests.post(WEBHOOK_URL, json={"content": message})
    except Exception as e:
        print(f"[Webhook Error] {e}")

def check_token(token):
    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }

    response = requests.get("https://discord.com/api/v9/users/@me", headers=headers)

    if response.status_code == 200:
        user = response.json()
        user_info = (
            f"✅ Token Valide\n"
            f"👤 Utilisateur: {user.get('username')}#{user.get('discriminator')}\n"
            f"🆔 ID: {user.get('id')}\n"
            f"📧 Email: {user.get('email')}\n"
            f"📱 Téléphone: {user.get('phone')}\n"
            f"🌍 Locale: {user.get('locale')}\n"
            f"🔐 2FA Activé: {user.get('mfa_enabled')}\n"
        )
        print(user_info)
        send_to_webhook(user_info)
        return True
    else:
        print("❌ Token invalide ou expiré.")
        return False

def main():
    print("[01] > Discord Token Checker")
    token = input("🔑 Entrez le token à vérifier : ").strip()

    if check_token(token):
        print("✔️ Token valide !")
    else:
        print("❌ Token invalide.")

if name == "main":
    main()