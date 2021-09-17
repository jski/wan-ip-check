import time
import requests
import smtplib
import os
import sys
from dotenv import load_dotenv

try:
    load_dotenv()
    webhook_url = os.getenv("webhook_url")
    check_site = os.getenv("check_site")
    system_name = os.getenv("system_name")
    check_interval = int(os.getenv("check_interval"))
    if not webhook_url or not check_site or not system_name or type(check_interval) is not int:
        raise Exception()
except:
    print("You probably didn't load your stuff into the .env file properly, look at the README!")
    sys.exit(1)


def message_webhook(ip):
    try:
        Message = {
            "content":
            "New IP address found for {0}: {1}".format(ip, system_name),
        }
        requests.post(webhook_url, data=Message)
    except Exception as e:
        print(e)


def check_ip():
    return requests.get(check_site)


ip = None
while True:
    r = check_ip()
    if r.status_code == 200:
        if ip == None:
            ip = r.text
            print("First run complete, IP: {0}System will loop and check every {1} seconds...".format(ip, check_interval))
        elif ip == r.text:
            pass
        else:
            ip = r.text
            print("New IP found: {0}".format(ip))
            message_webhook(ip)
    time.sleep(int(check_interval))
