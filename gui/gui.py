import sys
from PyQt6.QtWidgets import QApplication, QStackedWidget, QWidget, QVBoxLayout, QLabel, QPushButton, QComboBox
import modules.language as language
from gui.algebra_gui import AlgebraGUI
from gui.calculus_gui import CalculusGUI
from gui.matrix_gui import MatrixGUI
from gui.basic_gui import BasicGUI

class MathApp(QWidget):
    def __init__(self):
        super().__init__()
        self.lang = "Chinese"
        self.texts = language.get_texts(self.lang)

        self.setWindowTitle("高级数学计算器")
        self.setGeometry(100, 100, 500, 500)
        self.layout = QVBoxLayout()

        self.stack = QStackedWidget()
        self.create_main_menu()
        self.algebra_ui = AlgebraGUI(self)
        self.calculus_ui = CalculusGUI(self)
        self.matrix_ui = MatrixGUI(self)
        self.basic_ui = BasicGUI(self)

        self.stack.addWidget(self.algebra_ui)
        self.stack.addWidget(self.calculus_ui)
        self.stack.addWidget(self.matrix_ui)
        self.stack.addWidget(self.basic_ui)

        self.layout.addWidget(self.stack)
        self.setLayout(self.layout)

    def create_main_menu(self):
        """创建主菜单"""
        self.main_menu = QWidget()
        layout = QVBoxLayout()

        self.language_combo = QComboBox()
        self.language_combo.addItems(["中文|Chinese", "英文|English"])
        self.language_combo.currentTextChanged.connect(self.change_language)
        layout.addWidget(QLabel("选择语言 | Select Language"))
        layout.addWidget(self.language_combo)

        self.mode_combo = QComboBox()
        self.mode_combo.addItems(["线性代数|Algebra", "微积分|Calculus", "矩阵|Matrix", "基础运算|Basic Operations"])
        layout.addWidget(QLabel("请选择计算模式"))
        layout.addWidget(self.mode_combo)

        start_button = QPushButton("开始计算 | Start Calculation")
        start_button.clicked.connect(self.switch_to_selected_mode)
        layout.addWidget(start_button)

        self.main_menu.setLayout(layout)
        self.stack.addWidget(self.main_menu)
        self.stack.setCurrentWidget(self.main_menu)

    def switch_to_selected_mode(self):
        selected_mode = self.mode_combo.currentText().split("|")[-1].strip()
        if selected_mode == "Matrix":
            self.stack.setCurrentWidget(self.matrix_ui)
        elif selected_mode == "Algebra":
            self.stack.setCurrentWidget(self.algebra_ui)
        elif selected_mode == "Calculus":
            self.stack.setCurrentWidget(self.calculus_ui)
        elif selected_mode == "Basic Operations":
            self.stack.setCurrentWidget(self.basic_ui)

    def change_language(self, lang):
        self.lang = lang
        self.texts = language.get_texts(self.lang)
        self.mode_combo.clear()
        self.mode_combo.addItems(["线性代数|Algebra", "微积分|Calculus", "矩阵|Matrix", "基础运算|Basic Operations"])
        self.setWindowTitle(self.texts["title"])

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MathApp()
    window.show()
    sys.exit(app.exec())
