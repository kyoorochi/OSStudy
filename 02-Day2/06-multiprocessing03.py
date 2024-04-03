from multiprocessing import Process
import os, time

def americano():
    print('아메리카노 프로세스 아이디:', os.getpid())
    print('부모 프로세스 아이디:', os.getppid())

def latte():
    print('라떼 프로세스 아이디:', os.getpid())
    print('부모 프로세스 아이디:', os.getppid())

def espresso():
    print('에스프레소 프로세스 아이디:', os.getpid())
    print('부모 프로세스 아이디:', os.getppid())

if __name__ == '__main__':
    print('06-multiprocessing03.py 프로세스 아이디:', os.getpid())
    child1 = Process(target=americano)
    child1.start()
    time.sleep(0.5)
    child2 = Process(target=latte)
    child2.start()
    time.sleep(0.5)
    child3 = Process(target=espresso)
    child3.start()
    time.sleep(0.5)