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
import aiohttp
import asyncio
from datetime import datetime
import sys 
from fake_useragent import UserAgent 
import agVar 
from agVar import *

hrefsBankVar = []
itemsCount = 0 
total_count = 0
yellowInfo = False

with open("proxyE.txt", encoding="utf-8") as f1:
    PROXY_LIST = []
    prLiE = ''.join(f1.readlines()).split('\n')
    prLiE = list(i.strip() for i in prLiE)
    prLiE = list(filter(lambda item: item != '', prLiE))    
    for _ in range(2):
        random.shuffle(prLiE)
        PROXY_LIST += prLiE 
with open("proxyAm.txt", encoding="utf-8") as f2:    
    prLiAm = ''.join(f2.readlines()).split('\n')
    prLiAm = list(i.strip() for i in prLiAm)
    prLiAm = list(filter(lambda item: item != '', prLiAm))

def random_headers(argLink):    
    global yellowInfo
    if yellowInfo == True:
       agVar.agRestart() 
 
    if argLink == 'ebay.com':        
       uaG = choice(agVar.uagEbay())
    else: 
        uaG = choice(agVar.uagAmazon())   
            
    device_memoryHelper = [2,4,8,16,32]
    sett = set()
    finHeaders = []
    headFront = [{
            'authority': f"www.{argLink}",
            'accept': choice(agVar.desktop_accept), 
            'User-Agent': uaG,           
            'accept-language': choice(agVar.aceptLengv),           
            'origin': f'https://www.{argLink}',
            'device-memory': f'{choice(device_memoryHelper)}'                      
            }]
    headersHelper = [       
            {"sec-fetch-dest": "empty"},
            {"sec-fetch-mode": "cors"},
            {"sec-fetch-site": "same-origin"},
            {"accept-ch": "sec-ch-ua-model,sec-ch-ua-platform-version,sec-ch-ua-full-version"},
            {'cache-control': 'no-cache'},
            {'content-type': 'application/json'},
            {'rtt': '200'},
            {"ect": "4g"},
            {'sec-fetch-user': '?1'},
            {"viewport-width": "386"},
            # {'accept-encoding': 'gzip, deflate, br'},
            {'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"'},
            {'upgrade-insecure-requests': '1'}
    ]
    headersHelperFormated = []
    strr = ''
    for i in headersHelper[0:len(headersHelper)-random.randrange(0,len(headersHelper))]:
        strr += ((str(choice(headersHelper)))[1:-1]).strip() + ',' + ' '  
         
    sett.add(strr)    
    headersHelperFormated = list(sett)    
    finHeaders = headFront + headersHelperFormated
    finHeaders[1] = eval("{" + finHeaders[1] + "}")    
    finfin = finHeaders[0]|finHeaders[1]    
    return finfin 

def proxyGenerator(proxArg):
    if proxArg == '':
        proxiess = {       
            "https": f"http://{choice(PROXY_LIST)}",            
            "socks5": f"http://{choice(PROXY_LIST)}"   
        }
    else:
        proxiess = {       
            "https": f"http://{proxArg}",            
            "socks5": f"http://{proxArg}"   
        }
        
    return proxiess

