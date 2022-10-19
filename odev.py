from unittest import result
import requests
import xml.etree.ElementTree as ET
from urllib.request import urlopen

url = "https://www.tcmb.gov.tr/kurlar/today.xml"
resp = requests.get(url=url)
#print(resp.text)

tree = ET.parse(urlopen(url))
root = tree.getroot()

liste = []
liste.append(root.findall('Currency')) 

for i in liste[0]:
    currencyCode = i.get('Kod')
    banknoteBuying = i.find("BanknoteBuying").text
    banknoteSelling = i.find("BanknoteSelling").text
    ForexBuying = i.find("ForexBuying").text
    ForexSelling = i.find("ForexSelling").text
    name = i.find("Isim").text

    if currencyCode == "USD":
        result = float(banknoteSelling) - float(banknoteBuying)
        print("USD", banknoteSelling)
        print("USD", banknoteBuying)
        print("Banka alış - satış arasındaki kur farkı -->", str(result))

    if currencyCode == "EUR":
        result = float(banknoteSelling) - float(banknoteBuying)
        print("EUR", banknoteSelling)
        print("EUR", banknoteBuying)
        print("Banka alış - satış arasındaki kur farkı -->", str(result))  

    if currencyCode == "QAR":
        result = float(ForexSelling) - float(ForexBuying)
        print("QAR", ForexSelling)
        print("QAR", ForexBuying)
        print("Para birimi adı:", name)
        print("Banka alış - satış arasındaki kur farkı -->", str(result))  




