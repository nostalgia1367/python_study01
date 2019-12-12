import os
import zipfile

def backup_to_zip(folder):
    # 폴더내의 파일을 zip 파일로 백업

    # 작업디렉토리 이동
    os.chdir(folder)
    print('current working directory is ' + os.getcwd())

    # zip 파일명 생성
    zip_filename = os.path.basename(folder) + '.zip'
    print('Creating %s' % zip_filename)

    # backup 폴더 생성
    os.mkdir('..\\backup')

    #backup 폴더에 백업파일을 생성
    backupzip = zipfile.ZipFile('..\\backup\\' + zip_filename, 'w')

    # 작업디렉토리를 순회하면서 백업파일을 생성
    # 1.확장자가 .jpg 파일을 백업하지 않는다.
    for foldername, subfolders, filenames in os.walk('.'):

        # 현재폴더를 ZIP파일에 추가
        backupzip.write(foldername)

        # 하위 폴더를 ZIP파일에 추가
        for subfolders in subfolders:
            backupzip.write(os.path.join(foldername + subfolders))

        # 하위 폴더의 파일들을 ZIP파일에 추가
        for zip_filename in zip_filename:
            if filename.endswith('.jpg'):
                print('skip compressing file : ' + filename)
                continue
            backupzip.write(os.path.join(foldername, filename))

    backupzip.close()
    print('backup completed..')


def main():
    backup_to_zip('C"\\Users\\Administrator\\PycharmProjects\\hello\\work-for-python')

if __name__ == '__main__':
    main()
