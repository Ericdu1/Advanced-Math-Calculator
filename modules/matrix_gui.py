import sys
import numpy as np
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton, QMessageBox

class MatrixInputGUI(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("矩阵输入")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        # 矩阵输入框
        self.label = QLabel("请输入矩阵（行用换行符分隔，列用空格分隔）：")
        self.text_input = QTextEdit()
        layout.addWidget(self.label)
        layout.addWidget(self.text_input)

        # 确认按钮
        self.submit_button = QPushButton("确认")
        self.submit_button.clicked.connect(self.submit_matrix)
        layout.addWidget(self.submit_button)

        self.setLayout(layout)
        self.matrix = None  # 存储输入的矩阵

    def submit_matrix(self):
        """ 处理用户输入的矩阵 """
        text = self.text_input.toPlainText().strip()
        if not text:
            QMessageBox.warning(self, "输入错误", "矩阵不能为空！")
            return
        
        try:
            rows = text.split("\n")
            matrix = [list(map(float, row.split())) for row in rows]
            self.matrix = np.array(matrix)
            self.close()
        except ValueError:
            QMessageBox.warning(self, "输入错误", "矩阵格式不正确，请重新输入！")

def get_matrix_input():
    """ 启动 GUI 并返回用户输入的矩阵 """
    app = QApplication.instance() or QApplication(sys.argv)
    gui = MatrixInputGUI()
    gui.show()
    app.exec() 
    return gui.matrix  

__all__ = ["get_matrix_input"]