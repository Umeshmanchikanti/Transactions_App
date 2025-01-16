import os
from flask import Flask, Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
from .models import Transaction
from .forms import TransactionForm
from . import db

home_bp = Blueprint('home', __name__)

@home_bp.route('/', methods=['GET', 'POST'])
def home():
    form = TransactionForm()
    transactions = Transaction.query.all()

    if form.validate_on_submit():
        reason = form.reason.data
        bill_image = form.bill_image.data

        # Save the image in a designated folder
        if bill_image:
            filename = secure_filename(bill_image.filename)
            upload_folder = os.path.join(os.path.dirname(__file__), 'static/uploads')
            os.makedirs(upload_folder, exist_ok=True)  # Ensure folder exists
            file_path = os.path.join(upload_folder, filename)
            bill_image.save(file_path)
        else:
            filename = None

        # Save transaction data in the database
        transaction = Transaction(reason=reason, bill_image=filename)
        db.session.add(transaction)
        db.session.commit()

        flash("Transaction added successfully!")
        return redirect(url_for('home.home'))

    return render_template('index.html', form=form, transactions=transactions)

@home_bp.route('/export', methods=['GET'])
def export_transactions():
    import pandas as pd

    transactions = Transaction.query.all()
    data = [{'ID': t.id, 'Date': t.date, 'Reason': t.reason, 'Bill Image': t.bill_image} for t in transactions]
    df = pd.DataFrame(data)

    # Save to an Excel file
    export_folder = os.path.join(os.path.dirname(__file__), 'static/exports')
    os.makedirs(export_folder, exist_ok=True)  # Ensure folder exists
    export_file = os.path.join(export_folder, 'transactions.xlsx')
    df.to_excel(export_file, index=False)

    return redirect(url_for('static', filename='exports/transactions.xlsx'))
