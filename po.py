import csv
import os
from dotenv import load_dotenv
from email.message import EmailMessage
import ssl
import smtplib
from tkinter import Tk
from tkinter import filedialog

# Cargar las variables de entorno
load_dotenv()
email_sender = "santiingles28@gmail.com"
password = os.getenv("PASSWORD")

subject = "Correo con adjuntos seleccionados manualmente"
body = "Este correo contiene los archivos que seleccionaste desde tu PC."

# Obtener correos destinatarios desde CSV
def obtener_correos_destinatarios(archivo_csv):
    correos = []
    with open(archivo_csv, mode="r") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            correos.append(row["Emails"])
    return correos

emails_destinatarios = obtener_correos_destinatarios("emails.csv")

# Seleccionar archivos a adjuntar
def seleccionar_archivos():
    root = Tk()
    root.withdraw()  # Ocultar ventana principal
    archivos = filedialog.askopenfilenames(title="Selecciona los archivos a enviar")
    return archivos

# Obtener lista de archivos adjuntos desde la GUI
archivos_adjuntos = seleccionar_archivos()

# Enviar los correos
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(email_sender, password)

    for email_reciver in emails_destinatarios:
        em = EmailMessage()
        em["From"] = email_sender
        em["To"] = email_reciver
        em["Subject"] = subject
        em.set_content(body)

        for ruta in archivos_adjuntos:
            with open(ruta, "rb") as f:
                datos = f.read()
                nombre_archivo = os.path.basename(ruta)
                tipo = "application"
                subtipo = "octet-stream"
                # Opcional: podrías detectar el tipo MIME con mimetypes

                em.add_attachment(datos, maintype=tipo, subtype=subtipo, filename=nombre_archivo)

        smtp.sendmail(email_sender, email_reciver, em.as_string())
        print(f"Correo enviado a {email_reciver} con {len(archivos_adjuntos)} archivos adjuntos.")
