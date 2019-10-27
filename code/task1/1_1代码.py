import pandas as pd 
import numpy as np

source = pd.read_csv('../../appendix/data.csv',encoding='gbk')  

#删除销售金额、销售数量、商品单价中有空值的行数据
def checkNull(df):
    index = ['销售金额','销售数量','商品单价']
    for i in index:
        nullIndexList = list(df.index[np.where(np.isnan(df[i]))[0]]) #获取当前属性列为空的行数据的索引
        df = df.drop(nullIndexList)
    return df

#删除重复的行数据
def checkRepeat(df):
    df = df.drop_duplicates()
    return df 

#删除日期为2015年2月29日的行数据
def checkDate(df):
    df = df.loc[(df['销售日期'] != 20150229)]
    return df 

#删除销售金额、销售数量、商品单价为负的行数据
def checkMinus(df):
    df = df.loc[(df['销售数量'] >= 0) & (df['销售金额'] >= 0) & (df['商品单价'] >= 0)]
    return df

#删除销售金额不等于销售数量乘商品单价，且不是促销的行数据
def checkPrice(df):
    index = []
    for i in df.index:
        #将计算结果均转换为两位小数进行比较，否则不准确
        if ('%.2f'%(df.loc[i,'销售数量']*df.loc[i,'商品单价']) != '%.2f'%(df.loc[i,'销售金额'])):
            if(df.loc[i,'是否促销'] == '否'):
                index.append(i)
    df = df.drop(index)
    return df 

if __name__ == '__main__':
    source = checkNull(source)
    source = checkRepeat(source)
    source = checkDate(source)
    source = checkMinus(source)
    source = checkPrice(source)
    source.to_csv('../../result/task1_1.csv',encoding='gbk')