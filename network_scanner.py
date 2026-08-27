from tabnanny import verbose

import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    print("IP\t\t\tMAC Addresss\n-----------------------------------------------")

    for element in answered_list:
        print(element[1].psrc+ "\t\t"+ element[1].hwsrc)
        print("\n")



scan("192.168.179.2/24")