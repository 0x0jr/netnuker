# 🚀 netnuker v1.2

<p align="center"><img src="https://github.com/mxntysec/netnuker/assets/166342298/4cdc54a2-ad99-4b14-a7d5-1bb89d8d7602" width="500px" alt="netnuker"></p> 

## 🗒️ Information

***netnuker is an all-in-one attack tool that performs TCP Syn Flood Attacks, Slowloris Attacks, Nmap scans, and Sub Directory Brute Forcing.***

***netnuker leverages nmap and a custom tool named subdestroyer for comprehensive reconnaissance.***

***You don't need to install subdestroyer!! it's built in, but you can find it here: https://github.com/mxntysec/subdestroyer***

## ✨ Features

- 💥 **TCP Syn Flood Attack (DoS)**
- 🔪 **Slowloris Attack HTTP (Effective)**
- 🔍 **Nmap Scans**:
  - Standard scans with service/version detection.
  - Most popular 100 UDP ports scan.
- 🔎 **Subdirectory Brute Forcing** with subdestroyer.

<p align="left"><img src="https://github.com/mxntysec/netnuker/assets/166342298/c387419d-2008-4f02-b6ad-561bb10aa387" width="250px" alt="netnuker in action"></p>

## 📋 Prerequisites

Ensure you have the following installed:

- `nmap`
- Python 3

Install the dependencies via the `requirements.txt` file:
```
pip install -r requirements.txt
```

## 🔧 Installation

1. **Clone this repository**:
   ```
   git clone https://github.com/mxntysec/netnuker.git
   cd netnuker
   ```

2. **Install dependencies**:
   ```
   pip install -r requirements.txt
   ```

## 🚀 Usage

Run `netnuker` with the following command:
```
python3 netnuker.py
```

### Available Options:

1. **TCP Syn Flood Attack (DDoS)**
2. **Nmap Scan (-sC -sV -p- --open)**
3. **Subdirectory Scan (subdestroyer)**
4. **Nmap Scan for Most Popular UDP Ports**

### Note:

The default subdirectory wordlist is located at `/usr/share/seclists/Discovery/Web-Content/raft-medium-directories.txt`. You can change this by editing the script on line 144 and modifying the `wordlist =` line.

## ⚠️ Disclaimer

**This tool is intended for educational purposes only and should only be used on networks and systems for which you have explicit permission to conduct security testing. Unauthorized use of this tool is illegal and unethical, and can result in severe legal consequences.**

## 🧪 Testing

**This tool is still in testing. If it doesn't work or has bugs, improvements are in progress. Enhancements to the efficiency of the TCP Syn Flood attack are ongoing.**

## 🛡️ Ethical Disclaimer

**This tool is intended for educational purposes only and should only be used on networks and systems for which you have explicit permission to conduct security testing. Unauthorized use of this tool is illegal and unethical, and can result in severe legal consequences.**

## 👇 My Socials

**Check out my medium page for HackTheBox writeups and TryHackMe writeups**
https://medium.com/@mxnty

**Here's my HackTheBox Account**
https://app.hackthebox.com/users/429685

---

Feel free to contribute to this project or raise any issues you encounter.

---
