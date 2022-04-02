from selenium import webdriver
from bs4 import BeautifulSoup


def scraper_alt(url):
    PATH = 'chromedriver.exe'
    driver = webdriver.Chrome(PATH)
    driver.get(url)
    source = driver.page_source
    data = []
    soup = BeautifulSoup(source, 'lxml')
    cars = soup.find_all('div', class_ = 'result-row')
    make = 'Honda'

    for car in cars:
        model = car.find('span', class_ = 'model').text
        engine = car.find('span', class_ = 'engine')
        if engine is not None:
            engine = engine.text
        price = int(car.find('span', class_ = 'price').text[1:])
        year = car.find('span', class_ = 'year')
        if year is not None:
            year = year.text
        mileage = car.find('span', class_ = 'mileage')
        if mileage is not None:
            mileage = int(mileage.text[:-3].replace('\xa0', ''))
        transmission = car.find('span', class_ = 'transmission')
        if transmission is not None:
            transmission = transmission.text
        data.append({'Make': make, 'Model': model, 'Engine': engine, 'Price': price, 'Year': year,
                     'Mileage': mileage, 'Transmission': transmission})
    print(data)
    driver.quit()

scraper_alt('https://eng.auto24.ee/kasutatud/nimekiri.php?bn=2&a=100&b=1&ae=2&af=50&ssid=50037856')
