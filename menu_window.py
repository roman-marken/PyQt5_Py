from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton
from question import Question

label_style = '''
    QLabel {
        color: #6EACDA;
        font-size: 14px;
    }
'''

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

input_style = '''
    QLineEdit {
        height: 30px;
        padding-left: 10px;
        background-color: #FFFFFF;
        color: #000000;
        border-radius: 10px;
    }
'''


class MenuWindow(QWidget):
    def __init__(self, questions):
        super().__init__()
        self.questions = questions
        self.setStyleSheet("background-color: #021526;")
        self.setWindowTitle("Меню")
        self.resize(500, 300)
        lbl_question = QLabel("Введіть запитання")
        lbl_question.setStyleSheet(label_style)
        lbl_correct = QLabel("Введіть вірну відповідь")
        lbl_correct.setStyleSheet(label_style)
        lbl_incorrect1 = QLabel("Введіть хибну відповідь")
        lbl_incorrect1.setStyleSheet(label_style)
        lbl_incorrect2 = QLabel("Введіть хибну відповідь")
        lbl_incorrect2.setStyleSheet(label_style)
        lbl_incorrect3 = QLabel("Введіть хибну відповідь")
        lbl_incorrect3.setStyleSheet(label_style)
        self.btn_add = QPushButton("Додати запитання")
        self.btn_add.setStyleSheet(button_style)
        self.btn_add.clicked.connect(self.handle_add_button)

        self.btn_clear = QPushButton("Очистити")
        self.btn_clear.setStyleSheet(button_style)
        self.btn_clear.clicked.connect(self.handle_clear_button)
        self.btn_back = QPushButton("Назад")
        self.btn_back.setStyleSheet(button_style)
        self.btn_back.clicked.connect(self.close_win)

        self.input_question = QLineEdit()
        self.input_question.setStyleSheet(input_style)
        self.input_correct = QLineEdit()
        self.input_correct.setStyleSheet(input_style)
        self.input_incorrect1 = QLineEdit()
        self.input_incorrect1.setStyleSheet(input_style)
        self.input_incorrect2 = QLineEdit()
        self.input_incorrect2.setStyleSheet(input_style)
        self.input_incorrect3 = QLineEdit()
        self.input_incorrect3.setStyleSheet(input_style)

        line1 = QHBoxLayout()
        line2 = QHBoxLayout()
        line3 = QHBoxLayout()
        line4 = QHBoxLayout()
        line5 = QHBoxLayout()
        line6 = QHBoxLayout()
        line7 = QHBoxLayout()

        line1.addWidget(lbl_question, 4)
        line1.addWidget(self.input_question, 5)
        line2.addWidget(lbl_correct, 4)
        line2.addWidget(self.input_correct, 5)
        line3.addWidget(lbl_incorrect1, 4)
        line3.addWidget(self.input_incorrect1, 5)
        line4.addWidget(lbl_incorrect2, 4)
        line4.addWidget(self.input_incorrect2, 5)
        line5.addWidget(lbl_incorrect3, 4)
        line5.addWidget(self.input_incorrect3, 5)
        line6.addWidget(self.btn_add)
        line6.addWidget(self.btn_clear)
        line7.addWidget(self.btn_back)

        main_col = QVBoxLayout()
        main_col.addLayout(line1)
        main_col.addLayout(line2)
        main_col.addLayout(line3)
        main_col.addLayout(line4)
        main_col.addLayout(line5)
        main_col.addLayout(line6)
        main_col.addLayout(line7)

        self.setLayout(main_col)

    def close_win(self):
        self.close()

    def handle_add_button(self):
        if self.input_question.text() != "" and self.input_correct.text() != "" and self.input_incorrect1.text() != "" and self.input_incorrect2.text() != "" and self.input_incorrect3.text() != "":
            self.questions.append(
                Question(self.input_question.text(), self.input_correct.text(), self.input_incorrect1.text(),
                         self.input_incorrect2.text(), self.input_incorrect3.text()))
            self.input_question.clear()
            self.input_correct.clear()
            self.input_incorrect1.clear()
            self.input_incorrect2.clear()
            self.input_incorrect3.clear()

    def handle_clear_button(self):
        self.input_question.clear()
        self.input_correct.clear()
        self.input_incorrect1.clear()
        self.input_incorrect2.clear()
        self.input_incorrect3.clear()