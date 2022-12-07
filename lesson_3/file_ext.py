filename1 = 'myfile.txt'
filename2 = 'mydocument.docx'
filename3 = 'run.exe'
filename4 = 'a.r.c.hi.ve.txt.zip'

print(filename4.rfind('.'))
print(filename4.find('.'))

# ищем точку, по ней отрезаем, но лучше искать с правой стороны (rfind)

print(filename1[filename1.rfind('.')+1:])
print(filename2[filename2.rfind('.')+1:])
print(filename3[filename3.rfind('.')+1:])
print(filename4[filename4.rfind('.')+1:])
