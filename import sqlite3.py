import sqlite3

# Koble til SQLite-databasen (eller opprett den hvis den ikke finnes)
conn = sqlite3.connect('sqllite.db')

# Opprett en cursor for å samhandle med databasen
cursor = conn.cursor()

# Opprett enhetstabellen
cursor.execute('''
CREATE TABLE IF NOT EXISTS devices (
    id INTEGER PRIMARY KEY AUTOINCREMENT,  
    mac_adresse TEXT NOT NULL,
    leverandør TEXT
)
''')

# PRIMARY KEY = Primærnøkkel.
# AUTOINCREMENT = øker automatisk hver gang scriptet kjøres.
#TEXT NOT NULL = kan ikke ha NULL-verdier. Alle poster må ha en verdi for denne kolonnen.

# Bekreft endringene og lukk tilkoblingen
conn.commit()
conn.close()

print("Database and table created successfully.")
