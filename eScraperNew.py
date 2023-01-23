from requests_html import HTMLSession
import requests
from bs4 import BeautifulSoup
import random 
from random import choice
import time
import random
import csv
import json
from lxml import etree
import math
import re
import multiprocessing
from fake_useragent import UserAgent
from datetime import datetime
import sys
start_time = time.time()
hrefsBankVar = []
uagent = UserAgent()
itemsCount = 0 
agrForAmazon = 'amazon.com'
agrForEbey = 'ebay.com'
adderLink = '&_ipg=240&_pgn=1'
total_count = 0 


ur = 'https://www.ebay.com/sch/i.html?_dkr=1&iconV2Request=true&_blrs=recall_filtering&_ssn=worxtools&store_cat=0&store_name=worxlawnandgardenequipment&_oac=1'
# url = 'https://www.ebay.com/sch/i.html?_dkr=1&iconV2Request=true&_blrs=recall_filtering&_ssn=worxtools&store_cat=0&store_name=worxlawnandgardenequipment&_oac=1'


# /////////////////////////////////ССЫЛКА НА МАГАЗИН


# ur = 'https://www.ebay.com/sch/i.html?_dkr=1&iconV2Request=true&_blrs=recall_filtering&_ssn=paedistributing&store_cat=0&store_name=paedistributing&_oac=1&LH_PrefLoc=1&LH_ItemCondition=3&LH_BIN=1'


# ////////////////////////////////////////////////////

adderLink = '&_ipg=240&_pgn=1'
url2 = f"{ur}{adderLink}"

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

with open("proxy.txt", encoding="utf-8") as file:
    PROXY_LIST = ''.join(file.readlines()).split('\n')
def proxyGenerator():
    proxiess = {
        "https": f"http://{choice(PROXY_LIST)}",
        "http": f"http://{choice(PROXY_LIST)}"     
    }
    return proxiess
def sessionReq(url1, shopArg):
    session = HTMLSession()
    session.trust_env = False    
    # r = session.get(url1, headers=random_headers(shopArg), timeout=(29, 57), proxies=proxyGenerator())
    r = session.get(url1, headers=random_headers(shopArg), timeout=(29, 77))
    return r

def paginationReply(url2): 
    # paginController = 0   
    lastPagin = 0
    agrForEbey = 'ebay.com' 
    print('Старт...')      
    try:
        r = sessionReq(url2, agrForEbey)          
        # print(r)
        if str(r) == '<Response [200]>':
            print('Первый ответ сервера положительный')
        if str(r) == '<Response [503]>':
            try:
                time.sleep(random.randrange(31,37))
                r = sessionReq(url2, agrForEbey)
            except:
                pass
        if str(r) == '<Response [403]>':
            try:
                time.sleep(random.randrange(69,87))
                r = sessionReq(url2, agrForEbey)
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
            print(ex)
                  
        print(f"Количество страниц пагинации: {lastPagin}")
            # print('exPagin and sec req')           
    except Exception as ex:  
        print(f"pagin:  {ex}")
        # paginController +=1
        # if paginController >1:
        #     print('Упс! Что-то пошло не так')
        #     return
        # else:
        #     paginationReply(url2)
    finally:
        try:
            gather_Registrtor_Ebay(lastPagin)
        except:
            return
    # except Exception as ex:
    #     print(f"problem gather registor, error: {ex}")
        

# ///////////////////////////////////////////////////////////////////////////////////

    
def linkerCapturerEbay(itemsCount): 
    global hrefsBankVar
    global ur   
    
    agrForEbey = 'ebay.com'
    try:
        linkk = f'{ur}&_ipg=240&_pgn={itemsCount+1}'
        r = sessionReq(linkk, agrForEbey)
        # print(f"linker response:  {r}") 
        if str(r) == '<Response [503]>':
            try:
                time.sleep(random.randrange(31,37))
                return
            except:
                pass
        if str(r) == '<Response [403]>':
            try:
                time.sleep(random.randrange(61,87))
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
            for i, item in enumerate(hrefs):
                if item is None:
                    continue 
                else:
                    hrefsBankVar.append(item.get('href'))     

                # if i % 40 == 0:                    
                #     time.slep(random.randrange(2,7))                 
                # if i % 120 == 0:                    
                #     time.slep(random.randrange(28,35))                
            # print(hrefsBankVar)            

        except:
            print(f'исключение на 226 стр') 
            return 
    except Exception as ex:
         print(f"linker capturer:  {ex}") 
    finally: 
        try:      
           return hrefsBankVar
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
            try:
                time.sleep(random.randrange(31,37))
                return
            except:
                pass
        if str(r) == '<Response [403]>':
            try:
                time.sleep(random.randrange(61,87))
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
                # model_item = modelArr[0]                
                for itModN in modelArr:
                    model_itemPatern += itModN + '+'
                model = model_itemPatern[0:len(model_itemPatern)-1]
            else:
                pass                
        except:
               pass 
        try:
            mod = model.lower()            
        except:
            pass                     

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
                # upcUpc = upcUpc.lower()
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
            up = upc.lower()            
        except:
            pass
 
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
        print(f" error str 443:  {ex}")
        return      
    finally:
        try:        
           return result[0]
        except:
            return

