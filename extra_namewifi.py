##########################################################################################3
# EXTRAE LAS REDES QUE SE HA CONECTADO LA PC
import subprocess 
  
meta_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']) 
  
data = meta_data.decode('utf-8', errors ="backslashreplace") 
  
data = data.split('\n') 
  
names = [] 
  
for i in data: 
      
    # print("i ", i) 
    if "Perfil de todos los usuarios" in i : 
        i = i.split(":") 
        i = i[1] 
        i = i[1:-1] 
        names.append(i) 
  
print("All wifi that system has connected to are ") 
print("-----------------------------------------") 
for name in names: 
    print(name) 

##########################################################################################

# # LanIpScan.py
# import netifaces
# import nmap
 
# class LanIpScan:
#     # Obtener puerta de enlace
#     def get_gateways(self):
#         return netifaces.gateways()['default'][netifaces.AF_INET][0]
#                  # Obtenga la dirección de la puerta de enlace local, aquí devuelve 192.168.1.1
 
#         # return dict(dict(netifaces.gateways())['default'])[2][0]
#                  # Este método no se recomienda porque el módulo ha definido algunas constantes y usos específicos
 
#          # Obtener IP
#     def get_ip_lists(self, gateway):
#         ip_lists = []
#         for i in range(1, 256):
#             ip_lists.append('{}{}'.format(gateway[:-1], i))
#                          # Cambie los últimos datos de la puerta de enlace y agréguelos a la lista
#         return ip_lists
#                  # Volver a la lista ['192.168.1.1', -> '192.168.1.255']
 
#          # Ver dirección IP
#     def scan_ip_survial(self, ip):
#         nmScan = nmap.PortScanner()
#         nmScan.scan(hosts=ip, arguments='-sP')
#         try:
#            nmScan[ip]
#            return {'ScanInfo:': nmScan[ip]}
#         except:
#            print("Esta dirección IP no es válida : ", ip)
#             # KeyError
#             #              devuelve "Esta dirección IP no es válida", ip
 
#          # Obtener información del dispositivo
#     def get_all_devices(self, ip_lists):
#         survial_devices = []
#         for ip in ip_lists:
#             scan_result = LanIpScan.scan_ip_survial(ip)
#             if scan_result:
#                 survial_devices.append(scan_result)
#                 print(scan_result)
#         return survial_devices
 
# if __name__ == '__main__':
#     LanIpScan = LanIpScan()
#     gateway = LanIpScan.get_gateways()
#     ip_lists = LanIpScan.get_ip_lists(gateway)
#     LanIpScan.get_all_devices(ip_lists)
##########################################################################################

# import os,subprocess

# def main():
#  miDireccion = raw_input("ip privada>> ")

#  for p in range(0,256):
#   ip = '192.168.1.'+str(p)

#   saver = open('temp.txt','w')
#   subprocess.call(['ping','-n','1',ip],stdout=saver)
#   saver.close()

#   leerSaver = open('temp.txt','r')
#   linea = leerSaver.readlines()

#   estado = linea[2]

#   wrong = "Reply from "+ miDireccion +": Destination host unreachable.\n"

#   if estado == wrong:
#    pass
#   else:
#    data = "[+] El host " + ip + " se encuentra activo.\n"
#    dataSaver = open('hostActivos.txt','a')
#    dataSaver.write(data)
#    dataSaver.close()

#    print(data)
   
# main()

################################################################################
# #! py
# ######################################
# #Copyright of David Bombal, 2021     #
# #https://www.davidbombal.com         #
# #https://www.youtube.com/davidbombal #
# ######################################

# #    Import subprocess so we can use system commands.
# import subprocess

# #    Import the re module so we can make use of regular expressions. 
# import re

# #    Python allows us to run system commands using the function 
# #    provided by the subprocess module; 
# #    (subprocess.run(<list of command line arguments go here>, <specify the second argument if you want to capture the output>)).
# #
# #    This script is a parent process that creates a child process which 
# #    runs a system command and will only continue once the child process 
# #    is completed. 
# #
# #    To save the contents that get sent to the standard output stream 
# #    (the terminal), we must first specify that we want to capture the output.
# #    To do this we specify the second argument as capture_output = True. 
# #    This information gets stored in the stdout attribute as bytes and 
# #    needs to be decoded before being used as a String in Python.
# command_output = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output = True).stdout.decode()

# #    We imported the re module to make use of regular expressions. 
# #    We want to find all the wifi names which are listed after 
# #    "ALL User Profile     :". Using regular expressions we can create 
# #    a group of all characters until the return escape sequence (\r) appears.
# profile_names = (re.findall("Perfil de todos los usuarios     : (.*)\r", command_output))

# #    We create an empty list outside of the loop where dictionaries 
# #    containing all the wifi usernames and passwords will be saved.
# wifi_list = []

# #    If any profile names are not found this means that wifi connections 
# #    have also not been found. So we run this part to check the 
# #    details of the wifi and see whether we can get their passwords.
# if len(profile_names) != 0:
#     for name in profile_names:
#         #    Every wifi connection will need its own dictionary which 
#         #    will be appended to the variable wifi_list.
#         wifi_profile = {}
#         #    We can now run a more specific command to see the information 
#         #    about the wifi connection and if the Security key
#         #    is not absent it may be possible to get the password.
#         profile_info = subprocess.run(["netsh", "wlan", "show", "profile", name], capture_output = True).stdout.decode()
#         #    We use the regular expression to only look for the absent cases so we can ignore them.
#         if re.search("Security key           : Absent", profile_info):
#             continue
#         else:
#             #    Assign the ssid of the wifi profile to the dictionary.
#             wifi_profile["ssid"] = name
#             #    These cases aren't absent and we should run the 
#             #    "key=clear" command part to get the password.
#             profile_info_pass = subprocess.run(["netsh", "wlan", "show", "profile", name, "key=clear"], capture_output = True).stdout.decode()
#             #    Again run the regular expression to capture the 
#             #    group after the : (which is the password).
#             password = re.search("Key Content            : (.*)\r", profile_info_pass)
#             #    Check if we found a password using the regular expression. 
#             #    Some wifi connections may not have passwords.
#             if password == None:
#                 wifi_profile["password"] = None
#             else:
#                 #    We assign the grouping (where the password is contained) that 
#                 #    we are interested in to the password key in the dictionary.
#                 wifi_profile["password"] = password[1]
#             #    We append the wifi information to the variable wifi_list.
#             wifi_list.append(wifi_profile) 

# for x in range(len(wifi_list)):
#     print(wifi_list[x]) 