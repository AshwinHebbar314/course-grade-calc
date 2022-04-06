diploma={'1':'Machine Learning Foundations','2':'Business Data Management','3':'Programming Data Structures and Algorithms using Python','4':'Database management system','5':'Application development - 1','6':'Programming concepts using Java','7':'Machine Learning Techniques','8':'Machine Learning Practice','9':'Business Analytics','10':'Tools in Data Science','11':'System commands','12':'Application Development - 2'}

class DiplomaSubject:
    def __init__(self,id,d):
        self.id=id
        self.d = d
    def calculate(self):
        if self.id == '1':
            gaa = float(self.d['gaa'])
            q1 = float(self.d['q1'])
            q2 = float(self.d['q2'])
            f = float(self.d['f'])
            t = 0.1*gaa+ max(0.6*f + 0.25*max(q1, q2), 0.4*f + 0.25*q1 + 0.25*q2)
            return t

        if self.id == '2':
            Qz1 = float(self.d['q1'])
            Qz2 = float(self.d['q2'])
            GAA = float(self.d['gaa'])
            P = float(self.d['p'])
            OP = float(self.d['op'])
            F = float(self.d['f'])
            bonus = float(self.d['bonus'])
            t = 0.2*max(Qz1,Qz2)+0.3*GAA+0.2*max(P,OP)+0.3*F+bonus
            return t

        if self.id == '3':
            GAA = float(self.d['gaa'])
            Qz1 = float(self.d['q1'])
            Qz2 = float(self.d['q2'])
            OP = float(self.d['op'])
            F = float(self.d['f'])
            t =  0.1*GAA + max ((0.5*F+0.2*OP+0.15*max(Qz1, Qz2)),  (0.4*F+0.2*OP+0.15*Qz1+0.15*Qz2 ))
            return t 

        if self.id == '4':
            GAA = float(self.d['gaa'])
            Qz1 = float(self.d['q1'])
            Qz2 = float(self.d['q2'])
            OP = float(self.d['op'])
            F = float(self.d['f'])
            t =  0.1*GAA+ 0.2*OP+ max (0.5*F + 0.15*max(Qz1, Qz2),  0.4*F + 0.15*Qz1 + 0.15*Qz2 )  
            return t 

        if self.id == '5':
            GA = float(self.d['gaa'])
            Qz1 = float(self.d['q1'])
            Qz2 = float(self.d['q2'])
            PV = float(self.d['p'])
            F = float(self.d['f'])
            t = 0.25*PV+0.15*GA+ max(0.3*F+0.15*Qz1+0.15*Qz2, 0.4*F+0.15*max(Qz1,Qz2))
            return t 

        if self.id == '6':
            GAA = float(self.d['gaa'])
            Qz1 = float(self.d['q1'])
            Qz2 = float(self.d['q2'])
            PE1 = float(self.d['op1'])
            PE2 = float(self.d['op2'])
            F = float(self.d['f'])
            t =((0.1*GAA + 0.2*max(PE1,PE2)+ 0.10*min(PE1,PE2)+max(0.4*F+0.25*max(Qz1,Qz2),0.3*F+0.2*Qz1+0.2*Qz2))/110)*100
            return t 

        if self.id == '7':
            GAA = float(self.d['gaa'])
            Qz1 = float(self.d['q1'])
            Qz2 = float(self.d['q2'])
            OPE1 = float(self.d['op1'])
            OPE2 = float(self.d['op2'])
            F = float(self.d['f'])
            t = ((0.1*GAA + 0.15*max(Qz1,Qz2) + 0.5*F+0.2*max(OPE1,OPE2) + 0.10*min(OPE1,OPE2) +0.05*min(Qz1,Qz2))/110)*100
            return t

        if self.id == '8':
            GAA = float(self.d['gaa'])
            Qz1 = float(self.d['q1'])
            Qz2 = float(self.d['q2'])
            OPE1 = float(self.d['op1'])
            OPE2 = float(self.d['op2'])
            F = float(self.d['f'])
            t = ((0.1*GAA + 0.15*max(Qz1,Qz2) + 0.5*F+0.2*max(OPE1,OPE2) + 0.10*min(OPE1,OPE2) +0.05*min(Qz1,Qz2))/110)*100
            return t

        if self.id == '9':
            Qz1 = float(self.d['q1'])
            Qz2 = float(self.d['q2'])
            Asgn1 = float(self.d['a1'])
            Asgn2 = float(self.d['a2'])
            Asgn3 = float(self.d['a3'])
            F = float(self.d['f'])
            t = 0.20*max(Qz1,Qz2) + 0.10*Asgn1 + 0.15*Asgn2 + 0.15*Asgn3 + 0.40*F
            return t 

        if self.id == '10':
            GAA = float(self.d['gaa'])
            OPE = float(self.d['op'])
            P1 = float(self.d['p1'])
            P2 = float(self.d['p2'])
            F = float(self.d['f'])
            t = 0.1*GAA +  0.25*F+ 0.25*OPE + 0.2*P1 + 0.2*P2
            return t 

        if self.id == '11':
            GAA = float(self.d['gaa'])
            Qz1 = float(self.d['q1'])
            Qz2 = float(self.d['q2'])
            OPE = float(self.d['op'])
            F = float(self.d['f'])
            t = 0.1*GAA + 0.25*OPE+ max(0.4*F+0.2*max(Qz1,Qz2), 0.3*F+0.15*Qz1+0.2*Qz2)
            return t

        if self.id == '12':
            GA = float(self.d['gaa'])
            Qz1 = float(self.d['q1'])
            Qz2 = float(self.d['q2'])
            PV = float(self.d['p'])
            F = float(self.d['f'])
            t = 0.25*PV+0.15*GA+ max(0.3*F+0.15*Qz1+0.15*Qz2, 0.4*F+0.15*max(Qz1,Qz2))
            return t  