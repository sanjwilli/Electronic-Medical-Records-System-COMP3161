from app import app, db
from flask import render_template, request, redirect, url_for, flash, jsonify, json, session, abort

# -----------------------------------------------------------------
@app.route('/')
def home():
	return render_template('home.html')

@app.route('/profile')
def profile():
	if not session.get('logged_in'):
		abort(401)

@app.route('/login', methods=['POST', 'GET'])
def login():
	if request.method == 'POST':
		pass
		# if not valid info:
		# 	pass
		# else:
		# 	if ID matches respective type_:
		# 		return render_template('admin.html')
		# 	elif ID matches respective type_:
		# 		return render_template('doctor.html')
		# 	elif ID matches respective type_:
		# 		return render_template('nurse.html')
		# 	elif ID matches respective type_:
		# 		return render_template('secretary.html')
	return render_template('login.html')

@app.route('/logout')
def logout():
	session.pop('logged_in', None)
	flash('You were loggged out')
	return redirect(url_for('home'))

# -----------------------------------------------------------------

@app.route('/admin')
def admin():
	return render_template('admin.html')

@app.route('/doctor')
def doctor():
	return render_template('doctor.html')

@app.route('/nurse')
def nurse():
	return render_template('nurse.html')

@app.route('/secretary')
def secretary():
	return render_template('secretary.html')


# -----------------------------------------------------------------

@app.route('/add/doctor')
def addDoc():
	return render_template('add_doctor.html')

@app.route('/add/nurse')
def addNur():
	return render_template('add_nurse.html')

@app.route('/add/secretary')
def addSec():
	return render_template('add_secretary.html')


# -----------------------------------------------------------------

@app.route('/add/patient')
def create_patient():
	return render_template('add_patient.html')

@app.route('/edit/patient')
def edit_patient():
	return render_template('edit_patient.html')

# -----------------------------------------------------------------
@app.after_request
def add_header(response):
	''' 
	Add header to both force lastest IE rendering engine or Chome Frame
	and also to cache the rendered page for 10  minutes 
	'''
	response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
	response.headers['Cache-Control'] = 'public, max-Age=0'
	return response

@app.errorhandler(404)
def pAge_not_found(error):
	''' Custom 404 pAge '''
	return render_template('404.html'), 404

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port='8080')