import numpy as np 
import pandas as pd 
import random
import openpyxl
'''#将Excel表格创建封装成为函数
#创建一个Excel表格用以导入数据
wb=openpyxl.Workbook()
sheet=wb.active
sheet['A1']='二项分布'
sheet['B1']='整数类型'
sheet['C1']='范围'
for i in range(3):
    #用input函数导入各行数据
    a=np.random.uniform(0,100)
    b=np.random.randint(0,100)
    c=np.random.random()
    sheet.append([a,b,c])
#存储Excel表格
wb.save('Nu&Pa Exercise.xlsx')       

#读取Excel表格数据并进行数据清洗    
df=pd.read_excel('Nu&Pa Exercise.xlsx')
aar=df.applymap(lambda x: str(x)+'---')
print(aar)
#根据现有的列去生成新列
df['new_num']=df.apply(lambda x: x.二项分布 + x.整数类型, axis=1)
print(df['new_num'])'''
#随机创建多维数组并进行describe分析
zzr=pd.DataFrame({'a':[random.expovariate(2)for _ in range(4)],'b':[random.random()for _ in range(4)],
    'c':[random.uniform(0,10)for _ in range(4)]})
print(zzr)
#describe
nf=zzr.describe()
print(nf)
#添加新的一行
zzr['new_numb']=zzr.apply(lambda x: x.a+20,axis=1)
print(zzr)