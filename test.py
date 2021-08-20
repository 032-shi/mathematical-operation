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