import pandas as pd
import matplotlib.pyplot as plt 

#读取数据
supermarket = pd.read_csv("../../result/task1_1.csv", encoding="GBK")

#统计每个大类的销售金额

#1、获取每个大类的商品名称
name = set(supermarket["大类名称"])
name = list(name)

#2、计算每个大类每月的销售额
def Month_volume(n):
    name_jine = list()
    for i in name:
        namez = supermarket.loc[(supermarket["大类名称"] == i) & (supermarket["销售月份"] == n)]
        sumz = namez["销售金额"].sum()
        name_jine.append(sumz)
    return name_jine

January_volume = Month_volume(201501)
February_volume = Month_volume(201502)
March_volume = Month_volume(201503)
April_volume = Month_volume(201504)

#3、生成新的数据表
df = pd.DataFrame({
                   "一月销售金额":January_volume,
                   "二月销售金额":February_volume,
                   "三月销售金额":March_volume,
                   "四月销售金额":April_volume},index=name)
df.index.name = "大类名称"

#绘制饼图
plt.rcParams['font.sans-serif']=['SimHei'] #设置正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #设置正常显示负号
fig = plt.figure(1,figsize=(19.2,10.8))
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)
df['一月销售金额'].plot(ax=ax1,kind='pie',autopct='%.2f%%',title='一月各大类商品销售金额占比饼图')
df['二月销售金额'].plot(ax=ax2,kind='pie',autopct='%.2f%%',title='二月各大类商品销售金额占比饼图')
df['三月销售金额'].plot(ax=ax3,kind='pie',autopct='%.2f%%',title='三月各大类商品销售金额占比饼图')
df['四月销售金额'].plot(ax=ax4,kind='pie',autopct='%.2f%%',title='四月各大类商品销售金额占比饼图')
ax4.legend(loc=2, bbox_to_anchor=(1.2,1.0),borderaxespad=0)
plt.savefig('../../result/task2_2.png')
plt.show()