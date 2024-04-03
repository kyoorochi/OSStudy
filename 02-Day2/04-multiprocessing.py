from multiprocessing import Process
import os

def func():
    print('안녕, 나는 실험용으로 대충 만들어본 함수야.')
    print('내 프로세스 아이디는:', os.getpid())
    print('나의 부모 프로세스 아이디는:', os.getppid()) # ppid는 부모프로세스 (parent process id)를 뜻한다.

if __name__ == '__main__':
    print('04-multiprocessing.py 프로세스 아이디:', os.getpid())
    child = Process(target=func).start()