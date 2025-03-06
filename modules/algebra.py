import sympy as sp

def simplify_expression(expression):
    """ 化简代数表达式 """
    try:
        expr = sp.sympify(expression)
        return sp.simplify(expr)
    except Exception as e:
        return f"错误: {e}"
