import pandas as pd 
import matplotlib.pyplot as plt 
import matplotlib.dates as mdates

source = pd.read_csv('../../result/task1_1.csv',encoding='gbk',usecols=[7,11,14]) #读取销售日期、商品类型、销售金额列的数据
source = source[source['商品类型'].isin(['一般商品','生鲜'])] #保留商品类型为一般商品和生鲜的数据
source['销售日期'] = source['销售日期'].map(lambda x: str(x)) #销售日期列的数据转换为字符串类型
source['销售日期'] = pd.to_datetime(source['销售日期']) #x销售日期列的数据转换为日期类型
sale = source.groupby(['商品类型','销售日期']).sum() #按商品类型、销售日期分组，累加销售额
data = sale.unstack('商品类型') #将数据按商品类型重新排列
data.columns.name = '商品类型'
plt.rcParams['font.sans-serif']=['SimHei'] #设置正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #设置正常显示负号
#绘制数据,横坐标设置为每周四显示
data.plot(title='生鲜商品和一般商品日销售金额折线图',xticks=pd.date_range('2015-01-01','2015-04-30',freq='W-THU')) 
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d')) #将横坐标以日期格式显示
plt.savefig('../../result/task2_1.png') #保存图像
plt.show() #显示图像