import glob
import os
import cv2
i=0
k=0
for im in glob.glob('D:/Video_yingyan/*'):
    print(im[-10:])
    if im[-10:] != '2023-01-17':
        continue
    for path in glob.glob(im+"/*"):
        cap=cv2.VideoCapture(path)
        while True:
            try:
                i += 1
                ret,frame=cap.read()
                if i % 40 != 0:
                    continue
                k+=1
                imageName = str(im[-10:])+'_'+str(k) + ".jpg"
                imagePath = r"D:/photo/"+str(im[-10:])+'/'
                if not os.path.exists(imagePath):
                    os.makedirs(imagePath)
                print(imagePath + imageName)
                cv2.imwrite(imagePath + imageName, frame, [cv2.IMWRITE_JPEG_QUALITY, 100])
                cv2.imshow('img', frame)
                cv2.waitKey(1)
            except Exception as e:
                break




