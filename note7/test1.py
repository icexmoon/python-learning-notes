fopen = open(file='main.log', mode='r')
for line in fopen:
    print(line)
fopen.close()
# 2021-03-05 17:16:34,829 - set.py[line:4] - this is error message1

# 2021-03-05 17:16:34,831 - set.py[line:5] - this is error message2