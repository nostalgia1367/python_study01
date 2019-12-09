# coding=utf-8
import pickle


colors = ['red', 'green', 'black']

f = open('colors.pickle', 'wb')

# dump를 사용하여 파일을 씀.
pickle.dump(colors, f)
f.close()


del colors

f = open('colors.pickle', 'rb')
colors = pickle.load(f)
print(colors)
f.close()


"""
파일 이동/복사는 shutil(shell util) 내장함수를 이용하여 처리가능.

shutil.copy(t, d)
shutil.move(t, d) # d에 이동하려는 파일명이 존재하면 무브X
os.unlink(path) 파일삭제
os.remove(path) 파일삭제
os.rmdir(path) 해당경로가 비워있어야 삭제가능
shutil.rmtree(path) 해당경로에 파일이 있어도 삭제가

안전삭제
# pip install send2trash

import send2trash


send2trash.send2trash('filename.txt')



"""