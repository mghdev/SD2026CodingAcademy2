from shared import safelyCallThenScoreAndPrintFeedback as check
from shared import printScore

def main():
    #See 'arithmetic-expressions.py' for instructions on how to use this script.
    score = [0,0,0]

    #==================================
    def example_1():
        return not True  # this is where you will find the expressions you should evaluate

    answer = False  # Already solved.
    check(example_1,answer,score)


    #==================================
    def example_2():
        return 2 < "a"

    answer = "TypeError"  # Already solved.
    check(example_2,answer,score)


    #==================================
    def exercise_1():
        return not False # this is the expression you should evaluate

    answer = None  # <== replace 'None' with your answer
    check(exercise_1,answer,score)


    #==================================
    def exercise_2():
        return True or False

    answer = None
    check(exercise_2,answer,score)


    #==================================
    def exercise_3():
        var = not False and True
        return var

    answer = None
    check(exercise_3,answer,score)


    #==================================
    def exercise_4():
        return False or not True

    answer = None
    check(exercise_4,answer,score)


    #==================================
    def exercise_5():
        return not (True or False)

    answer = None
    check(exercise_5,answer,score)


    #==================================
    def exercise_6():
        a = 4 < 9
        return a

    answer = None
    check(exercise_6,answer,score)


    #==================================
    def exercise_7():
        i = 4
        j = 4.0
        return i == j

    answer = None
    check(exercise_7,answer,score)


    #==================================
    def exercise_8():
        return True * 5

    answer = None
    check(exercise_8,answer,score)


    #==================================
    def exercise_9():
        return "apple" < "branch"

    answer = None
    check(exercise_9,answer,score)


    #==================================
    def exercise_10():
        return "a" >= "A"

    answer = None
    check(exercise_10,answer,score)


    #==================================
    def exercise_11():
        s = "water"
        n = 90
        return s >= n+10

    answer = None
    check(exercise_11,answer,score)


    #==================================
    def exercise_12():
        return (5 == 7-2) and (10/2 <= 5.0)

    answer = None
    check(exercise_12,answer,score)


    #==================================
    def exercise_13():
        return "doom"[1] < "electric"

    answer = None
    check(exercise_13,answer,score)


    #==================================
    def exercise_14():
        a = 24-3
        return (a%2 == 0 or a%3 == 0) or a**2 > 1000

    answer = None
    check(exercise_14,answer,score)


    #==================================
    def exercise_15():
        return ("a"*2+"b"*4)[2]*2 < "aardvark"

    answer = None
    check(exercise_15,answer,score)


    #==================================
    def exercise_16():
        return 0 and 2

    answer = None
    check(exercise_16,answer,score)


    #==================================
    def exercise_17():
        return 1 and 2

    answer = None
    check(exercise_17,answer,score)


    #==================================
    def exercise_18():
        return True and "a">=2

    answer = None
    check(exercise_18,answer,score)


    #==================================
    def exercise_19():
        return True or "a">=2

    answer = None
    check(exercise_19,answer,score)

    #==================================
    def exercise_20():
        return "b" in "bread"

    answer = None
    check(exercise_20,answer,score)


    #==================================
    printScore(score)

if __name__ == "__main__":
    main()