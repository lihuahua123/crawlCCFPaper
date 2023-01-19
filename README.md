# crawlCCFPaper
本项目用于爬取所有CCF A类会议和期刊（URL在CCFAURL.txt里，可以进行修改）的相关关键字的论文题目

 修改crawl.py 里的配置（要爬取的关键词，年份等）,之后
 ```
 pip install beautiful4
 python crawl.py
 ```
 结果默认保存在当前目录下的CCFsearch.txt
