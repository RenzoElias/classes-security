# Modified
import socket
# https://www.youtube.com/watch?v=kUblkdrfM8M&ab_channel=HackerSploit

def banner(ip, port):
    s = socket.socket()
    s.connect((ip, int(port)))
    s.settimeout(5)
    print(s.recv(1024))

def main():
    ip = input("Please enter the IP: ")
    # 192.168.1.1
    port = str(input("Please enter the port: "))
    # 22
    banner(ip, port)

main()



# MS PowerPoint

# import http.client
# from os import path

# if path.exists("vulnerables.txt"):
#     host = "localhost"

#     http = http.client.HTTPConnection(host, timeout=2)
#     http.request("HEAD", "")

#     server = http.getresponse().getheader("server")
#     vulnerables = open("vulnerables.txt", "r")
#     esVulnerable = False

#     for servicio in vulnerables:
#         s = servicio.split(" ")
#         if s[0] in server:
#             print(host, "tiene servicio", s[0], "con posible vulnerabilidad", s[1])
#             esVulnerable = True
#     if not esVulnerable:
#         print(
#             host,
#             "no cuenta con un servicio vulnerable de la lista, o no da la informacion",
#         )
# else:
#     print("No se encuentra la lista")
