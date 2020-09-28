import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 
#读取数据
data=pd.read_csv('liqing1.csv')
df=pd.DataFrame(data).T
#转化为列表，进行条件判断
ds=np.array(df.loc['Date'])#日期列表
dn=np.array(df.loc['A'])#A股股价列表
#条件判断，判断休市开市期
con=[]#空列表，存储第几个数据属于休市和开市的
row1=[]#空列表，存储对应的A股价格的数据
for i in range(0,len(ds)-1):
    if (ds[i+1])!=(ds[i]):#想要判断是否是星期五
        con.append(i)
        con.append(i+1)
        #将上面找到的日期，对应去寻找他们所对应的价格
        row1.append([dn[i],dn[i+1]])
#再判断它是做空还是做多
Large=[]#做多
Small=[]#做空
Num_Large=0
Num_Small=0
for x in range(0,len(row1)):
    if row1[x][1]-row1[x][0]>=0:
        Num_Large+=1#做多
        Large.append(x)
    elif row1[x][1]-row1[x][0]<0:
        Num_Small+=1#做空
        Small.append(x)

print(Large)
print(Num_Large)