# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 01:30:49 2022

@author: sandr
"""
 # INFORMACION DNS DE OBJETIVO

import dns.resolver

def main():
	informacion = ['A','AAAA','NS','SOA','MX','MF','MD','TXT']
	for c in informacion:
		try:
			a = dns.resolver.query("productosjr.com", c)
			for q in a:
				print(q)
		except:
			print("No pude obtener la consulta")

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		exit()
