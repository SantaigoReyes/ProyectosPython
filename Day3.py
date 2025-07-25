import csv
import os
from dotenv import load_dotenv
from email.message import EmailMessage
import ssl
import smtplib
from tkinter import Tk
from tkinter import filedialog
# Cargar las variables de entorno desde el archivo .env
load_dotenv()


email_sender = "santiingles28@gmail.com"
password = os.getenv("PASSWORD")

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
            correos.append(row["Emails"])  # Llama a la columna Emails
        print(correos)
    return correos

# Leer los correos de los destinatarios
emails_destinatarios = obtener_correos_destinatarios("emails.csv")
def seleccionar_archivos():
    root = Tk()
    root.withdraw()
    archivos= filedialog.askopenfilenames(title="Seleccionar archivos para subir")
    return archivos
archivos_adjuntos = seleccionar_archivos()
# Configurar el contexto de seguridad para enviar el correo
context = ssl.create_default_context()
# Conexión SMTP y envío de correos a todos los destinatarios
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(email_sender, password)

    for email_reciver in emails_destinatarios:
        # Crear objeto EmailMessage
        em = EmailMessage()
        em["From"] = email_sender
        em["To"] = email_reciver  # Asignar la dirección del destinatario
        em["Subject"] = subject
        em.set_content(body) 

        for ruta in archivos_adjuntos:
            with open(ruta,"rb") as f:
                datos = f.read()
                nombre_archivo = os.path.basename(ruta)
                tipo = "application"
                subtipo ="octet-stream"


        smtp.sendmail(email_sender, email_reciver, em.as_string())  
        print(f"Correo enviado a {email_reciver} con {len(archivos_adjuntos)} archivos adjuntos")


