# modules/language.py
"""
此模块存储所有语言相关的文本，并提供语言选择功能
"""

LANGUAGES = {
    "English": {
        "title": "==== Advanced Math Calculator ====",
        "menu": [
            "1. Algebra Operations",
            "2. Calculus Operations",
            "3. Matrix Operations",
            "4. Basic Operations (Add, Subtract, Multiply, Divide)",
            "5. Exit"
        ],
        "prompt": "Please select an option (1-5): ",
        "operation_select": "Select matrix operation (add, multiply, transpose, determinant, inverse): ",
        "expression_input": "Enter a mathematical expression: ",
        "result": "Result: ",
        "error_divide_by_zero": "Error: Cannot divide by zero",
        "algebra_input": "Enter an algebraic expression (e.g., '2*x + 3*x - 5'): ",
        "calculus_input": "Enter an expression (e.g., 'x**2 + 3*x'): ",
        "derivative": "Derivative: ",
        "integral": "Integral: ",
        "exit": "Exiting the program...",
        "invalid_input": "Invalid input, please select again!"
    },
    "Chinese": {
        "title": "==== 高级数学计算器 ====",
        "menu": [
            "1. 代数运算",
            "2. 微积分计算",
            "3. 矩阵运算",
            "4. 基础运算（加、减、乘、除）",
            "5. 退出"
        ],
        "prompt": "请选择一个功能（1-5）： ",
        "operation_select": "请选择矩阵运算（加法, 乘法, 转置, 行列式, 逆矩阵）：",
        "expression_input": "请输入数学表达式： ",
        "result": "结果：",
        "error_divide_by_zero": "错误: 不能除以零",
        "algebra_input": "请输入代数表达式（如 '2*x + 3*x - 5'）： ",
        "calculus_input": "请输入表达式（如 'x**2 + 3*x'）： ",
        "derivative": "导数：",
        "integral": "积分：",
        "exit": "退出程序",
        "invalid_input": "无效输入，请重新选择！"
    }
}

def select_language():
    """ 让用户选择语言（English 或 Chinese） """
    language_map = {
        "english": "English",
        "chinese": "Chinese"
    }

    while True:
        lang_input = input("Select language (English/Chinese): ").strip().lower()
        if lang_input in language_map:
            return language_map[lang_input]
        print("Invalid selection! Please enter 'English' or 'Chinese'.")
