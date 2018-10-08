# -- coding: utf-8 --

#リスト定義
list = ["a","b","c"]

#リストをすべて表示
i = 0
while i < len(list):
  print("{0} is {1}".format(i,list[i])) 
  i=i+1
else:
  print("----")

"""
[出力]
0 is a
1 is b
2 is c
----
"""


#リストを表示(値がcになるまで) 
i = 0
while list[i] != "c":
  print("{0} is {1}".format(i,list[i])) 
  i=i+1
else:
  print("----")

"""
[出力]
0 is a
1 is b
----
"""
