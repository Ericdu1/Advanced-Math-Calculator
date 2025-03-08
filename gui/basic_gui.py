import sys
import modules.language as language
import modules.utils as utils
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton

class BasicGUI(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.lang = parent.lang  # 继承主界面的语言设置
        self.texts = language.get_texts(self.lang)
        
        self.setWindowTitle(self.texts["basic_title"])
        self.setGeometry(100, 100, 500, 500)

        layout = QVBoxLayout()
        layout.addWidget(QLabel(self.texts["enter_expression"]))
        
        self.input_expr = QTextEdit()
        layout.addWidget(self.input_expr)
        
        submit_button = QPushButton(self.texts["calculate"])
        submit_button.clicked.connect(self.perform_basic_operation)
        layout.addWidget(submit_button)
        
        self.result_text = QLabel()
        layout.addWidget(self.result_text)
        
        back_button = QPushButton(self.texts["back_to_menu"])
        back_button.clicked.connect(lambda: self.parent.stack.setCurrentWidget(self.parent.main_menu))
        layout.addWidget(back_button)
        
        self.setLayout(layout)
    
    def perform_basic_operation(self):
        expr = self.input_expr.toPlainText().strip()
        try:
            result = utils.evaluate_expression(expr)
            self.result_text.setText(f"{self.texts['result']} {result}")
        except Exception as e:
            self.result_text.setText(f"{self.texts['error']}: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BasicGUI(None)
    window.show()
    sys.exit(app.exec())
