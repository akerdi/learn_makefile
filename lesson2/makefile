# %和*都是通配符, 但是完全不同.
# * 会搜索你的文件系统来匹配文件名. 但是建议使用wildcard 来包裹它, 不然会掉入常见陷阱中.

print: $(wildcard *.c)
	ls -la $?

print1: $(wildcard *.c)
	ls -la $<


# * 可以用在targets/prerequesites/wildcard函数中
# * 不能直接用在变量定义中
# 当*匹配不到文件时, 它将保持原样(除非被 wildcard 函数包裹)