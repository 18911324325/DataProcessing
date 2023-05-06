# -*- coding:utf-8 -*-
import glob
for data in glob.glob('./labels/*.txt'):
    f = open(data)  # 打开txt文件
    line = f.readline()  # 以行的形式进行读取文件
    list1 = []
    while line:
        a = line.split()
        b = a[0:10]       # 这是选取需要读取/修改的列        前两列
        list1.append(b)  # 将其添加在列表之中
        line = f.readline()
    f.close()

    with open(data, 'w+') as f_out:
        for i in list1:
            fir = '8'     # 第一列加前缀'9443_'
            print(fir)
            print(i[1])
            f_out.write(fir + ' ' + str(float(i[1])) +' '+str(float(i[2]))+' '+str(float(i[3])) +' '+str(float(i[4])) +'\n')    # 把前两列写入新的txt文件
