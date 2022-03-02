from crypt import methods
from flask import Flask
from flask import render_template, request, Response
import db

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route("/")
def index():
    tasks = db.select_all_tasks()
    # print(tasks[0]['task'])
    done_tasks = db.select_all_done_tasks()
    return render_template("to_do.html", tasks=tasks, done_tasks=done_tasks)


@app.route("/tasks")
def tasks():
    tasks = db.select_all_tasks()
    list = [dict(zip(task.keys(), task)) for task in tasks]
    return Response(f"{list}", mimetype='text/json')

@app.route("/new_task", methods=["POST"])
def new_task():
    task=request.form["task"]
    last_id = db.save_new_task(task)
    if last_id is not None:
        return f"{last_id}"
    return 500, ""


@ app.route("/delete", methods=["POST"])
def delete():
    try:
        id=request.form["id"]
        db.delete_task(id)
        return {"status": "OK"}
    except:
        return {"status": "ERROR"}

@app.route("/done", methods=["POST"])
def done():
    try:
        id=request.form["id"]
        db.update_task_to_done(id)
        return {"status": "OK"}
    except:
        return {"status": "ERROR"}
