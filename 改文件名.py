import glob
import os
i=0

for im in glob.glob('D:/TongChuang/DATA/广西鹰眼/卡车卸货/*.jpg'):
    i+=1
    dirname, filename = os.path.split(im)
    print(dirname, filename)
    path='kachexiehuo'+ str(i) +".jpg"
    new_file = os.path.join(dirname, path)
    os.rename(im, new_file)

