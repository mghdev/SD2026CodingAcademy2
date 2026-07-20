from shared import safelyCallThenScoreAndPrintFeedback as check
from shared import printScore

# This script contains code reading exercises.
# Each exercise is a function that returns an expression, like this:
#
#==================================
# def exercise():
#     return 1+1
# answer = None
#
# Your task is to evaluate the expressions returned by the exercise functions.
# Assign to 'answer' the literal value you think is returned.
# To solve the example above, you would replace 'answer = None' with:
#
# answer = 2
#
# In cases where an exercise causes an error, assign the name of the error instead (see example_2 below).
# Each exercise is passed to a 'check' function that counts correct answers and prints some feedback for incorrect answers.
# Have a look at the file 'shared.py' if you're curious to see how the check function is implemented.
def main():
    # score counts exercises that are: [correct, attempted, incomplete]
    score = [0,0,0]
    
    #==================================
    def example_1():
        return 16.0/2  # this is where you will find the expressions you should evaluate
    
    answer = 8.0  # Already solved. Note that you have to match the type, '8' would have been incorrect
    check(example_1,answer,score)
    
    
    #==================================
    def example_2():
        return 16/0
    
    answer = "ZeroDivisionError"  # Already solved.
    check(example_2,answer,score)
    
    
    #==================================
    def exercise_1():
        return 5+7 # this is the expression you should evaluate
    
    answer = None  # <== replace 'None' with your answer
    check(exercise_1,answer,score)
    
    
    #==================================
    def exercise_2():
        return 1-5
    
    answer = None
    check(exercise_2,answer,score)
    
    
    #==================================
    def exercise_3():
        return 1+4*4
    
    answer = None
    check(exercise_3,answer,score)
    
    
    #==================================
    def exercise_4():
        return 5/2
    
    answer = None
    check(exercise_4,answer,score)
    
    
    #==================================
    def exercise_5():
        return 5//2
    
    answer = None
    check(exercise_5,answer,score)
    
    
    #==================================
    def exercise_6():
        return -+-+1
    
    answer = None
    check(exercise_6,answer,score)
    
    
    #==================================
    def exercise_7():
        return 2+-+-2
    
    answer = None
    check(exercise_7,answer,score)
    
    
    #==================================
    def exercise_8():
        return 2**2.0
    
    answer = None
    check(exercise_8,answer,score)
    
    
    #==================================
    def exercise_9():
        return 13%2
    
    answer = None
    check(exercise_9,answer,score)
    
    
    #==================================
    def exercise_10():
        return 1+5*2**3
    
    answer = None
    check(exercise_10,answer,score)
    
    
    #==================================
    def exercise_11():
        a = 4
        b = 6
        return (a-2)/(b+2)
    
    answer = None
    check(exercise_11,answer,score)
    
    
    #==================================
    def exercise_12():
        a = 0
        a -= 2
        return a-1
    
    answer = None
    check(exercise_12,answer,score)
    
    
    #==================================
    def exercise_13():
        val = -2
        other_val = 4**val
        return other_val*2
    
    answer = None
    check(exercise_13,answer,score)
    
    
    #==================================
    def exercise_14():
        return 1+2
    
    answer = None
    check(exercise_14,answer,score)
    
    
    #==================================
    def exercise_15():
        return 0.1+0.2
    
    answer = None
    check(exercise_15,answer,score)
    
    
    #==================================
    def exercise_16():
        a = 3
        b = 4
        return a**2 + b**2
    
    answer = None
    check(exercise_16,answer,score)
    
    
    #==================================
    def exercise_17():
        p = 0.4
        a = 20
        b = 100
        return (1-p)*a+p*b
    
    answer = None
    check(exercise_17,answer,score)
    
    
    #==================================
    def exercise_18():
        n = 3.0
        return (n-2)**(n-1)/(n+1)
    
    answer = None
    check(exercise_18,answer,score)
    
    
    #==================================
    def exercise_19():
        return 5.0//-2
    
    answer = None
    check(exercise_19,answer,score)
    
    
    #==================================
    def exercise_20():
        return 7.0 % 0
    
    answer = None
    check(exercise_20,answer,score)
    
    
    #==================================
    def exercise_21():
        return 7%2 + 6%2 + 5%2 + 4%2 + 3%2 + 2%2 + 1%2
    
    answer = None
    check(exercise_21,answer,score)
    
    
    #==================================
    def exercise_22():
        return float(50)
    
    answer = None
    check(exercise_22,answer,score)
    
    
    #==================================
    def exercise_23():
        return int(0.1)
    
    answer = None
    check(exercise_23,answer,score)
    
    
    #==================================
    def exercise_24():
        return float(10**1000)
    
    answer = None
    check(exercise_24,answer,score)
    

    #==================================
    def exercise_25():
        a = 4.0
        b = 9
        c = 0
        return max(a,b) * min(a,c)
    
    answer = None
    check(exercise_25,answer,score)
    
    
    #==================================
    printScore(score)
    


if __name__ == "__main__":
    main()
