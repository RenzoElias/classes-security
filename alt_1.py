# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# BANNER GRABBINGS

import socket
import sys

def banner_grabber(ip, port):
    s = socket.socket()
    s.connect((ip, int(port)))
    banner = s.recv(1024)
    print(banner)
    
def main():
    if len(sys.argv) <= 1:
        print("Use --help")
    elif sys.argv[1]  == "--help":
        print("USAGE: ./banner.py <IP><PORT>")
    elif len(sys.argv) == 3:
        print("Right synstax")
        ip = sys.argv[1]
        port = sys.argv[2]
        banner_grabber(ip, port)
        
main()