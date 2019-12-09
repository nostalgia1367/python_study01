## Before
## 전역함수로 함수를 호출하지 말고 main()함수를 만들어서 메인을 호출하라
"""
def average(num):
    total = 0
    for n in num:
        total = total + n

    avg = total/len(num)
    return avg

# main
prices = [29, 21, 55, 10]

result = average(prices)

print(result)
"""


#After

def average(num):
    total = 0
    for n in num:
        total = total + n

    avg = total / len(num)
    return avg


def main():
    prices = [29, 21, 55, 10]

    result = average(prices)

    print(result)


main()


'''
함수 파라미터 
    - 위치 파라미터
    - 키워드 파라미터
'''

def connect_URI(server, port):
    str = 'http://' + server + ':' + port
    return print(str)

connect_URI('test.com', '8080')
connect_URI(port='8080', server='test.com')

connect_URI('test.com', port='8080') #하나만 키워드 파라미터 써도 됨.
connect_URI(port='8080', server='test.com') #위치를 바꿔도 무관함.

'''
기본 파라미터 값 지정
    - 파라미터에 기본값을 지정할 수 있다.
    - 함수를 호출할 때 파라미터를 제공하지 않으면 기본값을 사용한다.
'''

def times(a=10, b=20):
    return a * b

x = times()
y = times(5)

print(x)
print(y)


'''
함수 파라미터 : 가변 파라미터
'''

def var_param_test(*p):
    return p

a = var_param_test(1,2,3,4,5)
print(a)
print(type(a))

def var_param_test2(**p):
    for x,v in p.items():
        print(x,v)

a2 = var_param_test2(a=1, b=2, c=3, d=4, e=5, f=6)
print(a2)
print(type(a2))


