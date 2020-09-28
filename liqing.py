import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

data=pd.read_csv('liqing1.csv')
#利用pandas创建一个数据分析表格
df=pd.DataFrame(data).T
#如果Price这些行代表每个股票不同时间段的开盘价格，可以分析随着时间流逝，价格的波动情况
'''time=df.loc['Date']
Stock_1=df.loc['A']
#利用scatter图表去直观化数据
plt.scatter(x=time,y=Stock_1,s=10,alpha=0.4)
plt.show()'''
#分析一波B股大于某个值和小于某个值的个数，并进行柱状图的绘制
arr=2600
#自定义函数，统计大于2600这个点的个数
def getnums(columns1):
    con=0
    for i in columns1:
        if i>=arr:
            con+=1
    return con 
#进行数据的统计
#大于2600股指的个数
cc=getnums(df.loc['B'])
#小于2600股指的个数
dd=len(df.loc['B'])-cc
#注意：若要绘制百分比函数，一定要将除法写进入新建立的DataFrame表格内部，可能是因为这个是对新表格的绘图运算
ds=pd.DataFrame([cc/len(df.loc['B']),dd/len(df.loc['B'])],index=['Gold_Lead','Gold_Deficit'])
#绘制百分比柱状图
ds.plot.bar(stacked=True)
plt.show()