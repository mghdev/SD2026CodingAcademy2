
def safelyCallThenScoreAndPrintFeedback(func,answer,score,num_examples=2):
    if answer == None:
        score[2] += 1
        return False
    
    score[1] += 1
    try:
        result = func()
        if result == answer:
            if type(result) == type(answer):
                score[0] += 1
                return True
            print("Exercise ",score[1]-num_examples,": answer has the wrong type.\n",sep="")
        else:
            print("Exercise ",score[1]-num_examples,": answer has the wrong value.\n",sep="")
    except Exception as e:
        if answer == type(e).__name__:
            score[0] += 1
            return True
        print("Exercise ",score[1]-num_examples,": answer has the wrong value.\nHint: the expected answer is the name of an error.\n",sep="")
    return False


def printScore(score):
    if score[1] > 0:
        print(score[0]," out of ",score[1]," answers are correct.",sep="")
    if score[2] > 0:
        print(score[2]," exercises are incomplete.",sep="")