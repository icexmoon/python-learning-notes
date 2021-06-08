hellowStr = "Hellow world!"
hellowByte = bytes(hellowStr, encoding='ascii')
print(hellowByte)
print(hellowByte[0])
# 输出
# b'Hellow world!'
# 72
hellowBytes = "Hellow wolrd!".encode(encoding='ascii')
print(hellowBytes)
print(hellowBytes[0])
hellowStr = hellowBytes.decode(encoding='ascii')
print(hellowStr)
# b'Hellow wolrd!'
# 72
# Hellow wolrd!
hellowBytes = "你好 世界！".encode(encoding='UTF-8')
print(hellowBytes)
print(hellowBytes[0:6])
subBytes = hellowBytes[0:6]
print(subBytes.decode(encoding='UTF-8'))
hellowByteArray = bytearray(hellowBytes)
print(hellowByteArray)
print(hellowByteArray[0:6])
print(hellowByteArray[0:6].decode(encoding='UTF-8'))
# b'\xe4\xbd\xa0\xe5\xa5\xbd \xe4\xb8\x96\xe7\x95\x8c\xef\xbc\x81'
# b'\xe4\xbd\xa0\xe5\xa5\xbd'
# 你好
# bytearray(b'\xe4\xbd\xa0\xe5\xa5\xbd \xe4\xb8\x96\xe7\x95\x8c\xef\xbc\x81')
# bytearray(b'\xe4\xbd\xa0\xe5\xa5\xbd')
# 你好
with open(file='test.png',mode='rb') as fopen:
    imgView = memoryview(fopen.read())
headerView = imgView[0:10]
headerBytes = bytes(headerView)
print(headerBytes)
#b'\x89PNG\r\n\x1a\n\x00\x00'
"你好世界！".encode("ascii")
# Traceback (most recent call last):
#   File "d:\workspace\python\test\test.py", line 1, in <module>
#     "你好世界！".encode("ascii")
# UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-4: ordinal not in range(128)
hellowBytes = "你好世界ABC！".encode("ascii",errors='ignore')
print(hellowBytes)
print(hellowBytes.decode('ascii'))
hellowBytes = "你好世界ABC！".encode("ascii",errors='replace')
print(hellowBytes)
print(hellowBytes.decode('ascii'))
# b'ABC'
# ABC
# b'????ABC?'
# ????ABC?
hellowBytes = "你好世界ABC！".encode("UTF-8",errors='ignore')
hellowStr = hellowBytes.decode(encoding='gb2312',errors='ignore')
print(hellowStr)
hellowStr = hellowBytes.decode(encoding='gb2312')
# 浣濂戒ABC锛
# Traceback (most recent call last):
#   File "d:\workspace\python\test\test.py", line 4, in <module>
#     hellowStr = hellowBytes.decode(encoding='gb2312')
import chardet
hellowStr = "你好世界！"
hellowBytes = hellowStr.encode("UTF-8")
print(chardet.detect(hellowBytes))
hellowBytes = hellowStr.encode('gb2312')
print(chardet.detect(hellowBytes))
hellowStr = "当时时间仓促，就简单的配置了下，今天来探讨下如何使用Windows Teriminal进行SSH连接"
hellowBytes = hellowStr.encode('gb2312')
print(chardet.detect(hellowBytes))
# {'encoding': 'utf-8', 'confidence': 0.99, 'language': ''}
# {'encoding': None, 'confidence': 0.0, 'language': None}
# {'encoding': 'GB2312', 'confidence': 0.99, 'language': 'Chinese'}
with open(file='test.txt', mode='w', encoding='UTF-8') as fopen:
    print("你好世界！", file=fopen)
with open(file='test.txt', mode='r') as fopen:
    print(fopen)
