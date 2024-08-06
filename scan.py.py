from scapy.all import ARP, Ether, srp
import requests

def scan(ip_range):
    # Opprett en ARP-forespørselspakke
    arp = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp
    
    # Send pakken og motta svar
    result = srp(packet, timeout=3, verbose=False)[0]
    
    # Behandle resultatene
    devices = []
    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})
    
    return devices

def display_devices(devices):
    print("Available devices in the network:")
    print("IP Address\t\tMAC Address")
    print("-----------------------------------------")
    for device in devices:
        print(f"{device['ip']}\t\t{device['mac']}")

ip_range = "192.168.1.0/24"  # Erstatt med nettverkets IP-område
devices = scan(ip_range)
display_devices(devices)
