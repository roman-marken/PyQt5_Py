from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QGroupBox, QButtonGroup, QRadioButton, QHBoxLayout, QPushButton, QVBoxLayout, \
    QSpinBox, QLabel
from random import shuffle


button_style = '''
            QPushButton {
                background-color: #FFD700;
                color: #021526;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #FFD700;
                color: #021526;
                border-radius: 10px;
                border: 2px solid #021526;
            }
'''


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(600, 400)
        self.setWindowTitle("Memory Card")
        self.setStyleSheet("background-color: #021526;")
        self.btn_menu = QPushButton("Меню")
        self.btn_menu.setStyleSheet(button_style)
        self.btn_menu.setFixedSize(100, 30)
        self.btn_pause = QPushButton("Відпочити")
        self.btn_pause.setStyleSheet(button_style)
        self.btn_pause.setFixedSize(100, 30)
        self.btn_submit = QPushButton("Відповісти")
        self.btn_submit.setStyleSheet(button_style)
        self.btn_submit.setFixedSize(150, 40)

        font = QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setPointSize(18)

        sb_minutes = QSpinBox()
        sb_minutes.setStyleSheet("background-color: #FFD700; color: #021526")
        sb_minutes.setFixedSize(50, 30)
        sb_minutes.setValue(30)

        radio_group_box = QGroupBox("Варіанти відповідей")
        radio_group_box.setStyleSheet('''
            color: #6EACDA;
            font-size: 18px;
            border: 1px solid #6EACDA;
            border-radius: 10px;
            ''')
        self.radio_group = QButtonGroup()
        self.rbtn_ans1 = QRadioButton('1')
        self.rbtn_ans1.setStyleSheet("border: none")
        self.rbtn_ans2 = QRadioButton('2')
        self.rbtn_ans2.setStyleSheet("border: none")
        self.rbtn_ans3 = QRadioButton('3')
        self.rbtn_ans3.setStyleSheet("border: none")
        self.rbtn_ans4 = QRadioButton('4')
        self.rbtn_ans4.setStyleSheet("border: none")
        self.radio_group.addButton(self.rbtn_ans1)
        self.radio_group.addButton(self.rbtn_ans2)
        self.radio_group.addButton(self.rbtn_ans3)
        self.radio_group.addButton(self.rbtn_ans4)

        self.lbl_question = QLabel("Apple")
        self.lbl_question.setStyleSheet("color: #6EACDA;")
        self.lbl_question.setFont(font)

        rbtn_col1 = QVBoxLayout()
        rbtn_col2 = QVBoxLayout()
        rbtn_col1.addWidget(self.rbtn_ans1, alignment=Qt.AlignCenter)
        rbtn_col1.addWidget(self.rbtn_ans2, alignment=Qt.AlignCenter)
        rbtn_col2.addWidget(self.rbtn_ans3, alignment=Qt.AlignCenter)
        rbtn_col2.addWidget(self.rbtn_ans4, alignment=Qt.AlignCenter)

        line1 = QHBoxLayout()
        line2 = QHBoxLayout()
        line3 = QHBoxLayout()
        line4 = QHBoxLayout()
        main_col = QVBoxLayout()

        line1.addWidget(self.btn_menu)
        line1.addStretch(2)
        line1.addWidget(self.btn_pause)
        line1.addWidget(sb_minutes)
        line2.addWidget(self.lbl_question, alignment=Qt.AlignCenter)
        line3.addLayout(rbtn_col1)
        line3.addLayout(rbtn_col2)
        line4.addWidget(self.btn_submit, stretch=1)

        radio_group_box.setLayout(line3)

        main_col.addLayout(line1)
        main_col.addLayout(line2)
        main_col.addWidget(radio_group_box)
        main_col.addLayout(line4)

        self.setLayout(main_col)

    def set_question(self, question):
        self.lbl_question.setText(question.question)
        answers = [question.correct, question.incorrect1, question.incorrect2, question.incorrect3]
        shuffle(answers)
        self.rbtn_ans1.setText(answers[0])
        self.rbtn_ans2.setText(answers[1])
        self.rbtn_ans3.setText(answers[2])
        self.rbtn_ans4.setText(answers[3])































