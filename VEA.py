import time
from urllib.request import urlretrieve
from selenium import webdriver
import re
import datetime


from bs4 import BeautifulSoup

driver = webdriver.Chrome(executable_path="C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe")

file1 = open('VEA.txt', 'r') 
listaarchivo = file1.readlines()

def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )+2
        end = s.index( last, start )-2
        return s[start:end]
    except ValueError:
        return ""
        
a=""
for l in listaarchivo: 
    try: 
        driver.get(l)
        time.sleep(2)
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        s1 = str(soup.find_all('span', {'class':'vtex-store-components-3-x-productBrand'})[0].text)
        s2 = str(soup.find_all('span', {'class':'vtex-product-price-1-x-currencyInteger vtex-product-price-1-x-currencyInteger--shelf-main-selling-price'})[0].text)
        s3 = str(soup.find_all('span', {'class':'vtex-product-price-1-x-currencyFraction vtex-product-price-1-x-currencyFraction--shelf-main-selling-price'})[0].text)
        
        print(l)
        a = a + l.replace("\n","")  + ";" + s1 + ";" + s2 + "," + s3 + "\n" 
    except: 
        print("no se pudo acceder al url: " + l)
        

driver.close()

now = datetime.datetime.now()
nw=str(now.strftime("%Y-%m-%d %H-%M-%S"))
print(nw)
with open('VEA ' + nw + '.csv', 'w', newline="\n", encoding='ISO-8859-1') as f:
    f.write(a)
f.close