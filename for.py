


# List For
for i in [0,1,2,3,4,5,6,7,8,9,10]:
    print(i)

# range For
for i in range(0, 11):
    print(i)

# list & tuple For
hobby = ['game', 'shopping', 'work']
for h in hobby:
    print('내 취미는 %s' % h,' 입니다')
    print('내 취미는 ',h, ' 입니다.')

# dictinary For
hobby2 = {'item1':'game',
          'item2':'shopping',
          'item3':'work'
          }
for i, data in hobby2.items():
    print('%s in %s' % (i, data))

