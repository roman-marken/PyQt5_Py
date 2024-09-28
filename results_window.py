from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QHBoxLayout

font = QFont()
font.setPointSize(24)


button_style = '''
    QPushButton {
        height: 30px;
        background-color: #FFD700;
        color: #021526;
        border-radius: 10px;
    }
    QPushButton:hover {
        height: 30px;
        background-color: #FFD700;
        color: #021526;
        border-radius: 10px;
        border: 2px solid #021526;
    }
'''


class ResultsWindow(QWidget):                       
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: #021526;")
        self.setWindowTitle("Результати")
        self.resize(500, 300)
        self.title_label = QLabel("Результати")
        self.title_label.setFont(font)
        self.title_label.setStyleSheet("color: #FFFFFF;")
        font.setPointSize(12)
        self.amount_of_questions = QLabel()
        self.amount_of_questions.setFont(font)
        self.amount_of_questions.setStyleSheet("color: #FFFFFF;")
        self.amount_of_correct = QLabel()
        self.amount_of_correct.setFont(font)
        self.amount_of_correct.setStyleSheet("color: #FFFFFF;")
        self.percentage_of_correct = QLabel()
        self.percentage_of_correct.setFont(font)
        self.percentage_of_correct.setStyleSheet("color: #FFFFFF;")
        self.time_spent = QLabel()
        self.time_spent.setFont(font)
        self.time_spent.setStyleSheet("color: #FFFFFF;")

        layout = QVBoxLayout()
        layout.addWidget(self.title_label, alignment=Qt.AlignCenter)
        layout.addWidget(self.amount_of_questions, alignment=Qt.AlignCenter)
        layout.addWidget(self.amount_of_correct, alignment=Qt.AlignCenter)
        layout.addWidget(self.percentage_of_correct, alignment=Qt.AlignCenter)

        self.restart_button = QPushButton("Почати спочатку")
        self.restart_button.setStyleSheet(button_style)
        self.finish_button = QPushButton("Завершити")
        self.finish_button.setStyleSheet(button_style)

        line = QHBoxLayout()
        line.addWidget(self.restart_button)
        line.addWidget(self.finish_button)

        layout.addLayout(line)

        self.setLayout(layout)

    def set_results(self, amount_of_questions, amount_of_correct, time_spent):
        self.amount_of_questions.setText(f"Кількість питань: {amount_of_questions}")
        self.amount_of_correct.setText(f"Кількість правильних відповідей: {amount_of_correct}")
        self.percentage_of_correct.setText(f"Відсоток правильних відповідей: {amount_of_correct / amount_of_questions * 100:.2f}%")
        self.time_spent.setText(f"Час, витрачений на тест: {time_spent:.2f} секунд")