def paginationReply(url, determinantChanell):
    global start_time         
    lastPagin = 0
    agrForEbey = 'ebay.com'
    proxArg = ''
            
    try:
        if determinantChanell == 2:           
            r = requests.get(url, headers=random_headers(agrForEbey), proxies=proxyGenerator(proxArg), timeout=(9.15, 30.15))             
        else:
            r = requests.get(url, headers=random_headers(agrForEbey), timeout=(9.15, 30.15))      
        if str(r) == '<Response [200]>':
            print('Первый ответ сервера положительный')
        if str(r) == '<Response [503]>':            
            print('Хм, 503-я ошибка уже на старте!.. Хорошее начало!) Попробуйте еще раз!')
            sys.exit()

        if str(r) == '<Response [403]>':
            print('Сервер отверг запрос')
            sys.exit()

        if str(r) == '<Response [504]>':
            return  
        if str(r) == '<Response [404]>':
            print('Страница не найдена. Проверьте правильность url')
            sys.exit()
         
        try:    
            soup = BeautifulSoup(r.text, "lxml")
        except:
            pass            
        try:
            ptest = soup.find('h1', class_='srp-controls__count-heading')
            ptest = int(soup.find('h1', class_='srp-controls__count-heading').get_text().split(' ')[0].replace(',', '').replace('+', ''))
            lastPagin = math.ceil(int(ptest)/240)
        except Exception as ex: 
            pass           

    except Exception as ex:
        print('Упс! Что-то пошло не так...')
        return
            
    print(f"Всего в магазине товаров: {ptest}")       
    print(f"Всего страниц пагинации: {lastPagin}")        
    paginLimit = input('Введите лимит пагинации через дефис, например, 10-20', )
    if paginLimit == '' or paginLimit == ' ':
        hrefsBlockPagination = list(f"{url}&_ipg=240&_pgn={i}" for i in range(1, lastPagin+1))        
        start_time = time.time()  
        asyncio.run(gather_registrator_eBay(hrefsBlockPagination, determinantChanell))
        return    
    else:        
        try:
            startPagin = int((paginLimit.strip()).replace(' ', '').split('-')[0])
            finPagin = int((paginLimit.strip()).replace(' ', '').split('-')[1])
        except:            
            print(f'Выбрано значение по умолчанию 1-{lastPagin}')
            hrefsBlockPagination = list(f"{url}&_ipg=240&_pgn={i}" for i in range(1, lastPagin+1))
            start_time = time.time()  
            asyncio.run(gather_registrator_eBay(hrefsBlockPagination, determinantChanell))
            return     
                
        if lastPagin > finPagin and finPagin !=0:
            if startPagin == 0:
                startPagin = 1 
            hrefsBlockPagination = list(f"{url}&_ipg=240&_pgn={i}" for i in range(startPagin, finPagin+1))               
        else:
            hrefsBlockPagination = list(f"{url}&_ipg=240&_pgn={i}" for i in range(1, lastPagin+1))
            
    start_time = time.time()  
    asyncio.run(gather_registrator_eBay(hrefsBlockPagination, determinantChanell))            

async def linkerCapturerEbay(href, determinantChanell): 
    global hrefsBankVar
    proxArg = ''
    agrForEbey = 'ebay.com'   
    
    for _ in range(5):
        
        try:  
            if determinantChanell == 2:           
               r = requests.get(href, headers=random_headers(agrForEbey), proxies=proxyGenerator(proxArg), timeout=(9.15, 30.15))             
            else:
               r = requests.get(href, headers=random_headers(agrForEbey), timeout=(9.15, 30.15))          
            
            if str(r) == '<Response [503]>':
                print('Желтая карточка от сборщика ссылок')                                
                time.sleep(random.randrange(1,3))
                continue
            if str(r) == '<Response [403]>':
                return
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
                if hrefs is None:
                   time.sleep(random.randrange(1,3))
                   continue
                else:           
                    for item in hrefs:
                        try:                   
                           hrefsBankVar.append(item.get('href'))
                        except:
                            continue
                return
            except:
                time.sleep(random.randrange(1,4))
                continue

        except Exception as ex:
            time.sleep(random.randrange(1,4))
            continue

