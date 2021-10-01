import quiz_sql_handeler as db
def quizmaker():

    question = input("what is the question? ")
    right_answer = input("what is the correct answer? ")
    wrong1 = input("what is the first wront answer? ")
    wrong2 = input("what is the second wrong answer? ")
    wrong3 = input("what is the final wrong answer?")
    quiz = db.quizDB()
    quiz.add(question,right_answer,wrong1,wrong2,wrong3)
#past this point i will be reading this in to a database.
