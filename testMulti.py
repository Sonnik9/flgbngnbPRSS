from __future__ import print_function
from google.auth.transport.requests import Request
import os.path
import pickle
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
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
import asyncio
import aiohttp
from fake_useragent import UserAgent
from datetime import datetime
import sys


hrefsBank = list(range(700))


def linksHandlerAmazon(total):
    time.sleep(3)
    total2 = total * 3
    # print(total2)
    return total2
        
def hendlerLinks(x):
    time.sleep(3)
    t = x * 2
    # linksHandlerAmazon(t)
    return linksHandlerAmazon(t)
    # linksHandlerAmazon(t)    
    


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

def gather_Linker_Ebay(hrefsBank):       
    with multiprocessing.Pool(multiprocessing.cpu_count() *3) as p2:                      
        tot = p2.map(hendlerLinks, hrefsBank)
        p2.close()        
        p2.join()
        # print(tot)
#         # asyncio.run(gather_registrator_eBay(tot))
        # linksGagerHandlerAmazon(tot)
         
 
if __name__ == "__main__":
    start_time = time.time() 
    # asyncio.run(gather_registrator_eBay(hrefsBank))
    gather_Linker_Ebay(hrefsBank)
    finish_time = time.time() - start_time
    print(finish_time)
    
    
#  python testMulti.py
