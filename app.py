from flask import Flask,render_template,request
import os
app=Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/",methods=['POST'])
def sms():
	phonesms=request.form['phone']
	numbersms=request.form['noofmess']
	delaysms=request.form['delay']
	commwindows="bomber.py sms {} {} {}".format(phonesms,numbersms,delaysms)
	commlinux=" python3 bomber.py sms {} {} {}".format(phonesms,numbersms,delaysms)
	if os.name == 'nt':
		os.system(commwindows)
	else:
		os.system(commlinux)
	return render_template("index.html")


@app.route("/call")
def indexcall():
	return render_template("call.html")



@app.route("/call",methods=['GET','POST'])
def call():
	phone=request.form['phoneno']
	numbersms=request.form['messno']
	delay=request.form['del']
	commwindows="bomber.py call {} {} {}".format(phone,numbersms,delay)
	commlinux="python3 bomber.py call {} {} {}".format(phone,numbersms,delay)
	if (os.name == 'nt'):
		os.system(commwindows)
	else:
		os.system(commlinux)
	return render_template("call.html")



if __name__=="__main__":
	app.run(debug=True,host="0.0.0.0",port="1444")