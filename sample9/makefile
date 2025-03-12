global0 = I'm global

2.2.1:
	echo "I'm the default first"

2.2.2:
	echo "${global0}"
	echo "${global1}"

global1 = I'm global too

export cooly = "I'm cool"
2.2.3:
	mkdir -p subdir
	echo "target:\n\techo "\$${cooly}"" | sed -e 's/^ //' > subdir/makefile
	cd subdir && ${MAKE}

2.2.4:
	./example.py
	./example.sh

2.2.5:
# 下面这个是错误的
#	 global1 = "new global"
# 你可以使用eval 来赋值
	$(eval global1=$(shell echo "a b c" | sed -e 's/ /,/g'))
	echo "${global1}"

2.2.6:
#- 递归变量(`=`) - 只有在命令执行时才查找变量, 而不是在定义时
#- 简单变量(`:=`) - 就像普通命令式编程一样---只有当前已经定义的变量才会得到拓展

2.2.7:
	cd ..; ls
	cd ..
	ls
	cd .. && \
	ls

create_func = echo "functionname: $(0)" && echo "$(1)\n$(2)" > $(3)
2.2.8:
	$(call create_func,hello,world,helloworld.txt)

# 将example.env 拷贝为.env
include .env
include another_makefile.mk
2.2.9: another_target
	echo "variable from .env: ${variable}"

2.2.10:
# 这是注释
    # 这也是注释
	echo "It's 2.2.10"
