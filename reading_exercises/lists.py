from shared import safelyCallThenScoreAndPrintFeedback as check
from shared import printScore

def main():
    #See 'arithmetic-expressions.py' for instructions on how to use this script.
    score = [0,0,0]
    
    #==================================
    def example_1():
        return ["a","b"][0]  # this is where you will find the expressions you should evaluate
        
    answer = "a"  # Already solved.
    check(example_1,answer,score)
    
    
    #==================================
    def example_2():
        return ["a","b","c"][5]
        
    answer = "IndexError"  # Already solved.
    check(example_2,answer,score)
    
    
    #==================================
    def exercise_1():
        my_list = [1,2]
        return my_list[1]  # this is the expression you should evaluate
    
    answer = None  # <== replace 'None' with your answer
    check(exercise_1,answer,score)
    
    
    #==================================
    def exercise_2():
        return [3] + [2]
    
    answer = None
    check(exercise_2,answer,score)
    
    
    #==================================
    def exercise_3():
        return [12,15,7] - [7]
    
    answer = None
    check(exercise_3,answer,score)
    
    
    #==================================
    def exercise_4():
        return [1,0]*3
    
    answer = None
    check(exercise_4,answer,score)
    
    
    #==================================
    def exercise_5():
        return [1,0]*[2]
    
    answer = None
    check(exercise_5,answer,score)
    
    
    #==================================
    def exercise_6():
        return [1,0]*2.0
    
    answer = None
    check(exercise_6,answer,score)
    
    
    #==================================
    def exercise_7():
        my_list = [1,"2"]
        my_list += [-3]
        return my_list
    
    answer = None
    check(exercise_7,answer,score)
    
    
    #==================================
    def exercise_8():
        my_list = [2,3,5,7,11,13]
        return my_list[-2]
    
    answer = None
    check(exercise_8,answer,score)
    
    
    #==================================
    def exercise_9():
        my_list = [2,3,5,7,11,13]
        return my_list[1:4]
    
    answer = None
    check(exercise_9,answer,score)
    
    
    #==================================
    def exercise_10():
        return [1.0,2.0,3.0][1:]
    
    answer = None
    check(exercise_10,answer,score)
    
    
    #==================================
    def exercise_11():
        return [2,3,4,5,6,7,8,9][::2]
    
    answer = None
    check(exercise_11,answer,score)
    
    
    #==================================
    def exercise_12():
        my_list = [1,2]
        my_other_list = [3,4]
        return my_list + my_other_list[::-1]
    
    answer = None
    check(exercise_12,answer,score)
    
    
    #==================================
    def exercise_13():
        my_list = [1,2]
        my_other_list = [1,2]
        return (my_list + my_other_list)[::-1]
    
    answer = None
    check(exercise_13,answer,score)
    
    
    #==================================
    def exercise_14():
        my_list = ([1+2,3+4,5+6]+[-3,-7,-11])*2
        return my_list[7]
    
    answer = None
    check(exercise_14,answer,score)
    
    
    #==================================
    def exercise_15():
        return len([0,1,2,3])
    
    answer = None
    check(exercise_15,answer,score)
    
    
    #==================================
    def exercise_16():
        return [[1,1,2,3]][0]
    
    answer = None
    check(exercise_16,answer,score)
    
    
    #==================================
    def exercise_17():
        return [[1,1],[2,3]][2]
    
    answer = None
    check(exercise_17,answer,score)
    
    
    #==================================
    def exercise_18():
        return 4[0]
    
    answer = None
    check(exercise_18,answer,score)
    
    
    #==================================
    def exercise_19():
        my_list = [16,8,4,2,1]
        return (my_list[0:-1:2]*2)[3]
    
    answer = None
    check(exercise_19,answer,score)
    
    
    #==================================
    def exercise_20():
        return len([2,3,5,7]*5+[]+[]+[0,1])
    
    answer = None
    check(exercise_20,answer,score)
    
    
    #==================================
    def exercise_21():
        a = [4,8,16,32]
        b = [1,3,5,7,9]
        c = [2,3,5,7,11,13]
        return a[:-2] + b[2::2] + c[1]
    
    answer = None
    check(exercise_21,answer,score)
    
    
    #==================================
    def exercise_22():
        return [0][0.0]
    
    answer = None
    check(exercise_22,answer,score)
    
    
    #==================================
    printScore(score)
    

if __name__ == "__main__":
    main()
