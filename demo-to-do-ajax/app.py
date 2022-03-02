from flask import Flask
from flask import render_template, request, Response
import db

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route("/")
def index():
    tasks = db.select_all_tasks()
    return render_template("to_do.html", tasks=tasks)


@app.route("/tasks")
def tasks():
    tasks = db.select_all_tasks()
    list = [dict(zip(task.keys(), task)) for task in tasks]
    
    return Response(f"{list}", mimetype='text/json')

@ app.route("/new_task", methods=["POST"])
def new_task():
    task=request.form["task"]

    last_id=db.save_new_task(task)
    if last_id is not None:
        return f"""
            <li class="list_item">
                {task}
                <button class="done fas fa-check" todoid="{last_id}"></button>
                <button class="delete fas fa-trash-alt" todoid="{last_id}"></button>
            </li>
            """
    else:
        return ""


@ app.route("/delete", methods=["POST"])
def delete():
    try:
        id=request.form["id"]
        db.delete_task(id)
        return {"status": "OK"}
    except:
        return {"status": "ERROR"}