def linksHandlerAmazon(total):
    global yellowInfo
    agrForAmazon = 'amazon.com'    
    targetLinkPattern = 'https://www.amazon.com'   

    if total is None or total['linkSrchAmazon1'] == '':
        return
    try:
        model = f"{total['model']}".lower()
    except:
        pass 
    try:
        proxArg = total['proxArg']
    except:
        proxArg = ''
    try:
        determinantChanell = int(total["determinantChanell"])
    except:
        determinantChanell = '' 
 
    # time.sleep(random.randrange(1, 10))
    for sesCountt in range(2):
        flagSess = False

        try:
            link = total['linkSrchAmazon1']
        except:
            return 

        resultProto = []             
        finResult = []                                   
        quanityTargetItems = 0         
        k = 2 / random.randrange(1, 5)
        m = 1 / random.randrange(1, 11)
        g = random.randrange(1, 5)
        n = round(g + k + m, 2) 
        time.sleep(n)

        try:               
            if determinantChanell == 2:           
               r = requests.get(link, headers=random_headers(agrForAmazon), proxies=proxyGenerator(proxArg), timeout=(9.15, 30.15))             
            else:
               r = requests.get(link, headers=random_headers(agrForAmazon), timeout=(9.15, 30.15))
          
            if str(r) == '<Response [200]>':
                yellowInfo = False
                
            if str(r) == '<Response [503]>':
                print(f'Желтая карточка от Amazon. Текущее прокси: {proxArg} (см файл proxyAm.txt)')
                yellowInfo = True 
                proxArg = ''
                if sesCountt == 1:           
                    return
                else:
                    continue               
            if str(r) == '<Response [403]>':
                print('Amazon отверг запрос')
                return

            if str(r) == '<Response [504]>':
                return  
            if str(r) == '<Response [404]>':
                print('Страница не найдена')
                return 
            if str(r) == '<Response [400]>':
                return 
            if str(r) == '<Response [443]>':
                print('Проблемы с подключением...')                                
                pass 
               
        except Exception as ex:
            # print(f" str 300  {ex}")
            pass
        try:
            soup = BeautifulSoup(r.content, "html.parser")
            soup2 = BeautifulSoup(r.text, "lxml")
            dom = etree.HTML(str(soup)) 
        except:
            # print(f" str 307  {ex}")
            pass
        try:                   
            gf = dom.xpath('//*[@id="search"]/span/div/h1/div/div[1]/div/div/span[1]//text()')[0]         
            try:    
                quanityTargetItems = int(gf)
            except:                                             
                try:                                   
                    quanityTargetItems = int(gf.split(' ')[0].split('-')[1])                                           
                except Exception as ex:
                    pass
                    # print(f"что-то не так с количеством товаров Amazon  {ex}")                                        
        except:
            try:
                # print('case2 of quan items')
                gf2 = soup2.find('h1', attrs= {'class': 'a-size-base', 'class': 's-desktop-toolbar', 'class': 'a-text-normal'}).find('div', class_='sg-col-inner').find('div', attrs= {'class': 'a-section', 'class': 'a-spacing-small', 'class': 'a-spacing-top-small'}).find('span').get_text()
                # print(gf2)
                try:    
                    quanityTargetItems = int(gf2)
                except:                   
                    try:                                       
                        quanityTargetItems = int(gf2.split(' ')[0].split('-')[1])                                           
                    except Exception as ex:
                        # print(f"что-то не так с количеством товаров Amazon  {ex}")
                        pass 
            except Exception as ex:
                # print(f" str 332  {ex}")                      
                pass

        if quanityTargetItems > 50:
            quanityTargetItems = 50        
        try:
            resultProto = []
            firstBlock1 = soup2.find_all('div', attrs= {'class': 'a-row', 'class': 'a-size-base', 'class': 'a-color-base'})                      
            firstBlock2 = soup2.find_all('h2', attrs= {'class': 'a-size-mini', 'class': 'a-spacing-none', 'class': 'a-color-base', 'class': 's-line-clamp-2'})
                        
            for f, x in enumerate(firstBlock1):
                targetLinkPattern = 'https://www.amazon.com'                                         
                targetLink1 = ''
                targetPrice1  = ''
                titleCritery1 = ''
                asin1 = ''

                try:
                    targetPrice1 = x.find('span', class_= 'a-offscreen').get_text() 
                except:
                    pass  
                try:              
                    targetLink1 = x.find_next().get('href')
                except:
                    pass                    
                try:
                    titleCritery1Arr = []
                    titleCritery1Arr = targetLink1.split('/')[1].split('-')
                    
                    for it in titleCritery1Arr:       
                        it = it.lower()
                        if it == model or it == model[:-1]:
                            titleCritery1 = model
                            break                    
                        
                except:                        
                    pass
                try: 
                    asinArr = []                      
                    asinArr = targetLink1.split('/')
                    for i, a in enumerate(asinArr):
                        if asinArr[i] == 'dp':
                            asin1 = asinArr[i+1]                                               
                except:
                    pass
                if targetLink1 =='' or targetLink1 == None:
                    targetLink1 = ''
                if targetPrice1 == '' or targetPrice1 == None:
                    targetPrice1 = 'not found'
                if titleCritery1 =='' or titleCritery1 == None:
                    titleCritery1 = ''
                if asin1 == '' or asin1 == None:
                    asin1 = 'not found'
                resultProto.append({
                    "targetLink": f"{targetLinkPattern}{targetLink1}".strip(),
                    "targetPrice": targetPrice1.strip(),
                    "titleCritery": titleCritery1,                    
                    "asin": asin1.strip()
                })                                        
                if len(resultProto) == quanityTargetItems:                                               
                    break
                      
            for i, x in enumerate(firstBlock2):                                                                         
                targetLink2 = ''                              
                titleCritery2 = ''
                asin2 = ''
                
                try:              
                    targetLink2 = x.find('a').get('href')
                    # print(targetLink1)
                except Exception as ex:
                    # print(ex)
                    pass
                try:
                    asinArr = []                    
                    asinArr = targetLink2.split('/')
                    for i, a in enumerate(asinArr):
                        if asinArr[i] == 'dp':
                            asin2 = asinArr[i+1]
                            # print(asin2)                                               
                except:
                    pass
                try: 
                    titleCritery1Arr = []
                    titleCritery1Arr = x.find('span').get_text()              
                    titleCritery1Arr = titleCritery1Arr.split(' ')
                
                    for it in titleCritery1Arr:       
                        it = it.lower()
                        if it == model or it == model[:-1]:
                            titleCritery2 = model
                            if targetLink2 =='' or targetLink2 == None:
                                targetLink2 = ''
                            if titleCritery2 == '' or titleCritery2 == None:
                                titleCritery2 = ''
                            if asin2 == '' or asin2 == None:
                                asin2 = 'not found'
                            resultProto.append({
                                "targetLink": f"{targetLinkPattern}{targetLink2}".strip(),                            
                                "targetPrice": 'not found',
                                "titleCritery": titleCritery2,
                                "asin": asin2.strip()
                            })  
                            break                                           
                    
                except:
                    pass 
                if titleCritery2 == '':
                    try:
                        titleCritery1Arr = []
                        titleCritery1Arr = targetLink2.split('/')[1].split('-')
                        for it in titleCritery1Arr:       
                            it = it.lower()
                            if it == model or it == model[:-1]:
                                titleCritery2 = model
                                if targetLink2 =='' or targetLink2 == None:
                                    targetLink2 = ''
                                if titleCritery2 == '' or titleCritery2 == None:
                                    titleCritery2 = ''
                                if asin2 == '' or asin2 == None:
                                    asin2 = 'not found'                                
                                resultProto.append({
                                    "targetLink": f"{targetLinkPattern}{targetLink2}".strip(),                            
                                    "targetPrice": 'not found',
                                    "titleCritery": titleCritery2,
                                    "asin": asin2.strip()
                                })                              
                                break                         
                    except:                        
                        pass                        
            
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
            
            if len(resultProto) == 1:
                if resultProto[0]["targetLink"] == targetLinkPattern:                    
                   flagSess = True                              
                                        
            elif len(resultProto) > 1:
                if resultProto[1]["targetLink"] == targetLinkPattern:
                   flagSess = True 
    
        except Exception as ex:
            flagSess = True
            # print(f" str 392  {ex}")
        if flagSess == False:
            try:           
                return finResult[0]
            except:
                return 
        else:
            if sesCountt == 1:
                try:               
                    return finResult[0]
                except:
                    return
            else:
                continue 
        
