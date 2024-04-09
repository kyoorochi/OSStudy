number = 99

b_num = bin(number) # bin : 주어진 정수를 2진수로 반환한다.
print(b_num)

o_num = oct(number) # oct : 주어진 정수를 8진수로 반환한다.
print(o_num)

h_num = hex(number) # hex : 주어진 정수를 16진수로 반환한다.
print(h_num)

# 2진법을 8진법으로 구현시도 int(str(b_num), 2) 에서 , 2는 2진법임을 알려주는것. 8로 하면 8진법을 알려주는 게 된다.
decimal_number = int(str(b_num), 2)
oct_num = oct(decimal_number)
print(oct_num)