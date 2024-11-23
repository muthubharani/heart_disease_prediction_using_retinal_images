from flask import Flask, render_template, flash, request, session, send_file
import pickle
import numpy as np
import mysql.connector
import sys

app = Flask(__name__)
app.config['DEBUG']
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'


@app.route("/")
def homepage():
    return render_template('index.html')


@app.route("/Home")
def Home():
    return render_template('index.html')


@app.route("/AdminLogin")
def AdminLogin():
    return render_template('AdminLogin.html')


@app.route("/UserLogin")
def UserLogin():
    return render_template('UserLogin.html')


@app.route("/NewUser")
def NewUser():
    return render_template('NewUser.html')


@app.route("/AdminHome")
def AdminHome():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2heartnewdb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM regtb  ")
    data = cur.fetchall()
    return render_template('AdminHome.html', data=data)


@app.route("/adminlogin", methods=['GET', 'POST'])
def adminlogin():
    if request.method == 'POST':
        if request.form['uname'] == 'admin' and request.form['password'] == 'admin':

            conn = mysql.connector.connect(user='root', password='', host='localhost', database='2heartnewdb')
            cur = conn.cursor()
            cur.execute("SELECT * FROM regtb ")
            data = cur.fetchall()
            flash("Login successfully")
            return render_template('AdminHome.html', data=data)

        else:
            flash("UserName Or Password Incorrect!")
            return render_template('AdminLogin.html')


@app.route("/AReport")
def AReport():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2heartnewdb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM reportb  ")
    data = cur.fetchall()
    return render_template('AReport.html', data=data)


@app.route("/newuser", methods=['GET', 'POST'])
def newuser():
    if request.method == 'POST':
        name = request.form['name']
        mobile = request.form['mobile']

        email = request.form['email']

        address = request.form['address']

        uname = request.form['uname']
        password = request.form['password']
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2heartnewdb')
        cursor = conn.cursor()
        cursor.execute("SELECT * from regtb where UserName='" + uname + "'")
        data = cursor.fetchone()
        if data is None:
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='2heartnewdb')
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO regtb VALUES ('','" + name + "','" + email + "','" + mobile + "','" + address + "','" + uname + "','" + password + "')")
            conn.commit()
            conn.close()
            flash('User Register successfully')

            return render_template('UserLogin.html')

        else:
            flash('Already registered')
            return render_template('NewUser.html')




@app.route("/userlogin", methods=['GET', 'POST'])
def userlogin():
    if request.method == 'POST':
        username = request.form['uname']
        password = request.form['password']
        session['uname'] = request.form['uname']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2heartnewdb')
        cursor = conn.cursor()
        cursor.execute("SELECT * from regtb where username='" + username + "' and Password='" + password + "'")
        data = cursor.fetchone()
        if data is None:

            flash('Username or Password is wrong')
            return render_template('UserLogin.html')
        else:
            session['mob']=data[3]

            conn = mysql.connector.connect(user='root', password='', host='localhost', database='2heartnewdb')
            cur = conn.cursor()
            cur.execute("SELECT * FROM regtb where username='" + username + "' and Password='" + password + "'")
            data = cur.fetchall()
            flash("Login successfully")

            return render_template('UserHome.html', data=data)


@app.route("/UserHome")
def UserHome():
    uname = session['uname']

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2heartnewdb')
    # cursor = conn.cursor()
    cur = conn.cursor()
    cur.execute("SELECT * FROM  regtb where username='" + uname + "'  ")
    data = cur.fetchall()
    return render_template('UserHome.html', data=data)


@app.route("/Heart")
def Heart():
    return render_template('Heart.html')


@app.route("/heart", methods=['GET', 'POST'])
def heart():
    if request.method == 'POST':

        Answer = ''
        Prescription = ''

        uname = session['uname']
        age = request.form['age']
        gender = request.form['gender']
        height = request.form['height']
        weight = request.form['weight']
        aphi = request.form['aphi']
        aplo = request.form['aplo']
        choles = request.form['choles']
        glucose = request.form['glucose']
        smoke = request.form['smoke']
        alcohol = request.form['alcohol']
        activity = request.form['activity']
        age1 = int(age)

        age = int(age)*(365)



        filename2 = 'Heart/heart-model.pkl'
        classifier2 = pickle.load(open(filename2, 'rb'))

        data = np.array([[int(age), int(gender), int(height), int(weight), int(aphi), float(aplo), float(choles), int(glucose), int(smoke), int(alcohol), int(activity)]])
        print(data)
        my_prediction = classifier2.predict(data)
        print(my_prediction[0])

        if my_prediction == 1:
            Answer = session['uname'] + ' :According to our Calculations, You have Heart disease'

            print('Hello:According to our Calculations, You have Heart disease')
            ans = 'Heart disease'
            msg = 'Hello:According to our Calculations, You have Heart disease.Angiotensin-converting enzyme (ACE) inhibitors, Food: fish or seafood.'
            Prescription = 'Angiotensin-converting enzyme (ACE) inhibitors, Food: fish or seafood.'

        else:
            Answer = session['uname'] + " Congratulations!!  You DON'T have Heart disease"
            ans = 'No Heart disease'
            msg = 'Congratulations!!  You DON T have  Heart Disease'
            print('Congratulations!! You DON T have Heart disease')
            Prescription = 'Nill'

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2heartnewdb')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO reportb VALUES ('','" + uname + "','" + str(age1) + "' ,'" + str(gender) + "','" + str(height) + "','" + str(weight) + "','" + str(aphi) + "','" + str(aplo)
            + "','" + str(choles) + "','" + str(glucose) + "','" + str(smoke) + "','" + str(alcohol) + "','" + str(activity) + "','"+ ans +"','"+ Prescription +"')")
        conn.commit()
        conn.close()
        print(Prescription)
        return render_template('Answer.html', data=Answer,data1=Prescription,data3=my_prediction)


@app.route("/Report")
def Report():
    uname = session['uname']
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2heartnewdb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM  reportb where username='" + uname + "'  ")
    data = cur.fetchall()
    return render_template('Report.html', data=data)




@app.route("/sss",methods=['GET', 'POST'])
def sss():
    if request.method == 'POST':
        return render_template('Report.html')

def sendmsg(targetno,message):
    import requests
    requests.post(
        "http://sms.creativepoint.in/api/push.json?apikey=6555c521622c1&route=transsms&sender=FSSMSS&mobileno=" + targetno + "&text=Dear customer your msg is " + message + "  Sent By FSMSG FSSMSS")



if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
