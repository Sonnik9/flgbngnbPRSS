import requests
from bs4 import BeautifulSoup
import random 
from random import choice
import time


# ////////////////////////////////////
headers = ({'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/69.0'})
get_location_link = 'https://2ip.ru'

def checkIP(): 
    with open("proxyAm.txt", encoding="utf-8") as file:
        PROXY_LIST = []
        prLi = ''.join(file.readlines()).split('\n')
        prLi = list(i.strip() for i in prLi)
        prLi = list(filter(lambda item: item != '', prLi))
        print(len(prLi))


    # response = requests.get(url=get_location_link, headers=random_headers())
    # print(response)
    # soup = BeautifulSoup(response.text, 'lxml')
    # ip = soup.find('div', class_ = 'ip').text.strip()
    # location = soup.find('div', class_ = 'value-country').text.strip()
    # print(ip, ':', location)   
    print('А теперь через прокси:')
    for i, p in enumerate(prLi):
        
        proxiess = {              
        "https": f"http://{p}",       
        "socks5": f"http://{p}",
        } 
      
        try:
            response = requests.get(url=get_location_link, headers=headers, proxies=proxiess)
            print(response)
            soup = BeautifulSoup(response.text, 'lxml')
            ip = soup.find('div', class_ = 'ip').text.strip()
            location = soup.find('div', class_ = 'value-country').text.strip()
            print(f"{i}___  {ip, ':', location}")
            time.sleep(1)
        except Exception as ex:
            print(ex)
            continue

checkIP()

# python testProxy.py