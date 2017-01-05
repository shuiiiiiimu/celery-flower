# -*- coding: utf-8 -*-

from celery import Celery
from celery.task import periodic_task
from celery.schedules import crontab
from datetime import timedelta
import time 

broker = 'redis://{0}:{1}/5'.format('127.0.0.1', 6379)
backend = 'redis://{0}:{1}/6'.format('127.0.0.1', 6379)

app = Celery('task', broker=broker, backend=backend)


@app.task()
def add(x, y):
    time.sleep(10)
    return x + y



@app.task()
def test(x, y):
    time.sleep(5)
    print('----> test')
    return x + y


@periodic_task(run_every=timedelta(seconds=20))
def newfeeds():
    print('-------> newfeeds')
    return 'hello'


CELERYBEAT_SCHEDULE = {
    'test-every-monday-morning': {
        'task': 'task.test',
        'schedule': crontab(hour=7, minute=30, day_of_week=1),
        'args': (6, 5),
    },
    'test-every-30-seconds': {
        'task': 'task.test',
        'schedule': timedelta(seconds=30),
        'args': (26, 45),
    },
}

CELERY_CONFIG = {
    'CELERY_TIMEZONE': 'Asia/Shanghai',
    'CELERY_ENABLE_UTC': True,
    'CELERY_TASK_SERIALIZER': 'json',
    'CELERY_RESULT_SERIALIZER': 'json',
    'CELERY_ACCEPT_CONTENT': ['json'],
    'CELERYD_MAX_TASKS_PER_CHILD': 1,
    'CELERYBEAT_SCHEDULE': CELERYBEAT_SCHEDULE     # 启动beat，传入相关参数.
}

app.conf.update(**CELERY_CONFIG)