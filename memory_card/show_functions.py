from card_layout import*
from constants import*

def showResult():
   ''' показать панель ответов '''
   questionGroupBox.hide()
   answerGroupBox.show()
   answerButton.setText('Наступне питання')
 
def showQuestion():
   ''' показать панель вопросов '''
   questionGroupBox.show()
   answerGroupBox.hide()
   answerButton.setText('Відповісти')
   # сбросить выбранную радио-кнопку
   radioButtonGroup.setExclusive(False) # сняли ограничения, чтобы можно было сбросить выбор радиокнопки
   ansButton1.setChecked(False)
   ansButton2.setChecked(False)
   ansButton3.setChecked(False)
   ansButton4.setChecked(False)
   radioButtonGroup.setExclusive(True) # вернули ограничения, теперь только одна радиокнопка может быть выбрана


def showData(answer, wrongAnswer1, wrongAnswer2, wrongAnswer3):
   ''' показывает на экране нужную информацию '''
   # объединим в функцию похожие действия
   questionLabel.setText(QUESTION_TEXT)
   correctAnswerLabel.setText(RIGHT_TEXT)
   answer.setText(RIGHT_TEXT)
   wrongAnswer1.setText(WRONG_TEXT1)
   wrongAnswer2.setText(WRONG_TEXT2)
   wrongAnswer3.setText(WRONG_TEXT3)
 
def checkResult(answer, wrongAnswer1, wrongAnswer2, wrongAnswer3):
   ''' проверка, правильный ли ответ выбран
   если ответ был выбран, то надпись "верно/неверно" приобретает нужное значение
   и показывается панель ответов '''
   correct = answer.isChecked() # в этом радиобаттоне лежит наш ответ!
   if correct:
       # ответ верный, запишем
       resultLabel.setText(TEXT_CORRECT) # надпись "верно" или "неверно"
       showResult()
   else:
       incorrect = wrongAnswer1.isChecked() or wrongAnswer2.isChecked() or wrongAnswer3.isChecked()
       if incorrect:
           # ответ неверный, запишем и отразим в статистике
           resultLabel.setText(TEXT_WRONG) # надпись "верно" или "неверно"
           showResult()
 
def clickOK(answer, wrongAnswer1, wrongAnswer2, wrongAnswer3):
   # пока что проверяем вопрос, если мы в режиме вопроса, иначе ничего
   if answerButton.text() != 'Наступне питання':
       checkResult(answer, wrongAnswer1, wrongAnswer2, wrongAnswer3)