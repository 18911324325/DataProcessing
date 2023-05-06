import glob
import os
i=0
for path in glob.glob('C:/Users/10515/Downloads/铲车/2/Annotations/*'):
    i+=1
    if i % 2==0:
        os.remove(path)
        print(path)