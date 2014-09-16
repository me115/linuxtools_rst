readelf
作用：用于显示elf格式文件的信息；
描述：
这个工具和objdump命令提供的功能类似，但是它显示的信息更为具体，并且它不依赖BFD库(BFD库是一个GNU项目，它的目标就是希望通过一种统一的接口来处理不同的目标文件）；

ELF文件类型
ELF(Executable and Linking Format)是一种对象文件的格式，用于定义不同类型的对象文件(Object files)中都放了什么东西、以及都以什么样的格式去放这些东西。它自最早在 System V 系统上出现后，被 xNIX 世界所广泛接受，作为缺省的二进制文件格式来使用。可以说，ELF是构成众多xNIX系统的基础之一。

ELF文件有三种类型：
1.可重定位的对象文件(Relocatable file)
由汇编器汇编生成的 .o 文件
2.可执行的对象文件(Executable file)
可执行应用程序
3.可被共享的对象文件(Shared object file)
动态库文件，也即 .so 文件

1) .text section 里装载了可执行代码；
2) .data section 里面装载了被初始化的数据；
3) .bss section 里面装载了未被初始化的数据；
4) 以 .rec 打头的 sections 里面装载了重定位条目；
5) .symtab 或者 .dynsym section 里面装载了符号信息；
6) .strtab 或者 .dynstr section 里面装载了字符串信息；

更多关于ELF文件格式的参考：http://www.cnblogs.com/xmphoenix/archive/2011/10/23/2221879.html

eg:
想知道一个应用程序的可运行的架构平台：
readelf -h main| grep Machine
-h选项将显示文件头的概要信息，从里面可以看到，有很多有用的信息：
::

	/opt/app/todeav1/test$readelf -h main
	ELF Header:
	Magic:   7f 45 4c 46 02 01 01 00 00 00 00 00 00 00 00 00
	Class:                             ELF64
	Data:                              2 s complement, little endian
	Version:                           1 (current)
	OS/ABI:                            UNIX - System V
	ABI Version:                       0
	Type:                              EXEC (Executable file)
	Machine:                           Advanced Micro Devices X86-64
	Version:                           0x1
	Entry point address:               0x400790
	Start of program headers:          64 (bytes into file)
	Start of section headers:          5224 (bytes into file)
	Flags:                             0x0
	Size of this header:               64 (bytes)
	Size of program headers:           56 (bytes)
	Number of program headers:         8
	Size of section headers:           64 (bytes)
	Number of section headers:         29
	Section header string table index: 26


一个编译好的应用程序，想知道其编译时是否使用了-g选项（加入调试信息）：
readelf -S main| grep debug
用-S选项是显示所有段信息；如果编译时使用了-g选项，则会有debug段；
更多参考：http://quietheart.blog.51cto.com/1933493/610400
