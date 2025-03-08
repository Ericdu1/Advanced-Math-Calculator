import numpy as np
import modules.algebra as algebra
import modules.calculus as calculus
import modules.matrix as matrix
import modules.utils as utils
import modules.language as language
from gui.gui import MathApp
from PyQt6.QtWidgets import QApplication
import sys

def handle_algebra(texts):
    expr = input(texts["algebra_input"]).strip()
    print(texts["result"], algebra.simplify_expression(expr))

def handle_calculus(texts):
    expr = input(texts["calculus_input"]).strip()
    print(texts["result"], calculus.differentiate(expr))
    print(texts["integral"], calculus.integrate(expr))

def handle_matrix(texts):
    A = input_matrix(texts)
    if A is None:
        return

    operation = input(texts["operation_select"]).strip().lower()

    if operation in [texts["add"], "add"]:
        B = input_matrix(texts)
        if B is None:
            return
        print(texts["result"], matrix.add_matrices(A, B))

    elif operation in [texts["multiply"], "multiply"]:
        B = input_matrix(texts)
        if B is None:
            return
        print(texts["result"], matrix.multiply_matrices(A, B))

    elif operation in [texts["transpose"], "transpose"]:
        print(texts["result"], matrix.transpose_matrix(A))

    elif operation in [texts["determinant"], "determinant"]:
        print(texts["result"], matrix.determinant(A))

    elif operation in [texts["inverse"], "inverse"]:
        print(texts["result"], matrix.inverse_matrix(A))

    else:
        print(texts["invalid_input"])

def handle_basic_operations(texts):
    expr = input(texts["expression_input"]).strip()
    print(texts["result"], utils.evaluate_expression(expr))

def input_matrix(texts):
    try:
        rows = input(texts["matrix_input"]).strip().split("\n")
        matrix = [list(map(float, row.split())) for row in rows]
        return np.array(matrix)
    except:
        print(texts["invalid_input"])
        return None

def main():
    app = QApplication(sys.argv)
    window = MathApp()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
