# app\__init__.py

import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap


db = SQLAlchemy()

bootstrap = Bootstrap()


def create_app(config_type):
    """
    Description: Create a new flask application using the given config type.
    param: 
        config_type: The type of configuration. It can be one of three types, development, test, or production.
        returns: The new flask application    
    """
    
    app = Flask(__name__)
    configuration = os.path.join(os.getcwd(), 'config', config_type + '.py')
    app.config.from_pyfile(configuration)                                       # here app is instace of Flask class

    db.init_app(app)                                                            # Initialize the database instance   (app is a instace of Flask class )
    bootstrap.init_app(app)                                                     # Initialize the bootstrap instance      

    from app.catlog import main                                                 # import blueprint (app : root folder)
    app.register_blueprint(main)                                                # register blueprint (app is instace of Flask class)   

    return app

