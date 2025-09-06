# Writer :fuyuan360
# Email  :fuyuan360@qq.com
import csv
with open("./数据集/updated_city_happiness.csv",encoding="utf-8-sig") as file_date:
    reader = csv.DictReader(file_date)
    for row in reader:
        province =row["省份"]
        city =row["城市"]
        happiness:float =row["幸福指数"]
        print(f"{province} {city}幸福指数为 {int(float(happiness))}")