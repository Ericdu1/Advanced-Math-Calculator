texts = {
    "Chinese": {
        "title": "高级数学计算器",
        "operation_select": "请选择计算模式（代数、微积分、矩阵、基础运算）：",
        "algebra_title": "代数 计算器",
        "calculus_title": "微积分 计算器",
        "matrix_title": "矩阵 计算器",
        "basic_title": "基础运算 计算器",
        "enter_expression": "请输入表达式：",
        "calculate": "计算",
        "result": "计算结果：",
        "back_to_menu": "返回主菜单",
        "error": "错误",
        "matrix_operations": "请选择矩阵运算：",
        "transpose": "转置",
        "add": "加法",
        "multiply": "乘法",
        "determinant": "行列式",
        "inverse": "逆矩阵",
        "simplify": "化简",
        "factor": "因式分解",
        "expand": "展开"
    },
    "English": {
        "title": "Advanced Math Calculator",
        "operation_select": "Please select a calculation mode (Algebra, Calculus, Matrix, Basic Operations):",
        "algebra_title": "Algebra Calculator",
        "calculus_title": "Calculus Calculator",
        "matrix_title": "Matrix Calculator",
        "basic_title": "Basic Operations Calculator",
        "enter_expression": "Enter an expression:",
        "calculate": "Calculate",
        "result": "Result:",
        "back_to_menu": "Back to Main Menu",
        "error": "Error",
        "matrix_operations": "Select a matrix operation:",
        "transpose": "Transpose",
        "add": "Addition",
        "multiply": "Multiplication",
        "determinant": "Determinant",
        "inverse": "Inverse Matrix",
        "simplify": "Simplify",
        "factor": "Factorize",
        "expand": "Expand"
    }
}

def get_texts(lang):
    return texts.get(lang, texts["English"])
