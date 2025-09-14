# Writer :fuyuan360
# Email  :fuyuan360@qq.com
import lxml.html
import requests

base_url = "http://www.mcxs.info/"
url = "http://www.mcxs.info/75_75310/"
# 小说首页网址内容获取
top_html = lxml.html.fromstring(requests.get(url).text)
# 小说标题
title = top_html.xpath("//h1/text()")[0]
print(title)
# 小说目录
catalog_texts = top_html.xpath('//*[@id="list"]/dl/dd/a/text()')[12 :]
href_list = top_html.xpath('//*[@id="list"]/dl/dd/a/@href')[12 :]
catalogs = [dict(catalog_text=text, href=href) for text, href in zip(catalog_texts, href_list)]
# 小说内容 这里只获取第一章
chapter_html = lxml.html.fromstring(requests.get(base_url + href_list[0]).text)
content = chapter_html.xpath('//*[@id="content"]/text()')
with open(str(catalogs[0]["catalog_text"]) + ".txt", "w", encoding="utf-8") as f :
    for text in content :
        f.write(text.replace(" ", "") + "\n")