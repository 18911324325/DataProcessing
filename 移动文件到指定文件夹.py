import os
import shutil
import glob
# srcfile 需要复制、移动的文件
# dstpath 目的地址

def mymovefile(srcfile, dstpath):  # 移动函数
    if not os.path.isfile(srcfile):
        print("%s not exist!" % (srcfile))
    else:
        fpath, fname = os.path.split(srcfile)  # 分离文件名和路径
        if not os.path.exists(dstpath):
            os.makedirs(dstpath)  # 创建路径
        shutil.move(srcfile, dstpath + fname)  # 移动文件
        print("move %s -> %s" % (srcfile, dstpath + fname))

if __name__ == '__main__':
    src_dir = 'D:/YINGYAN/labels/train2023/'
    dst_dir = 'D:/YINGYAN/labels/val2023/'  # 目的路径记得加斜杠
    src_file_list = glob.glob(src_dir + '*')  # glob获得路径下所有文件，可根据需要修改
    i=0
    for srcfile in src_file_list:
        i+=1
        if i % 5 == 0:
            mymovefile(srcfile, dst_dir)  # 移动文件