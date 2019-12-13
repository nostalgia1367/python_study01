import zipfile
import os

"""Zip파일 압축하기"""

path = os.getcwd()
print(path)

newZip = zipfile.ZipFile('this.zip', 'w')
newZip.write('for.py', compress_type=zipfile.ZIP_DEFLATED)
newZip.close()
