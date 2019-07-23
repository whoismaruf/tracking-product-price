from src import market

# Samsung A0 
# Daraz.com.bd

daraz_url = 'https://www.daraz.com.bd/products/samsung-galaxy-a50-smartphone-blue-i104168392-s1018896624.html'
daraz_tag = 'span'
daraz_class = 'pdp-price'
daraz_price = market.Product(daraz_url, daraz_tag, daraz_class).price()
print(daraz_price)

