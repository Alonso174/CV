from flask import Flask, redirect, url_for, render_template, request, session
from flask import render_template

app = Flask(__name__)
app.secret_key = '1704'


@app.route('/', methods=['GET', 'POST', 'DELETE', 'PUT'])
def hello_world():
    return render_template('AlonCV.html')


@app.route('/contactList', methods=['GET', 'POST', 'DELETE', 'PUT'])
def hello_contact():
    return render_template('Contact.html')


@app.route('/assignment8', methods=['GET', 'POST', 'DELETE', 'PUT'])
def hello_assignment8():
    return render_template('assignment8.html',
                           user={'name': "Alon Levin"},
                           hobbies=['Football', 'E-Games', 'Climbing'])


UsersList = {
    "Rony89": {"firstName": "Rony", "lastName": "Levin", "email": "Ronyle89@gmail.com"},
    "Gaby63": {"firstName": "Gaby", "lastName": "Levin", "email": "Gaby1063@gmail.com"},
    "Nir62": {"firstName": "Nir", "lastName": "Levin", "email": "NirLevin43@gmail.com"},
    "Goduu": {"firstName": "Godu", "lastName": "Bakarish", "email": "wheresGodu@gmail.com"},
    "Bushkape": {"firstName": "Bush", "lastName": "Kape", "email": "Bushkape111@gmail.com"}
}


@app.route('/assignment9', methods=['GET', 'POST', 'DELETE', 'PUT'])
def hello_assignment9():
    if request.method == 'GET':
        if request.args:
            if "username" in request.args:
                UserInList = request.args["username"]
                if UserInList in UsersList and UserInList != '':
                    return render_template("assignment9.html", username=UserInList, users=UsersList[UserInList],
                                           found=True, search=True)
                elif UserInList not in UsersList and UserInList != '':
                    return render_template("assignment9.html", found=False, search=True)
                else:
                    return render_template("assignment9.html", users=UsersList, search=True)
            else:
                return render_template("assignment9.html", search=False)
        else:
            return render_template("assignment9.html")

    elif request.method == 'POST':
        if not session.get('loggedIn'):
            if request.form['username'] not in UsersList:
                UsersList[request.form['username']] = {"firstName": request.form['firstname'],
                                                       "lastName": request.form['lastname'],
                                                       "email": request.form['email']}
                session['loggedIn'] = True
                session['username'] = request.form['username']
                return render_template("assignment9.html", exists=False)
            if request.form['username'] in UsersList:
                session['loggedIn'] = False
                return render_template("assignment9.html", exists=True)
        else:
            session['loggedIn'] = False
            return render_template("assignment9.html")


if __name__ == '__main__':
    app.run()
