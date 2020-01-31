# -- coding: utf-8 --

#辞書設定
dict_a = {'key1':10,'key2':100}

#キー名と値のペア取得
print(dict_a.items())

#キー名取得
print(dict_a .keys())

#値取得
print(dict_a .values())

#キーを指定して値を取得
print("dict_a['key1'] = {0}".format(dict_a['key1']))

#キーを指定して値を変更
dict_a['key1'] = 50
print("dict_a['key1'] = {0}".format(dict_a['key1']))
