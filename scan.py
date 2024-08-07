from scapy.all import ARP, Ether, srp
import requests
import sqlite3 

def scan(ip_range):
    # Opprett en ARP-forespørselspakke. (Address Resolution Protocol) for å kartlegge MAC-adressene til enhetene i nettverket.
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

def get_vendor(mac_address):
    # URL for å hente leverandørinformasjon basert på MAC-adressen
    url = f"https://api.macvendors.com/{mac_address}"
    # Gjør en GET-forespørsel til API-et
    response = requests.get(url)
    # Sjekk om forespørselen var vellykket (statuskode 200)
    if response.status_code == 200:
        return response.text
    else:
        return "Unknown"

def save_to_database(devices):
    # Koble til SQLite-databasen
    conn = sqlite3.connect('sqllite.db')
    cursor = conn.cursor()
    
    # Sett inn data i tabellen
    for device in devices:
        vendor = get_vendor(device['mac'])
        cursor.execute('''
        INSERT INTO devices (mac_adresse, leverandør)
        VALUES (?, ?)
        ''', (device['mac'], vendor))
    
    conn.commit()
    conn.close()

# Definer IP-området
ip_range = "192.168.1.0/24"  # Erstatt med ditt nettverks IP-område

# Skann nettverket
devices = scan(ip_range)

# Vis enhetene
display_devices(devices)

# Lagre enhetene i databasen
save_to_database(devices)
