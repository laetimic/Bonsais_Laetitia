# scripts/send_update_email.py
import smtplib
from email.mime.text import MIMEText
import os
from datetime import datetime

# Récupérer les variables d'environnement (passées par GitHub Actions)
commit_hash = os.getenv('COMMIT_HASH', 'N/A')
commit_message = os.getenv('COMMIT_MESSAGE', 'N/A')
repo_name = os.getenv('REPO_NAME', 'N/A')
commit_url = f"https://laetimic.github.io/Bonsais_Laetitia/"

# Contenu de l'email
sujet = f"🚀 Mise à jour du site {repo_name} - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
corps = f"""
Coucou,

Ton site internet Bonsai a été mis à jour aujourd'hui !

📅 **Date/Heure** : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
🔗 **Commit** : {commit_message}
🔢 **Hash** : {commit_hash}
🌐 **Lien** : {commit_url}

Gros Bisous

Mimi
"""

# Configuration de l'email
msg = MIMEText(corps)
msg['Subject'] = sujet
msg['From'] = os.getenv('SMTP_USER')
msg['To'] = os.getenv('EMAIL_TO')
msg['Bcc'] = os.getenv('SMTP_USER')



# Envoi de l'email
try:
    with smtplib.SMTP(os.getenv('SMTP_SERVER'), int(os.getenv('SMTP_PORT'))) as server:
        server.starttls()
        server.login(os.getenv('SMTP_USER'), os.getenv('SMTP_PASSWORD'))
        server.send_message(msg)
        print("✅ Email de mise à jour envoyé avec succès !")
except Exception as e:
    print(f"❌ Erreur lors de l'envoi : {e}")