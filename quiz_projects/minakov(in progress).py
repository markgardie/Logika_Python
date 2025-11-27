def question(q, right_answer):
    user_answer = input(q).lower()
    if user_answer == right_answer.lower():
        print("Вірно!")
    else:    
        print("Не вірно!")
        
question("в яких роках реал був в прайме?", "2016-2018")
question("скільки зм у крістіано роналдо?","5")
question("скільки лч у реалу?","15")
question("скшльки лч у барси?","5")