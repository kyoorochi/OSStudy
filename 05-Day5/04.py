# os 파일 시스템 관련 함수
import os

pwd = 'E:\OS-Study'

# 디렉토리 내부 리스트 업
filenames = os.listdir(pwd)
print(filenames)

# 디렉터리인지 아닌지 여부
print(os.path.isdir(filenames[1]))
print(os.path.isdir(pwd + '/01-Day1'))

# 파일인지 아닌지 여부
print(os.path.isfile(filenames[1]))
print(os.path.isfile(pwd + '/01-Day1'))

# 파일이름과 확장자 분리
filepath = pwd + '/' + filenames[1]
print(filepath)
name, ext = os.path.splitext(filepath)
print(name)
print(ext)