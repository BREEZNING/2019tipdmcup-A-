import pandas as pd 

source = pd.read_csv('../../result/task1_1.csv',encoding='gbk',usecols=[7,11,14]) #读取销售日期、商品类型、销售金额列的数据
source = source[source['商品类型'].isin(['一般商品','生鲜'])] #保留商品类型为一般商品和生鲜的数据
cuts = [20150101,20150108,20150115,20150122,20150129,20150205,20150212,20150219,20150226,
20150305,20150312,20150319,20150326,20150402,20150409,20150416,20150423,20150431] #设置每周分组
week = list(range(1,len(cuts))) #分组标签名
source['销售周'] = pd.cut(source['销售日期'],cuts,right=False,labels=week) #将每行数据匹配销售周，以每周四为一周开始，即设置分组为左闭合，分组标签名为销售周数
sale = source.groupby(['商品类型','销售周'])['销售金额'].sum() #按商品类型和销售周分组，累加销售金额
sale.to_csv('../../result/task1_4.csv',encoding='gbk')