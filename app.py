from flask import Flask,render_template,request
import os
from datetime import datetime
app=Flask(__name__)


def logger(a,b,c,d,e):
	now=datetime.now()
	with open("./templates/log.html","a+") as w:
		
		if(e=="call"):
			w.write("<br><li class='list-group-item list-group-item-danger'><b>{}</b> PHONE NO :{} , BOMBED no of times: <b>{}</b> , with delay : <b>{}</b> by <b>{}</b> - <b>{}</b></li>\r\n".format(now,a,b,c,d,e))
		else:
			w.write("<br><li class='list-group-item list-group-item-warning'><b>{}</b> PHONE NO :<b>{}</b> , BOMBED no of times: <b>{}</b> , with delay : <b>{}</b> by <b>{}</b> - <b>{}</b></li>\r\n".format(now,a,b,c,d,e))

        #w.write("<br><li><em>{}</em> phone no :{} , bombed no of times: {} , with delay : {} by {} - {}\r\n".format(now,a,b,c,d,e))

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/",methods=['POST'])
def sms():
	phonesms=request.form['phone']
	numbersms=request.form['noofmess']
	delaysms=request.form['delay']
	logger(phonesms,numbersms,delaysms,request.remote_addr,"sms")
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
	logger(phone,numbersms,delay,request.remote_addr,"call")
	commwindows="bomber.py call {} {} {}".format(phone,numbersms,delay)
	commlinux="python3 bomber.py call {} {} {}".format(phone,numbersms,delay)
	if (os.name == 'nt'):
		os.system(commwindows)
	else:
		os.system(commlinux)
	return render_template("call.html")

@app.route("/log")
def l():
	return render_template("log.html")



if __name__=="__main__":
	app.run(debug=True,host="0.0.0.0",port="1444")