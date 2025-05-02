from flask import Flask, render_template, request, redirect
import csv

app = Flask(app1.py)
FILENAME = 'patients.csv'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['GET', 'POST'])
def add_patient():
    if request.method == 'POST':
        data = [
            request.form['name'],
            request.form['age'],
            request.form['gender'],
            request.form['blood_group'],
            request.form['contact']
        ]
        with open(FILENAME, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(data)
        return redirect('/view')
    return render_template('add.html')

@app.route('/view')
def view_patients():
    with open(FILENAME, 'r') as file:
        reader = csv.reader(file)
        patients = list(reader)
    return render_template('view.html', patients=patients)

@app.route('/filter', methods=['GET', 'POST'])
def filter_patients():
    results = []
    if request.method == 'POST':
        field = request.form['field']
        keyword = request.form['keyword'].lower()
        with open(FILENAME, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if field == 'gender' and row[2].lower() == keyword:
                    results.append(row)
                elif field == 'blood_group' and row[3].lower() == keyword:
                    results.append(row)
                elif field == 'name' and keyword in row[0].lower():
                    results.append(row)
    return render_template('filter.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
