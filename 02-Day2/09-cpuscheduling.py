from multiprocessing import Process
import os, time

def americano():
    while True:
        try:
            print('아메리카노 프로세스 아이디:', os.getpid())
            print('부모 프로세스 아이디:', os.getppid())
        except KeyboardInterrupt:
            break

def latte():
    while True:
        try:
            print('라떼 프로세스 아이디:', os.getpid())
            print('부모 프로세스 아이디:', os.getppid())
        except KeyboardInterrupt:
            break

def espresso():
    while True:
        try:
            print('에스프레소 프로세스 아이디:', os.getpid())
            print('부모 프로세스 아이디:', os.getppid())
        except KeyboardInterrupt:
            break

if __name__ == '__main__':
    print('09-cpuscheduling.py 프로세스 아이디:', os.getpid())
    child1 = Process(target=americano)
    child1.start()
    time.sleep(0.5)
    child2 = Process(target=latte)
    child2.start()
    time.sleep(0.5)
    child3 = Process(target=espresso)
    child3.start()
    time.sleep(0.5)