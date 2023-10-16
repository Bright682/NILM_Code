import pandas as pd

from nilmtk import DataSet
import numpy as np
import matplotlib.pyplot as plt
#加载文件 保存到文件夹里
test = DataSet('E://CXD_File//NILM_Data//UKData//ukdale.h5')
for house_id in range(1,6):
    building = house_id  ## 选择家庭house
    test.set_window(start="18-03-2013") ## 2013年3月18号之后的作为数据集
    test_elec = test.buildings[building].elec
    gt= {}
    df=pd.DataFrame()
    col_id=1
    for meter in test_elec.submeters().meters:
        gen = next(meter.load())
        values = gen.values
        index = gen.index
        label = meter.label()
        i = 0;
        while(1):
            name = label+str(i)
            if name not in gt:
                break
            else:
                i += 1
        np.save('UKData'+str(house_id)+'/'+name,values)
        gt[name] = 1
        print(values.shape,'   ',index.shape)
        print('saving...', name)
        #df[name] = pd.Series(values[:,0])
        #col_id=col_id+1
    # 计算每一行的总和并插入到第一列
    #df.insert(0, 'Power_Sum', df.sum(axis=1))
    #df.to_csv("UK_Dale_csv//house"+str(house_id)+".csv")
    print("npy to csv completed!")
#加载文件夹里的.npy文件













