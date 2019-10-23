import pandas as pd

#读取数据
supermarket = pd.read_csv("../../result/task1_1.csv", encoding="GBK")

#统计每个大类的销售金额

#1、获取每个大类的商品名称
name = set(supermarket["大类名称"])
name = list(name)

#2、计算每个大类的销售额
name_jine = list()
for i in name:
    namez = supermarket.loc[(supermarket["大类名称"] == i)]
    sumz = namez["销售金额"].sum()
    name_jine.append(sumz)

#3、生成新的数据表
df = pd.DataFrame({"大类名称":name,"销售金额":name_jine})
df.to_csv("../../result/task1_2.csv", encoding="GBK")