def hendlerLinks(link):
    global yellowInfo
  
    agrForEbey = 'ebay.com'        
    dNotApl = 'does not apply'
    notAv = 'not available'
    try:
        arrArg = f"{link}".split('SamsonovNik')
        if len(arrArg) == 2:
            try:
               urlE = arrArg[0] 
            except:
                return
            try:
                determinantChanell = int(arrArg[1])
            except:
                determinantChanell = 1     
                
            proxArg = ''
            proxyAnswer = ''
            
        elif len(arrArg) == 4:
            try:
               urlE = arrArg[2] 
            except:
                return  
            try:         
               proxArg = arrArg[0]   
            except:
               proxArg = ''
            try:        
               proxyAnswer = arrArg[1]  
            except:
               proxyAnswer = ''
            try:
               determinantChanell = int(arrArg[-1]) 
            except:
               determinantChanell = 2    
        else:
            return
    except:
        return

    for sesCountt in range(2):
        result = [] 
        title = ''       
        price = ''      
        quanity = ''
        delivery = []
        delivery_main = ''       
        shippingArr = []
        shipping = ''
        brand = ''
        brand_namePatern = '' 
        model = ''
        upc = ''
        linkSrchAmazon1 = ''
        k = 1 / random.randrange(1, 5)
        m = 1 / random.randrange(1, 11)
        n = round(1.2 + k + m, 2) 
        time.sleep(n)
        try:            
            if determinantChanell == 2:           
               r = requests.get(urlE, headers=random_headers(agrForEbey), proxies=proxyGenerator(proxArg), timeout=(9.15, 30.15))             
            else:
               r = requests.get(urlE, headers=random_headers(agrForEbey), timeout=(9.15, 30.15))   
            if str(r) == '<Response [200]>':
                yellowInfo = False      
            if str(r) == '<Response [503]>':
                print(f'Желтая карточка от Ebay. Текущее прокси: {proxArg} (см файл proxyE.txt)')                         
                yellowInfo = True            
                proxArg = ''
                if sesCountt == 1:           
                    return
                else:
                    continue        

            if str(r) == '<Response [403]>':
                print('Ebay отверг запрос')
                return

            if str(r) == '<Response [504]>':
                return  
            if str(r) == '<Response [404]>':
                return 
            if str(r) == '<Response [400]>':
                return 
            if str(r) == '<Response [443]>':
                if sesCountt == 1:           
                    return
                else:
                    continue                        
            soup = BeautifulSoup(r.text, "lxml") 
            try:
                price = soup.find('div', class_='x-price-primary').find('span', class_='ux-textspans').get_text().strip()
            except:   
                price = ''        
            
            try:
                title = soup.find('h1', class_='x-item-title__mainTitle').find('span', class_='ux-textspans').get_text().strip()
            except:           
                title = ''        
                     
            try:
                quanity = soup.find('div', class_='d-quantity__availability').find('span').get_text().strip()                
            except:
                try:
                    quanity = soup.find('span', id='qtySubTxt').find('span').get_text().strip()                    
                except:
                    try:
                        quanity = soup.find('span', id='qtySubTxt').find('span').find('span').get_text().strip() 
                    except:                
                        quanity = ''                             
                
            try:
                delivery = soup.find('div', class_='ux-labels-values--deliverto').find('div', class_='col-9').find('div').find_all('span', class_='ux-textspans--BOLD')
                delivery_main = f"Estimated between {delivery[0].get_text()} and {delivery[1].get_text()}"
                for dell in delivery[0:-2]:
                    delivery_main += dell.get_text()                    
            except:
                try:
                    delivery = soup.find('div', class_='ux-labels-values--deliverto').find('div', class_='col-9').find('div').find_all('span', class_='ux-textspans')
                    delivery_main = f"Estimated between {delivery[0].get_text()} and {delivery[1].get_text()}"
                    for dell in delivery[0:-2]:
                        delivery_main += dell.get_text() 
                except: 
                    try:
                        delivery = soup.find('div', class_='ux-labels-values--deliverto').find('div', class_='col-9').find('div').find_all('span', class_='ux-textspans')
                        delivery_main = f"{delivery[0].get_text()}"
                    except Exception as ex:
                        # print(ex)                      
                        delivery_main = ''            

            try:
                shippingArr = soup.find('div', class_='ux-labels-values__values-content').find_all('span')
                for dell2 in shippingArr:
                    shipping += dell2.get_text().strip() + ' ' 

            except Exception as ex:
                # print(ex)
                pass
            try:
                delivery_main = delivery_main + '\n' + shipping   
                delivery_main = delivery_main.split('|')[0].strip()         
            except:              
                pass        
            
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
                       
            try:
                model = soup.find(attrs={'itemprop': 'model'}).find('span', class_='ux-textspans').get_text().strip()                                   
            except:           
                try:
                    model = soup.find(attrs={'itemprop': 'mpn'}).find('span', class_='ux-textspans').get_text().strip()                                       
                except:
                    model = ''
                
            model_itemPatern = ''            
            try:
                modelArr = model.split(', ')
                if len(modelArr) >1:
                                
                    for itModN in modelArr:
                        if itModN.lower() != 'ebay':
                           model_itemPatern += itModN + '+'
                    model = model_itemPatern[0:len(model_itemPatern)-1]
                else:
                    pass                
            except:
                pass 
            model_itemPatern2 = ''
            try:
                modelArr2 = model.split('-')
                if len(modelArr2) >1:
                                
                    for itModN in modelArr2:
                        if itModN.lower() != 'ebay': 
                           model_itemPatern2 += itModN + '+'
                    model = model_itemPatern2[0:len(model_itemPatern2)-1]
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

            try:
                if model != '':
                    linkSrchAmazon1 = f"https://www.amazon.com/s?k={brand}+{model}"
            except:
                pass
            try:
                if model == '' and upc != '':
                    linkSrchAmazon1 = f"https://www.amazon.com/s?k={brand}+{upc}"
            except:
                pass

            result.append({
                "urlItem": urlE,
                "title": str(title),
                "price": str(price),                
                "quanity": str(quanity),
                "delivery": str(delivery_main),
                "brand": str(brand),            
                "model": str(model),
                "upc": str(upc),
                "linkSrchAmazon1": f"{str(linkSrchAmazon1)}",                
                "proxArg": proxyAnswer,
                "determinantChanell": determinantChanell                       
            })  
                    
        except Exception as ex:
            # print(f'660 str {ex}')
            if sesCountt == 1:
                try: 
                    return linksHandlerAmazon(result[0])
                except:
                    return 
            else:
                continue 
        try: 
            return linksHandlerAmazon(result[0])
        except:
            return  

