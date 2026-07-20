from shared import safelyCallThenScoreAndPrintFeedback as check
from shared import printScore

def main():
    #See 'arithmetic-expressions.py' for instructions on how to use this script.
    score = [0,0,0]
    
    #==================================
    def example_1():
        d = {42:"Mike",11:"John"}
        return d[42]  # this is where you will find the expressions you should evaluate
        
    answer = "Mike"  # Already solved.
    check(example_1,answer,score)
    
    
    #==================================
    def example_2():
        d = {42:"Mike",11:"John"}
        return d[0]
        
    answer = "KeyError"  # Already solved.
    check(example_2,answer,score)
    
    
    #==================================
    def exercise_1():
        d = {}
        d[1] = [22]
        return d[0]  # this is the expression you should evaluate
    
    answer = None  # <== replace 'None' with your answer
    check(exercise_1,answer,score)
    

    #==================================
    def exercise_2():
        d = {}
        d[1] = [22]
        return d
    
    answer = None
    check(exercise_2,answer,score)
    

    #==================================
    def exercise_3():
        d = {"a":97}
        d["a"] = ["arc","antique"]
        return type(d["a"])
    
    answer = None
    check(exercise_3,answer,score)
    

    #==================================
    def exercise_4():
        d = {0:1,
             1:1,
             2:2,
             3:3,
             4:5}
        return d[3]+d[4]
    
    answer = None
    check(exercise_4,answer,score)
    

    #==================================
    def exercise_5():
        d = {"name":"Daniel","school":"UCLA"}
        e = {"major":"Physics"}
        return (d+e)["major"]
    
    answer = None
    check(exercise_5,answer,score)
    

    #==================================
    def exercise_6():
        d = {12:6,3:1}
        d[3] = 10
        return d
    
    answer = None
    check(exercise_6,answer,score)
    

    #==================================
    def exercise_7():
        phone = {"Adam":"232 123 4567","Thor":"358 777 0490"}
        return phone["Thor"][:3]
    
    answer = None
    check(exercise_7,answer,score)
    

    #==================================
    def exercise_8():
        d1 = {"Hominids":"Primates","Canidae":"Carnivora","Lemuridae":"Primates"}
        d2 = {"Primates":"Mammalia","Carnivora":"Mammalia"}
        return d2[d1["Canidae"]]
    
    answer = None
    check(exercise_8,answer,score)
    

    #==================================
    def exercise_9():
        d = {1.1:1,1.7:1,"a":2}
        return len(d)
    
    answer = None
    check(exercise_9,answer,score)
    

    #==================================
    def exercise_10():
        phone = {"Adam":"232 123 4567","Thor":"358 777 0490"}
        return "Adam" in phone
    
    answer = None
    check(exercise_10,answer,score)
    

    #==================================
    def exercise_11():
        d = {0:"abc",1:"def",2:"ghi"}
        return list(d)
    
    answer = None
    check(exercise_11,answer,score)
    

    #==================================
    def exercise_12():
        d = {"Sean Connery":["Highlander"]}
        del d["Sean Connery"]
        return d
    
    answer = None
    check(exercise_12,answer,score)
    

    #==================================
    def exercise_13():
        d1 = {50:1}
        d2 = {60:2}
        return d2 > d1
    
    answer = None
    check(exercise_13,answer,score)
    

    #==================================
    def exercise_14():
        d1 = {50:1,0:0}
        d2 = {0:0,50:1}
        return d2 == d1
    
    answer = None
    check(exercise_14,answer,score)
    

    #==================================
    def exercise_15():
        d = {"Sean Connery":["Highlander"]}
        values = d.values()
        d["Sean Connery"] += ["James Bond"]
        return list(values)
    
    answer = None
    check(exercise_15,answer,score)
    

    #==================================
    def exercise_16():
        d1 = {0:"bread",1:"cheese"}
        d2 = {0:"pepperoni",1:"tomatoes"}
        return d1.keys() == d2.keys()
    
    answer = None
    check(exercise_16,answer,score)
    

    #==================================
    def exercise_17():
        d = {0:"bread",1:"cheese"}
        return d.values() == d.values()
    
    answer = None
    check(exercise_17,answer,score)
    
    
    #==================================
    printScore(score)
    

if __name__ == "__main__":
    main()
