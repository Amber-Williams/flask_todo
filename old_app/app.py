from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    complete = db.Column(db.Boolean, default=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id

# PAGE ROUTES
@app.route('/', methods=['POST', 'GET'])
def get_index():
    tasks = Todo.query.order_by(Todo.date_created).all()

    # because folder name is templates you don't have to specify route
    return render_template('index.html', tasks=tasks)

# TASK LIST ROUTES
@app.route('/list', methods=['POST', 'GET'])
def list():
    if (request.method == 'POST'):
        task_content = request.form['content']
        new_task = Todo(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue creating task'

    else:
        return 'this is a get'

@app.route('/list/<int:id>/delete')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was an issue deleting task'

@app.route('/list/<int:id>/edit-complete')
def edit_complete(id):
    task_to_toggle = Todo.query.get_or_404(id)
    task_to_toggle.complete = not task_to_toggle.complete

    try:
        db.session.commit()
        return redirect('/')
    except:
        return 'There was an issue setting task complete state'

@app.route('/list/<int:id>/edit-content', methods=['POST', 'GET'])
def edit_task(id):
    task = Todo.query.get_or_404(id)

    if (request.method == 'GET'):
        # Takes user page to edit a task's content
        return render_template('edit_task_content.html', task=task)
    else:
        # updates task's content and redirects user to their todo list
        task.content = request.form['content']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue updating task content'

if __name__ == '__main__':
    app.run(debug=True)