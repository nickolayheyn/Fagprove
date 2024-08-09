from scapy.all import ARP, Ether, srp
import requests
import sqlite3
import time

# Funksjon for å skanne nettverket og finne tilkoblede enheter
def scan(ip_range):
    # Opprett en ARP-forespørselspakke
    arp = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp

    # Send pakken og motta svar
    result = srp(packet, timeout=3, verbose=False)[0]
    
    # Behandle resultatene
    devices = []
    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})
    
    return devices

# Funksjon for å vise enheter funnet på nettverket
def display_devices(devices):
    # Sjekk om listen med enheter er tom
    if not devices:
        print("Ingen enheter ble funnet i nettverket.")
        return  # Avslutt funksjonen hvis ingen enheter ble funnet

    # Hvis det er enheter, skriv dem ut
    print("Tilgjengelige enheter i nettverket:")
    print("IP-adresse\t\tMAC-adresse\t\tLeverandør")
    print("------------------------------------------------------")
    for device in devices:
        print(f"{device['ip']}\t{device['mac']}\t{device.get('vendor', 'Ukjent')}")

# Funksjon for å hente leverandørinformasjon basert på MAC-adresse
def get_vendor(mac_address):
    url = f"https://api.macvendors.com/{mac_address}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text.strip()
        else:
            return "Ukjent"
    except requests.exceptions.RequestException as e:
        print(f"Feil ved innhenting av leverandør for {mac_address}: {e}")
        return "Ukjent"

# Funksjon for å lagre enhetsinformasjon til en SQLite-database
def save_to_database(devices):
    # Koble til SQLite-databasen (eller opprett den hvis den ikke finnes)
    conn = sqlite3.connect('sqllite.db')
    cursor = conn.cursor()
    
    # Sett inn enhetsdata i databasen
    for device in devices:
        cursor.execute('''
            INSERT INTO devices (ip_adresse, mac_adresse, leverandør)
            VALUES (?, ?, ?)
        ''', (device['ip'], device['mac'], device['vendor']))
    
    # Bekreft endringene og lukk tilkoblingen
    conn.commit()
    conn.close()

# Hoveddel av skriptet
if __name__ == "__main__":
    # Skriv ut en melding til brukeren
    print("Vent et øyeblikk...")

    # Koble til SQLite-databasen (eller opprett den hvis den ikke finnes)
    conn = sqlite3.connect('sqllite.db')
    
    # Opprett en cursor for å samhandle med databasen
    cursor = conn.cursor()
    
    # Opprett enhetstabellen
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS devices (
        id INTEGER PRIMARY KEY AUTOINCREMENT,  
        ip_adresse TEXT NOT NULL,
        mac_adresse TEXT NOT NULL,
        leverandør TEXT
    )
    ''')
    
    # Bekreft endringene og lukk tilkoblingen
    conn.commit()
    conn.close()
    
    print("Database og tabell opprettet med suksess.")

    ip_range = "192.168.1.0/24"  # Erstatt med nettverkets IP-område
    devices = scan(ip_range)
    
    # Hent leverandørinformasjon for hver enhet
    for device in devices:
        device['vendor'] = get_vendor(device['mac'])
    
    display_devices(devices)
    
    save_to_database(devices)
    
    # Keep the program running until Enter is pressed
    print("\nTrykk Enter for å lukke programmet...")
    input()
