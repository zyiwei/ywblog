#-*- coding=utf-8 -*-
from flask import current_app,render_template,flash
from flask_mail import Message,Mail
from . import mail
from threading import Thread


def send_async_email(app,msg):
	with app.app_context():
		mail.send(msg)


def send_email(to,subject,template,**kargs):
	app=current_app._get_current_object()
	msg=Message(current_app.config['FLASKY_MAIL_SUBJECT_PREFIX']+subject,sender=current_app.config['FLASKY_MAIL_SENDER'],recipients=[to])
	msg.body=render_template(template+'.txt',**kargs)
	msg.html=render_template(template+'.html',**kargs)

	thr=Thread(target=send_async_email,args=[app,msg])
	thr.start()
	return thr