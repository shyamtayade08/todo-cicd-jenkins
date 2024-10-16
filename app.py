from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# A list to store the tasks
tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form['task']  # Get the task from the form
    tasks.append(task)  # Add it to the list of tasks
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    if task_id < len(tasks):
        tasks.pop(task_id)  # Remove the task from the list
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