# //////////////////////////////////////////////////////////////////////

def gather_Registrtor_Ebay(lastPagin):
    hrefss = []
    if lastPagin > 5:
        n = 4
        # lastPagin = 3
    else:
        n = lastPagin    
    with multiprocessing.Pool(multiprocessing.cpu_count() * 3) as p1:
        
        hrefsBank = p1.map(linkerCapturerEbay, list(range(lastPagin)))
        # print('hahaha')
        # p1.close()
        # p1.terminate()
        # p1.join()  
    
    for c in hrefsBank:            
        if c is None:
            continue 
        else:
            hrefss += c
    hrefsBank = []            
    print(f"Количество ссылок для обработки: {len(hrefss)}")        
    gather_Linker_Ebay(hrefss)


# /////////////////////////////////////////////////////////////////////////////

def gather_Linker_Ebay(hrefsBank):
    # print('linker ebay')
    resNew = []
    
    with multiprocessing.Pool(multiprocessing.cpu_count() * 3) as p2:        
        res = p2.map(hendlerLinks, hrefsBank[11:21])
        # p2.close()
        # p2.terminate()
        # p2.join() 
    for c in res:                
        if c is None:
            continue
        else:
            resNew.append(c)
    res = []
    print(f"Количество ссылок для парсинга:  {len(resNew)}")
    # print('linker ebay okey')
    gather_Linker_Amazon(resNew)
        
# /////////////////////////////////////////////////////////
# amazon start


def gather_Linker_Amazon(resNew):
    print('gather Amazon')
    total2 = []

    with multiprocessing.Pool(multiprocessing.cpu_count() * 3) as p3:       
        total = p3.map(linksHandlerAmazon, resNew)
        p3.close()
        p3.terminate()
        p3.join()   
    for c in total:                
        if c is None:
            continue
        else:
            total2.append(c)            
    total = []
    print('gager amazon ok')              
    print(f"str 509: {len(total2)}")   
    writerr(total2)        

