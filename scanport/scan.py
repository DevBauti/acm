import socket

ip = input()

for port in range(1,65355):
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.settimeout(5)

    result = sk.connect_ex(ip, port)

    if result == 0:
        print('Puesto abierto: '+ str(port))
        sk.close()
    else:
        print('Puesto cerrado: '+ str(port))
    
"""
esto es el inicio, tiene mil mejoras..
"""