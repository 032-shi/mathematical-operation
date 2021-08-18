# coding: UTF-8
# ターミナルに平方根などの特殊記号が出力されないため、Googlecolabを使用する
import math
import sympy

#print(math.sqrt(4))
#print(math.sqrt(6))

x, y = sympy.symbols("x y") #変数の設定
ex = x + 2 * y
print(ex)