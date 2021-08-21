# coding: UTF-8
# ターミナルの表示ではなく、googlecolabでの出力を確認する
import sympy
#print(sympy.sqrt(4))
#print(sympy.sqrt(8))

#2次方程式の処理
x, y = sympy.symbols("x y")
sympy.Eq(x ** 2 + 3 * x - 5, 0)
test = sympy.solve(sympy.Eq(x ** 2 + 3 * x - 5, 0), x)
print(test)

