from flask import Flask, render_template, request, redirect, send_from_directory
import os
import csv

app = Flask(__name__)


@app.route('/')
def landing():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static/assets'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database:
        fieldnames = ['email', 'subject', 'message']
        databasewriter = csv.DictWriter(database, fieldnames=fieldnames)
        databasewriter.writerow(data)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'Something went wrong.'
    else:
        return 'Something went wrong.'