async def gather_registrator_eBay(hrefsBlockPagination, determinantChanell):
    global hrefsBankVar
    
    async with aiohttp.ClientSession() as session:       
        tasks = [] 
        for href in hrefsBlockPagination:
            task = asyncio.create_task(linkerCapturerEbay(href, determinantChanell))
            tasks.append(task)
        await asyncio.gather(*tasks)      
    if determinantChanell == 2:
       gather_Linker_Ebay2(hrefsBankVar, determinantChanell)
    else:
       gather_Linker_Ebay1(hrefsBankVar, determinantChanell)
    hrefsBankVar = []
    

def gather_Linker_Ebay2(hrefsBankArg, determinantChanell):    
    from mpire import WorkerPool   
    arrHelpE = [] 
    arrHelpAm = []   
    hrefsBankArg = list(filter(None, hrefsBankArg))         
    print(f"Собрано ссылок для обработки: {len(hrefsBankArg)}")   
    qCycleE = round(len(hrefsBankArg) / len(prLiE)) + 2
    qCycleAm = round(len(hrefsBankArg) / len(prLiAm)) + 2
    
    for _ in range(qCycleE):
        random.shuffle(prLiE)
        arrHelpE += prLiE 
    for _ in range(qCycleAm):
        random.shuffle(prLiAm)
        arrHelpAm += prLiAm
    hrefs = list(f"{arrHelpE[i]}SamsonovNik{arrHelpAm[i]}SamsonovNik{hrefsBankArg[i]}SamsonovNik{determinantChanell}" for i in range(len(hrefsBankArg)))

    n = 21    
    with WorkerPool(n_jobs = n) as p2:                      
        finRes = p2.map(hendlerLinks, hrefs)        
        writerr(finRes) 
        hrefsBankArg = [] 
        finRes = []
        arrHelpE = []
        arrHelpAm = []  
        hrefs 

