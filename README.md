# Fagprøve
 
# Brukerveiledning:


# Helpdesk:

Pass på at du har en Windows maskin med administratorrettigheter.
Python må være installert. Hvis ikke, kan den installeres fra Microsoft Store.

Kjør dette i CMD:
pip install scapy requests

Installer npcap for å kunne scanne nettverket. Npcap 1.79 installer for Windows 7/2008R2, 8/2012, 8.1/2012R2, 10/2016, 2019, 11 (x86, x64, and ARM64).
https://npcap.com/#download 

Installer også SQLite: https://www.sqlite.org/download.html og velg sqlite-tools-win-x64-3460000.zip.
Pakk ut mappen og legg den under C:\
Åpne environment variables > System variables > Path > Edit > new, og legg til stien til sqlite mappa. Den burde ligne på dette: C:\sqlite-tools-win-x64-3460000

Åpne cmd, skriv ipconfig/all og noter ned ID-en for nettverket som skal brukes.

Åpne scan.py i en tekstredigerer eller utviklingsmiljø (f.eks VSCode), og endre ip_range variabelen til riktig nettverk på maskinen.

Python-scripten kan kjøres direkte fra VSCode eller i CMD med:
python script.py

For å lese databasen skriver du:
sqlite3 sqlite.db
SELECT * FROM devices;

# Drift:

Følg alle de samme stegene skrevet i # Helpdesk.
For å oppdatere og hente nyeste versjon av programmet kan du kjøre:
git pull origin main

For å gjøre programmet kjørbart kan du bruke:
pyinstaller --onefile scan.py



