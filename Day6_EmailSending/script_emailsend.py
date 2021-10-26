import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import pandas as pd


lista = pd.read_csv('nombres.csv', encoding = 'cp1252')

remitente = 'correo@dominio'
contra = 'XXXXXXXXX'
asunto = 'AsuntoXXX'

for i in lista.index: 
    print(lista["Fichero"][i])
    cuerpo = 'TEXTO TEXTO TEXTO otorga el certificado de aprobación al Sr(a/ita):' + lista["Nombre"][i] + ', y agradece su participación en el programa XXXXXXX'
    ruta_adjunto = 'certificados/' + lista["Fichero"][i]
    nombre_adjunto = lista["Fichero"][i]

    mensaje = MIMEMultipart()

    mensaje['From'] = remitente
    mensaje['To'] = lista["Email"][i]
    mensaje['Subject'] = asunto
 
    mensaje.attach(MIMEText(cuerpo, 'plain'))
     
    archivo_adjunto = open(ruta_adjunto, 'rb')
     
    adjunto_MIME = MIMEBase('application', 'octet-stream')
    adjunto_MIME.set_payload((archivo_adjunto).read())
    encoders.encode_base64(adjunto_MIME)
    adjunto_MIME.add_header('Content-Disposition', "attachment; filename= %s" % nombre_adjunto)
    mensaje.attach(adjunto_MIME)
     
    sesion_smtp = smtplib.SMTP('smtp.gmail.com', 587)
     
    sesion_smtp.starttls()
    
    sesion_smtp.login(remitente,contra) 
    
    texto = mensaje.as_string()
    sesion_smtp.sendmail(remitente, lista["Email"][i], texto)
    
    sesion_smtp.quit()
    

