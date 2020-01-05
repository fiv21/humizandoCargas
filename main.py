from flask import Flask, render_template, session, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import FormField, StringField, PasswordField, BooleanField, SubmitField, DateField, IntegerField, TimeField, FieldList
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.secret_key = 'SHH!'

class scheduleForm(FlaskForm):
   cursoID = IntegerField('cursoID')
   nombreCurso = StringField('nombreCurso', validators=[DataRequired()])
   date = DateField('date',format='%d-%m-%y', validators=[DataRequired()])
   horarioInicio = TimeField('horarioInicio', validators=[DataRequired()])
   horarioFin = TimeField('horarioFin', validators=[DataRequired()])
   timeout = IntegerField('timeoutInMinutes')

class Form(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])
    aula = StringField('aula', validators=[DataRequired()])
    fpsRate = StringField('fpsRate')
    institution = StringField('institution', validators=[DataRequired()])
    clase = FieldList(FormField(scheduleForm), min_entries=1, max_entries=200)
    button = SubmitField()


@app.route('/', methods=['post','get'])
def home():
   form = Form()
   return render_template('index.html', form=form)



if __name__ == "__main__":
    app.run(debug=True, port=8080)