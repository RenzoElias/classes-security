# Saber los nombres de wifi y la clave usados en el sistema
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