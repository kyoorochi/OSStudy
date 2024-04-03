# 내 파이썬 프로그램의 이름을 알아보자

import psutil, os

if __name__ == '__main__':
    print('10-homework.py 프로세스의 아이디는:', os.getpid())

for proc in psutil.process_iter():
    if os.getpid() == proc.pid:
        print(proc.name, proc.pid)