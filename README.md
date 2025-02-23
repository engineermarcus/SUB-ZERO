# **SUB-ZERO**  


![SUB-ZERO Banner](thumbnails/sub.png)  
## **Overview**  
SUB-ZERO is a multi-variant attack suite designed for network security testing and ethical hacking. It includes several attack vectors such as UDP flood, ICMP flood, HTTP POST flood, DNS reflection, and more. This tool is for educational and research purposes only.

## **Features**  
- **Multi-variant attack suite**: Includes multiple attack methods, modularized for easy expansion.  
- **Automated execution**: Runs indefinitely until manually stopped.  
- **Logging support**: Keeps track of attack attempts and network interactions.  
- **Modular design**: Easily extend the attack suite by adding new modules.  
- **Lightweight and fast**: Optimized to send packets efficiently with minimal delay.  

## **Installation**  

### **1. Clone the Repository**  

```bash
git clone https://github.com/engineermarcus/SUB-ZERO.git
cd SUB-ZERO

```
**2. Install Dependencies**

Ensure you have Python installed. Then, install the required modules:

```bash
pip install -r requirements.txt
```

```sh
pip install scapy
```
**3. Run the Attack Suite**

```bash

python ice.py
```
Press Ctrl + C to stop the attack manually.


---

Modules & Attack Variants


---

## **Configuration**

Modify ice.py to customize attack parameters:

Target IP: Change the target's IP address.

Attack Type: Specify which attack module to execute.

Logging: Enable or disable attack logging in logs.txt.


Example:

target_ip = "192.168.1.100"
attack_type = "udp_flood"
enable_logging = True


---

## **Log File Structure**

By default, logs are stored in logs.txt in the following format:

[2025-02-23 14:30:15] UDP Flood initiated against 192.168.1.100
[2025-02-23 14:30:20] ICMP Flood attack ongoing...
[2025-02-23 14:30:30] HTTP POST Flood request sent...


---

### **Legal Disclaimer**

This tool is intended only  for authorized  security testing on systems you own or have explicit permission to test. Unauthorized use of this tool on networks without consent is illegal and may result in severe consequences. The developers are not responsible for any misuse.

Use this software ethically and responsibly.


---

## **Contributors**

Marcus Onyango (Project Lead & Developer)




For contributions, open an issue or submit a pull request.


---

## **License**

This project is licensed under the MIT License.


---

## **Contact**

For questions, reach out via:

Email: engineermarcus72@gmail.com

GitHub Issues: Open an Issue




