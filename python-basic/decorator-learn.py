# coding:utf-8

# 需求：原来的系统太复杂，不敢改动，但又想实现一个记录日志功能。


# 原来的方法如下：

def year():
    return '2016'

def month():
    return '09'

def day():
    ...

print year()


# 改后的方式如下：


def log_year():
    print 'this is a log!'
    return year()
    
def log_month():
    print 'this is a log!'
    return month()


print log_year()


# 上面的方法，一来每个都需要去新建函数包裹起来，二来一旦发生改动，所有的方法都要改一遍。

def log_function(func):
    print 'this is a log!'
    result = func()
    return result

log_function(year)
log_function(month)


# 调用方式都变了，比如本来有很多个地方，调用时都是调用的year()，此时都得改成log_function(year)

year = log_function(year)
month = log_function(month)

# 装饰器

def log(func):
    def warpper(*args, **kw):
        print 'this is a log'
        return func(*args, **kw)
    return wrapper

year = log(year)
year = wrapper
year() = wrapper()
month = log(month)

year() -> wrapper() -> print,old_year()

# asdfasdf

def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print '%s %s():' % (text, func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator

year = log('execute')(year)
year = decorator(year)
year = wrapper

year() = wrapper()









