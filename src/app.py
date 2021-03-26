from __future__ import absolute_import, unicode_literals
from flask import Flask
from celery import Celery
import os
import logging.config
from celerytask import celeryconfig
import mongoengine


application = Flask(os.environ.get("APPLICATION_NAME"))
SETTINGS_FILE = os.environ.get("SETTINGS_FILE", "settings.local_settings")

application.config.from_object(SETTINGS_FILE)


#edited by sahil soni
def make_celery(app):#Flask app object is passed
    # create context tasks in celery
    celery = Celery(
        app.import_name,
        broker=app.config['BROKER_URL']
    )
    celery.conf.update(app.config)
    celery.from_object(celeryconfig)
    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = ContextTask

    return celery

celery = make_celery(application)






#done












with application.app_context():
    # this loads all the views with the app context
    # this is also helpful when the views import other
    # modules, this will load everything under the application
    # context and then one can use the current_app configuration
    # parameters
    from apis.urls import all_urls
    from scripts import ALL_CLI_COMMANDS

    for cli_name, cli_command in ALL_CLI_COMMANDS.items():
        application.cli.add_command(cli_command, name=cli_name)


# Adding all the url rules in the api application
for url, view, methods, _ in all_urls:
    application.add_url_rule(url, view_func=view, methods=methods)


logging.config.dictConfig(application.config["LOGGING"])

mongoengine.connect(
    alias='default',
    db=application.config['MONGO_SETTINGS']['DB_NAME'],
    host=application.config['MONGO_SETTINGS']['DB_HOST'],
    port=application.config['MONGO_SETTINGS']['DB_PORT'],
    username=application.config['MONGO_SETTINGS']['DB_USERNAME'],
    password=application.config['MONGO_SETTINGS']['DB_PASSWORD'],
)
