# coding: UTF-8
# ターミナルに平方根などの特殊記号が出力されないため、Googlecolabを使用する
import math
import sympy

#print(math.sqrt(4))
#print(math.sqrt(6))

x, y = sympy.symbols("x y") #変数の設定
ex = x + 2 * y
#print(ex)

#式展開の確認
exx = x * ex
print(exx) #結果が式が展開されずに表示される
expand_exx = sympy.expand(exx) #式展開する場合は、"expand関数"を使用する
print(expand_exx)

#方程式の処理
x, y = sympy.symbols("x y")
sympy.Eq(x ** 2, 1) #Eq関数で"Xの2乗=1"という方程式を定義する
#solve関数の第一引数の方程式について、第二引数の変数について解くことができる
test = sympy.solve(sympy.Eq(x ** 2, 1), x)
print(test)