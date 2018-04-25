#coding:utf-8
import os  
import time  
import tushare as ts  
import pandas as pd  
import numpy as np
  
 
def my_data_input(data):  
    tmp={}
    tmp['code']=input('你的股票代码是：')
    tmp['高价']=input('保底的价格：')
    tmp['成本价']=input('你的股票买入价格是：')
    tmp['低价']=input('期待的卖出价格：')
    tmp['数量']=input('你的股票买入数量是：')
    data.append(tmp)
    return data


#gu_code=['002070','002702','600202','600371','600462','601718','603899']
#gu_code=['002070','002702','600462','601718','000605']

gu_code=[]
my_data=[{'高价': '4.10', 'code':'002070','低价': '4.51', '成本价': 4.564,'数量':500},        
         {'高价': '5.2', 'code':'002702','低价': '5.9', '成本价': 5.805,'数量':1000},
         #{'高价': '8.1', 'code': '600202', '低价': '8.9', '成本价': 8.825,'数量':200}, 
         #{'高价': '10.1', 'code': '600371', '低价': '12.1', '成本价': 10.917,'数量':300},
         {'高价': '5.1', 'code': '600462', '低价': '6.1', '成本价': 5.910,'数量':500}, 
         {'高价': '5.0', 'code': '601718', '低价': '7.0', '成本价': 6.143,'数量':1900},
         #{'高价': '15.0', 'code': '002455', '低价': '7.0', '成本价': 8.820,'数量':600},
         {'高价': '27.0', 'code': '603803', '低价': '20.0', '成本价': 23.550,'数量':500},
         {'高价': '10.0', 'code': '603999', '低价': '5.0', '成本价': 8.215,'数量':200},
            ]
         #{'高价': '30.0', 'code': '603899', '低价': '26.0', '成本价': 29.451,'数量':100}]
#update_or_not = input('是否要更新数据')         
#if update_or_not  == 'y' or update_or_not == 'Y':
#    my_data=my_data_input(my_data)
for i in my_data:
    gu_code.append(i['code'])
    
      
def get_realtime_price(code_lists,my_data):
    #df2=pd.DataFrame(columns=['股票代码',"股票名字","当前价格","实时时间"])#创建一个空的数组格式
    df = ts.get_realtime_quotes(code_lists)
    #current_time = df[['time']]
    e=df.loc[:,['code','name','price']]
    #e.rename(columns={'code':'股票代码','name':'股票名称','price':"当前价格"},inplace=True)
    e['price'][0]=4.020
    origin_price = [value['成本价'] for value in my_data]
    low_price = [float(value['低价']) for value in my_data]
    high_price = [value['高价'] for value in my_data] 
    num = [value['数量'] for value in my_data] 
    #current_price=e['当前价格']
    #print (current_price)
    new_current_price=e.iloc[:,2].values
    new_current_price=[float(item) for item in new_current_price]
    #print (origin_price)
    #print (new_current_price)
    #difference = [value, for i in range(len(origin_price)) value = origin_price[i]-new_current_price[i]]
    difference =list(map(lambda x:x[0]-x[1],zip(new_current_price,origin_price))) 
    profit_loss=list(map(lambda x:x[0]*x[1],zip(difference,num))) 
    rate=list(map(lambda x:x[0]/x[1]*100,zip(difference,origin_price)))
        
    
    #e['time'] = current_time
    #print (difference)


    #e['origin_price'] =origin_price
    e['成本价'] =origin_price
    e['差价']  = difference
    #e['difference_price']  = difference
    
    #e['低价']  = low_price
    #e['高价']  =high_price
    #e['盈利率']  =rate
    e['rate_price']  =rate
    #['profit_loss']  =profit_loss
    e['利润']  =profit_loss

    print (e)
    loss_rate=0
    for loss in profit_loss:
        loss_rate +=loss
    print (('总的利润为%d' % loss_rate).center(50,'*'))
    #print (e['price'][0])# 打印单独的元素
    return rate
    
flag= True
while flag:
    differnent_rate = get_realtime_price(gu_code,my_data)
    for i_rate in differnent_rate:
        if i_rate > 10:
            print ('有股票开始盈利了，赶紧去看，盈利率 : %f' % i_rate)
            flag =False
            break
    time.sleep(5)
        
