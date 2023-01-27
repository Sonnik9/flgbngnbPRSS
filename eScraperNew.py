# from __future__ import print_function
# from google.auth.transport.requests import Request
# import os.path
# import pickle
# from googleapiclient.discovery import build
# from google_auth_oauthlib.flow import InstalledAppFlow
# from google.auth.transport.requests import Request
# from google.oauth2.credentials import Credentials

from requests_html import HTMLSession
import requests
from bs4 import BeautifulSoup
import random 
from random import choice
import time
import csv
import json
from lxml import etree
import math
import re
import multiprocessing
from multiprocessing import Pool
import asyncio
import aiohttp
import mpire
from mpire import WorkerPool
from fake_useragent import UserAgent
from datetime import datetime
import sys

# ////////////////// имя страницы гугл таблицы(сперва создайте)
# //////// https://docs.google.com/spreadsheets/d/1E8ApONqNaH9EXH8eeyOssTC2RNDRFyZ7njVucOnRNPs/ - ссылка на гугл таблицу

list_name = 'Test3'
hrefsBankVar = []
uagent = UserAgent()
itemsCount = 0 
agrForAmazon = 'amazon.com'
agrForEbey = 'ebay.com'
# start_time = ''
# adderLink = '&_ipg=240&_pgn=1'
total_count = 0 
# ress = []
# finResult = []
flag = False


# ur = 'https://www.ebay.com/sch/i.html?_dkr=1&iconV2Request=true&_blrs=recall_filtering&_ssn=worxtools&store_cat=0&store_name=worxlawnandgardenequipment&_oac=1'
# url = 'https://www.ebay.com/sch/i.html?_dkr=1&iconV2Request=true&_blrs=recall_filtering&_ssn=worxtools&store_cat=0&store_name=worxlawnandgardenequipment&_oac=1'


# /////////////////////////////////ССЫЛКА НА МАГАЗИН


# ur = 'https://www.ebay.com/sch/i.html?_dkr=1&iconV2Request=true&_blrs=recall_filtering&_ssn=paedistributing&store_cat=0&store_name=paedistributing&_oac=1&LH_PrefLoc=1&LH_ItemCondition=3&LH_BIN=1'



# ////////////////////////////////////////////////////

# adderLink = '&_ipg=240&_pgn=1'
# url2 = f"{ur}{adderLink}"

with open("proxy.txt", encoding="utf-8") as file:
    PROXY_LIST = ''.join(file.readlines()).split('\n')

