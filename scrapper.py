import os
import requests
from bs4 import BeautifulSoup

stack_jobs = []
wework_jobs = []
remoteok_jobs = []

def get_stack(word):
  stack_jobs=[]
  stack = f"https://stackoverflow.com/jobs?q={word.replace('+','%2B').replace('#','%23').replace('/','%2F')}"
  stack_req = requests.get(stack)
  stack_soup = BeautifulSoup(stack_req.text, 'html.parser')
  stack_grid = stack_soup.find('div', {"class": "listResults"}).find_all('div',{'class':'grid'})

  for grid in stack_grid:
    if(grid.find('div', {'class':'grid--cell fl1'}) == None):
      pass
    else:
      title = grid.find('div', {'class':'grid--cell fl1'}).find('h2').find('a')['title'].strip()
      link = grid.find('div', {'class':'grid--cell fl1'}).find('h2').find('a')['href'].strip()
      company = grid.find('div', {'class':'grid--cell fl1'}).find('h3', {'class':'fc-black-700'}).find('span').text.strip()
      stack_jobs.append({'title': title, 'company': company, 'link': link })
  return stack_jobs

def get_wework(word):
    wework_jobs=[]
    wework = f"https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term={word.replace('+','%2B').replace('#','%23').replace('/','%2F')}"
    wework_req = requests.get(wework)
    wework_soup = BeautifulSoup(wework_req.text, 'html.parser')
    if wework_soup.find('div',{'class':'jobs-container'},{'id':'job_list'}).find('section',{'id':'category-2'}) == None:
        pass
    else:
        wework_list = wework_soup.find('div',{'class':'jobs-container'},{'id':'job_list'}).find('section',{'id':'category-2'}).find_all('ul')
        for value in wework_list:
            for li in value.find_all('li'):

                if(li.find('a').find('span',{'class':'title'}) == None):
                    pass
                else:
                    if(li.find('a').find('span',{'class':'company'}) == None):
                        pass
                    else:
                        title = li.find('a').find('span',{'class':'title'}).text
                        company = li.find('a').find('span',{'class':'company'}).text
                        link = li.find('a')['href']
                
                        wework_jobs.append({'title':title,'company':company,'link':link})

    return wework_jobs

def get_remoteok(word):
    remoteok_jobs=[]
    remoteok = f"https://remoteok.io/remote-{word.replace('++','-plus-plus').replace('#','-sharp')}-jobs".lower()
    remoteok_req = requests.get(remoteok, headers = {'User-agent': 'Super Bot Power Level Over 9000'})
    remoteok_soup = BeautifulSoup(remoteok_req.text, 'html.parser')
    if remoteok_soup.find('div', {'class':'container'}) == None:
        pass
    else:
        remoteok_table = remoteok_soup.find('div', {'class':'container'}).find('table', {'id': 'jobsboard'}).find_all('tr')
        for cell in remoteok_table:
            if cell.find('td') == None:
                pass
            else:
                if cell.find('td', {'class': 'company'}) == None:
                    pass
                else:
                    company = cell.find('td', {'class': 'company'}).find('a',{'itemprop':'hiringOrganization'}).find('h3',{'itemprop': 'name'}).text
                    title = cell.find('td', {'class': 'company'}).find('h2',{'itemprop':'title'}).text
                    link  = cell.find('td', {'class': 'company'}).find('a', {'itemprop':'url'})['href']
                    remoteok_jobs.append({'title':title,'company':company,'link':link})

    return remoteok_jobs