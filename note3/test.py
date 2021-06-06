a = ("a","b","c")
print(a)
# ('a', 'b', 'c')
a = tuple(["a","b","c"])
print(a)
# ('a', 'b', 'c')
a = {"a","b","c"}
print(a)
# {'a', 'c', 'b'}
a = set("aabbccddee")
print(a)
# {'c', 'b', 'a', 'd', 'e'}
a = set("abcde")
b = set("be12345gw")
c = a.intersection(b)
print(a)
print(b)
print(c)
# {'d', 'c', 'b', 'e', 'a'}
# {'b', 'w', 'g', 'e', '2', '5', '1', '4', '3'}
# {'e', 'b'}
a = set("abcde")
b = set("be12345gw")
c = a.union(b)
print(a)
print(b)
print(c)
# {'d', 'a', 'b', 'e', 'c'}
# {'g', '4', 'w', 'b', '1', '2', 'e', '3', '5'}
# {'d', 'g', '4', 'a', 'w', 'b', '1', '2', 'e', '3', '5', 'c'}
a = set("abcde")
b = set("be12345gw")
c = a.difference(b)
print(a)
print(b)
print(c)
# {'d', 'c', 'b', 'e', 'a'}
# {'2', '3', 'w', '5', 'b', 'e', '1', 'g', '4'}
# {'d', 'a', 'c'}
a = set("abcde")
#追加元素
a.add("f")
print(a)
#删除元素
a.remove("a")
print(a)
# {'e', 'd', 'a', 'c', 'f', 'b'}
# {'e', 'd', 'c', 'f', 'b'}

