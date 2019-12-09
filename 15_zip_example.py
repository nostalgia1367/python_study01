import zipfile
import os

"""Zip파일 읽기"""

path = os.getcwd()
print(path)

exampleZip = zipfile.ZipFile('this.zip')
print('zip파일 목록:', exampleZip)

fileList = exampleZip.namelist()
fileListTxt = exampleZip.getinfo('fileListTxt.txt')

exampleZip.close()