desktop_agents = ['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                  uagent.random,
                 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                 UserAgent().chrome,
                 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14',
                 uagent.random,
                 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
                 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
                 UserAgent().chrome,
                 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
                 uagent.random,
                 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
                 UserAgent().chrome,
                 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                 uagent.random,
                 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0']
desktop_accept = ['text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                  '*/*',
                  'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                  'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                  'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8','application/signed-exchange;v=b3;q=0.9',
                  'text/html, */*; q=0.01',
                  ]

aceptLengv = [
            'en-US,en;q=0.8',
            'ru-RU,ru;q=0.9',
            ]

# random_headers(agrForEbey)

# ////////////////////////////////////

def random_headers(argLink):
    
    device_memoryHelper = [2,4,8,16,32]
    sett = set()
    finHeaders = []
    headFront = [{
            'authority': f"www.{argLink}",
            'accept': choice(desktop_accept), 
            'User-Agent': choice(desktop_agents),           
            "accept-ch": "sec-ch-ua-model,sec-ch-ua-platform-version,sec-ch-ua-full-version",
            'accept-language': choice(aceptLengv),            
            'cache-control': 'no-cache',
            'content-type': 'application/json',
            'origin': f'https://www.{argLink}',
            'device-memory': f'{choice(device_memoryHelper)}',
            'rtt': '200',            
            }]
    headersHelper = [       
            {"sec-fetch-dest": "empty"},
            {"sec-fetch-mode": "cors"},
            {"sec-fetch-site": "same-origin"},
            {"ect": "4g"},
            {"viewport-width": "386"}
    ]
    headersHelperFormated = []
    strr = ''
    for i in headersHelper[0:len(headersHelper)-random.randrange(0,5)]:
        strr += ((str(choice(headersHelper)))[1:-1]).strip() + ',' + ' '  
         
    sett.add(strr)    
    headersHelperFormated = list(sett)    
    finHeaders = headFront + headersHelperFormated
    finHeaders[1] = eval("{" + finHeaders[1] + "}")    
    finfin = finHeaders[0]|finHeaders[1]    
    return finfin
    
# python amazonHandler.py


def proxyGenerator():
    proxiess = {
        "https": f"http://{choice(PROXY_LIST)}",
        "http": f"http://{choice(PROXY_LIST)}"     
    }
    return proxiess
def sessionReq(url1, shopArg):
    session = HTMLSession()
    session.trust_env = False
    r = session.get(url1, headers=random_headers(shopArg), timeout=(3.15, 21.15))
    # randomChanel = choice(list(range(0, len(PROXY_LIST)+1)))  
    # if randomChanel == 0:
    #     r = session.get(url1, headers=random_headers(shopArg), timeout=(19, 27))
    # else:          
    #     r = session.get(url1, headers=random_headers(shopArg), timeout=(19, 27), proxies=proxyGenerator())    
    return r

def paginationReply(url):
    global start_time    
    paginController = 0
    flagPagin = False 
    # paginLimit = ''  
    lastPagin = 0
    agrForEbey = 'ebay.com' 
         
    try:
        r = sessionReq(url, agrForEbey)          
        # print(r)
        if str(r) == '<Response [200]>':
            print('Первый ответ сервера положительный')
        if str(r) == '<Response [503]>':
            try:
                time.sleep(random.randrange(1,5))
                r = sessionReq(url, agrForEbey)
            except:
                pass
        if str(r) == '<Response [403]>':
            try:
                time.sleep(random.randrange(1,7))
                r = sessionReq(url, agrForEbey)
            except:
                pass
        if str(r) == '<Response [504]>':
            return  
        if str(r) == '<Response [404]>':
            return 
        if str(r) == '<Response [400]>':
            return 
        if str(r) == '<Response [443]>':
            return          
            
        soup = BeautifulSoup(r.text, "lxml") 
        try:
            ptest = soup.find('h1', class_='srp-controls__count-heading')
            # print(ptest) 
            ptest = int(soup.find('h1', class_='srp-controls__count-heading').get_text().split(' ')[0].replace(',', '').replace('+', ''))
            lastPagin = math.ceil(int(ptest)/240)
        except Exception as ex: 
            pass           
            # print(ex)
           
    except Exception as ex:  
        print(f"pagin:  {ex}")
        paginController +=1
        if paginController >1:
            print('Упс! Что-то пошло не так')
            return
        else:
            paginationReply(url)
            
    print(f"Всего в магазине страниц пагинации: {lastPagin}")        
    paginLimit = input('Введите лимит пагинации (через дефис, например: 10-20) или введите Enter(значение по умолчанию)', )
    if paginLimit == '' or paginLimit == ' ':
        hrefsBlockPagination = list(f"{url}&_ipg=240&_pgn={i}" for i in range(1, lastPagin+1))
        start_time = time.time()  
        asyncio.run(gather_registrator_eBay(hrefsBlockPagination))
        return    
    else:
        
        try:
            startPagin = int((paginLimit.strip()).replace(' ', '').split('-')[0])
            finPagin = int((paginLimit.strip()).replace(' ', '').split('-')[1])
            # print(startPagin)
            # print(finPagin)  
        except:
            paginLimit = input('Пожалуйста, введите лимит на пагинацию еще раз:', )
            try:
                startPagin = int((paginLimit.strip()).replace(' ', '').split('-')[0])
                finPagin = int((paginLimit.strip()).replace(' ', '').split('-')[1])
                # print(startPagin)
                # print(finPagin)
            except:
                print('Программа вынуждена завершить работу(') 
                sys.exit() 
        if startPagin > finPagin:
            flagPagin = True
            paginLimit = input('Пожалуйста, введите лимит на пагинацию еще раз:', )
            try:
                startPagin = int((paginLimit.strip()).replace(' ', '').split('-')[0])
                finPagin = int((paginLimit.strip()).replace(' ', '').split('-')[1])
                # print(startPagin)
                # print(finPagin)  
            except:
                print('Программа вынуждена завершить работу(') 
                sys.exit()  
        elif lastPagin < finPagin and flagPagin == False:
            hrefsBlockPagination = list(f"{url}&_ipg=240&_pgn={i}" for i in range(1, lastPagin+1))
        elif lastPagin > finPagin:
            hrefsBlockPagination = list(f"{url}&_ipg=240&_pgn={i}" for i in range(startPagin, finPagin+1))
        elif lastPagin == finPagin:
            hrefsBlockPagination = list(f"{url}&_ipg=240&_pgn={i}" for i in range(1, lastPagin+1))

    start_time = time.time()  
    asyncio.run(gather_registrator_eBay(hrefsBlockPagination))            
   

# ///////////////////////////////////////////////////////////////////////////////////
    
async def linkerCapturerEbay(href): 
    global hrefsBankVar    
    global flag

    
    agrForEbey = 'ebay.com'
    while(True):
        flag = False
        countLincerCapturer = 0 
        countLincerCapturer2 = 0
        cycleControl = 0  
        try:            
            r = sessionReq(href, agrForEbey)
            # print(f"linker response:  {r}") 
            if str(r) == '<Response [503]>':
                try:
                    # time.sleep(random.randrange(1,5))
                    return
                except:
                    pass
            if str(r) == '<Response [403]>':
                try:
                    # time.sleep(random.randrange(1,7))
                    return
                except:
                    pass
            if str(r) == '<Response [504]>':
                return  
            if str(r) == '<Response [404]>':
                return
            if str(r) == '<Response [400]>':
                return
            if str(r) == '<Response [443]>':
                return
                        
            try:
                soup = BeautifulSoup(r.text, "lxml")
                hrefs = soup.find_all('a', class_='s-item__link')            
                for item in hrefs:
                    if item is None:
                        cycleControl +=1
                        if cycleControl == 180:
                            countLincerCapturer +=1
                            if countLincerCapturer >1:
                                print('Не удалось собрать нужное количество ссылок')
                                return
                            else:                                
                                flag = True
                                break
                        continue 
                    else:
                        hrefsBankVar.append(item.get('href'))      

            except:
                flag = True
                # print(f'исключение на 226 стр') 
                # pass 
        except Exception as ex:
            flag = True

        # finally:
        if flag == False:
            return 
        else:
            countLincerCapturer2 +=1
            if countLincerCapturer2 >1:
                print('Не удалось собрать нужное количество ссылок')
                return
            else:
                time.slep(random.randrange(1,3))
                continue     
                

def linksHandlerAmazon(total):
    # print('start Amazon')
    # global finResult
    if total is None:
        return
    try:
        model = total['model'].lower()
    except:
        pass    
    agrForAmazon = 'amazon.com'    
    targetLinkPattern = 'https://www.amazon.com'

    # print(f"url For Amazon: {url}")

    while(True):
        finResult = []
        counterRetry = 0
        counterExceptions = 0                     
        quanityTargetItems = 0
        flagEx1 = False
        try:
            r = ''   
            r = sessionReq(total['linkSrchAmazon'], agrForAmazon)            
            # print(f"ответ Амазона:  {r}")
            if str(r) == '<Response [503]>':
                print('Желтая карточка от Amazon')            
                # time.sleep(random.randrange(1,4))
                return

            if str(r) == '<Response [403]>':
                print('Amazon отверг запрос')

                # time.sleep(random.randrange(1,5))
                return

            if str(r) == '<Response [504]>':
                return  
            if str(r) == '<Response [404]>':
                print('Страница не найдена')
                return 
            if str(r) == '<Response [400]>':
                return 
            if str(r) == '<Response [443]>':
                print('Проблемы с подключениемю. Проверьте интернет соединение')
                # time.sleep(random.randrange(1,5))
                counterExceptions +=1
                if counterExceptions >1:
                    return
                else:                    
                   continue 
               
        except Exception as ex:
            return
        try:
            soup = BeautifulSoup(r.content, "html.parser")
            soup2 = BeautifulSoup(r.text, "lxml")
            dom = etree.HTML(str(soup)) 
        except:
            return
        try:                   
            gf = dom.xpath('//*[@id="search"]/span/div/h1/div/div[1]/div/div/span[1]//text()')[0] 
            # print(gf)            
            try:    
                quanityTargetItems = int(gf)
            except:
                try:
                    quanityTargetItems = int(gf.split(' ')[0])
                except:                                     
                    try:                
                        quanityTargetItems = int(gf.split(' ')[0].split('-')[1])                                           
                    except Exception as ex:
                        print(f"что-то не так с quanityTargetItems Amazon{ex}")
                        return
        # print(quanityTargetItems)
        
        except Exception as ex:
            # print(f" str 616  {ex}")
            return
            # return

        
        if quanityTargetItems > 50:
            quanityTargetItems = 50        
        try: 
            # try:                
            #     resultProto = [] 
                                           
            #     for i in range(quanityTargetItems):
            #         targetLinkPattern = 'https://www.amazon.com'                     
            #         targetLink = ''
            #         targetPrice  = ''
            #         titleCritery = ''
            #         asin = '' 
            #         if i == 0:
            #             try:
            #                 try:
            #                     targetLink = dom.xpath(f'//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[2]/div/div/div/div/div[2]/div[1]/h2/a')[0].get('href')                        
            #                     # 
            #                     # print(targetLink)
            #                 except Exception as ex:
            #                     pass
            #                     # print(f"636 {ex}")
            #                 try:
            #                     titleCritery1Arr = []
            #                     titleCritery1Arr = eval(str(dom.xpath(f'//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[2]/div/div/div/div/div[2]/div[1]/h2/a/span//text()')))[0]
                            
            #                     titleCritery1Arr = titleCritery1Arr.split(' ')
            #                     # print(titleCritery1Arr)
            #                     for it in titleCritery1Arr:       
            #                         it = it.lower()
            #                         if it == model or it == model[:-1]:
            #                             titleCritery = model
            #                             break                                           
            #                     # print(titleCritery) 

            #                     # print(titleCritery)
            #                     # //*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[2]/div/div/div/div/div[2]/div[1]/h2/a/span
            #                     # //*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/div/div/div[2]/div[1]/h2/a/span
            #                     # //*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[4]/div/div/div/div/div[3]/div[1]/h2/a/span

            #                     # //*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[6]/div/div/div/div/div[2]/div[1]/h2/a/span
            #                 except Exception as ex:
            #                     pass
            #                     # print(f"643 {ex}")
            #                 try:
            #                     targetPrice = dom.xpath(f'//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[2]/div/div/div/div/div[2]/div[3]/div/a/span[1]/span[1]//text()')[0]
            #                     # //*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[2]/div/div/div/div/div[2]/div[3]/div/a/span[1]/span[1]
            #                     # //*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[6]/div/div/div/div/div[2]/div[3]/div/a/span[1]/span[1]
            #                     # //*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[7]/div/div/div/div/div[2]/div[3]/div/a/span/span[1]
            #                 #    //*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[8]/div/div/div/div/div[2]/div[3]/div/a/span[1]/span[1]
            #                     # print(targetPrice)
            #                 except Exception as ex:
            #                     pass
            #                     #  print(f"649 str{ex}") 
            #                 try:                           
            #                     asinArr = targetLink.split('/')                           
                                
            #                     for i, a in enumerate(asinArr):
            #                         if asinArr[i] == 'dp':
            #                             asin = asinArr[i+1]
            #                 except Exception as ex:
            #                     #  print(f"657 str{ex}")
            #                     pass
                         
            #                 resultProto.append({
            #                     "targetLink": str(f"{targetLinkPattern}{targetLink}").strip(),
            #                     "titleCritery": str(titleCritery.strip()),
            #                     "targetPrice": str(targetPrice).strip(),
            #                     "asin": str(asin).strip()
            #                 })

            #             except Exception as ex:
            #                 pass
            #                 # print(f"667 str{ex}")

            #         else:                        
            #             try:
            #                 try:
            #                     targetLink = dom.xpath(f'//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[{i+2}]/div/div/div/div/div[2]/div[1]/h2/a')[0].get('href')
            #                     # //*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[2]/div/div/div/div/div[2]/div[1]/h2/a
            #                     # //*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/div/div/div[2]/div[1]/h2/a
            #                     # //*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[4]/div/div/div/div/div[3]/div[1]/h2/a
            #                     # //*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[6]/div/div/div/div/div[2]/div[1]/h2/a
            #                     # print(f"str 673: {targetLink}")
            #                     # print(targetLink)
            #                 except Exception as ex:
            #                     pass
            #                     # print(f"675 str{ex}")                               
                                
            #                 try:
            #                     titleCritery1Arr = []
            #                     titleCritery1Arr = eval(str(dom.xpath(f'///*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[{i+2}]/div/div/div/div/div[2]/div[1]/h2/a/span//text()')))[0]                                 
                                
            #                     titleCritery1Arr = titleCritery1Arr.split(' ')
            #                     # print(titleCritery1Arr)
            #                     for it in titleCritery1Arr:       
            #                         it = it.lower()
            #                         if it == model or it == model[:-1]:
            #                             titleCritery = model
            #                             break                                           
            #                     # print(titleCritery) 

            #                 except Exception as ex:
            #                     pass
            #                     # print(f"682 str{ex}")
                                
            #                 try:                      
            #                     targetPrice = dom.xpath(f'//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[{i+2}]/div/div/div/div/div[2]/div[3]/div/a/span[1]/span[1]//text()')[0]
                                
            #                     # print(f"str 277: {targetPrice}")
            #                 except Exception as ex:
            #                     pass
            #                     # print(f"689 str{ex}")
            #                 try:                       
            #                     asinArr = targetLink.split('/')
            #                     for i, a in enumerate(asinArr):
            #                         if asinArr[i] == 'dp':
            #                             asin = asinArr[i+1]
            #                     # print(asin)
                                
            #                 except Exception as ex:
            #                     pass
            #                     # print(f"697 str{ex}")
                           
            #                 resultProto.append({
            #                     "targetLink": str(f"{targetLinkPattern}{targetLink}").strip(),
            #                     "titleCritery": str(titleCritery.strip()),
            #                     "targetPrice": str(targetPrice).strip(),
            #                     "asin": str(asin).strip()
            #                 })
                        
            #                 if len(resultProto) == quanityTargetItems:                                
            #                     break
            #             except:
            #                 # print(f"707 {ex}")
            #                 pass
           
                        
            # except Exception as ex:
            #     # print(ex)
            #     pass
            # if len(resultProto) == 1:
            #     if resultProto[0]['asin'] == '' or resultProto[0]['asin'] == None:                    
            #         flagEx1 = True               
                                        
            # elif len(resultProto) > 1:
            #     if resultProto[1]['asin'] == '' or resultProto[1]['asin'] == None:
            #         flagEx1 = True 
            # print(f" str 316{resultProto}")           
            # if flagEx1 == False:
                resultProto = []
                # flagEx1 == False                
                # print('case 2')
                firstBlock = soup2.find_all('div', attrs= {'class': 'a-row', 'class': 'a-size-base', 'class': 'a-color-base'})
                # print(f"f bloc len: {len(firstBlock)}")

                for f, x in enumerate(firstBlock):
                    targetLinkPattern = 'https://www.amazon.com'                                         
                    targetLink = ''
                    targetPrice  = ''
                    titleCritery = ''

                    try:
                        targetPrice = x.find('span', class_= 'a-offscreen').get_text()
                        # print(targetPrice)    
                    except:
                        pass  
                    try:              
                        targetLink = x.find_next().get('href')                 
                        # print(targetLink) 
                    except:
                        pass

                    # python eScraperNew.py
                    try:
                        titleCritery1Arr = []
                        titleCritery1Arr = targetLink.split('/')[1].split('-')
                        for it in titleCritery1Arr:       
                            it = it.lower()
                            if it == model or it == model[:-1]:
                                titleCritery = model
                                break                                           
                        # print(titleCritery) 
                    except:
                        # print('ex2')
                        pass
                    try:                       
                        asinArr = targetLink.split('/')
                        for i, a in enumerate(asinArr):
                            if asinArr[i] == 'dp':
                                asin = asinArr[i+1]                                               
                    except:
                        pass
                   
                    resultProto.append({
                        "targetLink": str(f"{targetLinkPattern}{targetLink}").strip(),
                        "titleCritery": str(titleCritery.strip()),
                        "targetPrice": str(targetPrice).strip(),
                        "asin": str(asin).strip()
                    })                  

                    # print(f" str 364{resultProto}")                       
                    if len(resultProto) == quanityTargetItems:                                               
                        break
                if len(resultProto) == 1:
                    if resultProto[0]['asin'] == '' or resultProto[0]['asin'] == None:                    
                        flagEx1 = True               
                                            
                elif len(resultProto) > 1:
                    if resultProto[1]['asin'] == '' or resultProto[1]['asin'] == None:
                        flagEx1 = True         
                if flagEx1 == True:         
                    counterRetry += 1
                    if counterRetry > 1:
                        return
                    else:
                        time.slep(random.randrange(1,4))
                        continue   
    
        except Exception as ex:
            # print(ex)
            pass
                
        finally:           
            finResult.append({                
                "urlEbayItem": total["urlItem"],
                "title": total["title"],
                "price": total['price'],
                "quanity": total['quanity'],
                "delivery": total['delivery'],
                "brand": total['brand'],
                "model": total['model'],                
                "amazonBlock": resultProto,                               
            })
            # print(finResult)
            # print('yes')
            try:
                return finResult[0]
            except:
                return
 
# //////////////////////////////////////////////////////////////////

def hendlerLinks(link):
    result = []
    upc = ''
    agrForEbey = 'ebay.com'        
    dNotApl = 'does not apply'
    notAv = 'not available'
    # print('start handler')

    try:            
        r = sessionReq(link, agrForEbey)          
        # print(f"ответ обработчика ссілок Ебей:  {r}")
        if str(r) == '<Response [503]>':
            
            # time.sleep(random.randrange(1,5))
            return

        if str(r) == '<Response [403]>':
            
            # time.sleep(random.randrange(1,7))
            return

        if str(r) == '<Response [504]>':
            return  
        if str(r) == '<Response [404]>':
            return 
        if str(r) == '<Response [400]>':
            return 
        if str(r) == '<Response [443]>':
            return

                        
        soup = BeautifulSoup(r.text, "lxml")           
        priceChecer = soup.find('div', class_='x-price-primary').find('span', class_='ux-textspans').get_text().strip()
        price = ''
        try:
            price = soup.find('div', class_='x-price-primary').find('span', class_='ux-textspans').get_text().strip()
        except:   
            price = ''             
            # print(f"price ex: {k}")
        title = ''
        try:
            title = soup.find('h1', class_='x-item-title__mainTitle').find('span', class_='ux-textspans').get_text().strip()
        except:
            # print(f"title ex: {k}")
            title = ''
    
        quanity = ''            
        try:
            quanity = soup.find('span', id='qtySubTxt').find('span').get_text().strip()
        except:
            try:
                quanity = soup.find('span', id='qtySubTxt').find('span').find('span').get_text().strip()
            except:
                # print(f"quanity2 ex: {k}")
                quanity = ''
            quanity = ''
            # print(f"quanity ex1: {k}") 
            
        delivery_text = ''
        try:
            delivery = soup.find('div', class_='ux-labels-values--deliverto').find('div', class_='col-9').find('div').find_all('span', class_='ux-textspans--BOLD')
            delivery_text = f"Estimated between {delivery[0].get_text()} and {delivery[1].get_text()}"
            for dell in delivery[0:-2]:
                delivery_text += dell.get_text()                    
        except:
            # print(f"delivery ex: {k}") 
            delivery = ''
            
        # /////////////////// brand
        brand = ''
         
        try:
            brand = soup.find(attrs={'itemprop': 'brand'}).find('span', class_='ux-textspans').get_text().strip()                
        except:                       
            try:
                CompatibleBrand = soup.find_all('div', class_='ux-layout-section__row')
                cpBrd = 'compatible brand'     

                for row in CompatibleBrand:
                    section = row.find_all('span', class_='ux-textspans')
                    for j, compBrand in enumerate(section):                                        
                        try:
                            try:
                                sec = (f"{section[j].get_text().strip()}").lower() 
                            except:
                                sec = section[j].get_text().strip()
                                         
                            match = re.search(f'{r}"{cpBrd}"', sec)
                            if match:
                                brand = section[j+1].get_text().strip() 
                                break 
                        except: 
                            continue                                             
            except:
                brand = ''
                 
        brand_namePatern = ''            
        try:
            brdArr = brand.split(' ')
            if len(brdArr) >1:                                
                for itBrN in brdArr:
                    brand_namePatern += itBrN + '+'
                brand = brand_namePatern[0:len(brand_namePatern)-1]
            else:
                pass
                
        except:
            pass         
            
        # /////////////////////////////////////////////////////////// brand
        model = ''
        try:
            model = soup.find(attrs={'itemprop': 'mpn'}).find('span', class_='ux-textspans').get_text().strip()                   
        except:           
            try:
                model = soup.find(attrs={'itemprop': 'model'}).find('span', class_='ux-textspans').get_text().strip()                   
            except:
                model = ''
            
        model_itemPatern = ''            
        try:
            modelArr = model.split(', ')
            if len(modelArr) >1:
                               
                for itModN in modelArr:
                    model_itemPatern += itModN + '+'
                model = model_itemPatern[0:len(model_itemPatern)-1]
            else:
                pass                
        except:
               pass 
        try:
            mod = ''
            mod = model.lower()            
        except:
            mod = model                     

        if model == '' or mod == dNotApl or mod == notAv:
           model = ''  

        # ////////////////////////////////////////////////////////////////////////// upc
         
        upc = ''
        try:
            upc = soup.find(attrs={'itemprop': 'gtin13'}).find('span', class_='ux-textspans').get_text().strip()                         
        except Exception as ex:          
            try:   
                upc = soup.find_all('div', class_='ux-layout-section__row')
                upcUpc = 'upc'
                
                for row in upc:
                    section = row.find_all('span', class_='ux-textspans')
                    for j, upcc in enumerate(section):
                                            
                        try:
                            try: 
                               ses = (f"{section[j].get_text().strip()}").lower()
                            except:
                                ses = section[j].get_text().strip()
                                       
                            match = re.search(f'{r}"{upcUpc}"', ses)
                            if match:
                                upc = section[j+1].get_text().strip()                               
                                break
                        except: 
                            continue
            except:
                upc = ''                                                                    
        try:
            up = ''
            up = upc.lower()            
        except:
            up = upc
 
        if upc == '' or up == dNotApl or up == notAv:
           upc = ''
        else:
            try:
                int(upc[1]) 
                upc = upc 
            except:
                try:
                    int((upc.split(', ')[0])[1])
                    upc = upc.split(', ')[0]
                except:
                    upc = ''
                    
        # ////////////////////////////////////////////////////////////////////////// upc 
            
        linkSrchAmazon = ''
        
        try:
            if upc != '' and model != '':
               linkSrchAmazon = f"https://www.amazon.com/s?k={brand}+{model}+{upc}"
            elif upc != '' and model == '':
                linkSrchAmazon = f"https://www.amazon.com/s?k={brand}+{upc}"
                
            elif upc == '' and model != '':
                linkSrchAmazon = f"https://www.amazon.com/s?k={brand}+{model}"
            else:
                linkSrchAmazon = ''                
                
        except: 
            pass

        result.append({
            "urlItem": link,
            "title": str(title),
            "price": str(price),                
            "quanity": str(quanity),
            "delivery": str(delivery_text),
            "brand": str(brand),            
            "model": str(model),
            "upc": str(upc),
            "linkSrchAmazon": f"{str(linkSrchAmazon)}",                          
        })  
                
    except Exception as ex:
        # print(f" error str 443:  {ex}")
        pass     
    finally:
        # print(result[0])
        # if result[0] is None:        
        #     return 
        # else:
        try: 
           return linksHandlerAmazon(result[0])
        except:
            return

# //////////////////////////////////////////////////////////////////////

async def gather_registrator_eBay(hrefsBlockPagination):
    global hrefsBankVar   
    async with aiohttp.ClientSession() as session:       
        tasks = [] 
        for href in hrefsBlockPagination:
            task = asyncio.create_task(linkerCapturerEbay(href))
            tasks.append(task)
        await asyncio.gather(*tasks) 
      
    gather_Linker_Ebay(hrefsBankVar)
    hrefsBankVar = []

# /////////////////////////////////////////////////////////////////////////////
def gather_Linker_Ebay(hrefsBank):
    # global start_time
    print(f"Количество ссылок для обработки: {len(hrefsBank)}")
    hrefsBank = list(filter(None, hrefsBank))
    # prepTime = time.time() - start_time 
    # print(f"Prep time:  {prepTime}")
    # n = multiprocessing.cpu_count() * 10  
    n = 21
    # 21 для моего  # 
    with WorkerPool(n_jobs = n) as p2:                      
        finRes = p2.map(hendlerLinks, hrefsBank)
        print(len(finRes))
        writerr(finRes) 
        hrefsBank = [] 
        finRes = []
                
# /////////////////////////////////////////////////////////
# amazon start

# python eScraperNew.py

# amazon finish
# ////////////////////////////////////////////////////////////////////////////////////////

# ////////////////////////////////////////////////////////////////////////////////////////
# писатель результатов старт


# class GoogleSheet:
#     SPREADSHEET_ID = '1E8ApONqNaH9EXH8eeyOssTC2RNDRFyZ7njVucOnRNPs'
#     SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
#     service = None

#     def __init__(self):
#         creds = None
#         if os.path.exists('token.pickle'):
#             with open('token.pickle', 'rb') as token:
#                 creds = pickle.load(token)

#         if not creds or not creds.valid:
#             if creds and creds.expired and creds.refresh_token:
#                 creds.refresh(Request())
#             else:                
#                 flow = InstalledAppFlow.from_client_secrets_file(
#                     'credentials.json', self.SCOPES)
#                 creds = flow.run_local_server(port=0)
#             with open('token.pickle', 'wb') as token:
#                 pickle.dump(creds, token)

#         self.service = build('sheets', 'v4', credentials=creds)

#     def updateRangeValues(self, range, values):
#         data = [{
#             'range': range,
#             'values': values
#         }]
#         body = {
#             'valueInputOption': 'USER_ENTERED',
#             'data': data
#         }
#         result = self.service.spreadsheets().values().batchUpdate(spreadsheetId=self.SPREADSHEET_ID, body=body).execute()        

def writerr(total):
    print('Запись результатов')
    global total_count
    # global list_name    
    # gs = GoogleSheet()   
    
    total = list(filter(None, total)) 
    total = list(filter(lambda item: item['amazonBlock'] != [], total))
    total = list(filter(lambda item: item['amazonBlock'] != '', total))
    
    for item in total:
        item['amazonBlock'] = list(filter(lambda it: it['asin'] != '', item['amazonBlock']))
    for item in total:
        amazonLink = ''
        amazonPrice = ''
        amazonAsin = ''
        if len(item['amazonBlock']) > 1:
            item['amazonBlockNew'] = list(filter(lambda it: it['titleCritery'] != '', item['amazonBlock']))
            if len(item['amazonBlockNew']) == 0:
                item['amazonBlock'] = item['amazonBlock'][0:7] 
            else:              
                item['amazonBlock'] = item['amazonBlockNew']                   
            del item['amazonBlockNew']
      
        for it in item['amazonBlock']:
            if len(item['amazonBlock']) == 0:
                try:
                    amazonLink = it['targetLink'] + '\n'
                    amazonPrice = it['targetPrice'] + '\n'
                    amazonAsin = it['asin'] + '\n'
                except:
                    pass
                break
            else:
                try:
                    amazonLink += it['targetLink'] + '\n'
                    amazonPrice += it['targetPrice'] + '\n'
                    amazonAsin += it['asin'] + '\n'
                except:
                    pass
        item['amazonLink'] = amazonLink
        item['amazonPrice'] = amazonPrice
        item['amazonAsin'] = amazonAsin
                                
        del item['amazonBlock']                   
        
    # total = list(filter(lambda item: item['amazonBlock'] != [], total))    
    total_count = len(total) 
    now = datetime.now() 
    curentTimeForFile = now.strftime("%m_%d_%Y__%H_%M")     

    with open(f'Result_{curentTimeForFile}.json', "a", encoding="utf-8") as file: 
        json.dump(total, file, indent=4, ensure_ascii=False)

    with open(f'Result_{curentTimeForFile}.csv', 'w', newline='', encoding='cp1251', errors="ignore") as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Ссылка на eBay маназин','Название товара', 'Цена', 'Наличие на складе', 'Дата доставки', 'Бренд', 'Модель', 'Ссылка на соответствующий товар на Amazon', 'Цена на Amazon', 'Асин'])
        for item in total:
            writer.writerow([item['urlEbayItem'], item ['title'], item['price'], item['quanity'], item['delivery'], item['brand'], item['model'], item['amazonLink'], item['amazonPrice'], item['amazonAsin']])      
    time.sleep(1)
    # with open(f'Result_{curentTimeForFile}.json', encoding="utf-8") as file: 
    #     total = json.load(file)

    # test_range = f'{list_name}!A2:J{len(total)+1}'   
    # test_values = [[] for i in range(0,len(total))]
    # for i, item in enumerate(total):
    #    test_values[i] = [item['urlEbayItem'], item['title'], item['price'], item['quanity'], item['delivery'], item['brand'], item['model'], item['amazonLink'], item['amazonPrice'], item['amazonAsin']]
    # gs.updateRangeValues(test_range, test_values) 
    if len(total) == 0:
        print('Упс! Что-то пошло не так...')
    total = []
    
# # /////////////////////////////   
# # писатель результатов финиш 

# ///////////// инпут

def reciveInput():
    global list_name
    url = input('Введите адрес магазина', )
    # list_name = input('Создайте и введите название страницы Гугл Таблицы', )   
    print('Старт...') 
    paginationReply(url)
    
# ////////////////////////// инпут финиш

# # функция запуска скрипта
# # ////////////////////////////////

def main():
    global total_count
    global start_time
    
    reciveInput()            
    finish_time = time.time() - start_time
    print(f"Общее время работы парсера:  {math.ceil(finish_time)} сек")
    print(f"Количество мультипроцессов:  {multiprocessing.cpu_count() *2}")
    print(f"Общее количество товаров:  {total_count}")
    sys.exit()
    
if __name__ == "__main__":
    main()

# python eScraperNew.py 
 

# pip install aiohttp
# pip install mpire    
# pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

# если не получается запушить
# git config --global push.autoSetupRemote true
# git push


# ur = 'https://www.ebay.com/sch/i.html?_dkr=1&iconV2Request=true&_blrs=recall_filtering&_ssn=worxtools&store_cat=0&store_name=worxlawnandgardenequipment&_oac=1'
# url = 'https://www.ebay.com/sch/i.html?_dkr=1&iconV2Request=true&_blrs=recall_filtering&_ssn=worxtools&store_cat=0&store_name=worxlawnandgardenequipment&_oac=1'



