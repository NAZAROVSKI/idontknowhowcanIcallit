#создай приложение для запоминания и
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QGroupBox, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox, QRadioButton)
app = QApplication([])
window = QWidget()
window.setWindowTitle('Какой национальности нет?')
RadioGroupBox = QGroupBox("Варианты ответов")
rbtn_1 = QRadioButton('Энцы')
rbtn_2 = QRadioButton('Смурфы')
rbtn_3 = QRadioButton('Чулымцы')
rbtn_4 = QRadioButton('Алеуты')
layout_ans1 = QHBoxLayout()
layout_ans2 = QHBoxLayout()
layout_ans3 = QHBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1)
layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2)
window.setLayout(layout_card)
window.show()
app.exec()
def ask(question, right_answer, wrong1, wrong2, wrong3):
    app = QApplication([])
    btn_OK = QPushButton('Ответить')
    lb_Question = QLabel('Самый сложный вопрос в мире!')
    from random import shuffle
    answer = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
    shuffle(answer)
    RadioGroupBox = QGroupBox("Варианты ответов")
    rbtn_1 = QRadioButton('Энцы')
    rbtn_2 = QRadioButton('Смурфы')
    rbtn_3 = QRadioButton('Чулымцы')
    rbtn_4 = QRadioButton('Алеуты')
    layout_ans1 = QHBoxLayout()
    layout_ans2 = QHBoxLayout()
    layout_ans3 = QHBoxLayout()
    layout_ans2.addWidget(rbtn_1)
    layout_ans2.addWidget(rbtn_2)
    layout_ans3.addWidget(rbtn_3)
    layout_ans3.addWidget(rbtn_4)
    layout_ans1.addLayout(layout_ans2)
    layout_ans1.addLayout(layout_ans3)
    RadioGroupBox.setLayout(layout_ans1)
    AnsGroupBox = QGroupBox("Результат теста")
    lb_Result = QLabel('Прав ты или нет?')
    lb_Correct = QLabel('ответ будет тут!')
    layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignCenter))
    layout_line2.addWidget(RadioGroupBox)
    layout_line3.addStretch(1)
    layout_line3.addWidget(btn_OK, stretch=2)
    window.setLayout(layout_card)
    window.show()
    app.exec()
def test():
    '''Временна функция, которая позволяет нажатием на кнопку вызывать по очереди show_result() либо show_question() '''
    if 'Ответить'
def show_results():
    ''' показать панель ответов '''
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setWindowTitle
    from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QGroupBox, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox, QRadioButton)
from random import shuffle

class Question():
    ''' содержит вопрос, правильный ответ и три неправельных'''
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
app = QApplication([])
btn_OK = QPushButton('Ответить')
lb_Question = QLabel('Самый сложный вопрос в мире!')
RadioGroupBox = QGroupBox("Варианты ответов")
rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')
RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1)
AnsGroupBox = QGroupBox('Рзультат теста')
lb_Result = QLabel('прав ты или нет?')
lb_Correct = QLabel('ответ будет тут!')
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
class Question():
    ''' содержит вопрос, правильный ответ и три неправельных'''
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
question_list = []
question_list.append(
    Question('Государственный язык Бразилии', 'Португальский, Английский, Испанский, Бразильский'))
question_list.append(
    Question('Какого цвета нет на флаге России', 'зелёного, красного, синего, белого')
)
def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn.OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)
answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q)
def next_question():
    window.total += 1
    print('Статистика\n-Всего')
def click_OK():
    btn_OK.text() == 'Ответить'
window = QWidget()
window.setLayout(layout_card)
