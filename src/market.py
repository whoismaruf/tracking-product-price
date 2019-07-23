class Product:
    def __init__(self, url, tag, classname):
        self.url = url
        self.tag = tag
        self.classname = classname

    def price(self):
        import requests
        from bs4 import BeautifulSoup
        print("Checking price from Daraz...")
        source = requests.get(self.url).text
        soup = BeautifulSoup(source, 'lxml')
        price = soup.find(self.tag, class_=self.classname).text
        return float(price[2:8].replace(',', ''))
