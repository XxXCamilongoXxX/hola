import os
import time
import msvcrt
gentuza=[]
while True:
    print("menusito")
    print("1) Inicio sesion\n2) Registrar usuario\n3)Eliminar usuario\n4) Salir")
    opc = int(input("Eliga opción: "))
    if opc==1:
        pass
    elif opc==2:
        print("Registro :3")
        non = input("Ingrese su nombre de usuario: ")
        con = input("Ingrese su contraseña: ")
        usuario ={
            "Nombre": non,
            "Contrasena": con,}
        gentuza.append(usuario)
        print("Wena papu estas registrado como un papu")
    elif opc==3:
        pass
    else:
        print("CHAO TONTO")
        time.sleep(3)
        os.system('cls')
