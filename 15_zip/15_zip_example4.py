# coding=utf-8

import os, zipfile

def backup_to_zip(folder):

    # 폴더내의 파일을 zip 파일로 백업

    # 작업디렉토리 이동
    os.chdir(folder)
    print('해당 디렉토리 확인: '+ os.getcwd())

    # zip 파일명 생성
    zip_filename = os.path.basename(folder) + '.zip'

    print('폴더경로 확인: ' + os.path.dirname(folder))
    print('파일이름 확인: '+ zip_filename)

    # backup 폴더 생성
    if(os.path.exists(os.path.join(os.path.dirname(folder), 'backup_temp'))):
        print('폴더 존재X')
    else:
        print('폴더 존재 > 폴더 생성')
        os.mkdir(os.path.join(os.path.dirname(folder) , 'backup_temp'))




    # backup 폴더에 백업파일 생성
    backupzip = zipfile.ZipFile(os.path.join(os.path.dirname(folder),'backup_temp')+ '/' + zip_filename, 'w')


    # 작업디렉토리를 순회하면서 백업파일을 생성
    # 1. 확장자가 .jpg 파일은 백업X
    for foldername, subfolders, filenames in os.walk('.'):

        # 현재폴더를 zip파일에 추가
        #backupzip.write(foldername)
        print('foldername: '+ foldername)

        # 하위 폴더를 zip파일에 추가
        for subfolder in subfolders:
            backupzip.write(os.path.join(foldername,  subfolder))
            print('subfolder: ' + subfolder)

        # 하위 폴더의 파일들을 ZIP파일에 추가
        for filename in filenames:
            #backupzip.write(os.path.join(foldername, filename))
            print('filename: '+ filename)

    backupzip.close()
    print('압축이 완료되었습니다.')

def main():
    # backup_to_zip(os.path.join('/Users/nostalgia','Documents','keyfile'))
    backup_to_zip('/Users/nostalgia/Documents/keyfile')

main()

