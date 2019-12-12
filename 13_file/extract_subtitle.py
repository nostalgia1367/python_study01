
def extract_text_from_subtitle(file_name):
    sub_title_contents = []

    file = open(file_name, 'r')
    for line in file:
        line = line.replace('\n', '')
        if len(line) < 3 and line.isnumeric():
            continue
        elif line.count(':') > 2 and line.count('-->') > 0:
            pass
        elif line == '':
            pass
        else:
            sub_title_contents.append(line)

    file.close()
    return sub_title_contents

def make_file_and_save(content, file_name, ext='txt'):
    # 리스트로 파일을 생성
    with open(file_name + '.' + ext, 'w') as file:
        for line in content:
            file.write('%s\n' % line)

def main():
    file_name = 'subtitle.srt'
    subtitle_contents = extract_text_from_subtitle(file_name)
    make_file_and_save(subtitle_contents, file_name, 'txt')
    print('job completed..')


if __name__ == '__main__':
    main()