#Este codigo se encarga de encontrar los subdominios de un sitio web

import requests

def responde(url):
    try:
        return requests.get(url)
    except requests.exceptions.ConnectionError:
        pass

lista=[]
objetivo_url="google.com"
with open('doc/sub_dominioList.txt') as file:
    for dicc in file.readlines():
        palabras=dicc.strip()
        #print(palabras)
        new_url=palabras + "." + objetivo_url
      
        datos = responde("http://"+new_url)

        if (datos):
            lista.append(new_url)
            print("Subdominio encontrado: " + new_url ) 
        else:
          pass  #print("Subdominio NO encontrado " + new_url)


print(lista)
with open('doc/subdominios_Encontrados.txt', 'a') as datos_guardado:
 for subdoLista in lista:
     datos_guardado.write( subdoLista + "\n" )

print(datos_guardado)

#####################################################################3

# #Este codigo se encarga de encontrar los directorios de un sitio web
# import requests

# def responde(url):
#     try:
#         return requests.get(url)
#     except requests.exceptions.ConnectionError:
#         pass

# lista=[]
# objetivo_url="google.com/"
# with open('doc/sub_dominioList.txt') as file:
#     for dicc in file.readlines():
#         palabras=dicc.strip()
#         #print(palabras)
#         new_url=objetivo_url + palabras
      
#         datos = responde("http://"+new_url)

#         if (datos):
#             lista.append(new_url)
#             print("Direcctorio encontrado: " + new_url ) 
#         else:
#           pass  #print("Subdominio NO encontrado " + new_url)

#      #http://

# print(lista)
# with open('doc/subd_Ocultos/subdominios_Encontrados.txt', 'w') as datos_guardado:
#  for subdoLista in lista:
#      datos_guardado.write( subdoLista + "\n" )

# print(datos_guardado)