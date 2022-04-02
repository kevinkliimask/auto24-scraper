from selenium import webdriver


def scraper(url):
    PATH = 'chromedriver.exe'
    driver = webdriver.Chrome(PATH)
    driver.get(url)
    data = []
    make = driver.find_element_by_xpath('//*[@id="usedVehiclesSearchResult-flex"]/div[1]/div[2]/div[1]/a/span[1]').text

    for result in driver.find_elements_by_class_name("result-row"):
        model = result.find_element_by_class_name('model').text
        try:
            engine = result.find_element_by_class_name('engine').text
        except:
            engine = None
        price = result.find_element_by_xpath('div[2]/div[2]/span/span').text
        try:
            year = result.find_element_by_xpath('div[2]/div[3]/span[@class = "year"]').text
        except:
            year = None
        try:
            mileage = result.find_element_by_xpath('div[2]/div[3]/span[@class = "mileage"]').text
            mileage = int(mileage[:-3])
        except:
            mileage = None
        try:
            transmission = result.find_element_by_xpath('div[2]/div[3]/span[@class = "transmission sm-none"]').text
        except:
            transmission = None
        data.append({'Make': make, 'Model': model, 'Engine': engine, 'Price': price, 'Year': year, 'Mileage': mileage,
                     'Transmission': transmission})

    driver.quit()
    return data

