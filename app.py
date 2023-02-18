from flask import Flask,redirect,url_for,render_template,request,session
import mysql.connector
import obj


app = Flask(__name__)
app.secret_key="hey"


@app.route("/login",methods=['GET','POST'])
def login():
    if request.method=='POST':
        
        p_num=request.form['p_name']
        first_name=request.form['first_name']
        last_name=request.form['last_name']
        gender=request.form['gender']
        dob=request.form['dob']
        email_id=request.form['email_id']
        obj.User(p_num,first_name,last_name,gender,dob,email_id)

        return redirect(url_for('create',p_num=p_num,first_name=first_name,last_name=last_name,))
    else:
        return render_template("index.html")


# @app.route("/register",methods=['GET','POST'])
# def login():
#     if request.method=='POST':
#         ssn=request.form['passport']
#         ssn=request.form['first_name']
#         ssn=request.form['last_name']
#         ssn=request.form['gender']
#         ssn=request.form['dob']
#         ssn=request.form['email_id']
#         return redirect(url_for('create',name=ssn))
#     else:
#         return render_template("index.html")
        

# @app.route("/flights",methods=['GET','POST'])
# def login():
#     if request.method=='POST':
#         ssn=request.form['ssn']
#         return redirect(url_for('create',name=ssn))
#     else:
#         # x=flights()
#         return redirect(url_for('create'))
        
# @app.route("/details",methods=['GET','POST'])
# def login1():
#     if request.method=='POST':
#         ssn=request.form['ssn']
#         return redirect(url_for('create',name=ssn))
#     else:
#         return render_template("details.html")
        
# @app.route("/booking",methods=['GET','POST'])
# def login():
#     if request.method=='POST':
#         ssn=request.form['ssn']
#         return redirect(url_for('create',name=ssn))
#     else:
#         return render_template("booking.html")

# @app.route("/confirmed",methods=['GET','POST'])
# def login():
#     if request.method=='POST':
#         ssn=request.form['ssn']
#         return redirect(url_for('create',name=ssn))
#     else:
#         return render_template("confirmed.html")
                
# @app.route("/mytickets",methods=['GET','POST'])
# def login():
#     if request.method=='POST':
#         ssn=request.form['ssn']
#         return redirect(url_for('create',name=ssn))
#     else:
#         return render_template("confirmed.html")
                
if(__name__=="__main__"):
    app.run(debug=True)