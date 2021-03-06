
from turtle import update
from flask import Blueprint, render_template, current_app, redirect, request, url_for
from flask_login import current_user
from webapp import people
from webapp.people.forms import AddPeople
from webapp.people.models import People
from datetime import datetime, date
from operator import attrgetter
from webapp.model import db
blueprint = Blueprint('people',__name__)
 
@blueprint.route('/')
def index():
    if not current_user.is_authenticated:
        return redirect(url_for('user.login'))
    page_title="Список дней рождений"
    peoples = People.query.filter(People.user_id == current_user.id).all()
    for people in peoples:
        if date.today() > people.date_of_birth.replace(year=datetime.now().year):
            people.day_to_bd = people.date_of_birth.replace(year=datetime.now().year+1) - date.today()
            people.age = datetime.now().year - people.date_of_birth.year
        else:
            people.day_to_bd = people.date_of_birth.replace(year=datetime.now().year) - date.today()
            people.age = datetime.now().year - people.date_of_birth.year - 1
        
    peoples = sorted(peoples, key=attrgetter('day_to_bd'),reverse=False)
    return render_template('people/index.html', peoples=peoples, page_title=page_title)

@blueprint.route('/view/<id>', methods = ['GET','POST'])
def view(id):
    if request.method == 'GET':
        data = People.query.get(id)
        return render_template('people/view.html',people=data)


@blueprint.route('/create', methods = ['GET','POST'])
def add():
    form=AddPeople()
    if request.method == 'GET':
        return render_template('people/create.html',form=form)
    if request.method == 'POST' :
        user_id = current_user.id
        name = request.form['name']
        group_id = request.form['group_id']
        date_of_birth = request.form['date_of_birth']
        date_of_birth = datetime.strptime(date_of_birth, '%Y-%m-%d')
        phone = request.form['phone']
        profile = request.form['profile']
        hobbies = request.form['hobbies']
        reminder_rule = request.form['reminder_rule']
        
        data = People(user_id=user_id,name=name,group_id=group_id,date_of_birth=date_of_birth,phone=phone,profile=profile,hobbies=hobbies,reminder_rule=reminder_rule)
        db.session.add(data)
        db.session.commit()

        return redirect(url_for('people.index'))

@blueprint.route('/update/<id>', methods = ['GET','POST'])
def update(id):
    if request.method == 'GET':
        print(id)
        data = People.query.filter_by(id=id).first()
        print(data)
        return render_template('people/update.html', people=data)
    if request.method == 'POST' :
        data = People.query.get(request.form.get('id'))
        print(data)
        data.name = request.form['name']
        data.group_id = request.form['group_id']
        date_of_birth = request.form['date_of_birth']
        data.date_of_birth = datetime.strptime(date_of_birth, '%Y-%m-%d')
        data.phone = request.form['phone']
        data.profile = request.form['profile']
        data.hobbies = request.form['hobbies']
        data.reminder_rule = request.form['reminder_rule']

        db.session.commit()

        return redirect(url_for('people.index'))

@blueprint.route('/delete/<id>/', methods = ['GET','POST'])
def delete(id):
        if request.method == 'GET':
            data = People.query.filter_by(id=id).first()
            return render_template('people/delete.html', people=data)
        if request.method == 'POST' :
            data = People.query.get(id)
            db.session.delete(data)
            db.session.commit()
            return redirect(url_for('people.index'))