def gather_Linker_Ebay1(hrefsBankArg, determinantChanell):      
    from mpire import WorkerPool          
    finResArr = [] 
    total = []    
    hrefsBankArg = list(filter(None, hrefsBankArg))         
    print(f"Собрано ссылок для обработки: {len(hrefsBankArg)}")
    hrefs = list(f"{hrefsBankArg[i]}SamsonovNik{determinantChanell}" for i in range(len(hrefsBankArg)))
    # n = multiprocessing.cpu_count() * 10  
    n = 21
    vpnFraction = random.randrange(75,125)
    for i in range(0, len(hrefsBankArg), vpnFraction):        
        n1 = i 
        n2 = i+vpnFraction
        if n2 > len(hrefsBankArg):
            n2 = len(hrefsBankArg)
        if n2 != len(hrefsBankArg) and i != 0:  
            yellowInput = input('Пожалуйста смените VPN', )
            if yellowInput:
                pass
        with WorkerPool(n_jobs = n) as p2:                      
            finRes = p2.map(hendlerLinks, hrefs[n1:n2])
            finResArr.append(finRes)           
            # time.sleep(random.randrange(63,79))            
    for item in finResArr:
        total +=item
    writerr(total)     
    hrefsBankArg = [] 
    finRes = []
  

def writerr(total):
   from itertools import groupby
   print('Запись результатов')
   global total_count 

   try:
      total = list(filter(None, total))  
      total = list(filter(lambda item: item["amazonBlock"] != '' and item["amazonBlock"] != [], total))
      total = [el for el, _ in groupby(total)]  
   except Exception as ex:
       pass
    #   print(f"36 {ex}")
   try:
      for item in total:
         item["amazonBlock"] = list(filter(lambda it: it["targetLink"] != 'https://www.amazon.com' and it["asin"] !='', item["amazonBlock"]))
         item["amazonBlock"] = [el for el, _ in groupby(item["amazonBlock"])] 
      for item in total:
         if len(item["amazonBlock"]) > 1:
               item["amazonBlockNew"] = list(filter(lambda it: it["titleCritery"] != '', item["amazonBlock"]))
               if len(item["amazonBlockNew"]) == 0:
                  item["amazonBlock"] = item["amazonBlock"][0:7] 
               else:              
                  item["amazonBlock"] = item["amazonBlockNew"]                   
               del item["amazonBlockNew"]            
         for it in item["amazonBlock"]:                     
               del it["titleCritery"] 

   except Exception as ex:
       pass
    #   print(f"54 {ex}")
     
   try:
      for item in total:
         dataI = set()
         dataIArr = []

         for i in range(len(item["amazonBlock"])):           
            for k in range(len(item["amazonBlock"])): 
               if k !=i: 
               
                  if item["amazonBlock"][i]["targetLink"] == item["amazonBlock"][k]["targetLink"] and item["amazonBlock"][i]["targetPrice"] == 'not found':
                    dataI.add(i)
                  if i == len(item["amazonBlock"]) -1 and item["amazonBlock"][i]["targetLink"] == item["amazonBlock"][k]["targetLink"] and item["amazonBlock"][i]["targetPrice"] == 'not found':
                    dataI.add(i)         
         dataIArr = list(dataI)        

         for m in dataIArr:
            item["amazonBlock"][m] = ''
         item["amazonBlock"] = list(filter(lambda ita: ita != '', item["amazonBlock"]))
   except Exception as ex:
    #   print(f"76 {ex}")
      pass   
            
   now = datetime.now() 
   curentTimeForFile = now.strftime("%d_%m_%Y__%H_%M") 
   try:       
      with open(f'Result_{curentTimeForFile}.json', "a", encoding="utf-8") as file: 
            json.dump(total, file, indent=4, ensure_ascii=False)
      try:        
            for item in total: 
               amazonLink = ''
               amazonPrice = ''
               amazonAsin = '' 
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
      except:
            pass
      
      with open(f'Result_{curentTimeForFile}.csv', 'w', newline='', encoding='cp1251', errors="ignore") as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(['Ссылка на eBay маназин','Название товара', 'Цена', 'Наличие на складе', 'Дата доставки', 'Бренд', 'Модель', 'Ссылка на соответствующий товар на Amazon', 'Цена на Amazon', 'Асин'])
            for item in total:
               writer.writerow([item['urlEbayItem'], item ['title'], item['price'], item['quanity'], item['delivery'], item['brand'], item['model'], item['amazonLink'], item['amazonPrice'], item['amazonAsin']]) 
   except:
      pass    
   total_count = len(total)    
   total = []

