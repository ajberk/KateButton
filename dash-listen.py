from scapy.all import *
import requests
import os
import random
from adjectives import Words

def send_message():
    print "sending message"
    url = "http://textbelt.com/text"
    data = {
        'number': os.environ['KATES_NUMBER'],
        'message': "Kate! Your booty is " + random.choice(Words.adjectives())
    }
    response = requests.post(url, data=data)
    print response.status_code


def arp_display(pkt):

  if (pkt[ARP].hwsrc == '74:75:48:38:4d:94') or (pkt[ARP].hwsrc == '74:c2:46:1d:b6:d8'):
    print "YOOO"
    print "ARP Probe from: " + pkt[ARP].hwsrc
    send_message()

print sniff(prn=arp_display, filter="arp", store=0, count=100)