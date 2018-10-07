# -- coding: utf-8 --

#メソッドサンプル(戻り値あり)
def method_sample(user_name):
  result = 'Hi! '+ user_name
  return result

#メソッド利用(単体実行用)
if __name__ == '__main__':
  print('{0}'.format(method_sample('UserA')))
