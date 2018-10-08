# -- coding: utf-8 --

#メソッドサンプル(戻り値あり)
def method_sample(user_name):
  result = 'Hi! '+ user_name
  return result

#メソッドサンプル(可変引数)
def __method_variable_argument_sample(*args):
  print(args)

#メソッドサンプル(ディクショナリ)
def __method_dictionary_sample(**args):
  print(args)

def __method_dictionary_sample2(args):
  if isinstance(args,dict):
    print(args)
  else:
    print('not dictionary!')

#メソッド利用(単体実行用)
if __name__ == '__main__':
  print('{0}'.format(method_sample('UserA')))
  __method_variable_argument_sample('a',1,2,3,4.6)
  __method_dictionary_sample(a=1,b=2,c=3)
  __method_dictionary_sample2({'a':1})
  __method_dictionary_sample2('a')
