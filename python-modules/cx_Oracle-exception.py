# 结论：
# 如果自己写了自己的异常，那么在处理异常时，不要MyException(e)，而是MyException(str(e))，或者MyException("xxx" % e)
# 前面只会输出一个<exception...>，后面则会打印具体的报错信息
