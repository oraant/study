# coding:utf-8
from __future__ import absolute_import
from time import sleep
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
        file.write('- %s -\n' % msg)

@app.task
def preserve(msg, count):
    for i in range(count):
        sleep(1)
        output(msg)

@app.task(bind=True) #, default_retry_delay=3, max_retries=2)
def raiseerror(self, msg, count):

    # output messages
    req = self.request
    output(req.called_directly)
    output(req.retries)

    self.update_state(state='STARTED')

    # set config
    self.track_started = True
    self.max_retries = 2
    
    delay = (3 if req.retries == 1 else 1)
    self.default_retry_delay = delay

    # do the main job
    try:
        [job(i, msg) for i in range(count)]
    except Exception as e:
        self.update_state(state='ERROR')
        self.retry(exc=e) # todo

def job(i, msg):

    output('--%s%s' % (i, msg));
    sleep(1)

    if i != 2: return
    raise StandardError('this is a error')

# 结论：
# retry时，不要设置tried之类的变量，来判断是否重启过。因为每次重启，都会将其搞成初始值。可以考虑用request来设置这个。
# retry时，如果是像pull这样一直不会结束的任务，max_retries就相当于一个会执行几次。所以最好设置成一直尝试重启，然后重启间隔为一天
# 在task中可以动态修改task的属性，如default_retry_delay等，但要注意的是，根据request的retries来判断次数并修改retry的配置时，下次retry才会生效
