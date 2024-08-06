# Fagprøve
 
# Brukerveiledning:

Pass på at du har en Windows maskin med administratorrettigheter.
Python må være installert. Hvis ikke, kan den installeres fra Microsoft Store.

Kjør dette i CMD:
pip install scapy requests

Installer npcap for å kunne scanne nettverket. Npcap 1.79 installer for Windows 7/2008R2, 8/2012, 8.1/2012R2, 10/2016, 2019, 11 (x86, x64, and ARM64).
https://npcap.com/#download 

Åpne scan.py i en tekstredigerer eller utviklingsmiljø (f.eks VSCode).
Kjør list_interfaces.py og endre ip_range variabelen til riktig nettverksgrensesnitt på maskinen

Python-scriptene kan kjøres direkte fra VSCode eller i CMD med:
python list_interfaces / script.py
