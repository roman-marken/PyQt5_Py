from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout


class TimerWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Таймер")
        self.resize(400, 300)
        self.setStyleSheet("background-color: #021526;")
        self.timer = QTimer()
        self.timer.timeout.connect(self.handle_timeout)
        self.timer.start(1000)
        self.lbl_time = QLabel()
        self.lbl_time.setStyleSheet("color: #6EACDA; font-size: 24px;")
        self.lbl_time.setAlignment(Qt.AlignCenter)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.lbl_time)
        self.setLayout(self.layout)

    def handle_timeout(self):
        self.lbl_time.setText(str(self.timer.remainingTime() / 1000))