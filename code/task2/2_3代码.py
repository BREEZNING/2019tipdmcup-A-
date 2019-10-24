import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

source = pd.read_csv('../../result/task1_1.csv',encoding='gbk',usecols=[7,14,16]) #读取销售日期、是否促销、销售金额列的数据
cuts = [20150101,20150108,20150115,20150122,20150129,20150205,20150212,20150219,20150226,
20150305,20150312,20150319,20150326,20150402,20150409,20150416,20150423,20150431] #设置每周分组
week = list(range(1,len(cuts))) #分组标签名
source['销售周'] = pd.cut(source['销售日期'],cuts,right=False,labels=week) #将每行数据匹配销售周，以每周四为一周开始，即设置分组为左闭合，分组标签名为销售周数
sell = source.groupby(['是否促销','销售周'])['销售金额'].sum() #按是否促销、销售周分组，累加销售金
increase = {} #存放促销产品和非促销产品的周环比增长率
for x in ['是','否']:
    increase[x] = {}
    #第一周无法得知上周的销售金额，从第二周开始计算周环比增长率
    for i in range(2,18): 
        #increase[x][i] = "%.2f%%" %(((sell[x][i] - sell[x][i-1])/sell[x][i-1])*100) #本周环比增长率=(本周销售总额-上周销售总额)/上周销售总额，转换为百分比
        increase[x][i] = (sell[x][i] - sell[x][i-1])/sell[x][i-1]

increasement = pd.DataFrame(increase)
increasement.columns = increasement.columns.map({'是':'促销','否':'非促销'})
increasement.index.name = '销售周数'

#将坐标轴转换为百分比的方法
def to_percent(temp, position):
    return '%.1f'%(10*temp) + '%'

#绘图
plt.rcParams['font.sans-serif']=['SimHei'] #设置正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #设置正常显示负号
increasement.plot(kind='bar',title='促销和非促销商品销售金额的周环比增长率柱状图',yticks=np.arange(-0.8,0.9,0.1))
plt.gca().yaxis.set_major_formatter(FuncFormatter(to_percent))
plt.savefig('../../result/task2_3.png')
plt.show()