from main import app
from flask import render_template,request
from .diploma import *
from .grade import *
from .foundation import *

#Homepage
@app.route("/")
def homepage():
    return render_template("homepage.html")

#Foundation
@app.route("/foundation", methods = ['GET', 'POST'])
def foundation_index():
    subject_id = request.args.get('subject')
    if request.method == "GET":
        if request.args == {}:
            return render_template("foundation.html", flag = 0, d = subid)
        if int(request.args.get('subject')) in [1,2,3,4,5,6,7,8]:
            return foundation_sub(subject_id)
    else:
        sub = FoundationSubs(subject_id, request.form)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print(request.args.get('subject'))
        print(request.form)
        t = sub.calculate()
        print(t)
        # g = grade(int(t))
        # print(g)
        return render_template("result.html", t = t)


@app.route("/foundation/<subjectid>", methods = ['GET', 'POST'])
def foundation_sub(subjectid):
    if request.method == "GET":
        if int(subjectid) in [1,2,3,4,5,6,8]:
            return render_template("foundation/type1.html", subname = subid[subjectid], subid = subjectid)
        elif int(subjectid) == 7:
            return render_template("foundation/type2.html", subname = subid[subjectid])


#Diploma
@app.route("/diploma",methods = ['GET','POST'])
def index():
    if request.method == 'GET':
        if request.args == {}:
            return render_template("diploma.html",flag=0,d=diploma)
        if request.args.get("subject") == '1':
            i = '1'
            return render_template("diploma/sub1.html",flag=1,x=i,y=diploma[i])
        if request.args.get("subject") == '2':
            i = '2'
            return render_template("diploma/sub2.html",flag=1,x=i,y=diploma[i])
        if request.args.get("subject") == '3':
            i = '3'
            return render_template("diploma/sub3.html",flag=1,x=i,y=diploma[i])
        if request.args.get("subject") == '4':
            i = '4'
            return render_template("diploma/sub4.html",flag=1,x=i,y=diploma[i])
        if request.args.get("subject") == '5':
            i = '5'
            return render_template("diploma/sub5.html",flag=1,x=i,y=diploma[i])
        if request.args.get("subject") == '6':
            i = '6'
            return render_template("diploma/sub6.html",flag=1,x=i,y=diploma[i])
        if request.args.get("subject") == '7':
            i = '7'
            return render_template("diploma/sub7.html",flag=1,x=i,y=diploma[i])
        if request.args.get("subject") == '8':
            i = '8'
            return render_template("diploma/sub8.html",flag=1,x=i,y=diploma[i])
        if request.args.get("subject") == '9':
            i = '9'
            return render_template("diploma/sub9.html",flag=1,x=i,y=diploma[i])
        if request.args.get("subject") == '10':
            i = '10'
            return render_template("diploma/sub10.html",flag=1,x=i,y=diploma[i])
        if request.args.get("subject") == '11':
            i = '11'
            return render_template("diploma/sub11.html",flag=1,x=i,y=diploma[i])
        if request.args.get("subject") == '12':
            i = '12'
            return render_template("diploma/sub12.html",flag=1,x=i,y=diploma[i])
        if request.args.get("subject") == 'Choose Subject':
            return 'Choose a valid subject'

    if request.method == 'POST':
        sub=DiplomaSubject(request.form['subject'],request.form)
        t = round(sub.calculate(),2)
        g = grade(t)
        return render_template("diplomaresult.html",t=t,g=g,i=request.form['subject'],subject=diploma[request.form["subject"]])