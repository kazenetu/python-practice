# -- coding: utf-8 --

#辞書設定
dict_a = {'key1':10,'key2':100}

#キー名と値のペア取得
print(dict_a.items())

#キー名取得
print(dict_a .keys())

#値取得
print(dict_a .values())

#要素数取得
print('len(dict_a) = {0}'.format(len(dict_a)))

#指定した文字列が辞書のキーにあるか確認
print("'key1' in dict_a = {0}".format('key1' in dict_a))
print("'key3' in dict_a = {0}".format('key3' in dict_a))

#指定した値が辞書の値にあるか確認
print('10 in dict_a.values() = {0}'.format(10 in dict_a.values()))
print('20 in dict_a.values() = {0}'.format(20 in dict_a.values()))

#指定した値が辞書や値にないことを確認
print("'key1' not in dict_a = {0}".format('key1' not in dict_a))
print('10 not in dict_a.values() = {0}'.format(10 not in dict_a.values()))

#キーを指定して値を取得
print("dict_a['key1'] = {0}".format(dict_a['key1']))

#キーを指定して値を変更
dict_a['key1'] = 50
print("dict_a['key1'] = {0}".format(dict_a['key1']))

#キーの追加
dict_a['new_key'] = 'new_value'
print(dict_a.items())

#キーと値の削除
del dict_a['key2']
print(dict_a.items())
