import re
import time
import random
import shutil



"""
    search()
    fidnall()
    sub()
    
"""


print(random.choice([1,2,3,4,5]))

print(random.rand)

phonenum_regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
print(round(time.time()))


mo = phonenum_regex.search('My number is 415-555-4242.')

area_code, num = mo.groups()

print(area_code)

