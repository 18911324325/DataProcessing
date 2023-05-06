import os
import sys
import glob
import re
it=0
list1=[]
list3=[]
for data in glob.glob('D:/TongChuang/DATA/广西鹰眼/ann/*.xml'):
    f = open(data,'r',encoding='utf-8')
    lin=f.read()
    lines=lin.strip().split('\n')
    for line in lines:
        # print(line.strip())
        name=re.match('^<name>.*</name>$',line.strip())
        if name:
            name_str=str(name.group()[6:-7])
            if name_str=='WJZY':
                list3.append(data[:-4])
                it+=1
            list1.append(name_str)

print(len(list1))
print('truck:',it)
list2=list(set(list1))
print(list2)


# for data in glob.glob('../img/*'):
#     # print(data[7:-4])
#     # print(list3[:-4])
#     for i in list3[:-4]:
#         if data[7:-4] == i:
#             f = open(data, 'rb')
#             ll=f.read()
#             with open('../im/' + data[7:], 'wb') as f_out:
#                 f_out.write(ll)

