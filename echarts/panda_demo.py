# 1. pandas获取数据(数据库 爬虫)
# 2. 数据特征值(列)筛选
# 3. 清洗数据
# 4. 数据分成训练集(75%)和测试集(25%)
# 5. 算法  ：分类 (K近邻，随机森林)
#                  线性回归()        -->正确率
# 6. 交叉验证(改成50 50 ) +网格搜索
# 7. 模型保存使用

from pandas import Series ,DataFrame
import numpy as np

#Series 为一列（一个特征） 多列则叫DataFrame
ss = Series(data = list("ABCD"),index=list("1234"),name="tezhengA",dtype=np.str) #dtype默认为np.object np.str也会显示成object的
print(ss)

#多个Series组成DataFrame
# np.array([]) np.arange
df = DataFrame(data=np.arange(12).reshape(3,4),index=list("123"),columns=list("xyz"))
print (df)
print(df.values,type(df.values))
print(df.index)
print(df.columns)
print(df.dtypes)

import pandas as pd
#加载本地的CSV文件
df = pd.read_csv("groupby.csv")
# 查询DataFrame相关信息
print("-"*20)
df.info()
print(df.head(n=3))
print(type(df))