def linksHandlerAmazon(total):
    # print('start Amazon')
    finResult = []
    brand = total['brand'].lower()    
    agrForAmazon = 'amazon.com'
    case = 0        
    # while(True):   
          
    quanityTargetItems = 0
    flagEx1 = False
    targetLinkPattern = 'https://www.amazon.com'        
    if total['linkSrchAmazon'] == '':
        return
    # print(f"url For Amazon: {url}")
    try:   
        r = sessionReq(total['linkSrchAmazon'], agrForAmazon)
        # print(f"ответ Амазона:  {r}")
        if str(r) == '<Response [503]>':
            print('Желтая карточка от сервера')
            try:
                time.sleep(random.randrange(31,37))
                return
            except:
                pass
        if str(r) == '<Response [403]>':
            print('Сервер отверг запрос')
            try:
                time.sleep(random.randrange(61,87))
                return
            except:
                pass
        if str(r) == '<Response [504]>':
            return  
        if str(r) == '<Response [404]>':
            print('Страница не найдена')
            return 
        if str(r) == '<Response [400]>':
            return  
        if str(r) == '<Response [443]>':
            print('Проблемы с подключениемю. Проверьте интернет соединение')
            return 
    except Exception as ex:
        pass

    soup = BeautifulSoup(r.content, "html.parser")
    soup2 = BeautifulSoup(r.text, "lxml")
    dom = etree.HTML(str(soup)) 
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
                    pass
    # print(quanityTargetItems)
    
    except Exception as ex:
        return

    
    if quanityTargetItems > 10:
        quanityTargetItems = 10
            
    try: 
        try:
            resultProto = [] 
            case = 1                            
            for i in range(quanityTargetItems):
                targetLinkPattern = 'https://www.amazon.com'                     
                targetLink = ''
                targetPrice  = ''
                titleCritery = ''
                asin = '' 
                if i == 0:
                    try:
                        try:
                            targetLink = dom.xpath(f'//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/div/div/div[3]/div[3]/div/a')[0].get('href')                        
                            # print(targetLink)
                        except Exception as ex:
                            pass
                            # print(ex)
                        try:
                            titleCritery = eval(str(dom.xpath(f'//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/div/div/div[3]/div[1]/h2/a/span//text()')))[0]
                            # print(titleCritery)
                        
                        except Exception as ex:
                            pass
                            # print(f"titleCritery ex: {ex}")
                        try:
                            targetPrice = dom.xpath(f'//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/div/div/div[3]/div[3]/div/a/span//text()')[0]

                            # print(targetPrice)
                        except:
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
                            "titleCritery": str(titleCritery).strip(),
                            "targetPrice": str(targetPrice).strip(),
                            "asin": str(asin).strip()
                        })

                    except Exception as ex:
                        pass

                else:                        
                    try:
                        try:
                            targetLink = dom.xpath(f'//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[{i+3}]/div/div/div/div/div[2]/div[3]/div/a')[0].get('href')
                            # print(f"str 272: {targetLink}")
                        except:
                            pass
                        try:
                            titleCritery = eval(str(dom.xpath(f'//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[{i+3}]/div/div/div/div/div[2]/div[1]/h2/a/span//text()')))[0]
                            # print(titleCritery)
                        
                        except Exception as ex:
                            # print(f"titleCritery ex: {ex}")
                            pass
                        try:                      
                            targetPrice = dom.xpath(f'//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[{i+3}]/div/div/div/div/div[2]/div[3]/div/a/span[1]/span[1]/text()')[0]
                            
                            # print(f"str 277: {targetPrice}")
                        except:
                            pass
                        try:                       
                            asinArr = targetLink.split('/')
                            for i, a in enumerate(asinArr):
                                if asinArr[i] == 'dp':
                                    asin = asinArr[i+1]
                            # print(asin)
                            
                        except:
                            pass
                        resultProto.append({
                            "targetLink": str(f"{targetLinkPattern}{targetLink}").strip(),
                            "titleCritery": str(titleCritery.strip()),
                            "targetPrice": str(targetPrice).strip(),
                            "asin": str(asin).strip()
                        })
                        if len(resultProto) == quanityTargetItems:                                
                            break
                    except:
                        # print(f"sec stap{ex}")
                        # flagEx1 = True
                        pass
                        # break
                    # else:
                    #     break            
                    
        except Exception as ex:
            # print(ex)
            pass
        if len(resultProto) == 1:
            if resultProto[0]['asin'] == '' or resultProto[0]['asin'] == None:                    
                flagEx1 = True               
                                    
        elif len(resultProto) > 1:
            if resultProto[1]['asin'] == '' or resultProto[1]['asin'] == None:
                flagEx1 = True 
        # print(f" str 316{resultProto}")           
        if flagEx1 == True:
            resultProto = []
            # flagEx1 = False
            case = 2
            # print('case 2')
            firstBlock = soup2.find_all('div', attrs= {'class': 'a-row', 'class': 'a-size-base', 'class': 'a-color-base'})
            # print(f"f bloc len: {len(firstBlock)}")

            for f, x in enumerate(firstBlock):
                targetLinkPattern = 'https://www.amazon.com'                                         
                targetLink = ''
                targetPrice  = ''
                titleCritery = ''
                asin = ''
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
                try:                                
                    titleCritery1 = targetLink.split('keywords')[1].split('=')[1].split('+')[0]
                    # print(titleCritery1)
                    titleCritery2 = targetLink.split('keywords')[1].split('=')[1].split('+')[1]
                    try:
                        tc = titleCritery1.lower()
                    except:
                        pass
                    # print(titleCritery2) 
                    if tc == brand:
                        titleCritery = titleCritery2
                    else:
                        titleCritery = titleCritery1                                            
                    # print(titleCritery) 
                except:
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
      

    except Exception as exSession:
        # print(exSession)
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
            # "urlForAmazon": str(total),
            "amazonBlock": resultProto, 
            "case": case                 
        })
        # print('yes') 
        try:           
            return finResult[0]
        except:
            return
            
# amazon finish
# ////////////////////////////////////////////////////////////////////////////////////////

# ////////////////////////////////////////////////////////////////////////////////////////
# писатель результатов старт
 
