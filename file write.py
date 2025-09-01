# Writer :fuyuan360
# Email  :fuyuan360@qq.com
with open("my_goal.txt","w",encoding='utf-8') as f:
    f.write("先挣tmd一个亿\n")
    f.write("娶刘亦菲一样美的女孩\n")
    f.write("找到仙丹，可以长生不老。\n")
with open("my_goal.txt","a",encoding='utf-8') as f:
    f.write("去宇宙中找个遍地黄金的星球")
for i in open("my_goal.txt","r",encoding='utf-8'):
    print(i,end="")
