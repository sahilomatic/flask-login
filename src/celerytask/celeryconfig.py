from celery.schedules import crontab


CELERY_IMPORTS = ('celerytask.task')
CELERY_TASK_RESULT_EXPIRES = 30
CELERY_TIMEZONE = 'UTC'

CELERY_ACCEPT_CONTENT = ['json', 'msgpack', 'yaml']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

CELERYBEAT_SCHEDULE = {
    'test-celery': {
        'task': 'celerytask.task.last_login_task',
        # Every minute
        'schedule': crontab(minute="*"),
    }
}