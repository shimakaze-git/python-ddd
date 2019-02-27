from datetime import datetime

print(datetime.now().date())

test_list = [
    {
        'id':1
    },
    {
        'id':2
    },
    {
        'id':3
    },
]



# test_list[0]['id'] = 10

for test in test_list:
    if test['id'] == 1:
        test['id'] = 100
        break
    # print(test)

print(test_list)


import datetime

tstr = '2012-12-29'
tdatetime = datetime.datetime.strptime(tstr, '%Y-%m-%d')
tdate = datetime.date(tdatetime.year, tdatetime.month, tdatetime.day)

print(tdatetime)
print(tdate)
