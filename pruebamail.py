import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


def SendMail():
    archivo = open("archivos/diff.txt", 'rb')
    msg = MIMEMultipart()
    msg['Subject'] = 'Evidencia 3'
    msg['From'] = 'cefriasm@gmail.com'
    msg['To'] = 'crissvr777@gmail.com'

    text = MIMEText("Grupo 4CM1 - Equipo 4")
    msg.attach(text)
    #msg.attach(archivo)
    # Creamos un objeto MIME base
    adjunto_MIME = MIMEBase('application', 'octet-stream')
    # Y le cargamos el archivo adjunto
    adjunto_MIME.set_payload((archivo).read())
    # Codificamos el objeto en BASE64
    encoders.encode_base64(adjunto_MIME)
    # Agregamos una cabecera al objeto
    adjunto_MIME.add_header('Content-Disposition', "attachment; filename= %s" % "diff.txt")
    # Y finalmente lo agregamos al mensaje
    msg.attach(adjunto_MIME)

    sender = "cefriasm@gmail.com"
    smtp_server_name = 'smtp.gmail.com'
    port = '587'

    if port == '465':
        s = smtplib.SMTP_SSL('{}:{}'.format(smtp_server_name, port))
    else:
        s = smtplib.SMTP('{}:{}'.format(smtp_server_name, port))
        s.starttls()
    
    s.login(sender, 'RedesSensuales')
    s.sendmail(msg['From'], msg['To'], msg.as_string())
    s.quit()

