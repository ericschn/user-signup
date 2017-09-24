from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    """ Initial get request at root, empty form """
    return render_template('signup2.html', title="Signup")

@app.route('/', methods=['POST', 'GET'])
def check_form():
    """ Check validity of form, redirect to welcome page if no errors """
    # Put post requests into variables
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    # Initialize error strings as empty
    username_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''

    errors = 0

    if not check_name(username):
        username_error = 'Not a valid username'
        errors += 1
    if not check_name(password):
        password_error = 'Not a valid password'
        errors += 1
    if not verify_pass(password, verify):
        verify_error = 'Passwords do not match'
        errors += 1
    if not check_email(email):
        email_error = 'Not a valid email'
        errors += 1

    if not errors:
        return redirect('/welcome?username=' + username)

    return render_template('signup2.html', title="Signup",
                           username=username, email=email,
                           username_error=username_error, password_error=password_error,
                           verify_error=verify_error, email_error=email_error)

@app.route('/welcome')
def welcome():
    """ Display welcome page """
    username = request.args.get('username')
    return render_template('welcome.html', username=username)


def check_name(x):
    """ Check str 'x' for proper length and no space """
    if len(x) < 3 or len(x) > 20 or x.count(' ') > 0:
        return False
    return True

def check_email(x):
    """ Check str 'x' for proper length and inclusion of @ . """
    if x == '':
        return True
    if x.count('@') == x.count('.') == 1 and check_name(x):
        return True
    return False

def verify_pass(x,y):
    """ Check if equal """
    return x == y


app.run()
