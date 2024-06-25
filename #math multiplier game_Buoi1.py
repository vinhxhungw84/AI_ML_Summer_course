#math multiplier game
import random
def multiplier():
    score = int(0)
    for i in range (10):
        x = random.randint(0,10)
        y = random.randint(0,10)
        answer = int(input("Question {}: {} * {} =  ".format(str(i),str(x),str(y))))
        if (answer == x * y ):
            print("Right!!!")
            score += 1
        else:
            print("Wrong!!! The right answer is {}".format(str(x*y))) 
    if (score <= 6):        
        print("Your score is {}. Fucking loser~~".format(str(score)))    
    else: 
        print("Your score is {}. Good job, Champ!!!".format(str(score)))

while(1):
    multiplier()
