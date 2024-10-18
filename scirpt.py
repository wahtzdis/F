
import os
import sys
import socket
import requests
# multitool.py

def ping(host):
    response = os.system(f"ping -c 1 {host} > /dev/null 2>&1")
    if response == 0:
        print(f"{host} is up!")
    else:
        print(f"{host} is down!")

def get_ip():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    print(f"Your IP address is: {ip_address}")

def download_file(url, filename):
    response = requests.get(url)
    with open(filename, "wb") as file:
        file.write(response.content)
    print(f"Downloaded {filename} from {url}")

def run_command(command):
    os.system(command)

def display_menu():
    print("Multi-Tool")
  
    print("2. Get your IP address") 
    print("3. Download a file")
    print("4. Run a command")
    print("5. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")
        
