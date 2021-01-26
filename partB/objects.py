import os
path = input('Enter the path : ')
folder=jpg=txt=xlsx=jpg=c=cpp=py=html=log=oth=filecount=0
for path,dirs,files in os.walk(path):
    for filename in files:
        print(os.path.join(path ,filename))
    for dirss in dirs:
        folder+=1
    for fil in files:
        if fil.endswith('.jpg'):
            jpg += 1
        elif fil.endswith('.c'):
            c+=1
        elif fil.endswith('.txt'):
            txt+=1
        elif fil.endswith('.xlsx'):
            xlsx+=1
        elif fil.endswith('.cpp'):
            cpp += 1
        elif fil.endswith('.py'):
            py+=1
        elif fil.endswith('.html'):
            html+=1
        else:
            oth+=1
        filecount+=1
print('Folder : {}'.format(folder))
print('JPG : {}'.format(jpg))
print('HTML : {}'.format(html))
print('C : {}'.format(c))
print('CPP : {}'.format(cpp))
print('PY : {}'.format(py))
print('TXT : {}'.format(txt))
print('XLSX : {}'.format(xlsx))
print('OTHs : {}'.format(oth))
print('Total number of files : {}'.format(filecount))
