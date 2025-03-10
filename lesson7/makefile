# 函数
# 函数主要用于文本处理. 函数调用的语法是 $(fn, arguments) 或 $(fn, arguments). 你可以使用内置的函数call 来制作自己的函数.
# Make 拥有数量众多的[内置函数](https://www.gnu.org/software/make/manual/html_node/Functions.html)

bar := $(subst not,totally, "I am not superman")

all: recipe0 recipe1 recipe2

recipe0:
	@echo $(bar)

# 替换空格或逗号, 请使用变量:
comma := ,
empty :=
space := $(empty) $(empty)
foo := a b c
str := $(subst $(space),$(comma),$(foo))

recipe1:
	@echo $(str)

# 使用sed 方案, 当然也可以使用其他程序输出赋值的方法
tmp_str :=
recipe2:
	@echo "a b c" | sed -e 's/ /,/g' | xargs echo
	$(eval tmp_str=$(shell echo "a b c" | sed -e 's/ /,/g'))
#   $(eval tmp_str=$(shell python3 xxx))
	@echo tmp_str: $(tmp_str)