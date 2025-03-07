# 各种规则

## 隐式规则
#- 编译C时: 使用 $(CC) -c $(CPPFLAGS) $(CFLAGS) 形式的命令, n.o 会由n.c 自动生成
#- 编译C++时: 使用 $(CXX) -c $(CPPFLAGS) $(CXXFLAGS) 形式的命令, n.o 会由n.cc或n.pp 自动生成
#- 链接单个目标文件时: 通过运行 $(CC) $(LDFLAGS) n.o $(LOADLIBS) $(LDLIBS) 命令, n 会由 n.o 自动生成

# 上述隐式规则含义:
#- CC: 编译C程序的程序, 默认是cc
#- CXX: 编译C++程序的程序, 默认是G++
#- CFLAGS: 提供给C编译器的额外标志
#- CPPFLAGS: 提供给C预处理器的额外标志
#- LDFLAGS: 当编译器应该调用链接器时提供给编译器的额外标志

CC = gcc
CFLAGS = -g

blah: blah.o

blah.c:
	echo "int main() { return 0; }" > blah.c

clean:
	rm -f blah*