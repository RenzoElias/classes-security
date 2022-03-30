import http.client
from os import path

if path.exists("vulnerables.txt"):
    host = "localhost"

    http = http.client.HTTPConnection(host, timeout=2)
    http.request("HEAD", "")

    server = http.getresponse().getheader("server")
    vulnerables = open("vulnerables.txt", "r")
    esVulnerable = False

    for servicio in vulnerables:
        s = servicio.split(" ")
        if s[0] in server:
            print(host, "tiene servicio", s[0], "con posible vulnerabilidad", s[1])
            esVulnerable = True
    if not esVulnerable:
        print(
            host,
            "no cuenta con un servicio vulnerable de la lista, o no da la informacion",
        )
else:
    print("No se encuentra la lista")
