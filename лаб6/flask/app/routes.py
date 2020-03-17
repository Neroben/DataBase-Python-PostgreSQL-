from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import InsertClubForm, InsertConfederacyForm
from app.database import init


@app.route('/insert')
def insert():
    return render_template('insert.html')

@app.route('/insert/confederacy', methods=['GET', 'POST'])
def createconfederacy():
    form = InsertConfederacyForm()
    if form.validate_on_submit():
        con = init()
        curr = con.cursor()
        curr.execute('INSERT INTO confederacy (name) VALUES (\''+form.name.data+'\')')
        con.commit()
        curr.close()
        con.close()
        return redirect(url_for('index'))
    return render_template('createconfederacy.html', title='Create', form=form)


@app.route('/insert/club', methods=['GET', 'POST'])
def createclub():
    form = InsertClubForm()
    if form.validate_on_submit():
        con = init()
        curr = con.cursor()
        try:
            curr.execute('INSERT INTO club (name, rating, confederacy_id, sponsor_id) VALUES (%s, %s, %s, %s)', (form.name.data, form.rating.data,form.confederacy_id.data, form.sponsor_id.data))
            con.commit()
            curr.close()
            con.close()
            return redirect(url_for('index'))
        except BaseException:
            con.commit()
            curr.close()
            con.close()
            return render_template('createclub.html', title='Create', error2 = "Отрицательное значение", form=form)
    return render_template('createclub.html', title='Create', error2 = "",  form=form)

@app.route('/view')
def view():
    return render_template('view.html')

@app.route('/view/confederacy')
def confederacy():
    con = init()
    curr = con.cursor()
    curr.execute('''
        SELECT DISTINCT CO.name
        FROM confederacy CO
    ''')
    ligs = curr.fetchall()
    return render_template('viewbase.html', ligs=ligs)

@app.route('/view/club')
def club():
    con = init()
    curr = con.cursor()
    curr.execute('''
        SELECT DISTINCT CO.name
        FROM club CO
    ''')
    ligs = curr.fetchall()
    curr.close()
    con.close()
    return render_template('viewbase.html', ligs=ligs)

@app.route('/view/players')
def players():
    con = init()
    curr = con.cursor()
    curr.execute('''
        SELECT DISTINCT CO.lastname
        FROM player CO
    ''')
    ligs = curr.fetchall()
    return render_template('viewbase.html', ligs=ligs)

@app.route('/view/coach')
def coach():
    con = init()
    curr = con.cursor()
    curr.execute('''
        SELECT DISTINCT CO.lastname
        FROM coach CO
    ''')
    ligs = curr.fetchall()
    return render_template('viewbase.html', ligs=ligs)

@app.route('/view/match')
def match():
    con = init()
    curr = con.cursor()
    curr.execute('''
        SELECT DISTINCT CO.playdata
        FROM match CO
    ''')
    ligs = curr.fetchall()
    return render_template('viewbase.html', ligs=ligs)


#<a href={{ url_for('login') }}>Login</a>
@app.route('/login', methods=['GET', 'POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/')
@app.route('/index')
def index():
    user = {'username' : 'Alexandr'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author': {'username': 'Ипполит'},
            'body': 'Какая гадость эта ваша заливная рыба!!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
