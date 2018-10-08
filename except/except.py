# -- coding: utf-8 --

#エラーなく処理完了
try:
  10/10
except ZeroDivisionError as identifier:
  print(identifier)
else:
  print("Success")
finally:
  print("finally")

"""
[出力]
Success
finally
"""

#エラー発生
try:
  10/0
except ZeroDivisionError as identifier:
  print(identifier)
else:
  print("Success")
finally:
  print("finally")

"""
[出力]
integer division or modulo by zero
finally
"""

#エラー発生(Exceptionでエラー内容を捕捉する)
try:
  10/0
except Exception as identifier:
  print(identifier)
else:
  print("Success")
finally:
  print("finally")

"""
[出力]
integer division or modulo by zero
finally
"""

#例外エラーを発生させる
try:
  raise Exception('raise test')
except Exception as identifier:
  print(identifier)
else:
  print("Success")
finally:
  print("finally")

"""
[出力]
raise test
finally
"""
