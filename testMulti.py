# from __future__ import print_function
# from google.auth.transport.requests import Request
# import os.path
# import pickle
# from googleapiclient.discovery import build
# from google_auth_oauthlib.flow import InstalledAppFlow
# from google.auth.transport.requests import Request
# from google.oauth2.credentials import Credentials
# from requests_html import HTMLSession
# import requests
# from bs4 import BeautifulSoup
# import random 
from random import choice
import time
import mpire
from mpire import WorkerPool
# import csv
# import json
# from lxml import etree
# import math
# import re
import multiprocessing
from multiprocessing import Pool
import multiprocess

# import asyncio
# import aiohttp
from fake_useragent import UserAgent
# from datetime import datetime
# import sys


hrefsBank = list(range(100))

hrefsBank = [1, None, 3,4,5,6,7,8,9,None]


def linksHandlerAmazon(total):
    time.sleep(1)
    try:
       total2 = total * 3
    except:
        total2 = None
    # print(total2)
    return total2
        
def hendlerLinks(x):
    time.sleep(1)
    try:
       t = x * 2  
    except:
        t = None  
    return linksHandlerAmazon(t)

def gather_Linker_Ebay(hrefsBank):
    n = multiprocessing.cpu_count() * 10  
    n = 21
    # 21 для моего  # 
    with WorkerPool(n_jobs = 21) as p2:                      
        tot = p2.map(hendlerLinks, hrefsBank)
    print(tot)
               
        
        
    


# async def gather_registrator_eBay(hrefsBank):
#     # global hrefsBankVar   
#     async with aiohttp.ClientSession() as session:       
#         tasks = [] 
#         for item in hrefsBank:
#             task = asyncio.create_task(linksHandlerAmazon(item))
#             tasks.append(task)
#         await asyncio.gather(*tasks)    
    # gather_Linker_Ebay(hrefsBankVar)
    # hrefsBankVar = []


# def gather_Linker_Ebay(hrefsBank):       
#     with multiprocessing.Pool(2) as p2:                      
#         res = p2.map(hendlerLinks, hrefsBank)

#         p2.close()
#         # p2.terminate()
#         p2.join()
#         linksGagerHandlerAmazon(res)
        
# def linksGagerHandlerAmazon(preTotal):
#     with multiprocessing.Pool(multiprocessing.cpu_count() *3) as p2:                   
#         p2.map(linksHandlerAmazon, preTotal)       
#         p2.close()        
#         p2.join()


# def gather_Linker_Ebay(hrefsBank):       
#     with multiprocessing.Pool(multiprocessing.cpu_count() * 3) as p2:                      
#         # p2.map_async(hendlerLinks, hrefsBank, callback=linksHandlerAmazon)
#         for href in hrefsBank:      
#             p2.apply_async(hendlerLinks, args=(href, ), callback=linksHandlerAmazon)
#         p2.close()
#         # p2.terminate()
#         p2.join()
 
# def linksGagerHandlerAmazon(preTotal):
#     with multiprocessing.Pool(multiprocessing.cpu_count() *3) as p2:                   
#         p2.map(linksHandlerAmazon, preTotal)       
#         p2.close()        
#         p2.join()
#         # print(t)

# def gather_Linker_Ebay(hrefsBank):       
#     with multiprocessing.Pool(multiprocessing.cpu_count() *3) as p2:                      
#         tot = p2.map(hendlerLinks, hrefsBank)
#         p2.close()        
#         p2.join()
        # print(tot)
#         # asyncio.run(gather_registrator_eBay(tot))
        # linksGagerHandlerAmazon(tot)
        

         
 
if __name__ == "__main__":
    start_time = time.time() 
    # asyncio.run(gather_registrator_eBay(hrefsBank))
    gather_Linker_Ebay(hrefsBank)
    finish_time = time.time() - start_time
    print(finish_time)
# url = 'https://www.ebay.com/sch/i.html?_dkr=1&iconV2Request=true&_blrs=recall_filtering&_ssn=worxtools&store_cat=0&store_name=worxlawnandgardenequipment&_oac=1'
# lastPagin = 3
# hrefsBlockPagination = (f"{url}&_ipg=240&_pgn={i}" for i in range(1, lastPagin+1))
# print(list(hrefsBlockPagination))
    
    
#  python testMulti.py
