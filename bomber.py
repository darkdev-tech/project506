# Xenocrypt WhatsApp Bomber - Ethical Hacking Tool
# Developer: Xenocrypt Tech ©

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

# Stylish banner
os.system('clear')
print("\033[1;32m")
print(r"""
 __   __             _                                 _   
 \ \ / /__  _   _   | |__   ___  _ __  _ __   ___  _ __| |_ 
  \ V / _ \| | | |  | '_ \ / _ \| '_ \| '_ \ / _ \| '__| __|
   | | (_) | |_| |  | | | | (_) | |_) | |_) | (_) | |  | |_ 
   |_|\___/ \__,_|  |_| |_|\___/| .__/| .__/ \___/|_|   \__|
                               |_|   |_|                   
""")
print("\033[1;36m          Created by Xenocrypt Tech - WhatsApp hack Tool")
print("\033[0m")

# Input area
message = input("\033[1;33m[+] Enter the message to send: \033[0m")
count = int(input("\033[1;33m[+] How many times to send?: \033[0m"))
contact = input("\033[1;33m[+] Enter contact name (as in WhatsApp): \033[0m")

# Start browser
print("\033[1;34m[!] Launching WhatsApp Web... Please scan QR code.\033[0m")
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com")
input("\033[1;32m[✓] Press ENTER after scanning QR code.\033[0m")

# Search and open chat
search = driver.find_element(By.XPATH, '//div[@title="Search input textbox"]')
search.send_keys(contact)
search.send_keys(Keys.ENTER)

# Send messages
msg_box = driver.find_element(By.XPATH, '//div[@title="Type a message"]')
print("\033[1;35m[✓] Sending messages...\033[0m")
for i in range(count):
    msg_box.send_keys(message)
    msg_box.send_keys(Keys.ENTER)
    time.sleep(0.2)

print("\033[1;32m[✓] Done! All prank messages sent successfully.\033[0m")
driver.quit()
