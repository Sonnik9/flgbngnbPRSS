from requests_html import HTMLSession
import requests
from bs4 import BeautifulSoup
import time
import random
from random import choice
# import csv
import json
# import asyncio
# import aiohttp
import time
from requests_html import HTMLSession
from bs4 import BeautifulSoup
# from selenium.webdriver.common.keys import Keys
# from fake_useragent import UserAgent
import random 
import math
import re
import multiprocessing
from fake_useragent import UserAgent
from lxml import etree
import socks
import socket

# Selmenlo889:M7z1HsW@185.33.85.195:50100
# Selmenlo889:M7z1HsW@94.124.160.250:50100
# Selmenlo889:M7z1HsW@45.152.177.241:50100
# Selmenlo889:M7z1HsW@216.185.46.231:50100
# Selmenlo889:M7z1HsW@2.59.60.162:50100
# Selmenlo889:M7z1HsW@23.26.229.1:50100
# Selmenlo889:M7z1HsW@108.165.218.102:50100








def checkIP(): 
    with open("proxyE.txt", encoding="utf-8") as file:
        PROXY_LIST = []
        prLi = ''.join(file.readlines()).split('\n')
        prLi = list(i.strip() for i in prLi)
        prLi = list(filter(lambda item: item != '', prLi))
        print(len(prLi))

    print('А теперь через прокси:')
    for i, p in enumerate(prLi):
        proxiess = {       
            "https": f"http://{p}",            
            "socks5": f"http://{p}"   
        }
        # proxiess = {
        #     "http": f"socks5://{p}",
        #     "https": f"socks5://{p}"     
        # } 
        print(proxiess) 
        # socks.set_default_proxy(socks.SOCKS5, "localhost", 9150)
        # socket.socket = socks.socksocket
        
        ip = requests.get('http://checkip.dyndns.org', proxies=proxiess).content
        soup = BeautifulSoup(ip, 'html.parser')
        print(soup.find('body').text)

checkIP()

# python toKnowYourAdress.py