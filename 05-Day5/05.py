# 경로와 확장자를 이용해 파일을 찾고, 내용 읽기

import os

def searchFile(dirname, extension):
    filenames = os.listdir(dirname)
    for filename in filenames:
        filepath = os.path.join(dirname, filename)
        if os.path.isdir(filepath):
            searchFile(filepath, extension)
        elif os.path.isfile(filepath):
            name, ext = os.path.splitext(filepath)
            if ext == extension:
                with open(filepath, 'r', encoding='utf-8') as f:
                    print(f.read())

# 경로에 언더바가 아닌 대시가 붙어있어서인가 작동을 하지 않았다.
# 그러나 05-Day5 폴더명에서 05- 를 빼고 실행한 결과 정상 작동하였다.
searchFile('E:\OS-Study\05-Day5', '.js')