import os
import glob


for path in glob.glob('D:/TongChuang/DATA/XGJC_DATA/images/val2022/*'):
    dirname, filename = os.path.split(path)
    print(filename)
    if filename[:4]=='微信截图':
        file_new='person_car'+filename[4:]
        new_file = os.path.join(dirname, file_new)
        print(new_file)
        os.rename(path, new_file)