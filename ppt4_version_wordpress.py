# Ver la version de wordpress
import requests
from bs4 import BeautifulSoup
from os import path

def main():
    url = "https://shopage.es"
    cabecera = {'User-Agent':'Firefox'}
    peticion = requests.get(url=url, headers=cabecera)
    soup = BeautifulSoup(peticion.txt,'html5lib')
    for v in soup.find_all('meta'):
        if v.get('name') == 'generator':
            version = v.get('content')
    print(version)

if __name__ == '__main__':
	try:
		if path.exists("peticion.txt"):
			main()
	except KeyboardInterrupt:
		exit()
