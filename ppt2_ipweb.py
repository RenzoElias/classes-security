import dns.resolver

# Obtener informacion de una pagina web
# https://www.ibm.com/docs/es/capm?topic=monitors-dns-monitor

def main():
	informacion = ['A']
	for c in informacion:
		try:
			a = dns.resolver.query("shopage.es", c)
			# a = dns.resolver.query("productosjr.com", c)
			for q in a:
				print(q)
		except:
			print("No pude obtener la consulta")

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		exit()
