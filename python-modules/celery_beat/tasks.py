from __future__ import absolute_import

from main import app


@app.task
def add(x, y):
    return x + y


@app.task
def mul(x, y):
    return x * y


@app.task
def xsum(numbers):
    return sum(numbers)

@app.task
def output(msg):
    with open('log.txt', 'a') as file:
        file.write(msg)
