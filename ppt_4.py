# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 01:24:36 2022

@author: sandr
"""

# VERSION WORDPRESS

import requests
from bs4 import BeautifulSoup

def main():
	url = "http://productosjr.com"
	cabecera = {'User-Agent':'Firefox'}
	peticion = requests.get(url=url,headers=cabecera)
	soup = BeautifulSoup(peticion.text,'html5lib')
	for v in soup.find_all('meta'):
		if v.get('name') == 'generator':
			version = v.get('content')
	print(version)

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		print("Saliendo")
		exit()
