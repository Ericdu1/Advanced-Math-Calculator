import math

def evaluate_expression(expression):
    try:
        result = eval(expression, {"__builtins__": None}, {"sqrt": math.sqrt, "pow": pow, "abs": abs})
        return result
    except Exception as e:
        return f"错误: {e}"
