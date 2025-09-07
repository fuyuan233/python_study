# Writer :fuyuan360
# Email  :fuyuan360@qq.com
import re

import requests

base_url = "http://www.mcxs.info/"
url = "http://www.mcxs.info/75_75310/"
# 小说首页网址内容获取
top_html = requests.get(url).content.decode()
# 小说标题
title = re.findall(r'<meta property="og:title" content="(.*?)" />', top_html)[0]
print("标题：" + title)
# 小说目录
catalog = re.search(r'<dt>《夜无疆》正文</dt>(.*?)</dl>', top_html, re.S).group(1)
chapter_list = re.findall(r'<a style="" href="(.*?)">(.*?)</a></dd>', catalog)
# 小说内容 这里只获取第一章
chapter_low_url, chapter_name = chapter_list[0]
chapter_url = base_url + chapter_low_url
chapter_html = requests.get(chapter_url).content.decode()

content = re.search(r'<div id="content" deep="3">(.*?)<div align="center">', chapter_html, re.S).group(1)
with open(title + " " + chapter_name + ".txt", "w", encoding="utf-8") as f :
    f.write(content)