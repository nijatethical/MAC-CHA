#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
MAC Address Changer
Author: Cyber Nijat
Purpose: Educational tool for changing MAC addresses on Linux
"""

import os
import time

print()
print("""==============================
     MAC ADDRESS CHANGER       
==============================
    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    
    Analyzing Network          
==============================""")

# User input
interface = input("Interface (e.g. eth0 or wlan0): ")
mac_change = input("Enter new MAC (example: 00:aa:11:bb:33:cc): ")

print("\nChanging your MAC address...\n")
time.sleep(1.5)

# Execute commands
os.system(f"sudo ifconfig {interface} down")
os.system(f"sudo ifconfig {interface} hw ether {mac_change}")
os.system(f"sudo ifconfig {interface} up")

print(f"MAC address for {interface} has been changed to {mac_change}")
print()
print("by Cyber Nijat")
