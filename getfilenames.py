import os
def get_file_name(file_dir):
    L=[]
    for root,dirs,files in os.walk(file_dir):
        for file  in files:
            if os.path.splitext(file)[1] =='.flv':
                L.append(os.path.splitext(file)[0])
    print(type(L))
    print(L)
    return L

dirpath = "D:/drir"
txtname = 'D:/drir/list.txt'


Lis = get_file_name(dirpath)
f =open(txtname,'w')
for i in Lis:
    f.write(i+'\n')

f.close()