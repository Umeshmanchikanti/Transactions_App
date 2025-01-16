from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a_random_secret_key'

csrf = CSRFProtect(app)

class TransactionForm(FlaskForm):
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def home():
    form = TransactionForm()
    if form.validate_on_submit():
        return "Form Submitted Successfully"
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
