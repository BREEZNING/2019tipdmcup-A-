import pandas as pd

#读取数据
supermarket = pd.read_csv("../../result/task1_1.csv", encoding="GBK")

#先收集有多少位顾客，以及他们的相关消费信息
consumer = set(supermarket["顾客编号"])
consumer = list(consumer)

#再收集每位顾客每月的消费额
def Consumer_Volume(n):
    consumer_volume = list()
    for i in consumer:
        s_information = supermarket.loc[(supermarket["顾客编号"] == i)]#每位顾客的相关信息
        s_information_1 = s_information.loc[(s_information["销售月份"] == n)]#筛选出每个月的销售数据
        volume = s_information_1["销售金额"].sum()
        consumer_volume.append(volume)
    return consumer_volume


#最后收集每位顾客每月消费天数
def Consumer_Day(n):
    consumer_date = list()
    for j in consumer:
        s_information = supermarket.loc[(supermarket["顾客编号"] == j)]
        s_information_1 = s_information.loc[(s_information["销售月份"] == n)]
        s_information_2 = set(s_information_1["销售日期"])#记录每个月的销售日期
        s_information_2 = len(list(s_information_2))
        consumer_date.append(s_information_2)
    return consumer_date


#收集1-4月份每月的消费金额
list1 = Consumer_Volume(201501)
list2 = Consumer_Volume(201502)
list3 = Consumer_Volume(201503)
list4 = Consumer_Volume(201504)

#收集1-4月份每月的消费天数
month1 = Consumer_Day(201501)
month2 = Consumer_Day(201502)
month3 = Consumer_Day(201503)
month4 = Consumer_Day(201504)

df = pd.DataFrame({"顾客编号":consumer,
                   "1月消费金额":list1,
                   "2月消费金额":list2,
                   "3月消费金额":list3,
                   "4月消费金额":list4,
                   "1月消费天数":month1,
                   "2月消费天数":month2,
                   "3月消费天数":month3,
                   "4月消费天数":month4})

df.to_csv("../../result/task1_5.csv", encoding="GBK")