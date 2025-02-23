import subprocess
import time
import platform

def ping_test():
  # Function to check the OS and use the correct ping command
  def get_ping_command(target_ip):
      system_os = platform.system().lower()
      
      if system_os == "windows":
          return ["ping", "-n", "1", target_ip]  # Windows uses -n for count
      else:
          return ["ping", "-c", "1", target_ip]  # Linux/macOS uses -c for count
  
  # Target IP address
  target_ip = "197.136.218.3"
  
  # Number of pings
  num_pings = 10  # Set the number of times to ping
  
  # Get the correct ping command
  ping_command = get_ping_command(target_ip)
  
  print(f"Pinging {target_ip} {num_pings} times...\n")
  
  # Loop to send multiple pings
  for i in range(num_pings):
      try:
          # Run the ping command
          result = subprocess.run(ping_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
  
          # Check if ping was successful
          if result.returncode == 0:
              print(f"Ping {i+1}: Success")
          else:
              print(f"Ping {i+1}: Failed - {result.stderr.strip()}")
  
      except Exception as e:
          print(f"Error: {e}")
  
      # Delay between pings to avoid flood restriction
      time.sleep(0.3)  # 300ms delay (more than 200ms limit)
  
  print("\nPing test completed.")


