# Writer :fuyuan360
# Email  :fuyuan360@qq.com
import csv

data = [{"name": "fuyuan360", "age": 18,"sex": "male","work": "developer"},
        {"name":"alen","age": 16,"sex": "female","work": "student"},
        {"name": "xiaoming", "age": 10, "sex": "male", "work": "student"},
        {"name": "xiaohong", "age": 12, "sex": "female", "work": "teacher"}]
with open("./数据集/people_date.csv","w",encoding="utf-8-sig",newline="")as f:
        writer = csv.DictWriter(f,fieldnames=["name","age","sex","work"])
        writer.writeheader()
        writer.writerows(data)
        writer.writerow({"name": "xiaoli","age": 14, "sex": "female", "work": None})
        print("写入完成")