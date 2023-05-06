import glob

for path in glob.glob('D:/TongChuang/DATA/广西鹰眼/铲车/txt/*'):
    f=open(path, 'r')
    print(path,'****',path[31:])
    newPath='D:/TongChuang/DATA/广西鹰眼/铲车/txt1/'+path[31:]
    print(newPath)
    new_F=open(newPath, 'w')
    for line in f.readlines():
        if line[0]=='8':
            newline='4'+line[1:]
            new_F.write(newline)
        else:
            new_F.write(line)
    f.close()
    new_F.close()