import pandas as pd 
import matplotlib as plt 
import numpy as np 
import openpyxl
#将zzr写入excel表格内
wb=openpyxl.Workbook()
sheet=wb.active
sheet['A1']='Fri'
sheet['B1']='Imcubment Fri Price for A'
sheet['C1']='Mon'
sheet['D1']='Imcubment Mon Price for A'
#读取原始数据
data=pd.read_csv('liqing1.csv')
ccr=pd.DataFrame(data)
#提取Time列时间点为9：30和14：59的所有行Index
bbr=ccr.loc[ccr['Time'].str.contains('9:30|14:59')]
df=pd.DataFrame(bbr)

#拼接Date和Time
df['Newtime']=df['Date'].str.cat(df['Time'],sep=' ')
#利用dateofweek判断周一还是周五
df['new']=pd.to_datetime(df['Newtime'])
df['dayofweek']=df['new'].dt.dayofweek
#构建新的DataFrame结构，内部包含一周内的第几天，具体时间和A股价格
aar=np.array([df['dayofweek'],df['Newtime'],df['A']])
ds=pd.DataFrame(aar,index=['X th day in one week','Exact time','Stock A Price'])
#通过此DataFrame，找出前一个周五和下一个周一的A股价格
dn=np.array(ds.loc['X th day in one week'])
dd=np.array(ds.loc['Stock A Price'])
tt=np.array(ds.loc['Exact time'])
list1=[]
for i in range(0,len(dn)-1):
    if abs((dn[i+1])-(dn[i]))==4 and dn[i+1]==0:
        list1.append([tt[i],dd[i],tt[i+1],dd[i+1]])#里面元素从左到右依次为：星期五日期和周五价格，周一日期和周一价格
        #zzr=pd.DataFrame(np.array([tt[i],dd[i],tt[i+1],dd[i+1]])).T
        sheet.append([tt[i],dd[i],tt[i+1],dd[i+1]])
#存储Excel
wb.save('LiQing Flexbile Price.xlsx')
