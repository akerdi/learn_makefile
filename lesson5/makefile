# 变量
## 变量类型和修改
# 变量的类型有两种:
#- 递归变量(`=`) - 只有再命令执行时才查找变量, 而不是在定义时
#- 简单变量(`:=`) - 就像普通命令式编程一样---只有当前已经定义的变量才会得到拓展

# 这个会打印`one later`
one = one ${later_variable}
# 这个只打印`two`
two := two ${later_variable}

later_variable = later

all:
	echo $(one)
	echo $(two)