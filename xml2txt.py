
import os
import xml.etree.ElementTree as ET


def ConverCoordinate(imgshape, bbox):
    # 将xml像素坐标转换为txt归一化后的坐标
    xmin, xmax, ymin, ymax = bbox
    width = imgshape[0]
    height = imgshape[1]
    dw = 1. / width
    dh = 1. / height
    x = (xmin + xmax) / 2.0
    y = (ymin + ymax) / 2.0
    w = xmax - xmin
    h = ymax - ymin

    # 归一化
    x = x * dw
    y = y * dh
    w = w * dw
    h = h * dh

    return (x,y,w,h)

def readxml(image_set, filename):
    outfile = open('{}/txt/{}.txt'.format(image_set, filename), 'w')   # 注意：在’ann‘文件夹标注文件夹同级新建txt文件夹
    filetree = ET.parse('{}/ann/{}.xml'.format(image_set, filename))   # 'ann'为标注文件夹名称
    root = filetree.getroot()
    size = root.find('size')
    width = int(size.find('width').text)
    height = int(size.find('height').text)
    imgshape = (width, height)

    for obj in root.findall('object'):
        # 获取类别名，判断是否在classes中，不存在则跳过。
        obj_name = obj.find('name').text
        if obj_name not in classes:
            continue
        obj_id = classes.index(obj_name)
        # 获取每个obj的bbox框的左上和右下坐标
        bbox = obj.find('bndbox')
        xmin = float(bbox.find('xmin').text)
        xmax = float(bbox.find('xmax').text)
        ymin = float(bbox.find('ymin').text)
        ymax = float(bbox.find('ymax').text)
        bbox_coor = (xmin, xmax, ymin, ymax)

        txtvalue = ConverCoordinate(imgshape, bbox_coor)
        outfile.write('{}'.format(obj_id) + ' ' + ' '.join([str(i) for i in txtvalue]) + '\n')


if __name__ == '__main__':
    # 超参数
    image_set = 'D:/TongChuang/DATA/广西鹰眼/卡车卸货'  # xml到标注文件夹的上一级目录 不需要'/'
    # classes = ['person','gasDetect','smoke','mask', 'uniform', 'safehat', 'un_uniform']
    # classes = ['uniform', 'un_uniform', 'mask', 'safehat', 'un_safehat', 'person','gasDetect','smoke','face']
    # classes = ['person', 'car']   # 标注的类别
    classes = ['YC', 'LL','KC','KCZY','CC','CCZY','WJ','WJZY']   # 标注的类别
    # 配置JPEG文件路径
    localdir = os.getcwd()
    datasetdir = os.path.join(localdir, image_set)
    JPEGImagefiledir = os.path.join(datasetdir, 'ann')  # 'ann'为标注文件夹名称
    for filename in os.listdir(JPEGImagefiledir):
        print(filename[:-4])
        readxml(image_set, filename[:-4])
