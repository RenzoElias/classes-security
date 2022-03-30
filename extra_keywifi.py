##########################################################################################
# Python saber los dispositivos conectados y la clave a internet red
# https://stackoverflow.com/questions/12468179/unicodedecodeerror-utf8-codec-cant-decode-byte-0x9c
# https://www.youtube.com/watch?v=DBO1zJ4Yn7M&ab_channel=mringsanjuan
# https://www.youtube.com/watch?v=uApzI7TnX7E&ab_channel=RogerBiderbost

import subprocess 
import os

data = subprocess.check_output(["netsh", "wlan", "show", "profiles"]).decode('utf-8').split('\n')

profiles = [i.split(":")[1][1:-1] for i in data if "Perfil de todos los usuarios" in i]

# print(profiles)
print("{:<30}| {:<}".format('Red wifi', 'Contraseñas'))

for i in profiles:
    results = subprocess.check_output(["netsh", "wlan", "show", "profiles", i, "key=clear"]).decode('latin1').split('\n')
    # print(results)
    results = [a.split(":")[1][1:-1] for a in results if "Contenido de la clave" in a]
    
    try:
        print("{:<30}| {:<}".format(i, results[0]))
    except IndexError:
        print("{:<30}| {:<}".format(i, ""))

input('Presiona cualquier tecla.....')