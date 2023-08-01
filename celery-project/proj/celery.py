import os
from celery import Celery

app = Celery('proj',
             broker=os.environ['CELERY_BROKER_URL'],
             include=['proj.tasks'])


if __name__ == '__main__':
    app.start()