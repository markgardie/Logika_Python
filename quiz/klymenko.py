from time import*

score = 0
def question(q, right_answer):
    global score 
    user_answer = input(q + "").lower().strip()
    if user_answer == right_answer.lower():
       print("Вірно!\n")
       score += 1 
    else:
        print(f"Невірно! Правильна відповідь: {right_answer}\n")
start_time = time()      


question("у якому році помер чингісхан?", "1227")
question("як він помер?", "він впав с коня")
question("хто є хубілай хан для чингісхана?","хубілай його онук.")
question("скільки у чингісхана було дітей?", "десь 2000,але знають десь 4 сина")
question("що зробив хубілай?", "створив дінастію юань")
question("чім інтересувавя хубілай хан в дитинстві?","китайскою культурою")
question("хто сама головна жінка чингісхана?", "оєлун(хоелун)")
question("як звали дітей чингісхана?", "Угєдєй,толуй,джучи")