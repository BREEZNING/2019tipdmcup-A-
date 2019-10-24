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


#收集1-4月份每月的销售金额
list1 = Consumer_Volume(201501)
list2 = Consumer_Volume(201502)
list3 = Consumer_Volume(201503)
list4 = Consumer_Volume(201504)

df = pd.DataFrame({"顾客编号":consumer,
                   "1月消费金额":list1,
                   "2月消费金额":list2,
                   "3月消费金额":list3,
                   "4月消费金额":list4})

df_final = df["1月消费金额"] + df["2月消费金额"] + df["3月消费金额"] + df["4月消费金额"]
df.insert(5, "总消费金额", df_final)

df.sort_values(by=["总消费金额"], ascending=False, axis=0, inplace=True)
df.to_csv("../../result/task3_1.csv", encoding="GBK")


'''接下来做用户画像(这里是以用户的倾向性为标准来判断)'''
def Make_User_Portrait(n):
    name = set(supermarket["大类名称"])
    name = list(name)
    cost = list()
    
    user_portrait = supermarket.loc[(supermarket["顾客编号"] == n)]#找到目标用户的所有信息
    for i in name:
        user_portrait_new = user_portrait.loc[(user_portrait["大类名称"] == i)]
        user_volume = user_portrait_new["销售金额"].sum()#计算该大类所花费的金额
        cost.append(user_volume)
    return cost


name = set(supermarket["大类名称"])
name = list(name)
def User_Portrait(n):
    df_user = pd.DataFrame({"大类名称":name, "总消费":Make_User_Portrait(n)})
    df_user.to_csv("../../result/task3_1({}).csv".format(n), encoding="GBK")

user = [1177, 52, 986, 1385, 108, 210, 12, 395, 74, 1594]
for i in user:
    User_Portrait(i)