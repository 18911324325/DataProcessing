import glob
import os
i=0

for im in glob.glob('./Annotations_0508/*'):
    i+=1
    dirname, filename = os.path.split(im)
    print(dirname, filename)
    path='person_'+ str(i) +".xml"
    new_file = os.path.join(dirname, path)
    os.rename(im, new_file)

