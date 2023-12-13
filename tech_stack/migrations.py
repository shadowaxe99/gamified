from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

def run_migrations():
    migrate.init_app(app)
    migrate.upgrade()

def rollback_migrations():
    migrate.init_app(app)
    migrate.downgrade()

def create_migration(message: str):
    migrate.init_app(app)
    migrate.migrate(message)

def apply_migration(revision: str):
    migrate.init_app(app)
    migrate.stamp(revision)

def list_migrations():
    migrate.init_app(app)
    return migrate.history()
