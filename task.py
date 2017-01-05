# -*- coding: utf-8 -*-

from celery import Celery
from celery.task import periodic_task
from datetime import timedelta
import time 

broker = 'redis://{0}:{1}/5'.format('127.0.0.1', 6379)
backend = 'redis://{0}:{1}/6'.format('127.0.0.1', 6379)

app = Celery('tasks', broker=broker, backend=backend)


@app.task()
def add(x, y):
    time.sleep(10)
    return x + y



@app.task()
def test(x, y):
    time.sleep(100)
    return x + y


@periodic_task(run_every=timedelta(seconds=20))
def newfeeds():
    print('-------> newfeeds')
    return 'hello'