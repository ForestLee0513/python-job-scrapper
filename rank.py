import os
import requests
from bs4 import BeautifulSoup

top = []

def get_rank():
    top=[]
    top_req = requests.get('https://www.tiobe.com/tiobe-index/')
    top_parser = BeautifulSoup(top_req.text, 'html.parser')
    top_table = top_parser.find('table', {"class": "table-top20"}).find('tbody').find_all('tr')
    top_res = []
    for tr in top_table:
            for td in tr:
                top_res.append(td.string)
    top_list = [top_res[i * 6:(i + 1) * 6] for i in range((len(top_res) + 6 - 1) // 6 )]
    top=[]
    
    for a in top_list:
        top.append({'rank':a[0],'lang':a[3]})

    return top