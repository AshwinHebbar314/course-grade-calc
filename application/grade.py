"""Grade Calculation Function"""
#Common for both foundation and diploma
def grade(n):
    if n>=90:
        return "S"
    elif 80<=n<90:
        return "A"
    elif 70<=n<80:
        return "B"
    elif 60<=n<70:
        return "C"
    elif 50<=n<60:
        return "D"
    elif 40<=n<50:
        return "E"
    else:
        return "U"