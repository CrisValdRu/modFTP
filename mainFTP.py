from ftp_client import getArchivoConfig, setArchivoConfig, deleteOld
from ssh_client import reboot
import filecmp

repetir = True
while repetir:
    print('------------FTP Cliente------------'
        '\nSelecciona un valor:\n'
        '1) Extraer configuracion\n'
        '2) Mover archivos de configuracion\n'
        '3) Importar configuracion\n'
        '4) Comparar configuraciones\n'
        '5) Borrar configuraciones\n'
        '6) Copiar la configuracion de inicio a la configuracion en ejecucion')
    
    opcion=int(input())
    """print('Ingresa direccion ip del servidor')
    ip=input()
    print('Ingresa usuario')
    usuario=input()
    print('Ingresa el password')
    password=input()
    """
    usuario="archivos_user"
    password="123456"
    ip="localhost"
    
    if(opcion==1):
        getArchivoConfig(ip,usuario,password)
    elif(opcion==2):
        setArchivoConfig(ip,usuario,password)
    elif(opcion==3):
        setArchivoConfig(ip,usuario,password)
        reboot(ip, usuario, password)
    elif(opcion==4):
        with open('archivos/archivos_user_r1.startup-config', 'r') as file1:
            with open('archivos/ospf-R1.startup-config.txt', 'r') as file2:
                with open ("archivos/diff.txt", "w") as out_file:
                    f2_lines = set(file2)
                    for line in file1:
                        if line not in f2_lines:
                            print(line)
                            out_file.write(line)
                            f2_lines.add(line)   
    elif(opcion==5):
        deleteOld(ip, usuario, password)  
    else:
        print("aun no se programa el else")   
    print("Desea hacer otra operacion? Y/N: ")
    res=input()
    if(res=='Y' or res=='y' or res=="Yes"):
        repetir=True
    else:
        repetir=False
