import quiz_sql_handeler as quiz
import random

def questions_random():
    score = 0
    round = 0
    while True:

        #the following line makes a object
        quizq = quiz.quizDB()
        #the next row takes the highest id available in the id table
        x = quizq.highest_id()
        #next will grab a random number from 0 to the max id as repersented by x
        y = random.randint(1,x[0])
        #next i will use the random number to pick the corisponing id from the sql table.
        questions = quizq.fetch(y)
        #the next rows will be parcing the questions out in to diffrent vars
        question = questions[0]
        righta = questions[1]
        wrong1 = questions[2]
        wrong2 = questions[3]
        wrong3 = questions[4]
        #i will now turn the parced question in to a list. i could have kept it as a list to begin with, i just prefer to untanlge thing in my code before i tie it back up
        an = [righta,wrong1,wrong2,wrong3]
        random.shuffle(an)
        #now i asing a letter value to each the suffeled list
        a = an[0]
        b = an[1]
        c = an[2]
        d = an[3]
        print('\n')
        print("your score is ", score, " ouy of ", round)
        print('\n')
        round = round + 1
        print(question)
        print("a: ",a)
        print("b: ",b)
        print("c: ",c)
        print("d: ", d)
        print("to finish, tyoe exit")
        user = input("what is your answer? ").lower()
        if user == 'a' or user == 'b' or user == 'c' or user == 'd':
            if user == 'a' and a == righta:
                print("correct")
                score = score + 1
            if user == 'b' and b == righta:
                print("correct")
                score = score + 1
            if user == 'c' and c == righta:
                print("correct")
                score = score + 1
            if user == 'd' and d == righta:
                print("correct")
                score = score + 1
            if user == "exit":
                break
        else:
            print("incorrect")

