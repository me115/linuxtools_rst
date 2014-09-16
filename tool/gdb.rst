gdb

设置断点
-----------------
插入断点的几种方式：
break DASendHandler.cpp:1939
break 16 //在源文件第16行设置断点
break func1 //在函数func1()入口处设置断点
条件断点设置  b fn1 if a＞b
注：break可缩写为b

info break 查看断点信息
清除所有断点：delete breakpoints


常用命令
-----------------
r (run)     运行程序
n (next)    单步执行
c (confinue) 继续执行
l (list)     列出当前执行到的周围源码
p (print)    打印变量当前值
>>p i  打印变量i的值
直接回车    重复上一指令



进阶：

1.对C/C++程序的调试，需要在编译前就加上-g选项；
cc -g hello.c -o hello
g++ -g hello.cpp -o hello

启动gdb
--------------
gdb <program>
program也就是你的执行文件，一般在当前目录下。
gdb <program> <core dump file>
>>gdb program core.11127
用gdb同时调试一个运行程序和core文件，core是程序非法执行后core dump后产生的文件。
gdb <program> <PID>
>>gdb hello 11127
如果你的程序是一个服务程序，那么你可以指定这个服务程序运行时的进程ID。gdb会自动attach上去，并调试他。program应该在PATH环境变量中搜索得到。


info function 查询函数
扩展info locals 显示当前堆栈页的所有变量
TAB自动补全
对于有命名空间的补全 需要加单引号
bt backtrace 显示当前调用堆栈
up 改变堆栈显示的深度
down
watch 设置观嚓点

p/x a 十六进制显示a的值
x 也是打印 只针对地址和原始数据
x/d &a 十进制显示a的地址
call getpid（）调用程序中可见的函数
whatis 查询变量或函数
连接正在运行的进程 gdb procer pid
调试core
几种产生原因
SIGSEGV 段错误
SIGFEP浮点数错误
SIGABRT 异常中断
SIGBUS 总线错误
强制core ulimit -c unlimited
发送 abort（）
raise（SIGABRT）
gdb 的gcore


整合： colin的 gdb的博客；
gdb 调试服务程序

