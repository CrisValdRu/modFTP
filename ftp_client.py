import ftplib
import sys
import os
import time

def getFile(ftp, filename, ip):
    try:
        ftp.retrbinary("RETR " + filename ,open("archivos/"+ip+"_"+filename, 'wb').write)
    except:
        print ("Error")

def upload(ftp, file):
    ext = os.path.splitext(file)[1]
    if ext in (".txt", ".htm", ".html"):
        ftp.storlines("STOR " + file, open(file))
    else:
        files = obtenerNombreArchivos(ftp)
        numArchivos=len(files)
        print(numArchivos)
        if(numArchivos==1):
            nombreArchivo="v1.startup-config"
        elif(numArchivos==2):
            nombreArchivo="v2.startup-config"
        elif(numArchivos==3):
            nombreArchivo="v3.startup-config"
        elif(numArchivos==4):
            nombreArchivo="v4.startup-config"
        elif(numArchivos==5):
            ftp.delete("v1.startup-config")
            ftp.rename("v2.startup-config","v1.startup-config")
            ftp.rename("v3.startup-config","v2.startup-config")
            ftp.rename("v4.startup-config","v3.startup-config")
            nombreArchivo="v4.startup-config"
        else:
            print("error hay más de 4 archivos")
        ftp.storbinary("STOR " + nombreArchivo, open(file, "rb"), 1024)
        ftp.storbinary("STOR " + "startup-config", open(file, "rb"), 1024)
        
        
        

def getArchivoConfig(ip,usuario,password):
    ftp = createFTP(ip,usuario,password)
    getFile(ftp,'startup-config',ip)
    ftp.quit()

def setArchivoConfig(ip,usuario,password):
    ftp = createFTP(ip,usuario,password)
    upload(ftp,"archivos/"+ip+"_startup-config")
    ftp.quit()

def deleteOld(ip, usuario,password):
    ftp = createFTP(ip,usuario,password)
    files = obtenerNombreArchivos(ftp)
    numArchivos=len(files)
    if(numArchivos==4):
        ftp.delete("v1.startup-config")
    elif(numArchivos==5):
        ftp.delete("v1.startup-config")
        ftp.delete("v2.startup-config")
    elif(numArchivos==6):
        ftp.delete("v1.startup-config")
        ftp.delete("v2.startup-config")
        ftp.rename("v3.startup-config","v1.startup-config")
    elif(numArchivos==7):
        ftp.delete("v1.startup-config")
        ftp.delete("v2.startup-config")
        ftp.rename("v3.startup-config","v1.startup-config")
        ftp.rename("v4.startup-config","v2.startup-config")
    else:
        print("directorio vacio")
    ftp.quit()

def createFTP(ip, usuario, password):
    directory="/home/"+usuario+"/Documentos"
    ftp = ftplib.FTP(ip)
    ftp.login(usuario, password)
    #ftp.cwd(directory)         # change directory to /home/user/Escritorio
    return ftp

def obtenerNombreArchivos(ftp):
    try:
        files = ftp.nlst()
    except resp:
        if str(resp) == "550 No files found":
            print( "No files in this directory")
        else:
            raise

    for f in files:
        print (f)
    return files