import requests
from os import path
from progress.bar import Bar

def main():
    if path.exists("wp_plugins.txt"):
        w = open("wp_plugins.txt", 'r')
        w = w.read().split('\n')
        lista = []
        url = "https://shopage.es"
        b = Bar("Espere...", max = len(w))
        
        for plugin in w:
            b.next()
            try:
                p=requests.get(url=url+"/"+plugin)
                if p.status_code == 200:
                    final = url+"/"+plugin
                    lista.append(final.split("/")[-2])
            except:
                pass
        b.finish()
        for plugin in lista:
            print("Plugin encontrado: {}".format(plugin))
        if lista.length == 0:
            print("No se encontraron plugins") 
    else:
        print("No se encuentra la lista")

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		exit()