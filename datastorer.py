import sqlite3
import Scraper_alt

def datastorer():
    conn = sqlite3.connect('auto24.db')
    c = conn.cursor()
    data = Scraper_alt.scraper_alt('https://eng.auto24.ee/kasutatud/nimekiri.php?bn=2&a=100&b=1&ae=2&af=50&ssid=50037856')

    try:
        c.execute('''CREATE TABLE Listings(make TEXT, model TEXT, engine TEXT, price INT, year INT, mileage INT, transmission TEXT)''')
    except:
        c.execute('''DELETE FROM Listings''')

    for i in range(len(data)):
        c.execute('''INSERT INTO Listings VALUES (?,?,?,?,?,?,?)''', (
        data[i].get('Make'), data[i].get('Model'), data[i].get('Engine'), data[i].get('Price'), data[i].get('Year'),
        data[i].get('Mileage'), data[i].get('Transmission')))

    conn.commit()
    c.execute('''SELECT * FROM Listings''')
    results = c.fetchall()
    print(results)

datastorer()
