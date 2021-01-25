import os
from flask.cli import FlaskGroup

from app import create_app, db

#config_name = os.getenv('FLASK_CONFIG')
config_name = 'production'
app = create_app(config_name)

cli = FlaskGroup(app)

@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

if __name__ == '__main__':
    cli()
    #app.run()