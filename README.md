## Celery & Flower

Celery Flower 使用案例，使用 Redis 作为 broker 和 backend。

**安装依赖**

```bash
(.venv) ➜  celery-flower git:(master) ✗ pip install -r requirements.txt
```

**启动 Celery**

```bash
(.venv) ➜  celery-flower git:(master) ✗ celery -A task worker -l info -B # -B 是因为有定时任务
```

**调用队列任务**

```bash
(.venv) ➜  celery-flower git:(master) ✗ python
Python 3.5.1 (v3.5.1:37a07cee5969, Dec  5 2015, 21:12:44)
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from task import add
>>> from task import test
>>> re1 = add.delay(1, 2)
>>> re2 = test.delay(1, 2)
>>> re1.get()
3
```

**启动 Flower**

```bash
(.venv) ➜  celery-flower git:(master) ✗ flower -A task beat # beat 是因为设置了定时任务，需要做心跳
```

