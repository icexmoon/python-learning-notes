import random
print(random.random())
#生成一个随机整数
print(random.randint(1,10))
#在一个list中随机选定多个
print(random.sample([1,2,3,4,5,6],3))
# 0.9078117032490299
# 9
# [3, 2, 1]
import sys
print(sys.argv)
print(sys.path)
sys.path.append("D:\\worksapce\\python\\time_tools")
print(sys.path)
# ['D:\\workspace\\python\\python-learning-notes\\note5\\test.py']
# ['D:\\workspace\\python\\python-learning-notes\\note5', 'D:\\software\\Coding\\Python\\python39.zip', 'D:\\software\\Coding\\Python\\DLLs', 'D:\\software\\Coding\\Python\\lib', 'D:\\software\\Coding\\Python', 'C:\\Users\\70748\\AppData\\Roaming\\Python\\Python39\\site-packages', 'D:\\software\\Coding\\Python\\lib\\site-packages', 'D:\\software\\Coding\\Python\\lib\\site-packages\\you_get-0.4.1500-py3.9.egg']
# ['D:\\workspace\\python\\python-learning-notes\\note5', 'D:\\software\\Coding\\Python\\python39.zip', 'D:\\software\\Coding\\Python\\DLLs', 'D:\\software\\Coding\\Python\\lib', 'D:\\software\\Coding\\Python', 'C:\\Users\\70748\\AppData\\Roaming\\Python\\Python39\\site-packages', 'D:\\software\\Coding\\Python\\lib\\site-packages', 'D:\\software\\Coding\\Python\\lib\\site-packages\\you_get-0.4.1500-py3.9.egg', 'D:\\worksapce\\python\\time_tools']
