
'''
count = 0

if count < 5:
    print("if count", count)

while count < 5:
    print("while count", count)
    count += 1

for x in range(2, -1, -1):
    print("range 2부터 시작하여 -1까지 -1씩 가감", x)

for x in range(0, 11, 2):
    print("range 0부터 11까지 2씩 증가: ", x)

data = list(range(2000, 2016, 2))
print(data)

'''


'''
zip() 함수를 사용하여 어러 시퀀스 병렬로 순회하기
여러 시퀀스 중 가장 짧은 시퀀스가 완료되면 zip()은 멈춘다.
'''

days = ['Monday', 'TuesDay', 'Wednesday']
fruits = ['banana', 'orange', 'peach']
drinks = ['coffee', 'tea', 'beer']
desserts = ['tiramisu', 'ice cream', 'pie', 'pudding']

for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
    print(day, ": drink", drink, "-eat", fruit, "-enjoy", dessert)

kDays = ['월요일', '화요일', '수요일']

listData = list(zip(days, kDays))
print(listData)
print(listData[0])

dictData = dict(zip(days, kDays))
print(dictData)
print(dictData.get('Monday'))

'''
딕셔너리에 setdefault() 함수를 사용하면 해당키가 없으면 추가하고 해당키가 존재하면 아무런 동작을 하지 않는다.
'''