# -- coding: utf-8 --

#辞書設定
dict_a = {'key1':10,'key2':100}

#キー名と値のペア取得
print(dict_a.items())
'''
[出力]
dict_items([('key1', 10), ('key2', 100)])
'''

#キー名取得
print(dict_a .keys())
'''
[出力]
dict_keys(['key1', 'key2'])
'''

#値取得
print(dict_a .values())
'''
[出力]
dict_values([10, 100])
'''

#要素数取得
print('len(dict_a) = {0}'.format(len(dict_a)))
'''
[出力]
len(dict_a) = 2
'''

#指定した文字列が辞書のキーにあるか確認
print("'key1' in dict_a = {0}".format('key1' in dict_a))
print("'key3' in dict_a = {0}".format('key3' in dict_a))
'''
[出力]
'key1' in dict_a = True
'key3' in dict_a = False
'''

#指定した値が辞書の値にあるか確認
print('10 in dict_a.values() = {0}'.format(10 in dict_a.values()))
print('20 in dict_a.values() = {0}'.format(20 in dict_a.values()))
'''
[出力]
10 in dict_a.values() = True
20 in dict_a.values() = False
'''

#指定した値が辞書や値にないことを確認
print("'key100' not in dict_a = {0}".format('key100' not in dict_a))
print('1000 not in dict_a.values() = {0}'.format(1000 not in dict_a.values()))
'''
[出力]
'key100' not in dict_a = True
1000 not in dict_a.values() = True
'''

#キーを指定して値を取得
print("dict_a['key1'] = {0}".format(dict_a['key1']))
'''
[出力]
dict_a['key1'] = 10
'''

#キーを指定して値を変更
dict_a['key1'] = 50
print("dict_a['key1'] = {0}".format(dict_a['key1']))
'''
[出力]
dict_a['key1'] = 50
'''

#キーの追加
dict_a['new_key'] = 'new_value'
print(dict_a.items())
'''
[出力]
dict_items([('key1', 50), ('key2', 100), ('new_key', 'new_value')])
'''

#キーと値の削除
del dict_a['key2']
print(dict_a.items())
'''
[出力]
dict_items([('key1', 50), ('new_key', 'new_value')])
'''
