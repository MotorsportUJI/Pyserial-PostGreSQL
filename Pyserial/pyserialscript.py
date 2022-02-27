print()
print()
print()
print()
print("        MMMMMMMMMMMMMMMMMMMMMMWWMMMMMMMMMMMMMMMMMMMM        ")
print("     MMMMMMMMMMMMMMMMMMMMMMMMMWMWXNWMMMMMMMMMMMMMMMMMMM     ")
print("   MMMMMMMMMMMMMMMMMMMMMMWWWNOxxOXWWMMMMMMMMMMMMMMMMMMMMM   ")
print("   MMMMMMMMMMMMMMMMMMMMMWNOocldONXO0WMWMMMMMMMMMMMMMMMMMM   ")
print(" MMMMMMMMMMMMMMMWMMMMWKxl;,ckOkdc,,oOOkkOKNMMMMMMMMMMMMMMMM ")
print("MMMMMMMMMMMMMMMWWWNOl,.   .'..    .....;lkNMMMMWMMMMMMMMMMMM")
print("MMMMMMMMMMMMMWWX0x;..;ol'             .,cokXWMMMMMMMMMMMMMMM")
print("MMMMMMMMMMMWKo;..   .;;.                   .:dKWMMMMMMMMMMMM")
print("MMMMMMMNKKOl::.                               .:xXWWMMWWMMMM")
print("MMMMMMMk'.. ,lodo;.                  ..          .cdOKXWMMMM")
print("MMMMMMMK; ,d0KK0XXc                  .;'       .clccld0NMMMM")
print("MMMMMMMMKxxkO0xcc;.          .,;,.    .c:.      ,kNWWMWWMMMM       UJI MOTORSPORT ELECTRONIC DEPARTMENT ")
print("MMWX0OOkkxkKNx'.,coddol:'...,xXNNk,    ,lc'      .lXMMMMMMMM")
print("MMXxcclx0NNOc;o0WMMWWMMWNK0KNWMMMWk.   .col,       cXMMMMMMM                         by                 ")
print("WXOxxk0NWWN0kKWMMMMMMMMMWWMWXXWWMWd.   .:ool'       ;0WMMMMM")
print("WWWNWWWWWNNWMWWWNWWWMWWWWMMWk;;dXx.    .:oooc.  .c'  'kWMMMM       Victor, Jordi, Antonio, Luis, Ivan,  ")
print("MXl;xNWWx,,dNMWO;,oKk::0MMMMO. .,.     .ldodo'  '0Xkc,'oNMMM                   Izan and Mohamed         ")
print("Wd. lNWWl  :NMWd. ;O; .kMMMMk.         ;ddddd;  .kWWMWK0NMMM")
print("Wo  lWMNl  :NMWd. :k, .kMWMWd.        .oddddd:. .OMMMMMMMMMM")
print("Wl  'llc'  cOdl,  ck, .kMMMX:        .lddddddc. ,0MMMMMMMMMM")
print("Wd.........lx,...:0K:.,kWWWx.       .lxxxdddx:  cNMWMMMMMMMM        @motorsportuji ujimotorsport.uji.es ")
print(" NKKKK0K0K0XNK0KKNMWXKKKxO0,       ,oxxxxxxxd, .OWWWWMMMMMM ")
print("   MWXKXWNXXXXNXKKXXXXXOclc..,,,..:xkxdxkkxdo:,o0KXXXKKXX   ")
print("   MNK000K0O00K0kOKKOOOOx0l;OdcxkdOO0Ook000dx0KKkOK00kkKK   ")
print("     KN0KN0O0O00XKO0K00l;d;l0l:dxxKkddxOdkOdO0O0O00OOKK     ")
print("        XKOO000KXK0XNKk,ld:x0KKkddkKOdO0kkdx0O00OO0K        ")
print()
print()
print()
print()

#LECTURA DE LA SP32

import serial
import time 


#Te preguta que puerto quieres usar, y si no pones nada, coje el serial0 (default para la esp32)
def Puerto():

    Puerto = input("Que puerto estamos usando?: ")

    if Puerto == "" or Puerto ==  " ":
        Puerto = "/dev/serial0"

    return Puerto

#Te pregunta que baudrate quieres usar y si no pones nada, coje el 115200 que es el que usar la esp32
def baudRate():

    baudRate = input("Que baudrate quieres usar?: ")
    
    if baudRate == "" or baudRate == " ":
        baudRate = 115200

        return baudRate

    baudRate = int(baudRate)

    return baudRate
    
#Leo señal recibe los valores del puerto, los lee y decodifica en formato ASCII
#dev.readline lee y dev.decode decodifica
def leo_señal(dev):
    #Omitiendo lo anterior, podemos poner directamente:
    #cad = dev.readline().decode(ascii)

    cad = dev.readline()
    cad = cad.decode("ascii")

    return cad

#Simplemente imprimo los valores y los separo con una barra de asteriscos
#El time.sleep esta a 2 segundos para no saturar la impresión de datos
def imprimo_valores(cad):

    print("**********************************************************************************************************")
    print("*                                                                                                        *")
    print("*                                                                                                        *")
    print("*                                                                                                        *")
    print("*                                                                                                        *")
    print("*                                 Se está recibiendo lo siguiente:                                       *")
    print("*                                                                                                        *")
    print("*                                 {:>20}                                                                 *".format(cad))
    print("*                                                                                                        *") 
    print("*                                                                                                        *")
    print("*                                                                                                        *")
    print("*                                                                                                        *")
    print("* Created and Developed by UJI MotorSport Team Electronic Departament                                    *")
    print("**********************************************************************************************************")

    time.sleep(2)

#La función main que llama a las anteriores funciones 
def main():

    #Indico el puerto y el baudrate con serial.Serial.
    #ANOTACIÓN: EL BAUDRATE DE LA SP32 ES 115200, POR DEFECTO ES 9600 ASI QUE NO CAMBIAR

    puerto = Puerto()
    BaudRate = baudRate()
    
    dev = serial.Serial(puerto, baudrate = BaudRate)
    time.sleep(1)

    #BUCLE QUE PERMITE LA ENTRADA SUCCESCIVA DE DATOS EN TIEMPO REAL

    while True:

        lista = []
        for i in range(2):
            cad = leo_señal(dev)
            lista.append(cad)
            

        #imprimo_valores(cad)



main()
