import question_picker as quiz_runner
import quiz_maker
import sys
import time


selection = 0
def main_menue():
    while True:
        print("what wouleld you like to do?")
        x = input()
y= .23
def drama(string:str):
    for x in string:
        sys.stdout.write(x)
        sys.stdout.flush()

        time.sleep(y)
    print ('')
def slow_scroll(tims):
    s = 0
    while s <= tims:
        time.sleep(.1)
        print('\n')
        s = s + 1

dio1 = "welcome to quizilla"
dio2 = "brought to you by patrick cathcart"
menue_dio = "what will we be doing today?"
menue_dio1 = "please select a option"
menue_dio2 = "1: take a quiz"
menue_dio3 = "2: make quiz questions"

drama(dio1)
slow_scroll(10)

drama(dio2)
slow_scroll(5)

print(menue_dio)
time.sleep(3)

slow_scroll(5)
drama(menue_dio1)

slow_scroll(5)
drama(menue_dio2)
drama(menue_dio3)



while selection != 1 and selection != 2:
    selection = input("please select a number: ")
    selection = int(selection)
    if selection == 1:
        quiz_runner.questions_random()
        break
    if selection == 2:
        quiz_maker.quizmaker()
        break
    else:
        drama("invalid response")

        slow_scroll(10)