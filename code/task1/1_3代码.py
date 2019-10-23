import pandas as pd

data = pd.read_csv('../../result/task1_1.csv',encoding='gbk',usecols=[3,4,14,16]) #读取中类编码、中类名称、销售金额、是否促销列的数据
sale = data.groupby(['中类编码','中类名称','是否促销']).sum()  #按照中类编号、是否促销分类累加销售金额
sale.to_csv('../../result/task1_3.csv',encoding='gbk')