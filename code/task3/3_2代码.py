import pandas as pd
import matplotlib.pyplot as plt 

source = pd.read_csv('../../result/task1_1.csv',encoding='gbk',usecols=[2,8,14]) #读取大类名称、销售月份、销售数量、销售金额的数据
#获取各大类商品总销售金额的排序
totalSell = pd.read_csv('../../result/task1_2.csv',encoding='gbk')
totalSell.sort_values(ascending=False,inplace=True,by='销售金额')
totalSell.index = range(1,16)
topFive = list(totalSell.loc[1:5,'大类名称'])
middleFive = list(totalSell.loc[6:10,'大类名称'])
bottomFive = list(totalSell.loc[11:15,'大类名称'])

source['销售月份'] = source['销售月份'].map(lambda x:str(x))
sell_category = source.groupby(['大类名称','销售月份']).sum() #按大类名称、销售月份分组利用sum函数聚合，叠加销售量和销售额

#提取总销售额前五名，中间五名，后五名的大类商品的每月销售金额
sell_topfive = sell_category.loc[topFive].unstack('大类名称')
sell_middlefive = sell_category.loc[middleFive].unstack('大类名称')
sell_bottomfive = sell_category.loc[bottomFive].unstack('大类名称')

#绘图
plt.rcParams['font.sans-serif']=['SimHei'] #设置正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #设置正常显示负号
fig = plt.figure(1,figsize=(19.2,10.8))
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
sell_topfive.plot(ax=ax1,title='总销售额前五名的大类商品的月销售金额变化趋势折线图',xticks=range(0,4))
sell_middlefive.plot(ax=ax2,title='总销售额中间五名的大类商品的月销售金额变化趋势折线图',xticks=range(0,4))
sell_bottomfive.plot(ax=ax3,title='总销售额后五名的大类商品的月销售金额变化趋势折线图',xticks=range(0,4))
ax1.legend(loc=1,borderaxespad=0)
ax2.legend(bbox_to_anchor=(1.2,-0.1),borderaxespad=0)
ax3.legend(bbox_to_anchor=(1.3,0.5),borderaxespad=0)
plt.savefig('../../result/task3_2.png')
plt.show()