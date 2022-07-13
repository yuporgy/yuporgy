from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, SubmitField, DateField
from wtforms.validators import DataRequired

class AddPeople(FlaskForm):
    group_id = StringField('Группа',validators=[DataRequired()], render_kw={"class": "form-control"})
    name = StringField('Имя',validators=[DataRequired()], render_kw={"class": "form-control"})
    date_of_birth = DateField('День рождения',validators=[DataRequired()], render_kw={"class": "form-control"})
    phone = StringField('Телефон', render_kw={"class": "form-control"})
    profile = StringField('Профиль', render_kw={"class": "form-control"})
    hobbies = StringField('Хобби', render_kw={"class": "form-control"})
    reminder_rule = StringField('Напоминать за',validators=[DataRequired()], render_kw={"class": "form-control"})
    submit = SubmitField('Отправить!', render_kw={"class": "btn btn-primary"})
   