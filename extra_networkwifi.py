import os
import threading
# Saber los IP dispositivos conectados a la red
# https://www.youtube.com/watch?v=spGUEdavm1Y&ab_channel=JULIANGUILLERMOZAPATARUGELES

def search(ip_adress):
    comando="ping -c 1 "+ip_adress
    response=os.popen(comando).read()
    # print(response)
    if "perdidos = 0" in response:
        print("Encontrado en : ", ip_adress)


for ip in range(1,254):
    current_ip="192.168.10."+str(ip)
    # print("Analizando la ip: ", current_ip)
    # search(current_ip)
    
    run= threading.Thread(target=search, args = (current_ip,))
    run.start()
    

    