from flask import Flask,redirect,url_for,render_template,request,session
import mysql.connector
 


app = Flask(__name__)
app.secret_key="hey"


@app.route("/login",methods=['GET','POST'])
def login():
    if request.method=='POST':
        ssn=request.form['ssn']
        return redirect(url_for('create',name=ssn))
    else:
        return render_template("login.html")

if(__name__=="__main__"):
    app.run(debug=True)