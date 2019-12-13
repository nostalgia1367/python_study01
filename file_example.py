# coding=utf-8
import os
import glob

path = os.getcwd()

print(os.path.basename(path))
print(os.path.dirname(path))

allFiles = glob.glob('*')
print(allFiles, '==========', type(allFiles))

for filename in allFiles:
    print(filename)

'''파일 한줄만 읽어옴'''
'''
f = open('regExp.py', 'r')

line = f.readline()
print(line)
f.close()
'''

'''파일 한줄씩 읽어서 for처리
    큰 파일의 경우 비효율적일 수 있음
'''
'''
f = open('regExp.py', 'r')

lines = f.readlines()

for line in lines:
    print(line)

f.close()
'''


'''파일 한줄씩 읽어서 while처리
    큰 파일의 경우에도 효율적일 수 있음
'''
'''
f = open('regExp.py','r')

while True:
    line = f.readline()
    if not line: break
    print(line)

f.close()
'''


with open('regExp.py', 'rt', newline='') as f:

    while True:
        line = f.readline()
        if not line: break
        print(line.splitlines()[0])

    # f.close()  #with문을 사용할 경우 파일 close처리를 하지 않아도 됨.




'''
# tFile = open('파일', 'w')
# tFile.write('쓰기')
# tFile.close()

# tFile = open('파일명','s')
# print(tFile.read())
# tFile.close()

#파일을 읽을때는 readline()과 readlines()
#삭제시에는 os.rmdir(path) 또는 shtuil.rmtree(path)
'''
