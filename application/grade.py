"""Grade Calculation Function"""
#Common for both foundation and diploma

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
