# 其他特性
## include 指令
# include 指令告诉make 去读取其他makefiles 文件, 它是makefile中的一行, 如:

include filenames...

## vpath 指令
# vpath 指令用来指定某些prerequisites 的位置, 使用格式是: `vpath <pattern> <directories, space/colon separated>`
# <pattern> 中可以使用 %, 用来匹配0个活多个字符

# 指所有.h 文件在../headers 和 ../other-directory 上找
vpath %.h ../headers ../other-directory
# 所有.c 文件 在src中找
vpath %.c src
