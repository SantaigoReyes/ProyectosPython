import csv
import os
from dotenv import load_dotenv
from email.message import EmailMessage
import ssl
import smtplib

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Correo del remitente y contraseña de aplicación
email_sender = "santiingles28@gmail.com"
password = os.getenv("PASSWORD")  # Asegúrate de que tengas configurada esta variable en .env

# Asunto y cuerpo del correo
subject = "Probando envío de email con python con Day3"
body = """
Aquí va el cuerpo de correo para verificar que las cosas hayan salido bien.
"""

# Función para obtener los correos desde un archivo CSV
def obtener_correos_destinatarios(archivo_csv):
    correos = []
    with open(archivo_csv, mode="r") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            correos.append(row["Emails"])  # Suponiendo que el CSV tiene una columna llamada "Emails"
        print(correos)
    return correos

# Leer los correos de los destinatarios
emails_destinatarios = obtener_correos_destinatarios("emails.csv")

# Crear objeto EmailMessage
em = EmailMessage()
em["From"] = email_sender
em["Subject"] = subject
em.set_content(body)

# Configurar el contexto de seguridad para enviar el correo
context = ssl.create_default_context()

# Conexión SMTP y envío de correos a todos los destinatarios
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(email_sender, password)

    for email_reciver in emails_destinatarios:
        em["To"] = email_reciver  # Asignar la dirección del destinatario
        smtp.sendmail(email_sender, email_reciver, em.as_string())  # Enviar el correo
        print(f"Correo enviado a {email_reciver}")
        break
