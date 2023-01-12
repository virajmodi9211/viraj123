from flask import *

app = Flask(__name__)
app.secret_key = 'viraj'


@app.route('/')
def register():
    session.clear()
    return render_template('register.html')

@app.route('/login')
def login():
    error = None
    f_name = request.args.get('fname')
    l_name = request.args.get('lname')
    u_name = request.args.get('uname')
    passw = request.args.get('pass')
    session['k1'] = f_name
    session['k2'] = l_name
    session['k3'] = u_name
    session['k4'] = passw
    return render_template('login.html')


@app.route('/registration')
def registration():
    error = None
    u_name2 = request.args.get('uname2')
    pwd = request.args.get('pass2')
    session['k5'] = u_name2
    session['k6'] = pwd
    if session['k4'] == session['k6']:
        if session['k3'] == session['k5']:
            return render_template('welcome.html',uname3=session['k1'], lname3= session['k2'])
    else:
        error = 'login failed'
        flash("login failed", category="error")
        return redirect(url_for('login'))
        # return render_template('login.html',error=error)



if __name__ == '__main__':
    app.run(debug=True)
