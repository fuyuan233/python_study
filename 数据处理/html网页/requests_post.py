# Writer :fuyuan360
# Email  :fuyuan360@qq.com
import requests
import re

html = requests.post("http://exercise.kingname.info/exercise_requests_post",
                     data={"name"     : "kingname",
                           "password" : "123456"}).content.decode()
title = re.search('<title>(.*?)</title>', html, re.S).group(1)
content_list = re.findall('<p>(.*?)</p>', html, re.S)
content_str = "\n".join(content_list)
print("标题是：" + title)
print("内容是：\n" + content_str)