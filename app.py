from flask import Flask, render_template, url_for, request, redirect
from date_func import calc_datetime_difference, date_convert, date_format
from database import *

import datetime


@app.route('/form')
def form():
    projects = Projects.query.all()
    working_types = Working_Type.query.all()
    print(projects)
    print(working_types)
    return render_template('form.html', projects = projects, working_types = working_types)


@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':

        project = request.form['project']
        content = request.form['content']

        start_request_string = request.form['date_start']
        end_request_string = request.form['date_end']

        temp = date_convert(start_request_string, end_request_string)
        new_task = Project_Work(project=project, content=content, date_start = temp[0], date_end = temp[1], date = temp[2], time = temp[4])

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')

        except:
            return 'There was an issue adding your task'

    else:
        tasks = Project_Work.query
        return render_template('index.html', tasks=tasks)

@app.route('/summary')
def summary():
    tasks = Project_Work.query.all()
    
    for i in tasks:
        print (i.content)

    return render_template('summary.html', tasks=tasks)

@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Project_Work.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deleting that task'

#Following function updates existings entries in the database by using the entry-id.

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    
    projects = Projects.query.all()
    working_types = Working_Type.query.all()
    
    task = Project_Work.query.get_or_404(id)

    if request.method == 'POST':

        task.project = request.form['project']
        task.content = request.form['content']

        task.date_start = request.form['date_start']
        task.date_end = request.form['date_end']

        temp = date_convert(request.form['date_start'], request.form['date_end'])

        task.date = temp[2]
        task.time = temp[4]
        
        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue updating your task'

    else:
        return render_template('update.html', task=task, projects = projects, working_types = working_types)


if __name__ == "__main__":
    app.run(debug=True)