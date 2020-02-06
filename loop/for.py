# -- coding: utf-8 --

#回数指定(0～4)
for i in range(5):
  print("{0}".format(i))
else:
  print("----")

"""
[出力]
0
1
2
3
4
----
"""


#回数指定(1～4)
for i in range(1,5):
  print("{0}".format(i))
else:
  print("----")

"""
[出力]
1
2
3
4
----
"""

#リスト定義
list = ["a","b","c"]

#リスト指定(簡易的)
for idx in enumerate(list):
  print("{0}".format(idx))
else:
  print("----")

"""
[出力]
(0, 'a')
(1, 'b')
(2, 'c')
----
"""


#リスト指定
for idx,elem in enumerate(list):
  print("{0} is {1}".format(idx,elem))
else:
  print("----")

"""
[出力]
0 is a
1 is b
2 is c
----
"""


#リスト指定
for idx,elem in enumerate(list):
  print("{0} is {1}".format(idx,elem))
else:
  print("----")

"""
[出力]
0 is a
1 is b
2 is c
----
"""


#リスト指定(continue)
for idx,elem in enumerate(list):
  if elem == "b":
    continue
  print("{0} is {1}".format(idx,elem))
else:
  print("----")

"""
[出力]
0 is a
2 is c
----
"""


#リスト指定(break)
for idx,elem in enumerate(list):
  if elem == "b":
    break
  print("{0} is {1}".format(idx,elem))
else:
  print("----")

"""
[出力]
1 is b
----
"""

# 逆順
for idx in enumerate(reversed(list)):
  print("{0}".format(idx))
else:
  print("----")

"""
[出力]
(0, 'c')
(1, 'b')
(2, 'a')
----
"""

for i in reversed(list):
  print("{0}".format(i))
else:
  print("----")

"""
[出力]
c
b
a
----
"""
