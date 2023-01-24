import requests
from bs4 import BeautifulSoup
import re
import json
f = open("CCFAURL.txt", encoding="utf-8") # CCF A 会议和期刊的URL 文档
key = 'cloud' # 搜索关键词
year = 2018 # 只要大于year的论文
filename = 'CCFsearch.txt' # 爬到的年份+题目保存在文件中
links = f.readlines()
f.close()
links = [i for i in links if i != '\n']
newlinks = []
for i in links:
    newlinks.append(i.strip().replace('\n', ''))
writeli=""
with open(filename, 'w') as file_object:
    writeli += key + "\n"
    for link in newlinks:
        jouc = link.split('/')[-3]
        aname = link.split('/')[-2]
        searchurl = 'https://dblp.uni-trier.de/search?q={que}%20streamid%3A{jorc}%2F{name}%3A'.format(que=key,jorc=jouc,name=aname)
        strhtml = requests.get(searchurl)
        soup=BeautifulSoup(strhtml.text,'html.parser')
        titles = soup.select('span.title')
        time = soup.select('span[itemprop="datePublished"]')
        print(jouc+" "+aname)
        writeli += jouc+" "+aname+"\n"
        for i in range(len(titles)):
            if int(time[i].text) < year:
                break
            writeli += time[i].text+" "+titles[i].text+"\n"
    file_object.write(writeli)
file_object.close()
