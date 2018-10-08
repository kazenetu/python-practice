# -- coding: utf-8 --

# スーパークラス
class SuperClass:
  __val = 123

  def main_method(self,user_name = 'noname'):
    self.__sub_method(user_name)

  def __sub_method(self,user_name):
    print('Hi! {0}'.format(user_name))
    print('val is {0}'.format(self.__val))

#単体実行用
if __name__ == '__main__':
  target = SuperClass()
  target.main_method('test!')
  target.main_method()

  '''
  [出力]
  Hi! test!
  val is 123
  Hi! noname
  val is 123
  '''