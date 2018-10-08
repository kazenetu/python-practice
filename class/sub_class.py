# -- coding: utf-8 --

# スーパークラス呼び出し
from super_class import SuperClass

# サブクラス
class SubClass(SuperClass,object):
  def main_method(self,user_name):
    print('SubClass!')
    super(SubClass,self).main_method(user_name)

#単体実行用
if __name__ == '__main__':
  target = SubClass()
  target.main_method('test!')

  '''
  [出力]
  SubClass!
  Hi! test!
  val is 123
  '''