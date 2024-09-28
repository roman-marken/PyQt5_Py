from PyQt5.QtWidgets import QApplication
from main_window import MainWindow
from menu_window import MenuWindow
from results_window import ResultsWindow
from question import Question
from timer_window import TimerWindow
from time import time

questions = [
    Question("Apple", "Яблуко", "Груша", "Слива", "Апельсин"),
    Question("Banana", "Банан", "Ананас", "Мандарин", "Лимон"),
    Question("Cherry", "Вишня", "Чорниця", "Малина", "Смородина"),
    Question("Grape", "Виноград", "Арбуз", "Диня", "Кавун"),
    Question("Kiwi", "Ківі", "Авокадо", "Маракуйя", "Манго"),
]

current_question = 0
correct_answers = 0
start_time = time()

app = QApplication([])

main_win = MainWindow()
main_win.set_question(questions[current_question])
timer_win = TimerWindow()

menu_win = MenuWindow(questions)
results_win = ResultsWindow()


def open_menu():
    menu_win.show()


def handle_finish_button():
    app.quit()


def handle_pause_button():
    timer_win.show()


def handle_restart_button():
    global current_question, correct_answers, start_time
    current_question = 0
    correct_answers = 0
    start_time = time()
    results_win.hide()
    main_win.show()
    main_win.set_question(questions[current_question])


def handle_submit():
    global current_question, correct_answers
    if main_win.radio_group.checkedButton() is None:
        return
    if main_win.radio_group.checkedButton().text() == questions[current_question].correct:
        print("Correct")
        correct_answers += 1
    else:
        print("Incorrect")
    current_question += 1
    if current_question >= len(questions):
        results_win.set_results(len(questions), correct_answers, time() - start_time)
        results_win.show()
        main_win.hide()
    else:
        main_win.radio_group.setExclusive(False)
        main_win.set_question(questions[current_question])


main_win.btn_menu.clicked.connect(open_menu)
main_win.btn_submit.clicked.connect(handle_submit)
main_win.btn_pause.clicked.connect(handle_pause_button)

results_win.finish_button.clicked.connect(handle_finish_button)
results_win.restart_button.clicked.connect(handle_restart_button)

main_win.show()
app.exec_()

