from main import app
from flask import render_template,request
from .diploma import *
from .grade import *

@app.route("/",methods = ['GET','POST'])
def index():
    if request.method == 'GET':
        if request.args == {}:
            return render_template("index.html",flag=0,d=diploma)
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

    if request.method == 'POST':
        sub=DiplomaSubject(request.form['subject'],request.form)
        t = round(sub.calculate(),2)
        g = grade(t)
        return render_template("result.html",t=t,g=g)