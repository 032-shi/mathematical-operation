# coding: UTF-8
# ターミナルの表示ではなく、googlecolabでの出力を確認する
import sympy
#print(sympy.sqrt(4))
#print(sympy.sqrt(8))

#方程式の処理
x, y = sympy.symbols("x y")
test = sympy.Eq(x, y) #方程式"x=y"を定義する
print(test)