def writerr(total):
    print('start writer')
    global total_count 
    # totalTotal = [] 
    print(f"str 792: {len(total)}") 
    for item in total:
        if item is None:            
            del item
        else:
            for itemAm in item['amazonBlock']:           
                if itemAm['asin'] == '':
                    del itemAm 
            if item['amazonBlock'] == [] or item['amazonBlock'] == '':
                del item

    
    with open(f"resultBF9.json", "a", encoding="utf-8") as file: 
        json.dump(total, file, indent=4, ensure_ascii=False) 
        
    for item in total:
        amazonList = ''   
        # if len(item['amazonBlock']) > 1:                 
        #     item['amazonBlock'] = item['amazonBlock'][0:len(item['amazonBlock'])]
        # elif len(item['amazonBlock']) < 5 and len(item['amazonBlock']) !=1:
        #     item['amazonBlock'] = item['amazonBlock'][0:len(item['amazonBlock'])] 
        for itAm in item['amazonBlock']:

            if len(item['amazonBlock']) > 1:
                amazonList += itAm['targetLink'] + '\n' + itAm['targetPrice'] + '\n'+ itAm['asin'] + '\n\n'
                # flagCritery = False
                # if item['case'] == 2:
                #     if (f"{itAm['titleCritery']}").lower() == (f"{item['model']}").lower():
                #         try:
                #            amazonList += itAm['targetLink'] + '\n' + itAm['targetPrice'] + '\n'+ itAm['asin'] + '\n\n'                        
                #         except Exception as ex:
                #             print(f"str 810: {ex}")
                #     else:
                #         del itAm
                # if item['case'] == 1:
                #     itCritArr = (f"{itAm['titleCritery']}").split(' ')
                #     critery = (f"{item['model']}").lower()
                #     for j, _ in enumerate(itCritArr):                                            
                #         try:         
                #             match = re.search(f'r"{critery}"', (f"{itCritArr[j]}").lower())
                #             if match:
                #                 flagCritery = True                               
                #                 break
                #         except: 
                #             continue
                #     if flagCritery == True:
                #         try:
                #             amazonList += itAm['targetLink'] + '\n' + itAm['targetPrice'] + '\n'+ itAm['asin'] + '\n\n' 
                #         except Exception as ex:
                #             print(f"str 828: {ex}")
                #     else:
                #         del itAm                        
            # elif len(item['amazonBlock']) > 1 and amazonList == '':
            #     item['amazonBlock'] = item['amazonBlock'][0:len(item['amazonBlock'])] 
            #     for itt in item['amazonBlock']: 
            #         try:
            #             amazonList += itAm['targetLink'] + '\n' + itAm['targetPrice'] + '\n'+ itAm['asin'] + '\n\n' 
            #         except Exception as ex:
            #             print(f"str 828: {ex}")
            if len(item['amazonBlock']) == 1:
                try:
                    amazonList = itAm['targetLink'] + '\n' + itAm['targetPrice'] + '\n'+ itAm['asin'] + '\n\n'                          
                except Exception as ex:
                    print(f"str 836: {ex}")  
        item['amazonBlockNew'] = amazonList  
        del item['amazonBlock']
        del item['case'] 
   
    # now = datetime.now() 
    # curentTimeForFile = str(now.strftime("%m/%d/%Y__%H:%M"))  
    total_count = len(total)             
    with open(f'Result10.json', "a", encoding="utf-8") as file: 
        json.dump(total, file, indent=4, ensure_ascii=False) 
    with open(f'Result10.csv', 'w', newline='', encoding='cp1251', errors="ignore") as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Ссылка eBay маназмн','Название товара', 'Цена', 'Наличие на складе', 'Дата доставки', 'Бренд', 'Модель', 'Соответствующие товары на Amazon'])
        for item in total:
            writer.writerow([item['urlEbayItem'], item ['title'], item['price'], item['quanity'], item['delivery'], item['brand'], item['model'], item['amazonBlock']])      
    
# /////////////////////////////   
# писатель результатов финиш 

# функция запуска скрипта
# ////////////////////////////////

def main():
    global total_count         
    paginationReply(url2)       
    finish_time = time.time() - start_time
    print(f"Общее время работы парсера:  {math.ceil(finish_time)} сек")
    print(f"Количество мультипроцессов:  {multiprocessing.cpu_count()*3}")
    print(f"Общее количество товаров:  {total_count}")
    sys.exit()
    
if __name__ == "__main__":
    main()
    

    
# print(multiprocessing.cpu_count())
     
# python eScraperNew.py


# https://www.ebay.com/sch/i.html?_dkr=1&iconV2Request=true&_blrs=recall_filtering&_ssn=paedistributing&store_cat=0&store_name=paedistributing&_oac=1&LH_PrefLoc=1&LH_ItemCondition=3&LH_BIN=1


# https://www.ebay.com/sch/i.html?_dkr=1&iconV2Request=true&_blrs=recall_filtering&_ssn=paedistributing&store_cat=0&store_name=paedistributing&_oac=1&LH_PrefLoc=1&LH_ItemCondition=3&LH_BIN=1