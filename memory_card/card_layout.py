''' Окно для карточки вопроса '''
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
       QApplication, QHBoxLayout, QVBoxLayout,
       QGroupBox, QButtonGroup, QRadioButton, 
       QPushButton, QLabel, QSpinBox)
 
app = QApplication([])
 
# виджеты, которые надо будет разместить:
menuButton = QPushButton('Меню') # кнопка возврата в основное окно
sleepButton = QPushButton('Відпочити') # кнопка убирает окно и возвращает его после окончания таймера
minutesBox = QSpinBox() # ввод количества минут
minutesBox.setValue(30)
answerButton = QPushButton('Відповісти') # кнопка ответа
questionLabel = QLabel('') # текст вопроса
 
# Панель с вариантами:
questionGroupBox = QGroupBox("Варіанти відповіді") # группа на экране для переключателей с ответами
radioButtonGroup = QButtonGroup() # а это для группировки переключателей, чтобы управлять их поведением
 
ansButton1 = QRadioButton('')
ansButton2 = QRadioButton('')
ansButton3 = QRadioButton('')
ansButton4 = QRadioButton('')
 
radioButtonGroup.addButton(ansButton1)
radioButtonGroup.addButton(ansButton2)
radioButtonGroup.addButton(ansButton3)
radioButtonGroup.addButton(ansButton4)
 
# Панель с результатом:
answerGroupBox = QGroupBox("Результати тесту")
resultLabel = QLabel('') # здесь размещается надпись "правильно" или "неправильно"
correctAnswerLabel = QLabel('') # здесь будет написан текст правильного ответа
 
#  Теперь занимаемся размещением:
 
# Размещаем варианты ответов в два столбца внутри группы:
groupBoxRow = QHBoxLayout()  
column1 = QVBoxLayout() # вертикальные будут внутри горизонтального
column2 = QVBoxLayout()
column1.addWidget(ansButton1) # два ответа в первый столбец
column1.addWidget(ansButton2)
column2.addWidget(ansButton3) # два ответа во второй столбец
column2.addWidget(ansButton4)
 
groupBoxRow.addLayout(column1)
groupBoxRow.addLayout(column2) # разместили столбцы в одной строке
 
questionGroupBox.setLayout(groupBoxRow) # готова "панель" с вариантами ответов   

# размещаем результат:
resultColumn = QVBoxLayout()
resultColumn.addWidget(resultLabel, alignment=(Qt.AlignLeft | Qt.AlignTop))
resultColumn.addWidget(correctAnswerLabel, alignment=Qt.AlignHCenter, stretch=2)
answerGroupBox.setLayout(resultColumn)
answerGroupBox.hide()
 
# размещаем все виджеты в окне, они расположены в четыре строки:
mainRow1 = QHBoxLayout()
mainRow2 = QHBoxLayout()
mainRow3 = QHBoxLayout()
mainRow4 = QHBoxLayout()
 
mainRow1.addWidget(menuButton)
mainRow1.addStretch(1) # разрыв между кнопками делаем по возможности длиннее
mainRow1.addWidget(sleepButton)
mainRow1.addWidget(minutesBox)
mainRow1.addWidget(QLabel('хвилин')) # нам не нужна переменная для этой надписи
 
mainRow2.addWidget(questionLabel, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
mainRow3.addWidget(questionGroupBox)
mainRow3.addWidget(answerGroupBox)
 
mainRow4.addStretch(1)
mainRow4.addWidget(answerButton, stretch=2) # кнопка должна быть большой
mainRow4.addStretch(1)
 
# Теперь созданные 4 строки разместим одну под другой:
mainColumn = QVBoxLayout()
mainColumn.addLayout(mainRow1, stretch=1)
mainColumn.addLayout(mainRow2, stretch=2)
mainColumn.addLayout(mainRow3, stretch=8)
mainColumn.addStretch(1)
mainColumn.addLayout(mainRow4, stretch=1)
mainColumn.addStretch(1)
mainColumn.setSpacing(5) # пробелы между содержимым
 
# Результат работы этого модуля: виджеты помещены внутрь layout_card, который можно назначить окну.
 

