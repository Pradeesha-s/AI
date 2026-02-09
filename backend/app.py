from flask import Flask
from database.db import create_user_table, create_task_table
from routes.auth_routes import auth_routes
from database.db import insert_sample_tasks
from routes.dashboard_routes import dashboard_routes
from routes.chat_routes import chat_routes

app = Flask(__name__)

create_user_table()
create_task_table()
insert_sample_tasks()

app.register_blueprint(auth_routes)
app.register_blueprint(dashboard_routes)
app.register_blueprint(chat_routes)

@app.route("/")
def home():
    return "AI backend is running!"

if __name__ == "__main__":
    app.run(debug=True)
