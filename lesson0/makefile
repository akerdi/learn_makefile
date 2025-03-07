
# 像python/Ruby/JS 这样的解释型语言是不需要类似Makefile 的东西. Makefile 的目标是基于哪些文件发生了变化来编译需要被编译的一切文件. 但是, 当解释型语言的文件发生了变化, 是不需要重新编译的, 程序运行时会使用最新版的源码文件.
# makefile 各部分规则如下:
# targets: prerequesites
#	recipe

blah: blah.o
	cc blah.o -o blah

blah.o: blah.c
	cc -c blah.c -o blah.o

blah.c:
	echo "int main() { return 0; }" > blah.c
