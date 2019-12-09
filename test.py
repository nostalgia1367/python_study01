"""
주석입니다.
주석 주석
"""

'''
ㅇㄹㅇㅇㄹㅇㄹㅇㄹ
ㅇㄹㅇㄻㄴㅇㄹㄴㅇㄹ
'''

# 주석입니다.

a = 123
b = 1.23
print(a + b)
type(b)

empty_tuple1 = ('1', '2', '3')
empty_tuple2 = '1', '2', '3'

print('empty_tuple1: ', empty_tuple1)
print('empty_tuple2: ', empty_tuple2)
print(empty_tuple1 == empty_tuple2)

dict1 = {'item1': 'hello'}
print(dict1['item1'])

print(dict1.get('item1'))

listOfList = [['key1', 'value1'], ['key2', 'value2'], ['key3', 'value3']]
print(dict(listOfList), ' : : ', type(dict(listOfList)))

listOfString = ['aa', 'bb', 'cc']
print(dict(listOfString), ' : : ', type(dict(listOfString)))

tupleOfString = ('aa', 'bb', 'cc')
print(dict(tupleOfString), ' : : ', type(dict(tupleOfString)))



list_data = [{'1': '1'}, {'2', '2'}]  # list
print(list_data, type(list_data))

dict_data = {
    '1': {'data': '1'},
    '2': {'data': '2'}
}  # dictinary
print(dict_data, type(dict_data))


address = [
    {'id': 1, 'name': 'hong kildong', 'email' : 'hong@mail.com', 'hp_num': '010-222-3333'},
    {'id': 2, 'name': 'lee soonsin', 'email' : 'lee@mail.com', 'hp_num': '010-222-3333'},
    {'id': 3, 'name': 'jang youngsil', 'email' : 'jang@mail.com', 'hp_num': '010-222-3333'},
    {'id': 4, 'name': 'king sejong', 'email' : 'king@mail.com', 'hp_num': '010-222-3333'},
]

address_new = {
    '1': {'name': 'hong kildong', 'email': 'hong@mail.com', 'hp_num': '010-222-3333'},
    '2': {'name': 'lee soonsin', 'email': 'lee@mail.com', 'hp_num': '010-222-3333'},
    '3': {'name': 'jang youngsil', 'email': 'jang@mail.com', 'hp_num': '010-222-3333'},
    '4': {'name': 'king sejong', 'email': 'king@mail.com', 'hp_num': '010-222-3333'},
}



