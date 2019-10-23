import pandas as pd

#读取数据
supermarket = pd.read_csv("../../appendix/data.csv", encoding="GBK")

s1 = supermarket.loc[(supermarket["销售数量"] >= 0) & (supermarket["销售金额"] >= 0) & (supermarket["商品单价"] >= 0)]
s2 = s1.loc[(s1["销售日期"] != 20150229)]
s2.to_csv("../../result/task1_1.csv", encoding = "GBK")