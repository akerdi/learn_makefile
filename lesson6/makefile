# Makefile 的条件判断

# if/else

foo = ok

all: recipe0 recipe1 recipe2

recipe0:
ifeq ($(foo), ok)
	echo "foo equals ok"
else
	echo "nope"
endif

# 检查一个变量是否为空

nullstring =
foo = $(nullstring) # 注释前面有个空格

recipe1:
ifeq ($(strip $(foo)),)
	echo "foo is empty after being stripped"
endif
ifeq ($(nullstring),)
	echo "nullstring doesn't even have spaces"
endif

# 检查变量是否定义

bar =
foo = $(bar)

recipe2:
ifdef foo
	echo "foo is defined"
endif
ifdef bar
	echo "bat bar is not"
endif