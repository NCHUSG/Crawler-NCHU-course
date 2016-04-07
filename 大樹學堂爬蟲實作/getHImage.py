import requests, json
from bs4 import BeautifulSoup
import shutil
import os
try:
    os.chdir('img')
    #means cd path
except:
    print('path error')
res =requests.get('http://www.timliao.com/bbs/viewthread.php?tid=74448')
soup = BeautifulSoup(res.text)

for i in soup.select('img'):
    try:
        fname = i['src'].split('/')[-1]
        imageUrl = i['src']
        ires = requests.get(imageUrl,stream=True)
        f = open(fname,'wb')
        shutil.copyfileobj(ires.raw,f)
        f.close()
        del ires
    except Exception as e:
        print(i)
        print(e)