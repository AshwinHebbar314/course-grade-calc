subid = {
    '1':"Mathematics for Data Science I",
    '2':"Statistics for Data Science I",
    '3': "Computational Thinking",
    '4': "English I",
    '5': "Mathematics for Data Science II",
    '6': "Statistics for Data Science II",
    '7': "Programming in Python",
    '8': "English II"
}

class FoundationSubs:
    def __init__(self, id, d):
        self.id = id
        self.d = d
    def calculate(self):
        if self.id in ['1', '2', '3', '4', '5', '6', '8']:
            gaa = float(self.d['gaa'])
            q1 = float(self.d['q1'])
            q2 = float(self.d['q2'])
            f = float(self.d['f'])
            try:
                exAct = float(self.d['exAct'])
            except:
                exAct = 0
            t = 0.1*gaa + max(0.6*f + 0.25*max(q1, q2), 0.4*f + 0.25*q1 + 0.25*q2) + exAct

            return min(100,t)
        
        # elif self.id == '6':
        #     gaa = float(self.d['gaa'])
        #     q1 = float(self.d['q1'])
        #     q2 = float(self.d['q2'])
        #     f = float(self.d['f'])
        #     exAct = float(self.d['exAct']) #capped to 10

        #     t = 0.1*gaa + max(0.6*f + 0.25*max(q1, q2), 0.4*f + 0.25*q1 + 0.25*q2) + exAct

        #     return min(100,t)

        elif self.id == '7':
            gaa = float(self.d['gaa'])
            q1 = float(self.d['q1'])
            q2 = float(self.d['q2']) #oppe
            q3 = float(self.d['q3']) #oppe
            f = float(self.d['f'])
            t = 0.1*gaa + 0.2*max(q2,q3) + 0.1*min(q2,q3) + max(0.5*f + 0.2*q1, 0.6*f)

            return min(100,t)

        else:
            return "courseError: Course Does not exist."