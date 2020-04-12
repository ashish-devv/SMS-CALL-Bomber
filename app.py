from flask import Flask,render_template,request
import os
app=Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/call")
def indexcall():
	return render_template("call.html")

@app.route("/",methods=['POST'])
def sms():
	phonesms=request.form['phone']
	numbersms=request.form['noofmess']
	delaysms=request.form['delay']
	comm="bomber.py sms {} {} {}".format(phonesms,numbersms,delaysms)
	os.system(comm)
	return render_template("index.html")

@app.route("/call",methods=['POST'])
def call():
	phone=request.form['phoneno']
	numbersms=request.form['messno']
	delay=request.form['del']
	comm="bomber.py call {} {} {}".format(phone,numbersms,delay)
	os.system(comm)
	return render_template("call.html")



if __name__=="__main__":
	app.run(debug=True)