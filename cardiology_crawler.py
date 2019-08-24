#!/usr/bin/env python
# coding: utf-8

# In[8]:


from bs4 import BeautifulSoup
import requests
from itertools import chain


# In[312]:


def parse(response):
    data = requests.get(response)
    domain = 'https://www.hindawi.com'
    sp = BeautifulSoup(data.text)
    sp1 = sp.select('.middle_content')

    s2 = [s.find_all('a') for s in sp1]
    s3 = [s.text.split(',') for s in s2[0]]
    s4=list(chain(*s3[:-1]))
    l=(len(s4))

    sp3=[]
    for k in range(l-3):
        sp2 = [s.select('a')[k]['href'] for s in sp1]
        sp3.append(sp2)
    
    sp4=[]
    for i in sp3:
        if (len(str(i))-4) == 28:
            sp4.append(i)
        else:
            continue
    sp5=list(chain(*sp4))
    for e in sp5:
        parse_detail(domain + e)

def parse_detail(response):
    data = requests.get(response)
    d = BeautifulSoup(data.text)
    d2 = d.select('.middle_content')
    p = [s.select('h2') for s in d2]
    for pe in p[0]:
        title = pe.text
        with open("cardiology.txt", "a", encoding = 'utf8') as f:
            f.write(title + '\n')
            

    d3 = [s.select('p') for s in d2]
    d4 = [s.text for s in d3[0]]
    cont =''
    for t in d4:
        cont += t
	
    with open("cardiology.txt", "a", encoding = 'utf8') as f:
            f.write(cont + '\n')
            f.close


# In[311]:


if __name__ == '__main__':
    i=1
    while(i<=1):
        start_urls = "https://www.hindawi.com/journals/cric/contents/"+str(i)+"/"
        parse(start_urls)
        i+=1

