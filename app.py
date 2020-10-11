from flask import Flask, render_template, request, redirect, url_for

#init app
app = Flask(__name__)
db = []

#URI, endpoint

@app.route('/', methods=['GET', 'POST'])
def main():
    # custom post handling here
    if request.method == 'POST':
        new_task = request.form['new_task']
        if len(new_task) > 0 and new_task not in db:
            db.append(new_task)
    return render_template('index.html', todo=db, name='sole')

@app.route('/delete/<task>', methods = ['GET'])
def delete(task):
    db.remove(task)
    return redirect(url_for('main'))

@app.route('/update/<task>', methods=['GET', 'POST'])
def update(task):
    db.remove(task)
    update_task = request.form['update_task']
    db.append(update_task)

    return redirect(url_for('main'))

if __name__ == '__main__':
    app.run(debug=True)

