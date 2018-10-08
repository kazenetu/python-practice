# -- coding: utf-8 --

#セット設定
set_a = {1,2,3,1,'a',4,'a'}
set_b = {2,3,5,'a',4,'a'}
set_c = {2,5,'b'}

#union(重複分を除いたセットを作成)
print(set_a.union(set_b))
"""
[出力]
set(['a', 1, 2, 3, 4, 5])
"""

print(set_a.union(set_b,set_c))
"""
[出力]
set(['a', 1, 2, 3, 4, 5, 'b'])
"""

#intersection(セットすべてで重複する要素のセットを作成)
print(set_a.intersection(set_b))
"""
[出力]
set(['a', 2, 3, 4])
"""

print(set_a.intersection(set_b,set_c))
"""
[出力]
set([2])
"""

#difference(引数のセットらに存在しない要素のセットを作成)
print(set_a.difference(set_b))
"""
[出力]
set([1])
"""

print(set_b.difference(set_a))
"""
[出力]
set([5])
"""

print(set_a.difference(set_b,set_c))
"""
[出力]
set([1])
"""

#symmetric_difference(一方に存在しない要素のセットを作成)
print(set_a.symmetric_difference(set_b))
"""
[出力]
set([1, 5])
"""

print(set_b.symmetric_difference(set_a))
"""
[出力]
set([1, 5])
"""

print(set_a.symmetric_difference(set_c))
"""
[出力]
set(['a', 1, 'b', 4, 5, 3])
"""

#superset/subset(要素がすべて含まれるか)
set_super = set_a.copy()
set_super.add('b')

print("set_super.issuperset(set_a) = {0}".format(set_super.issuperset(set_a)))
"""
[出力]
set_super.issuperset(set_a) = True
"""

print("set_a.issuperset(set_super) = {0}".format(set_a.issuperset(set_super)))
"""
[出力]
set_a.issuperset(set_super) = False
"""

print("set_super.issubset(set_a) = {0}".format(set_super.issubset(set_a)))
"""
[出力]
set_super.issubset(set_a) = False
"""

print("set_a.issubset(set_super) = {0}".format(set_a.issubset(set_super)))
"""
[出力]
set_a.issubset(set_super) = True
"""