def determinantChanellFunc():
    determinantChanell = input('Выберите способ подключения: 1 - VPN; 2 - Proxy', )
    try:
        determinantChanell = int(determinantChanell.strip())
    except:        
        determinantChanell = 1
    return determinantChanell

def reciveInput():
    global start_time    
    determinantChanell = determinantChanellFunc()
    url = input('Введите адрес магазина', )
    url = url.strip() 
    start_time = time.time()    
    print('Старт...')    
    paginationReply(url, determinantChanell)
    
def main():
    global total_count
    global start_time
        
    reciveInput()            
    finish_time = time.time() - start_time    
    print(f"Общее время работы парсера:  {math.ceil(finish_time)} сек")
    if total_count == 0:
        print('Упс! Что-то пошло не так...')
    print(f"Общее количество товаров:  {total_count}")

    sys.exit()
    
if __name__ == "__main__":
    main()

# python mainScript.py  ---- запускает работу парсера
 
#  python -m venv venv ---- для настройки виртуального окружения
# venv\Scripts\activate ---- второй шаг для настройки вирт окружения, а также если слетело виртуальное окружение. если не помогает - в комбинации с вышеприведенной командой - сперва ту команду, затем эту

# для самой первой настройки виртуального окружения в системе Виндовс:
# - Открываем терминал PowerShell от админа.
# - Вставляем и запускаем - Set-ExecutionPolicy RemoteSigned
# - На вопрос отвечаем - A) 
# выбираем оболочку PowerShell в терминале редактора vs code

