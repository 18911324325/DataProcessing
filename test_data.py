import glob
j=0
for i,da in enumerate(glob.glob('*.jpg')):
    print(da,i)
    i+=1
    if i%35==0:
        j+=1
        f = open(str(da), 'rb')
        p = open('../反光马甲/unvest/'+str(j)+'.jpg', 'wb')
        ph=f.read()
        p.write(ph)
