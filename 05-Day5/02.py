# 파일 관련 예외는 OS와 관계가 있다.

try:
    f = open('none.txt', 'r')
    print(f.read())
    f.close()
except FileNotFoundError as e:
    print(e)
    print(issubclass(FileNotFoundError, OSError))
    print(issubclass(ZeroDivisionError, OSError))