# python -m pip install --upgrade pip
# pip install requests_html
# pip install -U pip requests_html
# ... затем устанавл недостоющие библиотеки:
# pip install aiohttp
# pip install mpire 

# /////////////////////////////////ССЫЛКИ НА МАГАЗИНЫ
# https://www.ebay.com/sch/i.html?_dkr=1&iconV2Request=true&_blrs=recall_filtering&_ssn=worxtools&store_cat=0&store_name=worxlawnandgardenequipment&_oac=1
# https://www.ebay.com/sch/i.html?_dkr=1&iconV2Request=true&_blrs=recall_filtering&_ssn=paedistributing&store_cat=0&store_name=paedistributing&_oac=1&LH_PrefLoc=1&LH_ItemCondition=3&LH_BIN=1

# https://www.ebay.com/sch/i.html?_dkr=1&iconV2Request=true&_blrs=recall_filtering&_ssn=tool007tool&store_cat=0&store_name=tool007tool&_oac=1
# https://www.ebay.com/sch/i.html?_dkr=1&iconV2Request=true&_blrs=recall_filtering&_ssn=cpo-outlets&store_cat=0&store_name=cpooutlets&_oac=1&LH_ItemCondition=3
# https://www.ebay.com/sch/i.html?_dkr=1&iconV2Request=true&_blrs=recall_filtering&_ssn=we_are_tools&store_cat=0&store_name=wearetoolswarehouse&_oac=1
# https://www.ebay.com/sch/i.html?_dkr=1&iconV2Request=true&_blrs=recall_filtering&_ssn=nailgunaccessories1&store_name=nailgunaccessories1&_oac=1&LH_ItemCondition=3


