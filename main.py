#Player's score
score = 0
numOfAnswer = 1
#This is the Guess animal-name game
print("Guess the Animal!")
#You've got 3 times to guess
chances = 3
#There are two questions
ques1 = "Which bear lives at the North Pole?"
ques2 = "Which cat is smallest in the world?"
#check answer function
def checkUserAnswer(question, answerOfUser):
  #The answers of two questions
  if (question == ques1):
    answerOf1 = "pollar bear"
  if (question == ques2):
    answerOf2 = "rusty spotted cat"
  #Check the answers
  if (answerOfUser == answerOf1 or answerOfUser == answerOf1):
    global numOfAnswer = numOfAnswer + 1
    score = score + 1
    return score
  else:
    chances = chances - 1
    return chances
#Check wheather the answer corrects or not
#There are two questions to answer
while (numOfAnswer < 3 and chances > 0):
  if (numOfAnswer > 2):
    break
  if (numOfAnswer == 1):
    answer1 = input(ques1)
    checkUserAnswer(ques1, answer1)
  if (numOfAnswer == 2):
    answer2 = input(ques2)
    checkUserAnswer(ques2, answer2)
  
#Display score
if chances == 0 or numOfAnswer > 2:
    print("User score: " + score)
