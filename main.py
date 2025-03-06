import modules.algebra as algebra
import modules.calculus as calculus
import modules.matrix as matrix
import modules.utils as utils
import modules.language as language  # ✅ 语言模块
from modules.matrix_gui import get_matrix_input


def handle_algebra(texts):
    """ 处理代数运算 """
    expr = input(texts["algebra_input"]).strip()
    print(texts["result"], algebra.simplify_expression(expr))


def handle_calculus(texts):
    """ 处理微积分运算 """
    expr = input(texts["calculus_input"]).strip()
    print(texts["derivative"], calculus.differentiate(expr))
    print(texts["integral"], calculus.integrate(expr))


def handle_matrix(texts):
    """ 处理矩阵运算 """
    A = get_matrix_input()
    if A is None:
        return

    operation = input(texts["operation_select"]).strip().lower()

    if operation in ["add", "加法"]:
        B = get_matrix_input()
        if B is None:
            return
        print(texts["result"])  # 让 "结果：" 单独占一行
        print(matrix.format_matrix(matrix.add_matrices(A, B)))

    elif operation in ["multiply", "乘法"]:
        B = get_matrix_input()
        if B is None:
            return
        print(texts["result"])
        print(matrix.format_matrix(matrix.multiply_matrices(A, B)))

    elif operation in ["transpose", "转置"]:
        print(texts["result"])
        print(matrix.format_matrix(matrix.transpose_matrix(A)))

    elif operation in ["determinant", "行列式"]:
        print(texts["result"], matrix.determinant(A))  # 行列式是单个数，无需格式化

    elif operation in ["inverse", "逆矩阵"]:
        print(texts["result"])
        print(matrix.format_matrix(matrix.inverse_matrix(A)))

    else:
        print(texts["invalid_input"])


def handle_basic_operations(texts):
    """ 处理基本运算 """
    expr = input(texts["expression_input"]).strip()
    print(texts["result"], utils.evaluate_expression(expr))


def main():
    """ 主程序 """
    lang = language.select_language()  # 选择语言
    texts = language.LANGUAGES[lang]  # 获取语言字典

    while True:
        print(f"\n{texts['title']}")
        for line in texts["menu"]:
            print(line)

        choice = input(texts["prompt"]).strip()

        if choice == "1":
            handle_algebra(texts)
        elif choice == "2":
            handle_calculus(texts)
        elif choice == "3":
            handle_matrix(texts)
        elif choice == "4":
            handle_basic_operations(texts)
        elif choice == "5":
            print(texts["exit"])
            break
        else:
            print(texts["invalid_input"])


if __name__ == "__main__":
    main()
