# coding:utf-8
def f1(name, *arg):
    print name
    print arg

def f2(name, *haha):
    print name
    print haha

f1('zhang')
f1('zhang', 'lala')
f1('zhang', 'lala', 'haha')
f2('zhang', 'lala', 'haha')

list_words = ['hello', 'world']
tuple_words = ('hello', 'world')

f2('zhang', list_words)
f2('zhang', tuple_words)
f2('zhang', *list_words)
f2('zhang', *tuple_words)

# 结论：
# ×arg可以有，也可以没有。
# arg名字可以是arg，也可以是其他的任何名字
# 传的时候列表和元组都是一个内容
# 如果已经有一个list或tuple，可以通过f(×list)的方式调用
