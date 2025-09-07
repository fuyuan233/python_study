# Writer :fuyuan360
# Email  :fuyuan360@qq.com
import time
from multiprocessing.dummy import Pool

import requests

# 单线程作业
start = time.time()
for i in range(100) :
    requests.get("http://www.baidu.com")
end = time.time()
print("单线程耗时：", end - start)
# 多线程作业
pool = Pool(5)
start = time.time()
pool.map(requests.get, ["http://www.baidu.com"] * 100)
end = time.time()
print("多线程耗时：", end - start)
#显然requests.get()对于网络情况要求很大
