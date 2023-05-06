import os
import sys
import glob
import re
it=0
list1=[]
for data in glob.glob('./label/*.xml'):
    lines = open(data,'r',encoding='utf-8').read().strip().split('\n')
    for line in lines:
        # print(line.strip())
        name=re.match('^<name>.*</name>$',line.strip())
        if name:
            name_str=str(name.group()[6:-7])
            # print(name_str)
            if name_str!='smoke':
            # if name_str!='smoke' and name_str!='gasDetect':
                print(data)
                it+=1
            list1.append(name_str)
print(len(list1))
print('marsk:',it)
list2=list(set(list1))
print(list2)



