# netnuker

**v1.1**

![image](https://github.com/mxntysec/netnuker/assets/166342298/e45a7b10-23f1-4b94-9536-8ae90c0e08ef)

`netnuker` is an all in-one attack tool which can do: `TCP Syn Flood Attacks, Nmap scans, Sub Directory Brute Forcing`

`netnuker` uses `nmap` and a custom tool I wrote named `subdestroyer` for recon.

![image](https://github.com/mxntysec/netnuker/assets/166342298/0c91a861-8c09-4773-9931-a180a9984651)

This tool can use `nmap` for the 100 most popular UDP ports in option 4

Disclaimer: The default sub directory wordlist is `/usr/share/seclists/Discovery/Web-Content/raft-medium-directories.txt` you can change this by going into the script on line 144 and changing the `wordlist = ` line.

![image](https://github.com/mxntysec/netnuker/assets/166342298/4a6c03fa-979b-40a2-b974-3802c6c99d6e)

You can install the dependencies with the requirements.txt file: `pip install -r requirements.txt` (you need `nmap` for option 2 to work)

Note: You can implement ip spoofing for TCP Syn Flooding but this tool just spoofs the source port.


# Testing:
`This tool is still in testing so if it doesn't work or has bugs that's something to be fixed (I need to add more effiency to the TCP Syn Flood attack)`

# ETHICAL DISCLAIMER:

**This tool is intended for educational purposes only and should only be used on networks and systems for which you have explicit permission to conduct security testing. Unauthorized use of this tool is illegal and unethical, and can result in severe legal consequences.**
