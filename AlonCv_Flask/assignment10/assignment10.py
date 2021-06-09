from flask import  Blueprint, render_template, request, url_for, redirect, flash
import mysql.connector

assignment10 = Blueprint('assignment10', __name__,
                          static_folder='static',
                          static_url_path='/assignment10',
                          template_folder='templates')


def interact_db(query, query_type: str):
    return_value = False
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         passwd='root',
                                         database='aloncv')
    cursor = connection.cursor(named_tuple=True)
    cursor.execute(query)

    if query_type == 'commit':
        connection.commit()
        return_value = True

    if query_type == 'fetch':
        query_result = cursor.fetchall()
        return_value = query_result

    connection.close()
    cursor.close()
    return return_value


@assignment10.route('/assignment10', methods=['GET', 'POST'])
def users():
    query = "select * from users"
    query_result = interact_db(query, query_type='fetch')
    return render_template('assignment10.html', users=query_result)


@assignment10.route('/insert_user', methods=['GET', 'POST'])
def insert_user():
        if request.method == 'POST':
            username = request.form['username']
            firstname = request.form['firstname']
            lastname = request.form['lastname']
            email = request.form['email']
            query = "INSERT INTO users(username, first_name, last_name, email) VALUES ('%s','%s', '%s', '%s')" % \
                    (username, firstname, lastname, email)
            interact_db(query=query, query_type='commit')
            flash('User inserted successfully')
        return redirect('/assignment10')


@assignment10.route('/delete_user', methods=['GET', 'POST'])
def delete_user():
    if request.method == 'GET':
        user_email = request.args['email']
        query = "DELETE FROM users Where email='%s';" % user_email
        interact_db(query=query, query_type='commit')
        flash('User deleted successfully')
        return redirect('/assignment10')


@assignment10.route('/update_user', methods=['GET', 'POST'])
def update_user():
    if request.method == 'GET':
        username = request.args['username']
        user_email = request.args['email']
        query = "UPDATE users SET username = %s WHERE email= %s" % (username, user_email)
        interact_db(query=query, query_type='commit')
        flash('You were successfully updated - %s' % user_email)
        return redirect('/assignment10')
