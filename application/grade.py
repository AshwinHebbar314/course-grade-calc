"""Grade Calculation Function"""
#Common for both foundation and diploma
from sqlalchemy import except_all


def grade(n):
    if n>=90:
        return ("S",10)
    elif 80<=n<90:
        return ("A",9)
    elif 70<=n<80:
        return ("B",8)
    elif 60<=n<70:
        return ("C",7)
    elif 50<=n<60:
        return ("D",6)
    elif 40<=n<50:
        return ("E",4)
    else:
        return ("U",0)

"""CGPA Calculation Function"""
def cgpa(L):
    gradepoint = {'S':10,'A':9,'B':8,'C':7,'D':6,'E':4,'U':0, 'I':0}
    total = 0
    for i in L:
        try:
            total += gradepoint[i]
        except:
            return "Invalid Input, Please Check Your Input. Only S,A,B,C,D,E,U,I are accepted."
    return round(total/len(L),2)