# <_io.TextIOWrapper name='test.txt' mode='r' encoding='cp936'>
from unicodedata import normalize
s1 = "café"
s2 = "cafe\u0301"
print(s1, s2)
print(s1 == s2)
print(len(s1), len(s2))
print(bytes(s1, encoding='UTF-8'), bytes(s2, encoding='UTF-8'))
# café café
# False
# 4 5
# b'caf\xc3\xa9' b'cafe\xcc\x81'
from unicodedata import normalize
s1 = "café"
s2 = "cafe\u0301"
print(normalize('NFC', s1) == normalize('NFC', s2))
print(normalize('NFD', s1) == normalize('NFD', s2))
# True
# True
from unicodedata import normalize
s = "9¹²"
print(normalize('NFKC', s))
# 912
from unicodedata import name
s = "ABC".casefold()
print(s)
s = "ABC".lower()
print(s)
# abc
# abc
from unicodedata import normalize


def nfcEqual(s1, s2):
    return normalize('NFC', s1) == normalize('NFC', s2)


def foldEqual(s1, s2):
    return normalize('NFC', s1).casefold() == normalize('NFC', s2).casefold()
l = ["你好","我好","大家好"]
print(sorted(l))
#['你好', '大家好', '我好']
import pyuca
ct = pyuca.Collator()
l = ["你好", "我好", "大家好"]
print(sorted(l, key=ct.sort_key))
#['你好', '大家好', '我好']
import re
import unicodedata
reDigit = re.compile(r'\d')
s = "1\xbc\xb2\u0969\u136b\u216b\u2466\u2480\u3285"
for char in s:
    print("U+%04x" % ord(char),
          char.center(6),
          're_dig' if reDigit.match(char) else '-',
          'is_dig' if char.isdigit() else '-',
          'is_num' if char.isnumeric() else '-',
          format(unicodedata.numeric(char), '5.2f'),
          unicodedata.name(char),
          sep='\t')
# U+0031    1     re_dig  is_dig  is_num   1.00   DIGIT ONE
# U+00bc    ¼     -       -       is_num   0.25   VULGAR FRACTION ONE QUARTER
# U+00b2    ²     -       is_dig  is_num   2.00   SUPERSCRIPT TWO
# U+0969    ३     re_dig  is_dig  is_num   3.00   DEVANAGARI DIGIT THREE
# U+136b    ፫     -       is_dig  is_num   3.00   ETHIOPIC DIGIT THREE
# U+216b    Ⅻ    -       -       is_num  12.00   ROMAN NUMERAL TWELVE
# U+2466    ⑦     -       is_dig  is_num   7.00   CIRCLED DIGIT SEVEN
# U+2480    ⒀    -       -       is_num  13.00   PARENTHESIZED NUMBER THIRTEEN
# U+3285    ㊅    -       -       is_num   6.00   CIRCLED IDEOGRAPH SIX
import re
reNumStr = re.compile(r'\d+')
reWordStr = re.compile(r'\w+')
reNumBytes = re.compile(rb'\d+')
reWordBytes = re.compile(rb'\w+')
s = ("Ramanujan saw \u0be7\u0bed\u0be8\u0bef"
"¼ 1 2 3 Ⅻ")
b = s.encode(encoding='UTF-8')
print('numbers')
print(reNumStr.findall(s))
print(reNumBytes.findall(b))
print('words')
print(reWordStr.findall(s))
print(reWordBytes.findall(b))
# numbers
# ['௧௭௨௯', '1', '2', '3']
# [b'1', b'2', b'3']
# words
# ['Ramanujan', 'saw', '௧௭௨௯¼', '1', '2', '3', 'Ⅻ']
# [b'Ramanujan', b'saw', b'1', b'2', b'3']
import os
import pprint
with open(file='测试.txt',mode='w',encoding='UTF-8') as fopen:
    pass
pprint.pprint(os.listdir('.'))
pprint.pprint(os.listdir(b'.'))
# ['.vscode',
#  'array.file',
#  'carrier_game',
#  'carrier_game.zip',
#  'carrier_game_error',
#  'response.html',
#  'test.png',
#  'test.py',
#  'test.txt',
#  '测试.txt']
# [b'.vscode',
#  b'array.file',
#  b'carrier_game',
#  b'carrier_game.zip',
#  b'carrier_game_error',
#  b'response.html',
#  b'test.png',
#  b'test.py',
#  b'test.txt',
#  b'\xe6\xb5\x8b\xe8\xaf\x95.txt']