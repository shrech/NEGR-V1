def generate_banner_url(user_id, banner_hash, webhook_url):
    if not banner_hash:
        print("⚠️ Aucun hash fourni. Impossible de générer la bannière.")
        return

    ext = "gif" if bannerhash.startswith("a") else "png"
    banner_url = f"https://cdn.discordapp.com/banners/%7Buser_id%7D/%7Bbanner_hash%7D.%7Bext%7D?size=1024"

    print(f"✅ URL de la bannière : {banner_url}")

    try:
        import requests
        requests.post(webhook_url, json={"content": f"🔗 Bannière de l'utilisateur {user_id} : {banner_url}"})
        print("✅ Envoyé au webhook !")
    except Exception as e:
        print(f"[Erreur Webhook] {e}")

def main():
    print("📥 Banner Grabber (sans token)")
    webhook = input("🔗 Entrez l'URL du webhook Discord : ").strip()
    user_id = input("🆔 Entrez l'ID de l'utilisateur : ").strip()
    banner_hash = input("🎨 Entrez le hash de la bannière (ex: a_123abc ou 456def) : ").strip()

    generate_banner_url(user_id, banner_hash, webhook)

if name == "main":
    main()