import time
import random

class MassReportSimulator:
    def init(self, user_id):
        self.user_id = user_id
        self.reports = 0
        self.start_time = time.time()

    def report_user(self):
        """Simule l'envoi automatique d'un rapport toutes les 5 secondes."""
        current_time = time.time()

        # Si plus de 5 rapports ont été envoyés dans les 60 secondes, avertir
        if self.reports >= 5 and current_time - self.start_time < 60:
            print(f"⚠️ Alerte : L'utilisateur {self.user_id} tente d'envoyer un trop grand nombre de rapports dans une période courte.")
            self.prevent_report()
        else:
            print(f"✅ Rapport envoyé automatiquement par {self.user_id}.")
            self.reports += 1
            # Vérifier si le seuil de rapports est dépassé
            if self.reports >= 5:
                print("⚠️ Alerte : L'utilisateur a atteint la limite de rapports dans la fenêtre de 60 secondes.")

    def prevent_report(self):
        """Simule l'empêchement d'un rapport massif."""
        print(f"❌ Rapport rejeté pour l'utilisateur {self.user_id}. L'automatisation est détectée.")

    def run_auto_reporting(self):
        """Lance l'automatisation des rapports à intervalles réguliers."""
        while True:
            self.report_user()
            time.sleep(5)  # Attente de 5 secondes avant d'envoyer le prochain rapport

def main():
    print("[⚔️] Mass Report")

    # Demander l'ID de l'utilisateur
    user_id = input("Entrez l'ID : ").strip()
    simulator = MassReportSimulator(user_id)

    print("Démarrage de l'envoi automatique de rapports...")

Démarrer le processus d'envoi automatique de rapports
    simulator.run_auto_reporting()

if name == "main":
    main()