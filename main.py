from flask import Flask,render_template,request,redirect,url_for, session
import sqlite3
import os
from application import config
from application.config import LocalDevelopmentConfig
from application.database import db
app = None

def create_app():
    app = Flask(__name__, template_folder = "templates")
    if os.getenv('ENV', "development") == "production":
        raise Exception("Currently no production config is setup.")
    else:
        print("Starting Local Development")
        app.config.from_object(LocalDevelopmentConfig)
    db.init_app(app)
    app.app_context().push()
    return app

app = create_app()


# Import all the controllers so they are loaded
from application.controllers import *


if __name__=="__main__":
    app.run(debug=True)
