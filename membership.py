#!/usr/bin/python
# coding: utf-8
from flask import Flask, request, render_template, url_for, redirect
import requests
import mailgun

app = Flask(__name__)

@app.route("/sign-up")
def signup():
	return render_template("signup.html")


@app.route("/register-membership", methods=['POST'])
def register_membership():
	if request.method == 'POST':
		# Samtykkeærklering
		if request.form.get('samtykke', False) == '1':
			mailgun.send_message(
				to=request.form.get('email'),
				subject=u"Vennligst bekreft medlemskap i komponistkollektivet",
				msg=u"""
	Vi har mottatt innmelding for %(name)s som medlem i Komponistkollektivet. 
	Dersom dette stemmer klikk på linken nedenfor for å bekrefte ditt medlemskap.

	https://komponistkollektivet.no/#confirm-membership?id=%(email)s

	Dersom dette ikke stemmer kan du avbekrefte innmeldingen ved å klikke her: 
	https://komponistkollektivet.no/#no-membership-today-please?id=%(email)s
	""" % dict(name=request.form.get('firstname') + " " + request.form.get('lastname'), email=request.form.get('email'))
		
	)
			return "Du er nå medlem."
		else:
			return "Du har ikke samtykket, og er ikke medlem"
	else:
		return redirect(url_for('signup'))


if __name__ == '__main__':
	import webbrowser
	webbrowser.open("http://127.0.0.1:5000/sign-up")
	app.run(debug=True)