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
        return render_template("index.html")


@app.route("/register",methods=['GET','POST'])
def login():
    if request.method=='POST':
        ssn=request.form['ssn']
        return redirect(url_for('create',name=ssn))
    else:
        return render_template("index.html")
        

@app.route("/flights",methods=['GET','POST'])
def login():
    if request.method=='POST':
        ssn=request.form['ssn']
        return redirect(url_for('create',name=ssn))
    else:
        return render_template("flights.html")
        
@app.route("/details",methods=['GET','POST'])
def login():
    if request.method=='POST':
        ssn=request.form['ssn']
        return redirect(url_for('create',name=ssn))
    else:
        return render_template("details.html")
        
@app.route("/booking",methods=['GET','POST'])
def login():
    if request.method=='POST':
        ssn=request.form['ssn']
        return redirect(url_for('create',name=ssn))
    else:
        return render_template("booking.html")

@app.route("/confirmed",methods=['GET','POST'])
def login():
    if request.method=='POST':
        ssn=request.form['ssn']
        return redirect(url_for('create',name=ssn))
    else:
        return render_template("confirmed.html")
                
@app.route("/mytickets",methods=['GET','POST'])
def login():
    if request.method=='POST':
        ssn=request.form['ssn']
        return redirect(url_for('create',name=ssn))
    else:
        return render_template("confirmed.html")
                
if(__name__=="__main__"):
    app.run(debug=True)