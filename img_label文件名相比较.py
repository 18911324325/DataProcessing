import os
import sys
import glob
import re
it=0
list3=[]
list=[]
test=''

for data in glob.glob('D:/TongChuang/DATA/广西鹰眼/TXT/*'):
    list3.append(data[28:-4])

for data in glob.glob('D:/TongChuang/DATA/广西鹰眼/IMG/*'):
    for i in list3:
        if data[28:-4] == i:
            list.append(data[28:-4])
    if len(list)==0:
        print(data[28:-4])
        # os.remove(data)
    list=[]



