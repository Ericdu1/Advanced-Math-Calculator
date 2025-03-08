import sys
import sympy as sp
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton, QComboBox
import modules.language as language
from modules.algebra import simplify_expression, factor_expression, expand_expression

class AlgebraGUI(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.lang = parent.lang  # 继承主界面的语言设置
        self.texts = language.get_texts(self.lang)
        
        self.setWindowTitle(self.texts["algebra_title"])
        self.setGeometry(100, 100, 500, 500)

        layout = QVBoxLayout()
        layout.addWidget(QLabel(self.texts["enter_expression"]))
        
        self.input_expr = QTextEdit()
        layout.addWidget(self.input_expr)
        
        self.algebra_operation_combo = QComboBox()
        self.algebra_operation_combo.addItems([
            self.texts["simplify"], self.texts["factor"], self.texts["expand"]
        ])
        layout.addWidget(self.algebra_operation_combo)
        
        submit_button = QPushButton(self.texts["calculate"])
        submit_button.clicked.connect(self.perform_algebra_operation)
        layout.addWidget(submit_button)
        
        self.result_text = QLabel()
        layout.addWidget(self.result_text)
        
        back_button = QPushButton(self.texts["back_to_menu"])
        back_button.clicked.connect(lambda: self.parent.stack.setCurrentWidget(self.parent.main_menu))
        layout.addWidget(back_button)
        
        self.setLayout(layout)
    
    def perform_algebra_operation(self):
        expr = self.input_expr.toPlainText().strip()
        x = sp.Symbol('x')
        operation = self.algebra_operation_combo.currentText()
        try:
            parsed_expr = sp.sympify(expr)  # 解析表达式
            if operation == self.texts["simplify"]:
                result = simplify_expression(parsed_expr)
            elif operation == self.texts["factor"]:
                result = factor_expression(parsed_expr)
            elif operation == self.texts["expand"]:
                result = expand_expression(parsed_expr)
            else:
                result = self.texts["error"]
            
            self.result_text.setText(f"{self.texts['result']}: {result}")
        except Exception as e:
            self.result_text.setText(f"{self.texts['error']}: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AlgebraGUI(None)
    window.show()
    sys.exit(app.exec())
