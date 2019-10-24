import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

source = pd.read_csv('../../result/task1_1.csv',encoding='gbk',usecols=[7,14,16]) #读取销售日期、是否促销、销售金额列的数据
source['销售日期'] = source['销售日期'].map(lambda x: str(x)) #销售日期列的数据转换为字符串类型
source['销售日期'] = pd.to_datetime(source['销售日期']) #x销售日期列的数据转换为日期类型
sell = source.groupby(['是否促销','销售日期']).sum() #按是否促销、销售日期分组，累加销售额
sell_sale = sell.loc['是'] #提取促销商品的销售额
sell_not_sale = sell.loc['否'] #提取非促销商品的销售额
date = list(sell_sale.index)
date2 = list(sell_not_sale.index)
increase = {}
increase['促销'] = {}
increase['非促销'] = {}
#分别计算促销商品和非促销商品的日环比增长率
for i in list(range(1,len(sell_sale.index))): 
    day = date[i]
    increase['促销'][day] = (float(sell_sale.iloc[i]) - float(sell_sale.iloc[i-1]))/float(sell_sale.iloc[i-1])

for i in list(range(1,len(sell_not_sale.index))):
    day = date2[i]
    increase['非促销'][day] = (float(sell_not_sale.iloc[i]) - float(sell_not_sale.iloc[i-1]))/float(sell_not_sale.iloc[i-1])

daily_increasement = pd.DataFrame(increase)
daily_increasement.index.name = '销售日期'

#绘图
plt.rcParams['font.sans-serif']=['SimHei'] #设置正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #设置正常显示负号
#设置纵坐标的刻度
y = [-1,0,1]
for i in range(10,100,10):
    y.append(i)
daily_increasement.plot(title='促销和非促销商品销售金额日环比增长率折线图',xticks=pd.date_range('2015-01-01','2015-04-30',freq='W-THU'),
    yticks= y,figsize=(15,10))
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.savefig('../../result/task3_3.png')
plt.show()