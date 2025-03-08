import sys
import numpy as np
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton, QComboBox
import modules.language as language
from modules.matrix import add_matrices, multiply_matrices, transpose_matrix, determinant, inverse_matrix

class MatrixGUI(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.lang = parent.lang  # 继承主界面的语言设置
        self.texts = language.get_texts(self.lang)
        
        self.setWindowTitle(self.texts["matrix_title"])
        self.setGeometry(100, 100, 500, 500)

        layout = QVBoxLayout()
        layout.addWidget(QLabel(self.texts["enter_expression"]))
        
        self.matrix_input = QTextEdit()
        layout.addWidget(self.matrix_input)
        
        self.matrix_operation_combo = QComboBox()
        self.matrix_operation_combo.addItems([
            self.texts["transpose"], self.texts["add"], self.texts["multiply"],
            self.texts["determinant"], self.texts["inverse"]
        ])
        layout.addWidget(self.matrix_operation_combo)
        
        submit_button = QPushButton(self.texts["calculate"])
        submit_button.clicked.connect(self.perform_matrix_operation)
        layout.addWidget(submit_button)
        
        self.result_text = QLabel()
        layout.addWidget(self.result_text)
        
        back_button = QPushButton(self.texts["back_to_menu"])
        back_button.clicked.connect(lambda: self.parent.stack.setCurrentWidget(self.parent.main_menu))
        layout.addWidget(back_button)
        
        self.setLayout(layout)
    
    def perform_matrix_operation(self):
        text = self.matrix_input.toPlainText().strip()
        operation = self.matrix_operation_combo.currentText()

        try:
            A = np.array([list(map(float, row.split())) for row in text.split("\n")])
            if operation == self.texts["transpose"]:
                result = transpose_matrix(A)
            elif operation == self.texts["add"] or operation == self.texts["multiply"]:
                B_text = self.matrix_input.toPlainText().strip()
                B = np.array([list(map(float, row.split())) for row in B_text.split("\n")])
                if operation == self.texts["add"]:
                    result = add_matrices(A, B)
                else:
                    result = multiply_matrices(A, B)
            elif operation == self.texts["determinant"]:
                result = determinant(A)
            elif operation == self.texts["inverse"]:
                result = inverse_matrix(A)
            else:
                result = self.texts["error"]

            self.result_text.setText(str(result))
        except Exception as e:
            self.result_text.setText(f"{self.texts['error']}: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MatrixGUI(None)
    window.show()
    sys.exit(app.exec())
