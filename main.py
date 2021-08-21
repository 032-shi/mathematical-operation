# coding: UTF-8
# ターミナルの表示ではなく、googlecolabでの出力を確認する
import sympy
#print(sympy.sqrt(4))
#print(sympy.sqrt(8))

#方程式の処理
x, y = sympy.symbols("x y")
sympy.Eq(x ** 2, 1) #Eq関数で"Xの2乗=1"という方程式を定義する
#solve関数の第一引数の方程式について、第二引数の変数について解くことができる
test = sympy.solve(sympy.Eq(x ** 2, 1), x)
print(test)