from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Hello2008'


def get_db_connection():
    conn = sqlite3.connect('exemp.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/Authors.com')
@app.route('/')
def index():
    conn = get_db_connection()
    notes = conn.execute('SELECT * FROM users').fetchall()
    conn.close()
    return render_template('index.html', notes=notes)


@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        conn = get_db_connection()
        conn.execute('INSERT INTO users (title, content) VALUES (?, ?)',
                     (title, content))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('create.html')


if __name__ == '__main__':
    app.run(debug=True)
