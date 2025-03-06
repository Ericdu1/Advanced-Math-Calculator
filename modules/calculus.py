import sympy as sp

x = sp.Symbol('x')  # 设定默认变量

def differentiate(expression):
    """ 计算导数 """
    try:
        expr = sp.sympify(expression)
        return sp.diff(expr, x)
    except Exception as e:
        return f"错误: {e}"

def integrate(expression):
    """ 计算积分 """
    try:
        expr = sp.sympify(expression)
        return sp.integrate(expr, x)
    except Exception as e:
        return f"错误: {e}"
