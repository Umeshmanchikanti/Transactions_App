# forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FileField, TextAreaField
from wtforms.validators import DataRequired

class TransactionForm(FlaskForm):
    reason = TextAreaField("Reason for Transaction", validators=[DataRequired()])
    bill_image = FileField("Upload Bill Image")
    submit = SubmitField("Add Transaction")
